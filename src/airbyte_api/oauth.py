"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from airbyte_api import models, utils
from airbyte_api._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext, HookContext

class OAuth:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def oauth_callback(self, request: models.OauthCallbackRequest) -> models.OauthCallbackResponse:
        r"""Receive OAuth callbacks
        Redirected to by identity providers after authentication.
        """
        hook_ctx = HookContext(operation_id='oauthCallback', oauth2_scopes=[], security_source=None)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/oauth/callback'
        
        headers = {}
        query_params = {}
        
        query_params = { **utils.get_query_params(request), **query_params }
        headers['Accept'] = '*/*'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = models.OauthCallbackResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type') or '', raw_response=http_res)
        
        if http_res.status_code == 302:
            pass
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise models.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise models.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    

