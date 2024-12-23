# coding: utf-8

"""
    Stats API Documentation

    Official API for Major League Baseball.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.analytics_api import AnalyticsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAnalyticsApi(unittest.TestCase):
    """AnalyticsApi unit test stubs"""

    def setUp(self):
        self.api = AnalyticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_context_metrics(self):
        """Test case for context_metrics

        Get context metrics for a specific gamePk.  # noqa: E501
        """
        pass

    def test_context_metrics_with_averages(self):
        """Test case for context_metrics_with_averages

        Get a json file containing raw coordinate data and refined calculated metrics.  # noqa: E501
        """
        pass

    def test_context_metrics_with_averages_post(self):
        """Test case for context_metrics_with_averages_post

        Get a json file containing raw coordinate data and refined calculated metrics.  # noqa: E501
        """
        pass

    def test_game_guids(self):
        """Test case for game_guids

        Get the GUIDs (plays) for a specific game.   # noqa: E501
        """
        pass

    def test_game_guids_from_postgres_range(self):
        """Test case for game_guids_from_postgres_range

        Get the GUIDs (plays) for a specific game.   # noqa: E501
        """
        pass

    def test_game_guids_from_postgres_range_by_game(self):
        """Test case for game_guids_from_postgres_range_by_game

        Get all games by updated date.  # noqa: E501
        """
        pass

    def test_game_last_pitch(self):
        """Test case for game_last_pitch

        Get the last pitch for a list of games  # noqa: E501
        """
        pass

    def test_home_run_ballparks(self):
        """Test case for home_run_ballparks

        Get if the play is a home run is each park for a specific play.  # noqa: E501
        """
        pass

    def test_parsed_json_formatted_analytics(self):
        """Test case for parsed_json_formatted_analytics

        Get Statcast data for a specific play.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
