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


class VenuesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def venues(self, venue_id, **kwargs):  # noqa: E501
        """View venue info  # noqa: E501

        This endpoint allows you to pull venues  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.venues(venue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int venue_id: Unique Venue Identifier (required)
        :param list[int] venue_ids: Comma delimited list of Unique venue identifiers
        :param int league_id: Unique League Identifier
        :param list[int] league_ids: Comma delimited list of Unique league identifiers
        :param GameTypeEnum game_type: Type of Game. Available types in /api/v1/gameTypes
        :param list[GameTypeEnum] game_types: Comma delimited list of type of Game. Available types in /api/v1/gameTypes
        :param str season: Season of play
        :param list[str] seasons: Comma delimited list of Seasons of play
        :param list[str] fields: Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute
        :param bool active: Whether or not a player is active
        :param bool include_events:
        :param int sport_id: Top level organization of a sport
        :param list[int] sport_ids: Comma delimited list of top level organizations of a sport
        :return: VenuesRestObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.venues_with_http_info(venue_id, **kwargs)  # noqa: E501
        else:
            (data) = self.venues_with_http_info(venue_id, **kwargs)  # noqa: E501
            return data

    def venues_with_http_info(self, venue_id, **kwargs):  # noqa: E501
        """View venue info  # noqa: E501

        This endpoint allows you to pull venues  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.venues_with_http_info(venue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int venue_id: Unique Venue Identifier (required)
        :param list[int] venue_ids: Comma delimited list of Unique venue identifiers
        :param int league_id: Unique League Identifier
        :param list[int] league_ids: Comma delimited list of Unique league identifiers
        :param GameTypeEnum game_type: Type of Game. Available types in /api/v1/gameTypes
        :param list[GameTypeEnum] game_types: Comma delimited list of type of Game. Available types in /api/v1/gameTypes
        :param str season: Season of play
        :param list[str] seasons: Comma delimited list of Seasons of play
        :param list[str] fields: Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute
        :param bool active: Whether or not a player is active
        :param bool include_events:
        :param int sport_id: Top level organization of a sport
        :param list[int] sport_ids: Comma delimited list of top level organizations of a sport
        :return: VenuesRestObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['venue_id', 'venue_ids', 'league_id', 'league_ids', 'game_type', 'game_types', 'season', 'seasons', 'fields', 'active', 'include_events', 'sport_id', 'sport_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method venues" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'venue_id' is set
        if ('venue_id' not in params or
                params['venue_id'] is None):
            raise ValueError("Missing the required parameter `venue_id` when calling `venues`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'venue_id' in params:
            path_params['venueId'] = params['venue_id']  # noqa: E501

        query_params = []
        if 'venue_ids' in params:
            query_params.append(('venueIds', params['venue_ids']))  # noqa: E501
            collection_formats['venueIds'] = 'multi'  # noqa: E501
        if 'league_id' in params:
            query_params.append(('leagueId', params['league_id']))  # noqa: E501
        if 'league_ids' in params:
            query_params.append(('leagueIds', params['league_ids']))  # noqa: E501
            collection_formats['leagueIds'] = 'multi'  # noqa: E501
        if 'game_type' in params:
            query_params.append(('gameType', params['game_type']))  # noqa: E501
        if 'game_types' in params:
            query_params.append(('gameTypes', params['game_types']))  # noqa: E501
            collection_formats['gameTypes'] = 'multi'  # noqa: E501
        if 'season' in params:
            query_params.append(('season', params['season']))  # noqa: E501
        if 'seasons' in params:
            query_params.append(('seasons', params['seasons']))  # noqa: E501
            collection_formats['seasons'] = 'multi'  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'active' in params:
            query_params.append(('active', params['active']))  # noqa: E501
        if 'include_events' in params:
            query_params.append(('includeEvents', params['include_events']))  # noqa: E501
        if 'sport_id' in params:
            query_params.append(('sportId', params['sport_id']))  # noqa: E501
        if 'sport_ids' in params:
            query_params.append(('sportIds', params['sport_ids']))  # noqa: E501
            collection_formats['sportIds'] = 'multi'  # noqa: E501

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
            '/api/v1/venues', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VenuesRestObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def venues1(self, venue_id, **kwargs):  # noqa: E501
        """View venue info  # noqa: E501

        This endpoint allows you to pull venues  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.venues1(venue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int venue_id: Unique Venue Identifier (required)
        :param list[int] venue_ids: Comma delimited list of Unique venue identifiers
        :param int league_id: Unique League Identifier
        :param list[int] league_ids: Comma delimited list of Unique league identifiers
        :param GameTypeEnum game_type: Type of Game. Available types in /api/v1/gameTypes
        :param list[GameTypeEnum] game_types: Comma delimited list of type of Game. Available types in /api/v1/gameTypes
        :param str season: Season of play
        :param list[str] seasons: Comma delimited list of Seasons of play
        :param list[str] fields: Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute
        :param bool active: Whether or not a player is active
        :param bool include_events:
        :param int sport_id: Top level organization of a sport
        :param list[int] sport_ids: Comma delimited list of top level organizations of a sport
        :return: VenuesRestObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.venues1_with_http_info(venue_id, **kwargs)  # noqa: E501
        else:
            (data) = self.venues1_with_http_info(venue_id, **kwargs)  # noqa: E501
            return data

    def venues1_with_http_info(self, venue_id, **kwargs):  # noqa: E501
        """View venue info  # noqa: E501

        This endpoint allows you to pull venues  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.venues1_with_http_info(venue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int venue_id: Unique Venue Identifier (required)
        :param list[int] venue_ids: Comma delimited list of Unique venue identifiers
        :param int league_id: Unique League Identifier
        :param list[int] league_ids: Comma delimited list of Unique league identifiers
        :param GameTypeEnum game_type: Type of Game. Available types in /api/v1/gameTypes
        :param list[GameTypeEnum] game_types: Comma delimited list of type of Game. Available types in /api/v1/gameTypes
        :param str season: Season of play
        :param list[str] seasons: Comma delimited list of Seasons of play
        :param list[str] fields: Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute
        :param bool active: Whether or not a player is active
        :param bool include_events:
        :param int sport_id: Top level organization of a sport
        :param list[int] sport_ids: Comma delimited list of top level organizations of a sport
        :return: VenuesRestObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['venue_id', 'venue_ids', 'league_id', 'league_ids', 'game_type', 'game_types', 'season', 'seasons', 'fields', 'active', 'include_events', 'sport_id', 'sport_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method venues1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'venue_id' is set
        if ('venue_id' not in params or
                params['venue_id'] is None):
            raise ValueError("Missing the required parameter `venue_id` when calling `venues1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'venue_id' in params:
            path_params['venueId'] = params['venue_id']  # noqa: E501

        query_params = []
        if 'venue_ids' in params:
            query_params.append(('venueIds', params['venue_ids']))  # noqa: E501
            collection_formats['venueIds'] = 'multi'  # noqa: E501
        if 'league_id' in params:
            query_params.append(('leagueId', params['league_id']))  # noqa: E501
        if 'league_ids' in params:
            query_params.append(('leagueIds', params['league_ids']))  # noqa: E501
            collection_formats['leagueIds'] = 'multi'  # noqa: E501
        if 'game_type' in params:
            query_params.append(('gameType', params['game_type']))  # noqa: E501
        if 'game_types' in params:
            query_params.append(('gameTypes', params['game_types']))  # noqa: E501
            collection_formats['gameTypes'] = 'multi'  # noqa: E501
        if 'season' in params:
            query_params.append(('season', params['season']))  # noqa: E501
        if 'seasons' in params:
            query_params.append(('seasons', params['seasons']))  # noqa: E501
            collection_formats['seasons'] = 'multi'  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'active' in params:
            query_params.append(('active', params['active']))  # noqa: E501
        if 'include_events' in params:
            query_params.append(('includeEvents', params['include_events']))  # noqa: E501
        if 'sport_id' in params:
            query_params.append(('sportId', params['sport_id']))  # noqa: E501
        if 'sport_ids' in params:
            query_params.append(('sportIds', params['sport_ids']))  # noqa: E501
            collection_formats['sportIds'] = 'multi'  # noqa: E501

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
            '/api/v1/venues/{venueId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VenuesRestObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)