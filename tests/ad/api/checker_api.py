# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from ad.api_client import ApiClient


class CheckerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_checkers_get(self, x_api_key, **kwargs):   
        """Retrieve all checker instances.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_checkers_get(x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_api_key: The user's API key (required)
        :return: list[InlineResponse20015]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_checkers_get_with_http_info(x_api_key, **kwargs)   
        else:
            (data) = self.api_checkers_get_with_http_info(x_api_key, **kwargs)   
            return data

    def api_checkers_get_with_http_info(self, x_api_key, **kwargs):   
        """Retrieve all checker instances.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_checkers_get_with_http_info(x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_api_key: The user's API key (required)
        :return: list[InlineResponse20015]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_api_key']   
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_checkers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_api_key' is set
        if ('x_api_key' not in params or
                params['x_api_key'] is None):
            raise ValueError("Missing the required parameter `x_api_key` when calling `api_checkers_get`")   

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_api_key' in params:
            header_params['x-api-key'] = params['x_api_key']   

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])   

        # Authentication setting
        auth_settings = ['ApiKey']   

        return self.api_client.call_api(
            '/api/checkers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20015]',   
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_checkers_id_get(self, x_api_key, id, **kwargs):   
        """Get checker instance by id.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_checkers_id_get(x_api_key, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_api_key: The user's API key (required)
        :param str id: (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_checkers_id_get_with_http_info(x_api_key, id, **kwargs)   
        else:
            (data) = self.api_checkers_id_get_with_http_info(x_api_key, id, **kwargs)   
            return data

    def api_checkers_id_get_with_http_info(self, x_api_key, id, **kwargs):   
        """Get checker instance by id.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_checkers_id_get_with_http_info(x_api_key, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_api_key: The user's API key (required)
        :param str id: (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_api_key', 'id']   
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_checkers_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_api_key' is set
        if ('x_api_key' not in params or
                params['x_api_key'] is None):
            raise ValueError("Missing the required parameter `x_api_key` when calling `api_checkers_id_get`")   
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_checkers_id_get`")   

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']   

        query_params = []

        header_params = {}
        if 'x_api_key' in params:
            header_params['x-api-key'] = params['x_api_key']   

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])   

        # Authentication setting
        auth_settings = ['ApiKey']   

        return self.api_client.call_api(
            '/api/checkers/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20016',   
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
