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
from swagger_client.api.high_low_api import HighLowApi  # noqa: E501
from swagger_client.rest import ApiException


class TestHighLowApi(unittest.TestCase):
    """HighLowApi unit test stubs"""

    def setUp(self):
        self.api = HighLowApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_high_low(self):
        """Test case for high_low

        View high/low stats by player or team  # noqa: E501
        """
        pass

    def test_high_low_stats(self):
        """Test case for high_low_stats

        View high/low stat types  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
