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
from swagger_client.api.game_api import GameApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGameApi(unittest.TestCase):
    """GameApi unit test stubs"""

    def setUp(self):
        self.api = GameApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_boxscore(self):
        """Test case for boxscore

        Get game boxscore.  # noqa: E501
        """
        pass

    def test_color_feed(self):
        """Test case for color_feed

        Get game color feed.  # noqa: E501
        """
        pass

    def test_color_timestamps(self):
        """Test case for color_timestamps

        Retrieve all of the color timestamps for a game.  # noqa: E501
        """
        pass

    def test_content(self):
        """Test case for content

        Retrieve all content for a game.  # noqa: E501
        """
        pass

    def test_current_game_stats1(self):
        """Test case for current_game_stats1

        View a game change log  # noqa: E501
        """
        pass

    def test_get_game_context_metrics(self):
        """Test case for get_game_context_metrics

        Get the context metrics for this game based on its current state  # noqa: E501
        """
        pass

    def test_get_game_with_metrics(self):
        """Test case for get_game_with_metrics

        Get game info with metrics  # noqa: E501
        """
        pass

    def test_get_win_probability(self):
        """Test case for get_win_probability

        Get the win probability for this game  # noqa: E501
        """
        pass

    def test_linescore(self):
        """Test case for linescore

        Get game linescore  # noqa: E501
        """
        pass

    def test_live_game_diff_patch_v1(self):
        """Test case for live_game_diff_patch_v1

        Get live game status diffPatch.  # noqa: E501
        """
        pass

    def test_live_game_v1(self):
        """Test case for live_game_v1

        Get live game status.  # noqa: E501
        """
        pass

    def test_live_timestampv11(self):
        """Test case for live_timestampv11

        Retrieve all of the play timestamps for a game.  # noqa: E501
        """
        pass

    def test_play_by_play(self):
        """Test case for play_by_play

        Get game play By Play  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
