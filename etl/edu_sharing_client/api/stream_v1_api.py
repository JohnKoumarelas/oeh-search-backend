# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from edu_sharing_client.api_client import ApiClient


class STREAMV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_entry(self, body, repository, **kwargs):  # noqa: E501
        """add a new stream object.  # noqa: E501

        will return the object and add the id to the object if creation succeeded  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_entry(body, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StreamEntryInput body: Stream object to add (required)
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :return: StreamEntryInput
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_entry_with_http_info(body, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.add_entry_with_http_info(body, repository, **kwargs)  # noqa: E501
            return data

    def add_entry_with_http_info(self, body, repository, **kwargs):  # noqa: E501
        """add a new stream object.  # noqa: E501

        will return the object and add the id to the object if creation succeeded  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_entry_with_http_info(body, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StreamEntryInput body: Stream object to add (required)
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :return: StreamEntryInput
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_entry`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `add_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/stream/v1/add/{repository}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamEntryInput',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def can_access(self, repository, node, **kwargs):  # noqa: E501
        """test  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.can_access(repository, node, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str node: The property to aggregate (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.can_access_with_http_info(repository, node, **kwargs)  # noqa: E501
        else:
            (data) = self.can_access_with_http_info(repository, node, **kwargs)  # noqa: E501
            return data

    def can_access_with_http_info(self, repository, node, **kwargs):  # noqa: E501
        """test  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.can_access_with_http_info(repository, node, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str node: The property to aggregate (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'node']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method can_access" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `can_access`")  # noqa: E501
        # verify the required parameter 'node' is set
        if ('node' not in params or
                params['node'] is None):
            raise ValueError("Missing the required parameter `node` when calling `can_access`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'node' in params:
            path_params['node'] = params['node']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/stream/v1/access/{repository}/{node}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_entry(self, repository, entry, **kwargs):  # noqa: E501
        """delete a stream object  # noqa: E501

        the current user must be author of the given stream object  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_entry(repository, entry, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str entry: entry id to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_entry_with_http_info(repository, entry, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_entry_with_http_info(repository, entry, **kwargs)  # noqa: E501
            return data

    def delete_entry_with_http_info(self, repository, entry, **kwargs):  # noqa: E501
        """delete a stream object  # noqa: E501

        the current user must be author of the given stream object  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_entry_with_http_info(repository, entry, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str entry: entry id to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'entry']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `delete_entry`")  # noqa: E501
        # verify the required parameter 'entry' is set
        if ('entry' not in params or
                params['entry'] is None):
            raise ValueError("Missing the required parameter `entry` when calling `delete_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'entry' in params:
            path_params['entry'] = params['entry']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/stream/v1/delete/{repository}/{entry}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_property_values(self, repository, _property, **kwargs):  # noqa: E501
        """Get top values for a property  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_property_values(repository, _property, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str _property: The property to aggregate (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_property_values_with_http_info(repository, _property, **kwargs)  # noqa: E501
        else:
            (data) = self.get_property_values_with_http_info(repository, _property, **kwargs)  # noqa: E501
            return data

    def get_property_values_with_http_info(self, repository, _property, **kwargs):  # noqa: E501
        """Get top values for a property  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_property_values_with_http_info(repository, _property, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str _property: The property to aggregate (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', '_property']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_property_values" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_property_values`")  # noqa: E501
        # verify the required parameter '_property' is set
        if ('_property' not in params or
                params['_property'] is None):
            raise ValueError("Missing the required parameter `_property` when calling `get_property_values`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if '_property' in params:
            path_params['property'] = params['_property']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/stream/v1/properties/{repository}/{property}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search(self, repository, **kwargs):  # noqa: E501
        """Get the stream content for the current user with the given status.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search(repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param dict(str, str) body: map with property + value to search
        :param str status: Stream object status to search for
        :param str query: generic text to search for (in title or description)
        :param int max_items: maximum items per page
        :param int skip_count: skip a number of items
        :param list[str] sort_properties: sort properties, currently supported: created, priority, default: priority desc, created desc
        :param list[bool] sort_ascending: sort ascending, true if not set. Use multiple values to change the direction according to the given property at the same index
        :return: StreamList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_with_http_info(repository, **kwargs)  # noqa: E501
        else:
            (data) = self.search_with_http_info(repository, **kwargs)  # noqa: E501
            return data

    def search_with_http_info(self, repository, **kwargs):  # noqa: E501
        """Get the stream content for the current user with the given status.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_with_http_info(repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param dict(str, str) body: map with property + value to search
        :param str status: Stream object status to search for
        :param str query: generic text to search for (in title or description)
        :param int max_items: maximum items per page
        :param int skip_count: skip a number of items
        :param list[str] sort_properties: sort properties, currently supported: created, priority, default: priority desc, created desc
        :param list[bool] sort_ascending: sort ascending, true if not set. Use multiple values to change the direction according to the given property at the same index
        :return: StreamList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'body', 'status', 'query', 'max_items', 'skip_count', 'sort_properties', 'sort_ascending']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `search`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'max_items' in params:
            query_params.append(('maxItems', params['max_items']))  # noqa: E501
        if 'skip_count' in params:
            query_params.append(('skipCount', params['skip_count']))  # noqa: E501
        if 'sort_properties' in params:
            query_params.append(('sortProperties', params['sort_properties']))  # noqa: E501
            collection_formats['sortProperties'] = 'multi'  # noqa: E501
        if 'sort_ascending' in params:
            query_params.append(('sortAscending', params['sort_ascending']))  # noqa: E501
            collection_formats['sortAscending'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/stream/v1/search/{repository}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_entry(self, repository, entry, authority, status, **kwargs):  # noqa: E501
        """update status for a stream object and authority  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_entry(repository, entry, authority, status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str entry: entry id to update (required)
        :param str authority: authority to set/change status (required)
        :param str status: New status for this authority (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_entry_with_http_info(repository, entry, authority, status, **kwargs)  # noqa: E501
        else:
            (data) = self.update_entry_with_http_info(repository, entry, authority, status, **kwargs)  # noqa: E501
            return data

    def update_entry_with_http_info(self, repository, entry, authority, status, **kwargs):  # noqa: E501
        """update status for a stream object and authority  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_entry_with_http_info(repository, entry, authority, status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str entry: entry id to update (required)
        :param str authority: authority to set/change status (required)
        :param str status: New status for this authority (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'entry', 'authority', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `update_entry`")  # noqa: E501
        # verify the required parameter 'entry' is set
        if ('entry' not in params or
                params['entry'] is None):
            raise ValueError("Missing the required parameter `entry` when calling `update_entry`")  # noqa: E501
        # verify the required parameter 'authority' is set
        if ('authority' not in params or
                params['authority'] is None):
            raise ValueError("Missing the required parameter `authority` when calling `update_entry`")  # noqa: E501
        # verify the required parameter 'status' is set
        if ('status' not in params or
                params['status'] is None):
            raise ValueError("Missing the required parameter `status` when calling `update_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'entry' in params:
            path_params['entry'] = params['entry']  # noqa: E501

        query_params = []
        if 'authority' in params:
            query_params.append(('authority', params['authority']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/stream/v1/status/{repository}/{entry}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
