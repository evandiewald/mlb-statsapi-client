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
from swagger_client.api.skeletal_api import SkeletalApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSkeletalApi(unittest.TestCase):
    """SkeletalApi unit test stubs"""

    def setUp(self):
        self.api = SkeletalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_skeletal_chunked(self):
        """Test case for skeletal_chunked

        View Skeletal Data by playId and gameId chunked  # noqa: E501
        """
        pass

    def test_skeletal_data_file_names(self):
        """Test case for skeletal_data_file_names

        View Skeletal Data by playId and gameId files  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()