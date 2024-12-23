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

class BaseballScheduleItemTeamRestObject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'copyright': 'str',
        'league_record': 'WinLossRecordRestObject',
        'score': 'int',
        'team': 'BaseballTeamRestObject',
        'is_winner': 'bool',
        'probable_pitcher': 'BaseballPersonRestObject',
        'split_squad': 'bool',
        'series_number': 'int',
        'seed_number': 'int',
        'spring_league': 'LeagueRestObject'
    }

    attribute_map = {
        'copyright': 'copyright',
        'league_record': 'leagueRecord',
        'score': 'score',
        'team': 'team',
        'is_winner': 'isWinner',
        'probable_pitcher': 'probablePitcher',
        'split_squad': 'splitSquad',
        'series_number': 'seriesNumber',
        'seed_number': 'seedNumber',
        'spring_league': 'springLeague'
    }

    def __init__(self, copyright=None, league_record=None, score=None, team=None, is_winner=None, probable_pitcher=None, split_squad=None, series_number=None, seed_number=None, spring_league=None):  # noqa: E501
        """BaseballScheduleItemTeamRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._league_record = None
        self._score = None
        self._team = None
        self._is_winner = None
        self._probable_pitcher = None
        self._split_squad = None
        self._series_number = None
        self._seed_number = None
        self._spring_league = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if league_record is not None:
            self.league_record = league_record
        if score is not None:
            self.score = score
        if team is not None:
            self.team = team
        if is_winner is not None:
            self.is_winner = is_winner
        if probable_pitcher is not None:
            self.probable_pitcher = probable_pitcher
        if split_squad is not None:
            self.split_squad = split_squad
        if series_number is not None:
            self.series_number = series_number
        if seed_number is not None:
            self.seed_number = seed_number
        if spring_league is not None:
            self.spring_league = spring_league

    @property
    def copyright(self):
        """Gets the copyright of this BaseballScheduleItemTeamRestObject.  # noqa: E501


        :return: The copyright of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this BaseballScheduleItemTeamRestObject.


        :param copyright: The copyright of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def league_record(self):
        """Gets the league_record of this BaseballScheduleItemTeamRestObject.  # noqa: E501


        :return: The league_record of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :rtype: WinLossRecordRestObject
        """
        return self._league_record

    @league_record.setter
    def league_record(self, league_record):
        """Sets the league_record of this BaseballScheduleItemTeamRestObject.


        :param league_record: The league_record of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :type: WinLossRecordRestObject
        """

        self._league_record = league_record

    @property
    def score(self):
        """Gets the score of this BaseballScheduleItemTeamRestObject.  # noqa: E501


        :return: The score of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this BaseballScheduleItemTeamRestObject.


        :param score: The score of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def team(self):
        """Gets the team of this BaseballScheduleItemTeamRestObject.  # noqa: E501


        :return: The team of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :rtype: BaseballTeamRestObject
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BaseballScheduleItemTeamRestObject.


        :param team: The team of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :type: BaseballTeamRestObject
        """

        self._team = team

    @property
    def is_winner(self):
        """Gets the is_winner of this BaseballScheduleItemTeamRestObject.  # noqa: E501


        :return: The is_winner of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_winner

    @is_winner.setter
    def is_winner(self, is_winner):
        """Sets the is_winner of this BaseballScheduleItemTeamRestObject.


        :param is_winner: The is_winner of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :type: bool
        """

        self._is_winner = is_winner

    @property
    def probable_pitcher(self):
        """Gets the probable_pitcher of this BaseballScheduleItemTeamRestObject.  # noqa: E501


        :return: The probable_pitcher of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :rtype: BaseballPersonRestObject
        """
        return self._probable_pitcher

    @probable_pitcher.setter
    def probable_pitcher(self, probable_pitcher):
        """Sets the probable_pitcher of this BaseballScheduleItemTeamRestObject.


        :param probable_pitcher: The probable_pitcher of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :type: BaseballPersonRestObject
        """

        self._probable_pitcher = probable_pitcher

    @property
    def split_squad(self):
        """Gets the split_squad of this BaseballScheduleItemTeamRestObject.  # noqa: E501


        :return: The split_squad of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._split_squad

    @split_squad.setter
    def split_squad(self, split_squad):
        """Sets the split_squad of this BaseballScheduleItemTeamRestObject.


        :param split_squad: The split_squad of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :type: bool
        """

        self._split_squad = split_squad

    @property
    def series_number(self):
        """Gets the series_number of this BaseballScheduleItemTeamRestObject.  # noqa: E501


        :return: The series_number of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :rtype: int
        """
        return self._series_number

    @series_number.setter
    def series_number(self, series_number):
        """Sets the series_number of this BaseballScheduleItemTeamRestObject.


        :param series_number: The series_number of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :type: int
        """

        self._series_number = series_number

    @property
    def seed_number(self):
        """Gets the seed_number of this BaseballScheduleItemTeamRestObject.  # noqa: E501


        :return: The seed_number of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :rtype: int
        """
        return self._seed_number

    @seed_number.setter
    def seed_number(self, seed_number):
        """Sets the seed_number of this BaseballScheduleItemTeamRestObject.


        :param seed_number: The seed_number of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :type: int
        """

        self._seed_number = seed_number

    @property
    def spring_league(self):
        """Gets the spring_league of this BaseballScheduleItemTeamRestObject.  # noqa: E501


        :return: The spring_league of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :rtype: LeagueRestObject
        """
        return self._spring_league

    @spring_league.setter
    def spring_league(self, spring_league):
        """Sets the spring_league of this BaseballScheduleItemTeamRestObject.


        :param spring_league: The spring_league of this BaseballScheduleItemTeamRestObject.  # noqa: E501
        :type: LeagueRestObject
        """

        self._spring_league = spring_league

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
        if issubclass(BaseballScheduleItemTeamRestObject, dict):
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
        if not isinstance(other, BaseballScheduleItemTeamRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other