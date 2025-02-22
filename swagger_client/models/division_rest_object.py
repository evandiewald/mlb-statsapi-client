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

class DivisionRestObject(object):
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
        'id': 'int',
        'name': 'str',
        'season': 'str',
        'name_short': 'str',
        'link': 'str',
        'abbreviation': 'str',
        'conference': 'ConferenceRestObject',
        'league': 'LeagueRestObject',
        'sport': 'SportRestObject',
        'has_wildcard': 'bool',
        'sort_order': 'int',
        'num_playoff_teams': 'int',
        'active': 'bool'
    }

    attribute_map = {
        'copyright': 'copyright',
        'id': 'id',
        'name': 'name',
        'season': 'season',
        'name_short': 'nameShort',
        'link': 'link',
        'abbreviation': 'abbreviation',
        'conference': 'conference',
        'league': 'league',
        'sport': 'sport',
        'has_wildcard': 'hasWildcard',
        'sort_order': 'sortOrder',
        'num_playoff_teams': 'numPlayoffTeams',
        'active': 'active'
    }

    def __init__(self, copyright=None, id=None, name=None, season=None, name_short=None, link=None, abbreviation=None, conference=None, league=None, sport=None, has_wildcard=None, sort_order=None, num_playoff_teams=None, active=None):  # noqa: E501
        """DivisionRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._id = None
        self._name = None
        self._season = None
        self._name_short = None
        self._link = None
        self._abbreviation = None
        self._conference = None
        self._league = None
        self._sport = None
        self._has_wildcard = None
        self._sort_order = None
        self._num_playoff_teams = None
        self._active = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if season is not None:
            self.season = season
        if name_short is not None:
            self.name_short = name_short
        if link is not None:
            self.link = link
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if conference is not None:
            self.conference = conference
        if league is not None:
            self.league = league
        if sport is not None:
            self.sport = sport
        if has_wildcard is not None:
            self.has_wildcard = has_wildcard
        if sort_order is not None:
            self.sort_order = sort_order
        if num_playoff_teams is not None:
            self.num_playoff_teams = num_playoff_teams
        if active is not None:
            self.active = active

    @property
    def copyright(self):
        """Gets the copyright of this DivisionRestObject.  # noqa: E501


        :return: The copyright of this DivisionRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this DivisionRestObject.


        :param copyright: The copyright of this DivisionRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def id(self):
        """Gets the id of this DivisionRestObject.  # noqa: E501


        :return: The id of this DivisionRestObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DivisionRestObject.


        :param id: The id of this DivisionRestObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DivisionRestObject.  # noqa: E501


        :return: The name of this DivisionRestObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DivisionRestObject.


        :param name: The name of this DivisionRestObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def season(self):
        """Gets the season of this DivisionRestObject.  # noqa: E501


        :return: The season of this DivisionRestObject.  # noqa: E501
        :rtype: str
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this DivisionRestObject.


        :param season: The season of this DivisionRestObject.  # noqa: E501
        :type: str
        """

        self._season = season

    @property
    def name_short(self):
        """Gets the name_short of this DivisionRestObject.  # noqa: E501


        :return: The name_short of this DivisionRestObject.  # noqa: E501
        :rtype: str
        """
        return self._name_short

    @name_short.setter
    def name_short(self, name_short):
        """Sets the name_short of this DivisionRestObject.


        :param name_short: The name_short of this DivisionRestObject.  # noqa: E501
        :type: str
        """

        self._name_short = name_short

    @property
    def link(self):
        """Gets the link of this DivisionRestObject.  # noqa: E501


        :return: The link of this DivisionRestObject.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this DivisionRestObject.


        :param link: The link of this DivisionRestObject.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def abbreviation(self):
        """Gets the abbreviation of this DivisionRestObject.  # noqa: E501


        :return: The abbreviation of this DivisionRestObject.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this DivisionRestObject.


        :param abbreviation: The abbreviation of this DivisionRestObject.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def conference(self):
        """Gets the conference of this DivisionRestObject.  # noqa: E501


        :return: The conference of this DivisionRestObject.  # noqa: E501
        :rtype: ConferenceRestObject
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this DivisionRestObject.


        :param conference: The conference of this DivisionRestObject.  # noqa: E501
        :type: ConferenceRestObject
        """

        self._conference = conference

    @property
    def league(self):
        """Gets the league of this DivisionRestObject.  # noqa: E501


        :return: The league of this DivisionRestObject.  # noqa: E501
        :rtype: LeagueRestObject
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this DivisionRestObject.


        :param league: The league of this DivisionRestObject.  # noqa: E501
        :type: LeagueRestObject
        """

        self._league = league

    @property
    def sport(self):
        """Gets the sport of this DivisionRestObject.  # noqa: E501


        :return: The sport of this DivisionRestObject.  # noqa: E501
        :rtype: SportRestObject
        """
        return self._sport

    @sport.setter
    def sport(self, sport):
        """Sets the sport of this DivisionRestObject.


        :param sport: The sport of this DivisionRestObject.  # noqa: E501
        :type: SportRestObject
        """

        self._sport = sport

    @property
    def has_wildcard(self):
        """Gets the has_wildcard of this DivisionRestObject.  # noqa: E501


        :return: The has_wildcard of this DivisionRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._has_wildcard

    @has_wildcard.setter
    def has_wildcard(self, has_wildcard):
        """Sets the has_wildcard of this DivisionRestObject.


        :param has_wildcard: The has_wildcard of this DivisionRestObject.  # noqa: E501
        :type: bool
        """

        self._has_wildcard = has_wildcard

    @property
    def sort_order(self):
        """Gets the sort_order of this DivisionRestObject.  # noqa: E501


        :return: The sort_order of this DivisionRestObject.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this DivisionRestObject.


        :param sort_order: The sort_order of this DivisionRestObject.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def num_playoff_teams(self):
        """Gets the num_playoff_teams of this DivisionRestObject.  # noqa: E501


        :return: The num_playoff_teams of this DivisionRestObject.  # noqa: E501
        :rtype: int
        """
        return self._num_playoff_teams

    @num_playoff_teams.setter
    def num_playoff_teams(self, num_playoff_teams):
        """Sets the num_playoff_teams of this DivisionRestObject.


        :param num_playoff_teams: The num_playoff_teams of this DivisionRestObject.  # noqa: E501
        :type: int
        """

        self._num_playoff_teams = num_playoff_teams

    @property
    def active(self):
        """Gets the active of this DivisionRestObject.  # noqa: E501


        :return: The active of this DivisionRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this DivisionRestObject.


        :param active: The active of this DivisionRestObject.  # noqa: E501
        :type: bool
        """

        self._active = active

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
        if issubclass(DivisionRestObject, dict):
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
        if not isinstance(other, DivisionRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
