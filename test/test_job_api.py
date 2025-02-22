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
from swagger_client.api.job_api import JobApi  # noqa: E501
from swagger_client.rest import ApiException


class TestJobApi(unittest.TestCase):
    """JobApi unit test stubs"""

    def setUp(self):
        self.api = JobApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_datacasters(self):
        """Test case for datacasters

        Get datacaster jobs  # noqa: E501
        """
        pass

    def test_get_jobs_by_type(self):
        """Test case for get_jobs_by_type

        Get jobs by type  # noqa: E501
        """
        pass

    def test_official_scorers(self):
        """Test case for official_scorers

        Get official scorers  # noqa: E501
        """
        pass

    def test_umpire_schedule(self):
        """Test case for umpire_schedule

        Get umpires and associated game for umpireId  # noqa: E501
        """
        pass

    def test_umpires(self):
        """Test case for umpires

        Get umpires  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
