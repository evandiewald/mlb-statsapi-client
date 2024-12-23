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

class PlayerDraftInfoRestObject(object):
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
        'year': 'int',
        'round': 'str',
        'pick_overall': 'int',
        'pick_in_round': 'int',
        'team': 'BaseballTeamRestObject'
    }

    attribute_map = {
        'copyright': 'copyright',
        'year': 'year',
        'round': 'round',
        'pick_overall': 'pickOverall',
        'pick_in_round': 'pickInRound',
        'team': 'team'
    }

    def __init__(self, copyright=None, year=None, round=None, pick_overall=None, pick_in_round=None, team=None):  # noqa: E501
        """PlayerDraftInfoRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._year = None
        self._round = None
        self._pick_overall = None
        self._pick_in_round = None
        self._team = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if year is not None:
            self.year = year
        if round is not None:
            self.round = round
        if pick_overall is not None:
            self.pick_overall = pick_overall
        if pick_in_round is not None:
            self.pick_in_round = pick_in_round
        if team is not None:
            self.team = team

    @property
    def copyright(self):
        """Gets the copyright of this PlayerDraftInfoRestObject.  # noqa: E501


        :return: The copyright of this PlayerDraftInfoRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this PlayerDraftInfoRestObject.


        :param copyright: The copyright of this PlayerDraftInfoRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def year(self):
        """Gets the year of this PlayerDraftInfoRestObject.  # noqa: E501


        :return: The year of this PlayerDraftInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this PlayerDraftInfoRestObject.


        :param year: The year of this PlayerDraftInfoRestObject.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def round(self):
        """Gets the round of this PlayerDraftInfoRestObject.  # noqa: E501


        :return: The round of this PlayerDraftInfoRestObject.  # noqa: E501
        :rtype: str
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this PlayerDraftInfoRestObject.


        :param round: The round of this PlayerDraftInfoRestObject.  # noqa: E501
        :type: str
        """

        self._round = round

    @property
    def pick_overall(self):
        """Gets the pick_overall of this PlayerDraftInfoRestObject.  # noqa: E501


        :return: The pick_overall of this PlayerDraftInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._pick_overall

    @pick_overall.setter
    def pick_overall(self, pick_overall):
        """Sets the pick_overall of this PlayerDraftInfoRestObject.


        :param pick_overall: The pick_overall of this PlayerDraftInfoRestObject.  # noqa: E501
        :type: int
        """

        self._pick_overall = pick_overall

    @property
    def pick_in_round(self):
        """Gets the pick_in_round of this PlayerDraftInfoRestObject.  # noqa: E501


        :return: The pick_in_round of this PlayerDraftInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._pick_in_round

    @pick_in_round.setter
    def pick_in_round(self, pick_in_round):
        """Sets the pick_in_round of this PlayerDraftInfoRestObject.


        :param pick_in_round: The pick_in_round of this PlayerDraftInfoRestObject.  # noqa: E501
        :type: int
        """

        self._pick_in_round = pick_in_round

    @property
    def team(self):
        """Gets the team of this PlayerDraftInfoRestObject.  # noqa: E501


        :return: The team of this PlayerDraftInfoRestObject.  # noqa: E501
        :rtype: BaseballTeamRestObject
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PlayerDraftInfoRestObject.


        :param team: The team of this PlayerDraftInfoRestObject.  # noqa: E501
        :type: BaseballTeamRestObject
        """

        self._team = team

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
        if issubclass(PlayerDraftInfoRestObject, dict):
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
        if not isinstance(other, PlayerDraftInfoRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
