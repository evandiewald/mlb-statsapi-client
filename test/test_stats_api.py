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
from swagger_client.api.stats_api import StatsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStatsApi(unittest.TestCase):
    """StatsApi unit test stubs"""

    def setUp(self):
        self.api = StatsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_beast_stats(self):
        """Test case for beast_stats

        View stats from search  # noqa: E501
        """
        pass

    def test_get_outs_above_average(self):
        """Test case for get_outs_above_average

        Get outs above average for the current batter  # noqa: E501
        """
        pass

    def test_get_spray_chart(self):
        """Test case for get_spray_chart

        Get the spray chart info for the current batter  # noqa: E501
        """
        pass

    def test_get_stolen_base_probability(self):
        """Test case for get_stolen_base_probability

        Get the probability of a hit for the given hit data  # noqa: E501
        """
        pass

    def test_grouped_stats(self):
        """Test case for grouped_stats

        View grouped stats  # noqa: E501
        """
        pass

    def test_leaders2(self):
        """Test case for leaders2

        Get leaders for a statistic  # noqa: E501
        """
        pass

    def test_metric_stats(self):
        """Test case for metric_stats

        View metric stats  # noqa: E501
        """
        pass

    def test_stats2(self):
        """Test case for stats2

        View stats  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
