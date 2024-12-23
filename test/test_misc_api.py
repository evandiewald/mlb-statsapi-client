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
from swagger_client.api.misc_api import MiscApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMiscApi(unittest.TestCase):
    """MiscApi unit test stubs"""

    def setUp(self):
        self.api = MiscApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_aggregate_sort_enum(self):
        """Test case for aggregate_sort_enum

        List all stat fields  # noqa: E501
        """
        pass

    def test_baseball_stats(self):
        """Test case for baseball_stats

        List all baseball stats  # noqa: E501
        """
        pass

    def test_broadcast_availability_types(self):
        """Test case for broadcast_availability_types

        View broadcast availability options  # noqa: E501
        """
        pass

    def test_coaching_video_types(self):
        """Test case for coaching_video_types

        List all coaching video types  # noqa: E501
        """
        pass

    def test_event_status(self):
        """Test case for event_status

        List all possible event status types  # noqa: E501
        """
        pass

    def test_event_types(self):
        """Test case for event_types

        List all event types  # noqa: E501
        """
        pass

    def test_fielder_detail_types(self):
        """Test case for fielder_detail_types

        List fielder detail types  # noqa: E501
        """
        pass

    def test_free_game_types(self):
        """Test case for free_game_types

        View free game types  # noqa: E501
        """
        pass

    def test_game_status(self):
        """Test case for game_status

        List all status types  # noqa: E501
        """
        pass

    def test_game_types(self):
        """Test case for game_types

        List all game types  # noqa: E501
        """
        pass

    def test_gameday_types(self):
        """Test case for gameday_types

        List all gameday types  # noqa: E501
        """
        pass

    def test_get_lookup_values(self):
        """Test case for get_lookup_values

        View all lookup values  # noqa: E501
        """
        pass

    def test_group_by_types(self):
        """Test case for group_by_types

        List groupBy types  # noqa: E501
        """
        pass

    def test_hit_trajectories(self):
        """Test case for hit_trajectories

        List all hit trajectories  # noqa: E501
        """
        pass

    def test_job_types(self):
        """Test case for job_types

        List all job types  # noqa: E501
        """
        pass

    def test_languages(self):
        """Test case for languages

        List all support languages  # noqa: E501
        """
        pass

    def test_league_leader_types(self):
        """Test case for league_leader_types

        List all possible player league leader types  # noqa: E501
        """
        pass

    def test_logical_events(self):
        """Test case for logical_events

        List all logical event types  # noqa: E501
        """
        pass

    def test_media_state_types(self):
        """Test case for media_state_types

        View media state options  # noqa: E501
        """
        pass

    def test_metrics(self):
        """Test case for metrics

        List all possible metrics  # noqa: E501
        """
        pass

    def test_mound_visit_types(self):
        """Test case for mound_visit_types

        List all mound visit types  # noqa: E501
        """
        pass

    def test_performer_types(self):
        """Test case for performer_types

        List all possible performer types  # noqa: E501
        """
        pass

    def test_pitch_codes(self):
        """Test case for pitch_codes

        List all pitch codes  # noqa: E501
        """
        pass

    def test_pitch_types(self):
        """Test case for pitch_types

        List all pitch classification types  # noqa: E501
        """
        pass

    def test_platforms(self):
        """Test case for platforms

        List all possible platforms  # noqa: E501
        """
        pass

    def test_player_status_codes(self):
        """Test case for player_status_codes

        List all player status codes  # noqa: E501
        """
        pass

    def test_positions(self):
        """Test case for positions

        List all possible positions  # noqa: E501
        """
        pass

    def test_review_reasons(self):
        """Test case for review_reasons

        List all replay review reasons  # noqa: E501
        """
        pass

    def test_roof_types(self):
        """Test case for roof_types

        List all roof types  # noqa: E501
        """
        pass

    def test_roster_types(self):
        """Test case for roster_types

        List all possible roster types  # noqa: E501
        """
        pass

    def test_rule_settings(self):
        """Test case for rule_settings

        List all ruleSettings  # noqa: E501
        """
        pass

    def test_runner_detail_types(self):
        """Test case for runner_detail_types

        List runner detail types  # noqa: E501
        """
        pass

    def test_schedule_event_types(self):
        """Test case for schedule_event_types

        List all schedule event types  # noqa: E501
        """
        pass

    def test_schedule_types(self):
        """Test case for schedule_types

        List all possible schedule types  # noqa: E501
        """
        pass

    def test_sit_codes(self):
        """Test case for sit_codes

        List all situation codes  # noqa: E501
        """
        pass

    def test_sky(self):
        """Test case for sky

        List all sky options  # noqa: E501
        """
        pass

    def test_standings_types(self):
        """Test case for standings_types

        List all standings types  # noqa: E501
        """
        pass

    def test_stat_fields(self):
        """Test case for stat_fields

        List all stat fields  # noqa: E501
        """
        pass

    def test_stat_groups(self):
        """Test case for stat_groups

        List all stat groups  # noqa: E501
        """
        pass

    def test_stat_search_config(self):
        """Test case for stat_search_config

        Stats Search Config Endpoint  # noqa: E501
        """
        pass

    def test_stat_search_group_by_types(self):
        """Test case for stat_search_group_by_types

        List groupBy types  # noqa: E501
        """
        pass

    def test_stat_search_params(self):
        """Test case for stat_search_params

        List stat search parameters  # noqa: E501
        """
        pass

    def test_stat_search_stats(self):
        """Test case for stat_search_stats

        List stat search stats  # noqa: E501
        """
        pass

    def test_stat_types(self):
        """Test case for stat_types

        List all stat types  # noqa: E501
        """
        pass

    def test_statcast_position_types(self):
        """Test case for statcast_position_types

        List all statcast position types  # noqa: E501
        """
        pass

    def test_tracking_software_versions(self):
        """Test case for tracking_software_versions

        List the tracking software versions and notes  # noqa: E501
        """
        pass

    def test_tracking_system_owners(self):
        """Test case for tracking_system_owners

        List all tracking system owners  # noqa: E501
        """
        pass

    def test_tracking_vendors(self):
        """Test case for tracking_vendors

        List all tracking vendors  # noqa: E501
        """
        pass

    def test_tracking_versions(self):
        """Test case for tracking_versions

        List all tracking versions  # noqa: E501
        """
        pass

    def test_transaction_types(self):
        """Test case for transaction_types

        List all transaction types  # noqa: E501
        """
        pass

    def test_update_game_statuses(self):
        """Test case for update_game_statuses

        Clear all status types  # noqa: E501
        """
        pass

    def test_update_job_types(self):
        """Test case for update_job_types

        """
        pass

    def test_video_resolution_types(self):
        """Test case for video_resolution_types

        View video resolution options  # noqa: E501
        """
        pass

    def test_violation_types(self):
        """Test case for violation_types

        View available violationType options  # noqa: E501
        """
        pass

    def test_weather_trajectory_confidences(self):
        """Test case for weather_trajectory_confidences

        List all weather trajectories  # noqa: E501
        """
        pass

    def test_wind_direction(self):
        """Test case for wind_direction

        List all wind direction options  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
