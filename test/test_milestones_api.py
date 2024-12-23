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
from swagger_client.api.milestones_api import MilestonesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMilestonesApi(unittest.TestCase):
    """MilestonesApi unit test stubs"""

    def setUp(self):
        self.api = MilestonesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_achievement_statuses(self):
        """Test case for achievement_statuses

        View available achievementStatus options  # noqa: E501
        """
        pass

    def test_milestone_durations(self):
        """Test case for milestone_durations

        View available milestoneDurations options  # noqa: E501
        """
        pass

    def test_milestone_lookups(self):
        """Test case for milestone_lookups

        View available milestoneLookup options  # noqa: E501
        """
        pass

    def test_milestone_statistics(self):
        """Test case for milestone_statistics

        View available milestone statistics options  # noqa: E501
        """
        pass

    def test_milestone_types(self):
        """Test case for milestone_types

        View available milestoneType options  # noqa: E501
        """
        pass

    def test_milestones(self):
        """Test case for milestones

        View pending and achieved milestones.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
