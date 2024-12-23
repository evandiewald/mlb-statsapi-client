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


class AttendanceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_team_attendance(self, **kwargs):  # noqa: E501
        """Get team attendance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_attendance(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] team_id: Unique Team Identifier. Format: 141, 147, etc
        :param list[int] league_id: Comma delimited list of Unique league identifiers
        :param list[str] season: Comma delimited list of Seasons of play
        :param LeagueListsEnum league_list_id: Unique League List Identifier
        :param list[GameTypeEnum] game_type: Type of Game. Available types in /api/v1/gameTypes
        :param date _date: Date of Game. Format: YYYY-MM-DD
        :param date start_date: Start date for range of data (must be used with end date). Format: MM/DD/YYYY
        :param date end_date: End date for range of data (must be used with start date). Format: MM/DD/YYYY
        :param list[str] fields: Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute
        :return: AttendanceRestObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_team_attendance_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_team_attendance_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_team_attendance_with_http_info(self, **kwargs):  # noqa: E501
        """Get team attendance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_attendance_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] team_id: Unique Team Identifier. Format: 141, 147, etc
        :param list[int] league_id: Comma delimited list of Unique league identifiers
        :param list[str] season: Comma delimited list of Seasons of play
        :param LeagueListsEnum league_list_id: Unique League List Identifier
        :param list[GameTypeEnum] game_type: Type of Game. Available types in /api/v1/gameTypes
        :param date _date: Date of Game. Format: YYYY-MM-DD
        :param date start_date: Start date for range of data (must be used with end date). Format: MM/DD/YYYY
        :param date end_date: End date for range of data (must be used with start date). Format: MM/DD/YYYY
        :param list[str] fields: Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute
        :return: AttendanceRestObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_id', 'league_id', 'season', 'league_list_id', 'game_type', '_date', 'start_date', 'end_date', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_attendance" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'team_id' in params:
            query_params.append(('teamId', params['team_id']))  # noqa: E501
            collection_formats['teamId'] = 'multi'  # noqa: E501
        if 'league_id' in params:
            query_params.append(('leagueId', params['league_id']))  # noqa: E501
            collection_formats['leagueId'] = 'multi'  # noqa: E501
        if 'season' in params:
            query_params.append(('season', params['season']))  # noqa: E501
            collection_formats['season'] = 'multi'  # noqa: E501
        if 'league_list_id' in params:
            query_params.append(('leagueListId', params['league_list_id']))  # noqa: E501
        if 'game_type' in params:
            query_params.append(('gameType', params['game_type']))  # noqa: E501
            collection_formats['gameType'] = 'multi'  # noqa: E501
        if '_date' in params:
            query_params.append(('date', params['_date']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
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
            '/api/v1/attendance', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AttendanceRestObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)