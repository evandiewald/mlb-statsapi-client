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
from swagger_client.api.attendance_api import AttendanceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAttendanceApi(unittest.TestCase):
    """AttendanceApi unit test stubs"""

    def setUp(self):
        self.api = AttendanceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_team_attendance(self):
        """Test case for get_team_attendance

        Get team attendance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
