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

class ExpandEnum(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    PERSON_STATS = "PERSON_STATS"
    PERSON_NAMES = "PERSON_NAMES"
    PERSON_CURRENT_TEAM = "PERSON_CURRENT_TEAM"
    PERSON_SOCIAL = "PERSON_SOCIAL"
    AWARDS_PERSON = "AWARDS_PERSON"
    AWARDS_TEAM = "AWARDS_TEAM"
    AWARDS_RESULTS = "AWARDS_RESULTS"
    ROSTER_PERSON = "ROSTER_PERSON"
    BATTING_STATS_TEAM = "BATTING_STATS_TEAM"
    STANDINGS_TEAM = "STANDINGS_TEAM"
    STANDINGS_LEAGUE = "STANDINGS_LEAGUE"
    STANDINGS_DIVISION = "STANDINGS_DIVISION"
    STANDINGS_CONFERENCE = "STANDINGS_CONFERENCE"
    STANDINGS_RECORD = "STANDINGS_RECORD"
    STANDINGS_RECORD_DIVISION = "STANDINGS_RECORD_DIVISION"
    STANDINGS_RECORD_CONFERENCE = "STANDINGS_RECORD_CONFERENCE"
    STANDINGS_RECORD_OVERALL = "STANDINGS_RECORD_OVERALL"
    TEAM_LEAGUE = "TEAM_LEAGUE"
    TEAM_STATS = "TEAM_STATS"
    TEAM_ROSTER = "TEAM_ROSTER"
    TEAM_DIVISION = "TEAM_DIVISION"
    TEAM_CONFERENCE = "TEAM_CONFERENCE"
    TEAM_FRANCHISE = "TEAM_FRANCHISE"
    TEAM_LEADERS = "TEAM_LEADERS"
    TEAM_SCHEDULE_NEXT = "TEAM_SCHEDULE_NEXT"
    TEAM_SCHEDULE_PREVIOUS = "TEAM_SCHEDULE_PREVIOUS"
    TEAM_TICKET = "TEAM_TICKET"
    TEAM_CONTENT_HOME_ALL = "TEAM_CONTENT_HOME_ALL"
    TEAM_RECORD = "TEAM_RECORD"
    TEAM_PLAYOFF_INFO = "TEAM_PLAYOFF_INFO"
    TEAM_NAME = "TEAM_NAME"
    TEAM_SOCIAL = "TEAM_SOCIAL"
    TEAM_DEVICE_PROPERTIES = "TEAM_DEVICE_PROPERTIES"
    TEAM_CONTENT_SECTIONS = "TEAM_CONTENT_SECTIONS"
    SCHEDULE_LINESCORE = "SCHEDULE_LINESCORE"
    SCHEDULE_SCORING_PLAYS = "SCHEDULE_SCORING_PLAYS"
    SCHEDULE_DECISIONS = "SCHEDULE_DECISIONS"
    SCHEDULE_TEAM = "SCHEDULE_TEAM"
    SCHEDULE_TICKET = "SCHEDULE_TICKET"
    SCHEDULE_VENUE = "SCHEDULE_VENUE"
    SCHEDULE_BROADCASTS = "SCHEDULE_BROADCASTS"
    SCHEDULE_BROADCASTS_ALL = "SCHEDULE_BROADCASTS_ALL"
    SCHEDULE_RADIO_BROADCASTS = "SCHEDULE_RADIO_BROADCASTS"
    SCHEDULE_METADATA = "SCHEDULE_METADATA"
    SCHEDULE_GAME_CONTENT_ALL = "SCHEDULE_GAME_CONTENT_ALL"
    SCHEDULE_GAME_CONTENT_MEDIA_ALL = "SCHEDULE_GAME_CONTENT_MEDIA_ALL"
    SCHEDULE_GAME_CONTENT_EDITORIAL_ALL = "SCHEDULE_GAME_CONTENT_EDITORIAL_ALL"
    SCHEDULE_GAME_CONTENT_EDITORIAL_PREVIEW = "SCHEDULE_GAME_CONTENT_EDITORIAL_PREVIEW"
    SCHEDULE_GAME_CONTENT_EDITORIAL_RECAP = "SCHEDULE_GAME_CONTENT_EDITORIAL_RECAP"
    SCHEDULE_GAME_CONTENT_EDITORIAL_ARTICLES = "SCHEDULE_GAME_CONTENT_EDITORIAL_ARTICLES"
    SCHEDULE_GAME_CONTENT_MEDIA_EPG = "SCHEDULE_GAME_CONTENT_MEDIA_EPG"
    SCHEDULE_GAME_CONTENT_MEDIA_MILESTONES = "SCHEDULE_GAME_CONTENT_MEDIA_MILESTONES"
    SCHEDULE_GAME_CONTENT_HIGHLIGHTS_ALL = "SCHEDULE_GAME_CONTENT_HIGHLIGHTS_ALL"
    SCHEDULE_GAME_CONTENT_HIGHLIGHTS_SCOREBOARD = "SCHEDULE_GAME_CONTENT_HIGHLIGHTS_SCOREBOARD"
    SCHEDULE_GAME_CONTENT_HIGHLIGHTS_SCOREBOARD_PREVIEW = "SCHEDULE_GAME_CONTENT_HIGHLIGHTS_SCOREBOARD_PREVIEW"
    SCHEDULE_GAME_CONTENT_HIGHLIGHTS_GAMECENTER = "SCHEDULE_GAME_CONTENT_HIGHLIGHTS_GAMECENTER"
    SCHEDULE_GAME_CONTENT_HIGHLIGHTS_MILESTONE = "SCHEDULE_GAME_CONTENT_HIGHLIGHTS_MILESTONE"
    SCHEDULE_GAME_SERIES_SUMMARY = "SCHEDULE_GAME_SERIES_SUMMARY"
    SERIES_SUMMARY_SERIES = "SERIES_SUMMARY_SERIES"
    GAME_TEAM = "GAME_TEAM"
    DECISIONS_PERSON = "DECISIONS_PERSON"
    SCORING_PLAYS_PERSON = "SCORING_PLAYS_PERSON"
    STATS_TEAM = "STATS_TEAM"
    LEADERS_PERSON = "LEADERS_PERSON"
    LEAGUE_LEADERS_TEAM = "LEAGUE_LEADERS_TEAM"
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
        """ExpandEnum - a model defined in Swagger"""  # noqa: E501
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
        if issubclass(ExpandEnum, dict):
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
        if not isinstance(other, ExpandEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
