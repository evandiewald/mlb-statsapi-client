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

class PlayerLeader(object):
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
        'rank': 'int',
        'value': 'str',
        'team': 'BaseballTeam',
        'league': 'League',
        'person': 'BaseballPerson',
        'sport': 'Sport',
        'season': 'str',
        'num_teams': 'int'
    }

    attribute_map = {
        'rank': 'rank',
        'value': 'value',
        'team': 'team',
        'league': 'league',
        'person': 'person',
        'sport': 'sport',
        'season': 'season',
        'num_teams': 'numTeams'
    }

    def __init__(self, rank=None, value=None, team=None, league=None, person=None, sport=None, season=None, num_teams=None):  # noqa: E501
        """PlayerLeader - a model defined in Swagger"""  # noqa: E501
        self._rank = None
        self._value = None
        self._team = None
        self._league = None
        self._person = None
        self._sport = None
        self._season = None
        self._num_teams = None
        self.discriminator = None
        if rank is not None:
            self.rank = rank
        if value is not None:
            self.value = value
        if team is not None:
            self.team = team
        if league is not None:
            self.league = league
        if person is not None:
            self.person = person
        if sport is not None:
            self.sport = sport
        if season is not None:
            self.season = season
        if num_teams is not None:
            self.num_teams = num_teams

    @property
    def rank(self):
        """Gets the rank of this PlayerLeader.  # noqa: E501


        :return: The rank of this PlayerLeader.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this PlayerLeader.


        :param rank: The rank of this PlayerLeader.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def value(self):
        """Gets the value of this PlayerLeader.  # noqa: E501


        :return: The value of this PlayerLeader.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PlayerLeader.


        :param value: The value of this PlayerLeader.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def team(self):
        """Gets the team of this PlayerLeader.  # noqa: E501


        :return: The team of this PlayerLeader.  # noqa: E501
        :rtype: BaseballTeam
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PlayerLeader.


        :param team: The team of this PlayerLeader.  # noqa: E501
        :type: BaseballTeam
        """

        self._team = team

    @property
    def league(self):
        """Gets the league of this PlayerLeader.  # noqa: E501


        :return: The league of this PlayerLeader.  # noqa: E501
        :rtype: League
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this PlayerLeader.


        :param league: The league of this PlayerLeader.  # noqa: E501
        :type: League
        """

        self._league = league

    @property
    def person(self):
        """Gets the person of this PlayerLeader.  # noqa: E501


        :return: The person of this PlayerLeader.  # noqa: E501
        :rtype: BaseballPerson
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this PlayerLeader.


        :param person: The person of this PlayerLeader.  # noqa: E501
        :type: BaseballPerson
        """

        self._person = person

    @property
    def sport(self):
        """Gets the sport of this PlayerLeader.  # noqa: E501


        :return: The sport of this PlayerLeader.  # noqa: E501
        :rtype: Sport
        """
        return self._sport

    @sport.setter
    def sport(self, sport):
        """Sets the sport of this PlayerLeader.


        :param sport: The sport of this PlayerLeader.  # noqa: E501
        :type: Sport
        """

        self._sport = sport

    @property
    def season(self):
        """Gets the season of this PlayerLeader.  # noqa: E501


        :return: The season of this PlayerLeader.  # noqa: E501
        :rtype: str
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this PlayerLeader.


        :param season: The season of this PlayerLeader.  # noqa: E501
        :type: str
        """

        self._season = season

    @property
    def num_teams(self):
        """Gets the num_teams of this PlayerLeader.  # noqa: E501


        :return: The num_teams of this PlayerLeader.  # noqa: E501
        :rtype: int
        """
        return self._num_teams

    @num_teams.setter
    def num_teams(self, num_teams):
        """Sets the num_teams of this PlayerLeader.


        :param num_teams: The num_teams of this PlayerLeader.  # noqa: E501
        :type: int
        """

        self._num_teams = num_teams

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
        if issubclass(PlayerLeader, dict):
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
        if not isinstance(other, PlayerLeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other