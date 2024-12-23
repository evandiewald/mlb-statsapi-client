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

class GameTypeDates(object):
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
        'name': 'str',
        'short_name': 'str',
        'start_date': 'date',
        'end_date': 'date',
        'season': 'str',
        'round_robin': 'bool',
        'playoffs': 'bool',
        'playoff_round': 'int',
        'league': 'League',
        'sport': 'Sport',
        'game_type': 'GameTypeEnum'
    }

    attribute_map = {
        'name': 'name',
        'short_name': 'shortName',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'season': 'season',
        'round_robin': 'roundRobin',
        'playoffs': 'playoffs',
        'playoff_round': 'playoffRound',
        'league': 'league',
        'sport': 'sport',
        'game_type': 'gameType'
    }

    def __init__(self, name=None, short_name=None, start_date=None, end_date=None, season=None, round_robin=None, playoffs=None, playoff_round=None, league=None, sport=None, game_type=None):  # noqa: E501
        """GameTypeDates - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._short_name = None
        self._start_date = None
        self._end_date = None
        self._season = None
        self._round_robin = None
        self._playoffs = None
        self._playoff_round = None
        self._league = None
        self._sport = None
        self._game_type = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if season is not None:
            self.season = season
        if round_robin is not None:
            self.round_robin = round_robin
        if playoffs is not None:
            self.playoffs = playoffs
        if playoff_round is not None:
            self.playoff_round = playoff_round
        if league is not None:
            self.league = league
        if sport is not None:
            self.sport = sport
        if game_type is not None:
            self.game_type = game_type

    @property
    def name(self):
        """Gets the name of this GameTypeDates.  # noqa: E501


        :return: The name of this GameTypeDates.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GameTypeDates.


        :param name: The name of this GameTypeDates.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this GameTypeDates.  # noqa: E501


        :return: The short_name of this GameTypeDates.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this GameTypeDates.


        :param short_name: The short_name of this GameTypeDates.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def start_date(self):
        """Gets the start_date of this GameTypeDates.  # noqa: E501


        :return: The start_date of this GameTypeDates.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GameTypeDates.


        :param start_date: The start_date of this GameTypeDates.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this GameTypeDates.  # noqa: E501


        :return: The end_date of this GameTypeDates.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GameTypeDates.


        :param end_date: The end_date of this GameTypeDates.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def season(self):
        """Gets the season of this GameTypeDates.  # noqa: E501


        :return: The season of this GameTypeDates.  # noqa: E501
        :rtype: str
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this GameTypeDates.


        :param season: The season of this GameTypeDates.  # noqa: E501
        :type: str
        """

        self._season = season

    @property
    def round_robin(self):
        """Gets the round_robin of this GameTypeDates.  # noqa: E501


        :return: The round_robin of this GameTypeDates.  # noqa: E501
        :rtype: bool
        """
        return self._round_robin

    @round_robin.setter
    def round_robin(self, round_robin):
        """Sets the round_robin of this GameTypeDates.


        :param round_robin: The round_robin of this GameTypeDates.  # noqa: E501
        :type: bool
        """

        self._round_robin = round_robin

    @property
    def playoffs(self):
        """Gets the playoffs of this GameTypeDates.  # noqa: E501


        :return: The playoffs of this GameTypeDates.  # noqa: E501
        :rtype: bool
        """
        return self._playoffs

    @playoffs.setter
    def playoffs(self, playoffs):
        """Sets the playoffs of this GameTypeDates.


        :param playoffs: The playoffs of this GameTypeDates.  # noqa: E501
        :type: bool
        """

        self._playoffs = playoffs

    @property
    def playoff_round(self):
        """Gets the playoff_round of this GameTypeDates.  # noqa: E501


        :return: The playoff_round of this GameTypeDates.  # noqa: E501
        :rtype: int
        """
        return self._playoff_round

    @playoff_round.setter
    def playoff_round(self, playoff_round):
        """Sets the playoff_round of this GameTypeDates.


        :param playoff_round: The playoff_round of this GameTypeDates.  # noqa: E501
        :type: int
        """

        self._playoff_round = playoff_round

    @property
    def league(self):
        """Gets the league of this GameTypeDates.  # noqa: E501


        :return: The league of this GameTypeDates.  # noqa: E501
        :rtype: League
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this GameTypeDates.


        :param league: The league of this GameTypeDates.  # noqa: E501
        :type: League
        """

        self._league = league

    @property
    def sport(self):
        """Gets the sport of this GameTypeDates.  # noqa: E501


        :return: The sport of this GameTypeDates.  # noqa: E501
        :rtype: Sport
        """
        return self._sport

    @sport.setter
    def sport(self, sport):
        """Sets the sport of this GameTypeDates.


        :param sport: The sport of this GameTypeDates.  # noqa: E501
        :type: Sport
        """

        self._sport = sport

    @property
    def game_type(self):
        """Gets the game_type of this GameTypeDates.  # noqa: E501


        :return: The game_type of this GameTypeDates.  # noqa: E501
        :rtype: GameTypeEnum
        """
        return self._game_type

    @game_type.setter
    def game_type(self, game_type):
        """Sets the game_type of this GameTypeDates.


        :param game_type: The game_type of this GameTypeDates.  # noqa: E501
        :type: GameTypeEnum
        """

        self._game_type = game_type

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
        if issubclass(GameTypeDates, dict):
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
        if not isinstance(other, GameTypeDates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other