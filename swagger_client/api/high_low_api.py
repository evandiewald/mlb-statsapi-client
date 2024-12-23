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


class HighLowApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def high_low(self, high_low_type, **kwargs):  # noqa: E501
        """View high/low stats by player or team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.high_low(high_low_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HighLowTypeEnum high_low_type: Type of high/low stats ('player', 'team', 'game') (required)
        :param list[StatGroup] stat_group: Comma delimited list of  categories of statistic to return. Available types in /api/v1/statGroups
        :param list[HighLowStatEnum] sort_stat: Comma delimited list of baseball stats to sort splits by.
        :param list[str] season: Comma delimited list of Seasons of play
        :param list[GameTypeEnum] game_type: Comma delimited list of type of Game. Available types in /api/v1/gameTypes
        :param int team_id: Unique Team Identifier. Format: 141, 147, etc
        :param int league_id: Unique League Identifier
        :param int sport_id: Top level organization of a sport
        :param int offset: The pointer to start for a return set; used for pagination
        :param int limit: Number of results to return
        :param list[str] fields: Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute
        :return: HighLowWrapperRestObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.high_low_with_http_info(high_low_type, **kwargs)  # noqa: E501
        else:
            (data) = self.high_low_with_http_info(high_low_type, **kwargs)  # noqa: E501
            return data

    def high_low_with_http_info(self, high_low_type, **kwargs):  # noqa: E501
        """View high/low stats by player or team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.high_low_with_http_info(high_low_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HighLowTypeEnum high_low_type: Type of high/low stats ('player', 'team', 'game') (required)
        :param list[StatGroup] stat_group: Comma delimited list of  categories of statistic to return. Available types in /api/v1/statGroups
        :param list[HighLowStatEnum] sort_stat: Comma delimited list of baseball stats to sort splits by.
        :param list[str] season: Comma delimited list of Seasons of play
        :param list[GameTypeEnum] game_type: Comma delimited list of type of Game. Available types in /api/v1/gameTypes
        :param int team_id: Unique Team Identifier. Format: 141, 147, etc
        :param int league_id: Unique League Identifier
        :param int sport_id: Top level organization of a sport
        :param int offset: The pointer to start for a return set; used for pagination
        :param int limit: Number of results to return
        :param list[str] fields: Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute
        :return: HighLowWrapperRestObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['high_low_type', 'stat_group', 'sort_stat', 'season', 'game_type', 'team_id', 'league_id', 'sport_id', 'offset', 'limit', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method high_low" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'high_low_type' is set
        if ('high_low_type' not in params or
                params['high_low_type'] is None):
            raise ValueError("Missing the required parameter `high_low_type` when calling `high_low`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'high_low_type' in params:
            path_params['highLowType'] = params['high_low_type']  # noqa: E501

        query_params = []
        if 'stat_group' in params:
            query_params.append(('statGroup', params['stat_group']))  # noqa: E501
            collection_formats['statGroup'] = 'multi'  # noqa: E501
        if 'sort_stat' in params:
            query_params.append(('sortStat', params['sort_stat']))  # noqa: E501
            collection_formats['sortStat'] = 'multi'  # noqa: E501
        if 'season' in params:
            query_params.append(('season', params['season']))  # noqa: E501
            collection_formats['season'] = 'multi'  # noqa: E501
        if 'game_type' in params:
            query_params.append(('gameType', params['game_type']))  # noqa: E501
            collection_formats['gameType'] = 'multi'  # noqa: E501
        if 'team_id' in params:
            query_params.append(('teamId', params['team_id']))  # noqa: E501
        if 'league_id' in params:
            query_params.append(('leagueId', params['league_id']))  # noqa: E501
        if 'sport_id' in params:
            query_params.append(('sportId', params['sport_id']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
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
            '/api/v1/highLow/{highLowType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HighLowWrapperRestObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def high_low_stats(self, **kwargs):  # noqa: E501
        """View high/low stat types  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.high_low_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[BaseballStatsTypeRestObject]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.high_low_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.high_low_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def high_low_stats_with_http_info(self, **kwargs):  # noqa: E501
        """View high/low stat types  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.high_low_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[BaseballStatsTypeRestObject]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method high_low_stats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/highLow/types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BaseballStatsTypeRestObject]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)