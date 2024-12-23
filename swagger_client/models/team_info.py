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

class TeamInfo(object):
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
        'team': 'BaseballTeamRestObject',
        'runs': 'int',
        'hits': 'int',
        'errors': 'int',
        'left_on_base': 'int',
        'is_winner': 'bool'
    }

    attribute_map = {
        'copyright': 'copyright',
        'team': 'team',
        'runs': 'runs',
        'hits': 'hits',
        'errors': 'errors',
        'left_on_base': 'leftOnBase',
        'is_winner': 'isWinner'
    }

    def __init__(self, copyright=None, team=None, runs=None, hits=None, errors=None, left_on_base=None, is_winner=None):  # noqa: E501
        """TeamInfo - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._team = None
        self._runs = None
        self._hits = None
        self._errors = None
        self._left_on_base = None
        self._is_winner = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if team is not None:
            self.team = team
        if runs is not None:
            self.runs = runs
        if hits is not None:
            self.hits = hits
        if errors is not None:
            self.errors = errors
        if left_on_base is not None:
            self.left_on_base = left_on_base
        if is_winner is not None:
            self.is_winner = is_winner

    @property
    def copyright(self):
        """Gets the copyright of this TeamInfo.  # noqa: E501


        :return: The copyright of this TeamInfo.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this TeamInfo.


        :param copyright: The copyright of this TeamInfo.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def team(self):
        """Gets the team of this TeamInfo.  # noqa: E501


        :return: The team of this TeamInfo.  # noqa: E501
        :rtype: BaseballTeamRestObject
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TeamInfo.


        :param team: The team of this TeamInfo.  # noqa: E501
        :type: BaseballTeamRestObject
        """

        self._team = team

    @property
    def runs(self):
        """Gets the runs of this TeamInfo.  # noqa: E501


        :return: The runs of this TeamInfo.  # noqa: E501
        :rtype: int
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """Sets the runs of this TeamInfo.


        :param runs: The runs of this TeamInfo.  # noqa: E501
        :type: int
        """

        self._runs = runs

    @property
    def hits(self):
        """Gets the hits of this TeamInfo.  # noqa: E501


        :return: The hits of this TeamInfo.  # noqa: E501
        :rtype: int
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this TeamInfo.


        :param hits: The hits of this TeamInfo.  # noqa: E501
        :type: int
        """

        self._hits = hits

    @property
    def errors(self):
        """Gets the errors of this TeamInfo.  # noqa: E501


        :return: The errors of this TeamInfo.  # noqa: E501
        :rtype: int
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this TeamInfo.


        :param errors: The errors of this TeamInfo.  # noqa: E501
        :type: int
        """

        self._errors = errors

    @property
    def left_on_base(self):
        """Gets the left_on_base of this TeamInfo.  # noqa: E501


        :return: The left_on_base of this TeamInfo.  # noqa: E501
        :rtype: int
        """
        return self._left_on_base

    @left_on_base.setter
    def left_on_base(self, left_on_base):
        """Sets the left_on_base of this TeamInfo.


        :param left_on_base: The left_on_base of this TeamInfo.  # noqa: E501
        :type: int
        """

        self._left_on_base = left_on_base

    @property
    def is_winner(self):
        """Gets the is_winner of this TeamInfo.  # noqa: E501


        :return: The is_winner of this TeamInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_winner

    @is_winner.setter
    def is_winner(self, is_winner):
        """Sets the is_winner of this TeamInfo.


        :param is_winner: The is_winner of this TeamInfo.  # noqa: E501
        :type: bool
        """

        self._is_winner = is_winner

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
        if issubclass(TeamInfo, dict):
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
        if not isinstance(other, TeamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
