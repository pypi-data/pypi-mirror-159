import pdb
import re

from mitmproxy.http import Headers, Request as MitmproxyRequest
from mitmproxy.coretypes import multidict
from typing import Callable, List, Union
from urllib.parse import urlparse

from stoobly_agent.app.settings.constants import request_component
from stoobly_agent.app.settings.rewrite_rule import RewriteRule, ParameterRule
from stoobly_agent.config.constants import custom_headers
from stoobly_agent.lib.logger import Logger, bcolors

from .request_body_facade import MitmproxyRequestBodyFacade
from .request import Request

class MitmproxyRequestFacade(Request):

    ###
    #
    # @param request [ActionDispatch::Request]
    #
    # @return [Hash]
    #
    def __init__(self, request: MitmproxyRequest):
        self.request = request
        self.__redact_rules: List[ParameterRule] = []
        self.__rewrite_rules: List[ParameterRule] = []

        self.__body = MitmproxyRequestBodyFacade(request)

    @property
    def url(self):
        return self.request.url

    @property
    def path(self):
        uri = urlparse(self.request.path)
        return uri.path

    @property
    def base_url(self):
        return f"{self.request.scheme}://{self.request.host}:{self.request.port}"

    @property
    def method(self):
        return self.request.method

    @property
    def headers(self):
        return self.__filter_custom_headers(self.request.headers)

    @property
    def body(self):
        content = self.request.raw_content

        try:
            if isinstance(content, bytes):
                content = content.decode('utf-8')
        except:
            content = ''.join(map(chr, content))

        return content

    @property
    def parsed_body(self):
        return self.__body.get(self.content_type)

    @property
    def query(self):
        return self.request.query

    @property
    def content_type(self):
        return self.headers.get('content-type')

    @property
    def host(self):
        return self.request.host

    @property
    def port(self):
        return self.request.port

    @property
    def redact_rules(self) -> List[ParameterRule]:
        return self.__redact_rules
    
    @property
    def rewrite_rules(self) -> List[ParameterRule]:
        return self.__rewrite_rules

    def with_rewrite_rules(self, rules: List[RewriteRule]):
        if type(rules) == list:
            self.__rewrite_rules = self.select_parameter_rules(rules)
        return self 

    def with_redact_rules(self, rules: List[RewriteRule]):
        if type(rules) == list:
            self.__redact_rules = self.select_parameter_rules(rules)
        return self

    def redact(self):
        redacts = self.__redact_rules
        if len(redacts) != 0:
            self.__redact_headers(redacts)
            self.__redact_content(redacts)

    def rewrite(self):
        rewrites = self.__rewrite_rules
        if len(rewrites) != 0:
            self.__rewrite_headers(rewrites)
            self.__rewrite_content(rewrites)

    def select_parameter_rules(self, rules: List[RewriteRule]) -> List[ParameterRule]:
        # Find all the rules that match request url and method
        _rules = list(filter(self.__is_parameter_rule_selected, rules or []))
        
        if len(_rules) == 0:
            return []

        parameter_rules = list(map(lambda rule: rule.parameter_rules, _rules))

        return [item for sublist in parameter_rules for item in sublist] # flatten list

    def __is_parameter_rule_selected(self, rewrite_rule: RewriteRule):
        pattern = rewrite_rule.pattern

        try:
            url_matches = re.match(pattern, self.url)
        except re.error as e:
            Logger.instance().error(f"RegExp error '{e}' for {pattern}")
            return False

        method_matches = self.method in rewrite_rule.methods
        return url_matches and method_matches
    
    def __apply_rewrites(self, params: dict, rewrites: List[ParameterRule], handler: Callable):
        if len(rewrites) == 0:
            return params

        for param_name in params:
            for rewrite in rewrites:
                val = params[param_name]

                # For body params, will be given of the form key => [param1, param2]
                if type(val) == list and len(val) == 1:
                    val = val[0]

                # Convert to bytes
                params[param_name] = handler(rewrite, param_name, val)

    def __rewrite_headers(self, rewrites: List[ParameterRule]):
        self.__apply_headers(rewrites, self.__rewrite_handler)

    def __rewrite_content(self, rewrites: List[ParameterRule]):
        self.__apply_content(rewrites, self.__rewrite_handler)

    def __redact_headers(self, redacts: List[ParameterRule]):
        self.__apply_headers(redacts, self.__redact_handler)

    def __redact_content(self, redacts: List[ParameterRule]):
        self.__apply_content(redacts, self.__redact_handler)

    def __apply_headers(self, rewrites: List[ParameterRule], handler: Callable):
        rewrites = list(filter(lambda rewrite: rewrite.type == request_component.HEADER, rewrites))
        return self.__apply_rewrites(self.request.headers, rewrites, handler)

    def __apply_content(self, rewrites: List[ParameterRule], handler: Callable):
        parsed_content = self.__body.get(self.content_type)

        if isinstance(parsed_content, dict) or isinstance(parsed_content, multidict.MultiDictView):
            rewrites = list(filter(lambda rewrite: rewrite.type == request_component.BODY_PARAM, rewrites))
            rewritten_params = self.__apply_rewrites(parsed_content, rewrites, handler)

            self.__body.set(rewritten_params, self.content_type)

    def __redact_applies(self, rewrite: ParameterRule, param_name):
        if isinstance(param_name, bytes):
            param_name = param_name.decode('utf-8')
        
        pattern = rewrite.name

        try:
            return re.match(pattern, param_name)
        except re.error as e:
            Logger.instance().error(f"RegExp error '{e}' for {pattern}")
            return False

    def __redact_handler(self, rewrite: ParameterRule, param_name, val: Union[bytes, str]) -> bytes:
        # If the rule does not apply, set the param
        if not self.__redact_applies(rewrite, param_name):
            return val.encode() if isinstance(val, str) else val
        else:
            return '[REDACTED]'.encode()

    def __rewrite_handler(self, rewrite: ParameterRule, param_name, val: Union[bytes, str]) -> bytes:
        if not self.__redact_applies(rewrite, param_name):
            return val.encode() if isinstance(val, str) else val
        else:
            Logger.instance().debug(f"{bcolors.OKCYAN}Rewriting{bcolors.ENDC} {param_name} => {rewrite.value}")
            return (rewrite.value or '').encode()


    def __filter_custom_headers(self, request_headers: Headers):
        '''
        Remove custom headers
        '''
        _request_headers = Headers(**request_headers)

        headers = custom_headers.__dict__
        for key in headers:
            if key[0:2] == '__' and key[-2:] == '__':
                continue

            name = headers[key]

            if name not in request_headers:
                continue

            _request_headers.pop(name)

        return _request_headers