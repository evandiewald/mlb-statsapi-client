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

class BatterDetailType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    AT_BAT = "AT_BAT"
    AT_BAT_SCORING_POSITION = "AT_BAT_SCORING_POSITION"
    SINGLE = "SINGLE"
    DOUBLE = "DOUBLE"
    TRIPLE = "TRIPLE"
    GAME = "GAME"
    CATCHER_INTERFERENCE = "CATCHER_INTERFERENCE"
    HOME_RUN = "HOME_RUN"
    STRIKEOUT = "STRIKEOUT"
    WALK = "WALK"
    INTENT_WALK = "INTENT_WALK"
    RUN = "RUN"
    RBI = "RBI"
    HITS_SCORING_POSIITION = "HITS_SCORING_POSIITION"
    HIT_BY_PITCH = "HIT_BY_PITCH"
    INFIELD_FLY = "INFIELD_FLY"
    FAN_INTERFERENCE = "FAN_INTERFERENCE"
    BATTER_INTERFERENCE = "BATTER_INTERFERENCE"
    GROUND_RULE_DOUBLE = "GROUND_RULE_DOUBLE"
    INSIDE_THE_PARK_HOME_RUN = "INSIDE_THE_PARK_HOME_RUN"
    FOUL_OUT = "FOUL_OUT"
    LEFT_ON_BASE = "LEFT_ON_BASE"
    LEFT_ON_BASE_SCORING_POSITION = "LEFT_ON_BASE_SCORING_POSITION"
    TEAM_LEFT_ON_BASE = "TEAM_LEFT_ON_BASE"
    TEAM_LEFT_ON_BASE_SCORING_POSITION = "TEAM_LEFT_ON_BASE_SCORING_POSITION"
    SAC_FLY = "SAC_FLY"
    SAC_BUNT = "SAC_BUNT"
    FLY_OUT = "FLY_OUT"
    GROUND_OUT = "GROUND_OUT"
    STOLEN_BASE_2B = "STOLEN_BASE_2B"
    STOLEN_BASE_3B = "STOLEN_BASE_3B"
    STOLEN_BASE_HP = "STOLEN_BASE_HP"
    CAUGHT_STEALING_2B = "CAUGHT_STEALING_2B"
    CAUGHT_STEALING_3B = "CAUGHT_STEALING_3B"
    CAUGHT_STEALING_HP = "CAUGHT_STEALING_HP"
    PICKOFF_1B = "PICKOFF_1B"
    PICKOFF_2B = "PICKOFF_2B"
    PICKOFF_3B = "PICKOFF_3B"
    GROUND_INTO_DOUBLE_PLAY = "GROUND_INTO_DOUBLE_PLAY"
    GROUND_INTO_TRIPLE_PLAY = "GROUND_INTO_TRIPLE_PLAY"
    REACH_ON_ERROR = "REACH_ON_ERROR"
    PINCH_HIT = "PINCH_HIT"
    REACHED_ON_INTERFERENCE = "REACHED_ON_INTERFERENCE"
    PLATE_APPEARANCE = "PLATE_APPEARANCE"
    UNKNOWN = "UNKNOWN"
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
        """BatterDetailType - a model defined in Swagger"""  # noqa: E501
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
        if issubclass(BatterDetailType, dict):
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
        if not isinstance(other, BatterDetailType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other