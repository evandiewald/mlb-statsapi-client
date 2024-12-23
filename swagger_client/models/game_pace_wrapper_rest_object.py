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

class GamePaceWrapperRestObject(object):
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
        'teams': 'list[GamePaceRestObject]',
        'leagues': 'list[GamePaceRestObject]',
        'sports': 'list[GamePaceRestObject]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'teams': 'teams',
        'leagues': 'leagues',
        'sports': 'sports'
    }

    def __init__(self, copyright=None, teams=None, leagues=None, sports=None):  # noqa: E501
        """GamePaceWrapperRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._teams = None
        self._leagues = None
        self._sports = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if teams is not None:
            self.teams = teams
        if leagues is not None:
            self.leagues = leagues
        if sports is not None:
            self.sports = sports

    @property
    def copyright(self):
        """Gets the copyright of this GamePaceWrapperRestObject.  # noqa: E501


        :return: The copyright of this GamePaceWrapperRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this GamePaceWrapperRestObject.


        :param copyright: The copyright of this GamePaceWrapperRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def teams(self):
        """Gets the teams of this GamePaceWrapperRestObject.  # noqa: E501


        :return: The teams of this GamePaceWrapperRestObject.  # noqa: E501
        :rtype: list[GamePaceRestObject]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this GamePaceWrapperRestObject.


        :param teams: The teams of this GamePaceWrapperRestObject.  # noqa: E501
        :type: list[GamePaceRestObject]
        """

        self._teams = teams

    @property
    def leagues(self):
        """Gets the leagues of this GamePaceWrapperRestObject.  # noqa: E501


        :return: The leagues of this GamePaceWrapperRestObject.  # noqa: E501
        :rtype: list[GamePaceRestObject]
        """
        return self._leagues

    @leagues.setter
    def leagues(self, leagues):
        """Sets the leagues of this GamePaceWrapperRestObject.


        :param leagues: The leagues of this GamePaceWrapperRestObject.  # noqa: E501
        :type: list[GamePaceRestObject]
        """

        self._leagues = leagues

    @property
    def sports(self):
        """Gets the sports of this GamePaceWrapperRestObject.  # noqa: E501


        :return: The sports of this GamePaceWrapperRestObject.  # noqa: E501
        :rtype: list[GamePaceRestObject]
        """
        return self._sports

    @sports.setter
    def sports(self, sports):
        """Sets the sports of this GamePaceWrapperRestObject.


        :param sports: The sports of this GamePaceWrapperRestObject.  # noqa: E501
        :type: list[GamePaceRestObject]
        """

        self._sports = sports

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
        if issubclass(GamePaceWrapperRestObject, dict):
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
        if not isinstance(other, GamePaceWrapperRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
