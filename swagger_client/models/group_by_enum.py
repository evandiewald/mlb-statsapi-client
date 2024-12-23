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

class GroupByEnum(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    PLAYER = "PLAYER"
    PITCHER = "PITCHER"
    BATTER = "BATTER"
    VENUE = "VENUE"
    TEAM = "TEAM"
    BATTING_TEAM = "BATTING_TEAM"
    FIELDING_TEAM = "FIELDING_TEAM"
    SPORT = "SPORT"
    BATTING_SPORT = "BATTING_SPORT"
    FIELDING_SPORT = "FIELDING_SPORT"
    LEAGUE = "LEAGUE"
    BATTING_LEAGUE = "BATTING_LEAGUE"
    FIELDING_LEAGUE = "FIELDING_LEAGUE"
    DIVISION = "DIVISION"
    BATTING_DIVISION = "BATTING_DIVISION"
    FIELDING_DIVISION = "FIELDING_DIVISION"
    SEASON = "SEASON"
    POSITION = "POSITION"
    STAT_GROUP = "STAT_GROUP"
    GAME = "GAME"
    PITCH_TYPE = "PITCH_TYPE"
    EVENT_TYPE = "EVENT_TYPE"
    PITCH_CODE = "PITCH_CODE"
    BATTING_ORDER = "BATTING_ORDER"
    PITCH_HAND = "PITCH_HAND"
    BAT_SIDE = "BAT_SIDE"
    MONTH = "MONTH"
    DAY_OF_WEEK = "DAY_OF_WEEK"
    DAY_NIGHT = "DAY_NIGHT"
    GAME_TYPE = "GAME_TYPE"
    HOME_AWAY = "HOME_AWAY"
    BASE_STATE = "BASE_STATE"
    RISP = "RISP"
    INNING = "INNING"
    COUNT_BALLS = "COUNT_BALLS"
    COUNT_STRIKES = "COUNT_STRIKES"
    COUNT_OUTS = "COUNT_OUTS"
    HIT_TRAJECTORY = "HIT_TRAJECTORY"
    PITCH_NUMBER = "PITCH_NUMBER"
    AT_BAT_NUMBER = "AT_BAT_NUMBER"
    RUNNER_FIRST = "RUNNER_FIRST"
    RUNNER_SECOND = "RUNNER_SECOND"
    RUNNER_THIRD = "RUNNER_THIRD"
    CATCHER = "CATCHER"
    FIRST_BASEMAN = "FIRST_BASEMAN"
    SECOND_BASEMAN = "SECOND_BASEMAN"
    SHORTSTOP = "SHORTSTOP"
    THIRD_BASEMAN = "THIRD_BASEMAN"
    LEFT_FIELDER = "LEFT_FIELDER"
    CENTER_FIELDER = "CENTER_FIELDER"
    RIGHT_FIELDER = "RIGHT_FIELDER"
    DESIGNATED_HITTER = "DESIGNATED_HITTER"
    DEFENSIVE_ALIGNMENT = "DEFENSIVE_ALIGNMENT"
    SITUATION_CODE = "SITUATION_CODE"
    OPPONENT_TEAM = "OPPONENT_TEAM"
    HIT_DIRECTION = "HIT_DIRECTION"
    PITCH_ZONE = "PITCH_ZONE"
    DATE = "DATE"
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
        """GroupByEnum - a model defined in Swagger"""  # noqa: E501
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
        if issubclass(GroupByEnum, dict):
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
        if not isinstance(other, GroupByEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
