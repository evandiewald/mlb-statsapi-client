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

class RunnerDetailType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    START_BASE = "START_BASE"
    SEQUENCE = "SEQUENCE"
    RUNNER_GOING = "RUNNER_GOING"
    END_BASE = "END_BASE"
    RUNNER_OUT = "RUNNER_OUT"
    FORCED_OUT = "FORCED_OUT"
    ADVANCED_ON_FORCE = "ADVANCED_ON_FORCE"
    ADVANCED_ON_THROW = "ADVANCED_ON_THROW"
    ADVANCED_ON_PLAY = "ADVANCED_ON_PLAY"
    DOUBLED_OFF = "DOUBLED_OFF"
    THROWN_OUT = "THROWN_OUT"
    TAGGED_OUT = "TAGGED_OUT"
    OUT_STRETCHING = "OUT_STRETCHING"
    LEFT_EARLY = "LEFT_EARLY"
    FIELDERS_CHOICE = "FIELDERS_CHOICE"
    OUT_ON_APPEAL = "OUT_ON_APPEAL"
    OUT_ADVANCING = "OUT_ADVANCING"
    DEFENSIVE_INDIFFERENCE = "DEFENSIVE_INDIFFERENCE"
    INTERFERENCE = "INTERFERENCE"
    HIT_BY_BATTED_BALL = "HIT_BY_BATTED_BALL"
    OUT_OVER_RUNNING = "OUT_OVER_RUNNING"
    OUT_RETURNING = "OUT_RETURNING"
    RUNDOWN = "RUNDOWN"
    CAUGHT_STEALING_2B = "CAUGHT_STEALING_2B"
    CAUGHT_STEALING_3B = "CAUGHT_STEALING_3B"
    CAUGHT_STEALING_HOME = "CAUGHT_STEALING_HOME"
    PICKOFF_CAUGHT_STEALING_2B = "PICKOFF_CAUGHT_STEALING_2B"
    PICKOFF_CAUGHT_STEALING_3B = "PICKOFF_CAUGHT_STEALING_3B"
    PICKOFF_CAUGHT_STEALING_HOME = "PICKOFF_CAUGHT_STEALING_HOME"
    STOLEN_BASE_2B = "STOLEN_BASE_2B"
    STOLEN_BASE_3B = "STOLEN_BASE_3B"
    STOLEN_BASE_HOME = "STOLEN_BASE_HOME"
    PICKOFF_1B = "PICKOFF_1B"
    PICKOFF_2B = "PICKOFF_2B"
    PICKOFF_3B = "PICKOFF_3B"
    PICKOFF_ERROR_1B = "PICKOFF_ERROR_1B"
    PICKOFF_ERROR_2B = "PICKOFF_ERROR_2B"
    PICKOFF_ERROR_3B = "PICKOFF_ERROR_3B"
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
        """RunnerDetailType - a model defined in Swagger"""  # noqa: E501
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
        if issubclass(RunnerDetailType, dict):
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
        if not isinstance(other, RunnerDetailType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
