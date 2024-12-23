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
from swagger_client.api.uniforms_api import UniformsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUniformsApi(unittest.TestCase):
    """UniformsApi unit test stubs"""

    def setUp(self):
        self.api = UniformsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_uniforms_by_game(self):
        """Test case for uniforms_by_game

        View Game Uniform info  # noqa: E501
        """
        pass

    def test_uniforms_by_team(self):
        """Test case for uniforms_by_team

        View Team Uniform info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()