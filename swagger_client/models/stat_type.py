# coding: utf-8

"""
    Stats API Documentation

    Official API for Major League Baseball.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StatType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    PROJECTED = "PROJECTED"
    PROJECTED_ROS = "PROJECTED_ROS"
    YEAR_BY_YEAR = "YEAR_BY_YEAR"
    YEAR_BY_YEAR_ADVANCED = "YEAR_BY_YEAR_ADVANCED"
    YEAR_BY_YEAR_PLAYOFFS = "YEAR_BY_YEAR_PLAYOFFS"
    SEASON = "SEASON"
    STANDARD = "STANDARD"
    ADVANCED = "ADVANCED"
    CAREER = "CAREER"
    CAREER_REGULAR_SEASON = "CAREER_REGULAR_SEASON"
    CAREER_ADVANCED = "CAREER_ADVANCED"
    SEASON_ADVANCED = "SEASON_ADVANCED"
    CAREER_STAT_SPLITS = "CAREER_STAT_SPLITS"
    CAREER_PLAYOFFS = "CAREER_PLAYOFFS"
    GAME_LOG = "GAME_LOG"
    PLAY_LOG = "PLAY_LOG"
    PITCH_LOG = "PITCH_LOG"
    METRIC_LOG = "METRIC_LOG"
    METRIC_AVERAGES = "METRIC_AVERAGES"
    PITCH_ARSENAL = "PITCH_ARSENAL"
    OUTS_ABOVE_AVERAGE = "OUTS_ABOVE_AVERAGE"
    EXPECTED_STATISTICS = "EXPECTED_STATISTICS"
    SABERMETRICS = "SABERMETRICS"
    SPRAY_CHART = "SPRAY_CHART"
    TRACKING_STATISTICS = "TRACKING_STATISTICS"
    VS_PLAYER = "VS_PLAYER"
    VS_PLAYER_TOTAL = "VS_PLAYER_TOTAL"
    VS_PLAYER_5Y = "VS_PLAYER_5Y"
    VS_TEAM = "VS_TEAM"
    VS_TEAM_5Y = "VS_TEAM_5Y"
    VS_TEAM_TOTAL = "VS_TEAM_TOTAL"
    LAST_X_GAMES = "LAST_X_GAMES"
    BY_DATE_RANGE = "BY_DATE_RANGE"
    BY_DATE_RANGE_ADVANCED = "BY_DATE_RANGE_ADVANCED"
    BY_MONTH = "BY_MONTH"
    BY_MONTH_PLAYOFFS = "BY_MONTH_PLAYOFFS"
    BY_DAY_OF_WEEK = "BY_DAY_OF_WEEK"
    BY_DAY_OF_WEEK_PLAYOFFS = "BY_DAY_OF_WEEK_PLAYOFFS"
    HOME_AND_AWAY = "HOME_AND_AWAY"
    HOME_AND_AWAY_PLAYOFFS = "HOME_AND_AWAY_PLAYOFFS"
    WIN_LOSS = "WIN_LOSS"
    WIN_LOSS_PLAYOFFS = "WIN_LOSS_PLAYOFFS"
    RANKINGS = "RANKINGS"
    RANKINGS_BY_YEAR = "RANKINGS_BY_YEAR"
    STATS_SINGLE_SEASON = "STATS_SINGLE_SEASON"
    STATS_SINGLE_SEASON_ADVANCED = "STATS_SINGLE_SEASON_ADVANCED"
    HOT_COLD_ZONES = "HOT_COLD_ZONES"
    AVAILABLE_STATS = "AVAILABLE_STATS"
    OPPONENTS_FACED = "OPPONENTS_FACED"
    GAME_TYPE_STATS = "GAME_TYPE_STATS"
    FIRST_YEAR_STATS = "FIRST_YEAR_STATS"
    LAST_YEAR_STATS = "LAST_YEAR_STATS"
    STAT_SPLITS = "STAT_SPLITS"
    STAT_SPLITS_ADVANCED = "STAT_SPLITS_ADVANCED"
    AT_GAME_START = "AT_GAME_START"
    VS_OPPONENTS = "VS_OPPONENTS"
    SABERMETRICS_MULTI_TEAM = "SABERMETRICS_MULTI_TEAM"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """StatType - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StatType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StatType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other