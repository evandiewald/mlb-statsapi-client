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


class PredictionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_props(self, **kwargs):  # noqa: E501
        """Get play-level predictions based on input scenarios  # noqa: E501

        This endpoint allows you to get play-level predictions based on input scenarios  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_props(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int batter_id: Unique Player Identifier. Format: 434538, 429665, etc
        :param int pitcher_id: Unique Player Identifier. Format: 434538, 429665, etc
        :param int venue_id: Unique Venue Identifier
        :param str bat_side: Bat side of hitter
        :param str pitch_hand: Handedness of pitcher
        :param str batter_position: Position abbreviation. Format: SS, P, 1B, etc
        :param str pitcher_position: Position abbreviation. Format: SS, P, 1B, etc
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_props_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_props_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_props_with_http_info(self, **kwargs):  # noqa: E501
        """Get play-level predictions based on input scenarios  # noqa: E501

        This endpoint allows you to get play-level predictions based on input scenarios  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_props_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int batter_id: Unique Player Identifier. Format: 434538, 429665, etc
        :param int pitcher_id: Unique Player Identifier. Format: 434538, 429665, etc
        :param int venue_id: Unique Venue Identifier
        :param str bat_side: Bat side of hitter
        :param str pitch_hand: Handedness of pitcher
        :param str batter_position: Position abbreviation. Format: SS, P, 1B, etc
        :param str pitcher_position: Position abbreviation. Format: SS, P, 1B, etc
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batter_id', 'pitcher_id', 'venue_id', 'bat_side', 'pitch_hand', 'batter_position', 'pitcher_position']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_props" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'batter_id' in params:
            query_params.append(('batterId', params['batter_id']))  # noqa: E501
        if 'pitcher_id' in params:
            query_params.append(('pitcherId', params['pitcher_id']))  # noqa: E501
        if 'venue_id' in params:
            query_params.append(('venueId', params['venue_id']))  # noqa: E501
        if 'bat_side' in params:
            query_params.append(('batSide', params['bat_side']))  # noqa: E501
        if 'pitch_hand' in params:
            query_params.append(('pitchHand', params['pitch_hand']))  # noqa: E501
        if 'batter_position' in params:
            query_params.append(('batterPosition', params['batter_position']))  # noqa: E501
        if 'pitcher_position' in params:
            query_params.append(('pitcherPosition', params['pitcher_position']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/props/play/predictions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_props_adjust(self, game_pk, **kwargs):  # noqa: E501
        """Get play-level predictions based on input scenarios  # noqa: E501

        This endpoint allows you to get play-level predictions based on input scenarios  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_props_adjust(game_pk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int game_pk: Unique Primary Key Representing a Game (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_props_adjust_with_http_info(game_pk, **kwargs)  # noqa: E501
        else:
            (data) = self.get_props_adjust_with_http_info(game_pk, **kwargs)  # noqa: E501
            return data

    def get_props_adjust_with_http_info(self, game_pk, **kwargs):  # noqa: E501
        """Get play-level predictions based on input scenarios  # noqa: E501

        This endpoint allows you to get play-level predictions based on input scenarios  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_props_adjust_with_http_info(game_pk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int game_pk: Unique Primary Key Representing a Game (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['game_pk']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_props_adjust" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'game_pk' is set
        if ('game_pk' not in params or
                params['game_pk'] is None):
            raise ValueError("Missing the required parameter `game_pk` when calling `get_props_adjust`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'game_pk' in params:
            query_params.append(('gamePk', params['game_pk']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/props/play/predictions/adjust', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
