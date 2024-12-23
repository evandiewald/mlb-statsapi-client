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

class PersonLeadersEnum(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ASSISTS = "ASSISTS"
    SHUTOUTS = "SHUTOUTS"
    HOME_RUNS = "HOME_RUNS"
    SACRIFICE_BUNTS = "SACRIFICE_BUNTS"
    SACRIFICE_FLIES = "SACRIFICE_FLIES"
    RUNS = "RUNS"
    GROUNDOUT_TO_FLYOUT_RATIO = "GROUNDOUT_TO_FLYOUT_RATIO"
    STOLEN_BASES = "STOLEN_BASES"
    BATTING_AVERAGE = "BATTING_AVERAGE"
    GROUNDOUTS = "GROUNDOUTS"
    NUMBER_OF_PITCHES = "NUMBER_OF_PITCHES"
    ON_BASE_PERCENTAGE = "ON_BASE_PERCENTAGE"
    CAUGHT_STEALING = "CAUGHT_STEALING"
    GROUND_INTO_DOUBLE_PLAYS = "GROUND_INTO_DOUBLE_PLAYS"
    TOTAL_BASES = "TOTAL_BASES"
    EARNED_RUN_AVERAGE = "EARNED_RUN_AVERAGE"
    FIELDING_PERCENTAGE = "FIELDING_PERCENTAGE"
    WALKS_HITS_PER_INNING_PITCHED = "WALKS_HITS_PER_INNING_PITCHED"
    FLYOUTS = "FLYOUTS"
    HIT_BY_PITCHES = "HIT_BY_PITCHES"
    GAMES_PLAYED = "GAMES_PLAYED"
    WALKS = "WALKS"
    SLUGGING_PERCENTAGE = "SLUGGING_PERCENTAGE"
    ON_BASE_PLUS_SLUGGING = "ON_BASE_PLUS_SLUGGING"
    RUNS_BATTED_IN = "RUNS_BATTED_IN"
    TRIPLES = "TRIPLES"
    EXTRA_BASE_HITS = "EXTRA_BASE_HITS"
    HITS = "HITS"
    AT_BAT = "AT_BAT"
    STRIKEOUTS = "STRIKEOUTS"
    DOUBLES = "DOUBLES"
    TOTAL_PLATE_APPEARANCES = "TOTAL_PLATE_APPEARANCES"
    INTENTIONAL_WALKS = "INTENTIONAL_WALKS"
    BASEBALL_WINS = "BASEBALL_WINS"
    LOSSES = "LOSSES"
    SAVES = "SAVES"
    WILD_PITCH = "WILD_PITCH"
    AIROUTS = "AIROUTS"
    BALK = "BALK"
    BLOWN_SAVES = "BLOWN_SAVES"
    CATCHER_ERA = "CATCHER_ERA"
    CATCHERS_INTERFERENCE = "CATCHERS_INTERFERENCE"
    CHANCES = "CHANCES"
    COMPLETE_GAME = "COMPLETE_GAME"
    DOUBLE_PLAYS = "DOUBLE_PLAYS"
    EARNED_RUN = "EARNED_RUN"
    ERRORS = "ERRORS"
    GAMES_FINISHED = "GAMES_FINISHED"
    GAMES_STARTED = "GAMES_STARTED"
    HIT_BATSMAN = "HIT_BATSMAN"
    HITS_PER_9_INN = "HITS_PER_9_INN"
    HOLDS = "HOLDS"
    INNINGS = "INNINGS"
    INNINGS_PITCHED = "INNINGS_PITCHED"
    OUTFIELD_ASSISTS = "OUTFIELD_ASSISTS"
    PASSED_BALLS = "PASSED_BALLS"
    PICKOFFS = "PICKOFFS"
    PITCHES_PER_INNING = "PITCHES_PER_INNING"
    PUT_OUTS = "PUT_OUTS"
    RANGE_FACTOR_PER_GAME = "RANGE_FACTOR_PER_GAME"
    RANGE_FACTOR_PER_9_INN = "RANGE_FACTOR_PER_9_INN"
    SAVE_OPPORTUNITIES = "SAVE_OPPORTUNITIES"
    STOLEN_BASE_PERCENTAGE = "STOLEN_BASE_PERCENTAGE"
    STRIKEOUTS_PER_9_INN = "STRIKEOUTS_PER_9_INN"
    STRIKEOUT_WALK_RATIO = "STRIKEOUT_WALK_RATIO"
    THROWING_ERRORS = "THROWING_ERRORS"
    TOTAL_BATTERS_FACED = "TOTAL_BATTERS_FACED"
    TRIPLE_PLAYS = "TRIPLE_PLAYS"
    WALKS_PER_9_INN = "WALKS_PER_9_INN"
    WIN_PERCENTAGE = "WIN_PERCENTAGE"
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
        """PersonLeadersEnum - a model defined in Swagger"""  # noqa: E501
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
        if issubclass(PersonLeadersEnum, dict):
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
        if not isinstance(other, PersonLeadersEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
