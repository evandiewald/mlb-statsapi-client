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

class BaseballABSChallenge(object):
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
        'has_challenges': 'bool',
        'away_challenges_used': 'int',
        'away_challenges_remaining': 'int',
        'home_challenges_used': 'int',
        'home_challenges_remaining': 'int',
        'challenging_team': 'BaseballTeam',
        'review_reason': 'str',
        'limit9th_inning': 'int',
        'away_challenges_used_overturned': 'int',
        'away_challenges_used_stands': 'int',
        'home_challenges_used_overturned': 'int',
        'home_challenges_used_stands': 'int'
    }

    attribute_map = {
        'has_challenges': 'hasChallenges',
        'away_challenges_used': 'awayChallengesUsed',
        'away_challenges_remaining': 'awayChallengesRemaining',
        'home_challenges_used': 'homeChallengesUsed',
        'home_challenges_remaining': 'homeChallengesRemaining',
        'challenging_team': 'challengingTeam',
        'review_reason': 'reviewReason',
        'limit9th_inning': 'limit9thInning',
        'away_challenges_used_overturned': 'awayChallengesUsedOverturned',
        'away_challenges_used_stands': 'awayChallengesUsedStands',
        'home_challenges_used_overturned': 'homeChallengesUsedOverturned',
        'home_challenges_used_stands': 'homeChallengesUsedStands'
    }

    def __init__(self, has_challenges=None, away_challenges_used=None, away_challenges_remaining=None, home_challenges_used=None, home_challenges_remaining=None, challenging_team=None, review_reason=None, limit9th_inning=None, away_challenges_used_overturned=None, away_challenges_used_stands=None, home_challenges_used_overturned=None, home_challenges_used_stands=None):  # noqa: E501
        """BaseballABSChallenge - a model defined in Swagger"""  # noqa: E501
        self._has_challenges = None
        self._away_challenges_used = None
        self._away_challenges_remaining = None
        self._home_challenges_used = None
        self._home_challenges_remaining = None
        self._challenging_team = None
        self._review_reason = None
        self._limit9th_inning = None
        self._away_challenges_used_overturned = None
        self._away_challenges_used_stands = None
        self._home_challenges_used_overturned = None
        self._home_challenges_used_stands = None
        self.discriminator = None
        if has_challenges is not None:
            self.has_challenges = has_challenges
        if away_challenges_used is not None:
            self.away_challenges_used = away_challenges_used
        if away_challenges_remaining is not None:
            self.away_challenges_remaining = away_challenges_remaining
        if home_challenges_used is not None:
            self.home_challenges_used = home_challenges_used
        if home_challenges_remaining is not None:
            self.home_challenges_remaining = home_challenges_remaining
        if challenging_team is not None:
            self.challenging_team = challenging_team
        if review_reason is not None:
            self.review_reason = review_reason
        if limit9th_inning is not None:
            self.limit9th_inning = limit9th_inning
        if away_challenges_used_overturned is not None:
            self.away_challenges_used_overturned = away_challenges_used_overturned
        if away_challenges_used_stands is not None:
            self.away_challenges_used_stands = away_challenges_used_stands
        if home_challenges_used_overturned is not None:
            self.home_challenges_used_overturned = home_challenges_used_overturned
        if home_challenges_used_stands is not None:
            self.home_challenges_used_stands = home_challenges_used_stands

    @property
    def has_challenges(self):
        """Gets the has_challenges of this BaseballABSChallenge.  # noqa: E501


        :return: The has_challenges of this BaseballABSChallenge.  # noqa: E501
        :rtype: bool
        """
        return self._has_challenges

    @has_challenges.setter
    def has_challenges(self, has_challenges):
        """Sets the has_challenges of this BaseballABSChallenge.


        :param has_challenges: The has_challenges of this BaseballABSChallenge.  # noqa: E501
        :type: bool
        """

        self._has_challenges = has_challenges

    @property
    def away_challenges_used(self):
        """Gets the away_challenges_used of this BaseballABSChallenge.  # noqa: E501


        :return: The away_challenges_used of this BaseballABSChallenge.  # noqa: E501
        :rtype: int
        """
        return self._away_challenges_used

    @away_challenges_used.setter
    def away_challenges_used(self, away_challenges_used):
        """Sets the away_challenges_used of this BaseballABSChallenge.


        :param away_challenges_used: The away_challenges_used of this BaseballABSChallenge.  # noqa: E501
        :type: int
        """

        self._away_challenges_used = away_challenges_used

    @property
    def away_challenges_remaining(self):
        """Gets the away_challenges_remaining of this BaseballABSChallenge.  # noqa: E501


        :return: The away_challenges_remaining of this BaseballABSChallenge.  # noqa: E501
        :rtype: int
        """
        return self._away_challenges_remaining

    @away_challenges_remaining.setter
    def away_challenges_remaining(self, away_challenges_remaining):
        """Sets the away_challenges_remaining of this BaseballABSChallenge.


        :param away_challenges_remaining: The away_challenges_remaining of this BaseballABSChallenge.  # noqa: E501
        :type: int
        """

        self._away_challenges_remaining = away_challenges_remaining

    @property
    def home_challenges_used(self):
        """Gets the home_challenges_used of this BaseballABSChallenge.  # noqa: E501


        :return: The home_challenges_used of this BaseballABSChallenge.  # noqa: E501
        :rtype: int
        """
        return self._home_challenges_used

    @home_challenges_used.setter
    def home_challenges_used(self, home_challenges_used):
        """Sets the home_challenges_used of this BaseballABSChallenge.


        :param home_challenges_used: The home_challenges_used of this BaseballABSChallenge.  # noqa: E501
        :type: int
        """

        self._home_challenges_used = home_challenges_used

    @property
    def home_challenges_remaining(self):
        """Gets the home_challenges_remaining of this BaseballABSChallenge.  # noqa: E501


        :return: The home_challenges_remaining of this BaseballABSChallenge.  # noqa: E501
        :rtype: int
        """
        return self._home_challenges_remaining

    @home_challenges_remaining.setter
    def home_challenges_remaining(self, home_challenges_remaining):
        """Sets the home_challenges_remaining of this BaseballABSChallenge.


        :param home_challenges_remaining: The home_challenges_remaining of this BaseballABSChallenge.  # noqa: E501
        :type: int
        """

        self._home_challenges_remaining = home_challenges_remaining

    @property
    def challenging_team(self):
        """Gets the challenging_team of this BaseballABSChallenge.  # noqa: E501


        :return: The challenging_team of this BaseballABSChallenge.  # noqa: E501
        :rtype: BaseballTeam
        """
        return self._challenging_team

    @challenging_team.setter
    def challenging_team(self, challenging_team):
        """Sets the challenging_team of this BaseballABSChallenge.


        :param challenging_team: The challenging_team of this BaseballABSChallenge.  # noqa: E501
        :type: BaseballTeam
        """

        self._challenging_team = challenging_team

    @property
    def review_reason(self):
        """Gets the review_reason of this BaseballABSChallenge.  # noqa: E501


        :return: The review_reason of this BaseballABSChallenge.  # noqa: E501
        :rtype: str
        """
        return self._review_reason

    @review_reason.setter
    def review_reason(self, review_reason):
        """Sets the review_reason of this BaseballABSChallenge.


        :param review_reason: The review_reason of this BaseballABSChallenge.  # noqa: E501
        :type: str
        """

        self._review_reason = review_reason

    @property
    def limit9th_inning(self):
        """Gets the limit9th_inning of this BaseballABSChallenge.  # noqa: E501


        :return: The limit9th_inning of this BaseballABSChallenge.  # noqa: E501
        :rtype: int
        """
        return self._limit9th_inning

    @limit9th_inning.setter
    def limit9th_inning(self, limit9th_inning):
        """Sets the limit9th_inning of this BaseballABSChallenge.


        :param limit9th_inning: The limit9th_inning of this BaseballABSChallenge.  # noqa: E501
        :type: int
        """

        self._limit9th_inning = limit9th_inning

    @property
    def away_challenges_used_overturned(self):
        """Gets the away_challenges_used_overturned of this BaseballABSChallenge.  # noqa: E501


        :return: The away_challenges_used_overturned of this BaseballABSChallenge.  # noqa: E501
        :rtype: int
        """
        return self._away_challenges_used_overturned

    @away_challenges_used_overturned.setter
    def away_challenges_used_overturned(self, away_challenges_used_overturned):
        """Sets the away_challenges_used_overturned of this BaseballABSChallenge.


        :param away_challenges_used_overturned: The away_challenges_used_overturned of this BaseballABSChallenge.  # noqa: E501
        :type: int
        """

        self._away_challenges_used_overturned = away_challenges_used_overturned

    @property
    def away_challenges_used_stands(self):
        """Gets the away_challenges_used_stands of this BaseballABSChallenge.  # noqa: E501


        :return: The away_challenges_used_stands of this BaseballABSChallenge.  # noqa: E501
        :rtype: int
        """
        return self._away_challenges_used_stands

    @away_challenges_used_stands.setter
    def away_challenges_used_stands(self, away_challenges_used_stands):
        """Sets the away_challenges_used_stands of this BaseballABSChallenge.


        :param away_challenges_used_stands: The away_challenges_used_stands of this BaseballABSChallenge.  # noqa: E501
        :type: int
        """

        self._away_challenges_used_stands = away_challenges_used_stands

    @property
    def home_challenges_used_overturned(self):
        """Gets the home_challenges_used_overturned of this BaseballABSChallenge.  # noqa: E501


        :return: The home_challenges_used_overturned of this BaseballABSChallenge.  # noqa: E501
        :rtype: int
        """
        return self._home_challenges_used_overturned

    @home_challenges_used_overturned.setter
    def home_challenges_used_overturned(self, home_challenges_used_overturned):
        """Sets the home_challenges_used_overturned of this BaseballABSChallenge.


        :param home_challenges_used_overturned: The home_challenges_used_overturned of this BaseballABSChallenge.  # noqa: E501
        :type: int
        """

        self._home_challenges_used_overturned = home_challenges_used_overturned

    @property
    def home_challenges_used_stands(self):
        """Gets the home_challenges_used_stands of this BaseballABSChallenge.  # noqa: E501


        :return: The home_challenges_used_stands of this BaseballABSChallenge.  # noqa: E501
        :rtype: int
        """
        return self._home_challenges_used_stands

    @home_challenges_used_stands.setter
    def home_challenges_used_stands(self, home_challenges_used_stands):
        """Sets the home_challenges_used_stands of this BaseballABSChallenge.


        :param home_challenges_used_stands: The home_challenges_used_stands of this BaseballABSChallenge.  # noqa: E501
        :type: int
        """

        self._home_challenges_used_stands = home_challenges_used_stands

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
        if issubclass(BaseballABSChallenge, dict):
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
        if not isinstance(other, BaseballABSChallenge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
