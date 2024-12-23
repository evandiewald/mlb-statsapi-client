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
from swagger_client.api.sports_api import SportsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSportsApi(unittest.TestCase):
    """SportsApi unit test stubs"""

    def setUp(self):
        self.api = SportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_sport_ballot(self):
        """Test case for all_sport_ballot

        Get ALL MLB ballot for sport  # noqa: E501
        """
        pass

    def test_sport_players(self):
        """Test case for sport_players

        Get all players for a sport level  # noqa: E501
        """
        pass

    def test_sports(self):
        """Test case for sports

        Get sports information  # noqa: E501
        """
        pass

    def test_sports1(self):
        """Test case for sports1

        Get sports information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
