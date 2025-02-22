# coding: utf-8

"""
    Stats API Documentation

    Official API for Major League Baseball.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ReviewsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_review_info(self, sport_id, season, **kwargs):  # noqa: E501
        """Get review info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_review_info(sport_id, season, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sport_id: Unique Team Identifier. Format: 141, 147, etc (required)
        :param str season: Comma delimited list of Seasons of play (required)
        :param GameTypeEnum game_type: Type of Game. Available types in /api/v1/gameTypes
        :param list[str] fields: Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute
        :return: StatContainerRestObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_review_info_with_http_info(sport_id, season, **kwargs)  # noqa: E501
        else:
            (data) = self.get_review_info_with_http_info(sport_id, season, **kwargs)  # noqa: E501
            return data

    def get_review_info_with_http_info(self, sport_id, season, **kwargs):  # noqa: E501
        """Get review info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_review_info_with_http_info(sport_id, season, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sport_id: Unique Team Identifier. Format: 141, 147, etc (required)
        :param str season: Comma delimited list of Seasons of play (required)
        :param GameTypeEnum game_type: Type of Game. Available types in /api/v1/gameTypes
        :param list[str] fields: Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute
        :return: StatContainerRestObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sport_id', 'season', 'game_type', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_review_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sport_id' is set
        if ('sport_id' not in params or
                params['sport_id'] is None):
            raise ValueError("Missing the required parameter `sport_id` when calling `get_review_info`")  # noqa: E501
        # verify the required parameter 'season' is set
        if ('season' not in params or
                params['season'] is None):
            raise ValueError("Missing the required parameter `season` when calling `get_review_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sport_id' in params:
            query_params.append(('sportId', params['sport_id']))  # noqa: E501
        if 'season' in params:
            query_params.append(('season', params['season']))  # noqa: E501
        if 'game_type' in params:
            query_params.append(('gameType', params['game_type']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501

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
            '/api/v1/review', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatContainerRestObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
