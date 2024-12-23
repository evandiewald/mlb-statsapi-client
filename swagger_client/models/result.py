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

class Result(object):
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
        'type': 'str',
        'event': 'str',
        'event_type': 'str',
        'description': 'str',
        'rbi': 'int',
        'away_score': 'int',
        'home_score': 'int',
        'is_out': 'bool'
    }

    attribute_map = {
        'copyright': 'copyright',
        'type': 'type',
        'event': 'event',
        'event_type': 'eventType',
        'description': 'description',
        'rbi': 'rbi',
        'away_score': 'awayScore',
        'home_score': 'homeScore',
        'is_out': 'isOut'
    }

    def __init__(self, copyright=None, type=None, event=None, event_type=None, description=None, rbi=None, away_score=None, home_score=None, is_out=None):  # noqa: E501
        """Result - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._type = None
        self._event = None
        self._event_type = None
        self._description = None
        self._rbi = None
        self._away_score = None
        self._home_score = None
        self._is_out = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if type is not None:
            self.type = type
        if event is not None:
            self.event = event
        if event_type is not None:
            self.event_type = event_type
        if description is not None:
            self.description = description
        if rbi is not None:
            self.rbi = rbi
        if away_score is not None:
            self.away_score = away_score
        if home_score is not None:
            self.home_score = home_score
        if is_out is not None:
            self.is_out = is_out

    @property
    def copyright(self):
        """Gets the copyright of this Result.  # noqa: E501


        :return: The copyright of this Result.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this Result.


        :param copyright: The copyright of this Result.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def type(self):
        """Gets the type of this Result.  # noqa: E501


        :return: The type of this Result.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Result.


        :param type: The type of this Result.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def event(self):
        """Gets the event of this Result.  # noqa: E501


        :return: The event of this Result.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this Result.


        :param event: The event of this Result.  # noqa: E501
        :type: str
        """

        self._event = event

    @property
    def event_type(self):
        """Gets the event_type of this Result.  # noqa: E501


        :return: The event_type of this Result.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Result.


        :param event_type: The event_type of this Result.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def description(self):
        """Gets the description of this Result.  # noqa: E501


        :return: The description of this Result.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Result.


        :param description: The description of this Result.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def rbi(self):
        """Gets the rbi of this Result.  # noqa: E501


        :return: The rbi of this Result.  # noqa: E501
        :rtype: int
        """
        return self._rbi

    @rbi.setter
    def rbi(self, rbi):
        """Sets the rbi of this Result.


        :param rbi: The rbi of this Result.  # noqa: E501
        :type: int
        """

        self._rbi = rbi

    @property
    def away_score(self):
        """Gets the away_score of this Result.  # noqa: E501


        :return: The away_score of this Result.  # noqa: E501
        :rtype: int
        """
        return self._away_score

    @away_score.setter
    def away_score(self, away_score):
        """Sets the away_score of this Result.


        :param away_score: The away_score of this Result.  # noqa: E501
        :type: int
        """

        self._away_score = away_score

    @property
    def home_score(self):
        """Gets the home_score of this Result.  # noqa: E501


        :return: The home_score of this Result.  # noqa: E501
        :rtype: int
        """
        return self._home_score

    @home_score.setter
    def home_score(self, home_score):
        """Sets the home_score of this Result.


        :param home_score: The home_score of this Result.  # noqa: E501
        :type: int
        """

        self._home_score = home_score

    @property
    def is_out(self):
        """Gets the is_out of this Result.  # noqa: E501

        Did the play result in an out?  # noqa: E501

        :return: The is_out of this Result.  # noqa: E501
        :rtype: bool
        """
        return self._is_out

    @is_out.setter
    def is_out(self, is_out):
        """Sets the is_out of this Result.

        Did the play result in an out?  # noqa: E501

        :param is_out: The is_out of this Result.  # noqa: E501
        :type: bool
        """

        self._is_out = is_out

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
        if issubclass(Result, dict):
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
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other