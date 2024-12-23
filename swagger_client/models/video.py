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

class Video(object):
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
        'play_id': 'str',
        'playback_groups': 'JsonNode',
        'at_bat_number': 'int',
        'pitch_number': 'int',
        '_date': 'datetime'
    }

    attribute_map = {
        'play_id': 'playId',
        'playback_groups': 'playbackGroups',
        'at_bat_number': 'atBatNumber',
        'pitch_number': 'pitchNumber',
        '_date': 'date'
    }

    def __init__(self, play_id=None, playback_groups=None, at_bat_number=None, pitch_number=None, _date=None):  # noqa: E501
        """Video - a model defined in Swagger"""  # noqa: E501
        self._play_id = None
        self._playback_groups = None
        self._at_bat_number = None
        self._pitch_number = None
        self.__date = None
        self.discriminator = None
        if play_id is not None:
            self.play_id = play_id
        if playback_groups is not None:
            self.playback_groups = playback_groups
        if at_bat_number is not None:
            self.at_bat_number = at_bat_number
        if pitch_number is not None:
            self.pitch_number = pitch_number
        if _date is not None:
            self._date = _date

    @property
    def play_id(self):
        """Gets the play_id of this Video.  # noqa: E501


        :return: The play_id of this Video.  # noqa: E501
        :rtype: str
        """
        return self._play_id

    @play_id.setter
    def play_id(self, play_id):
        """Sets the play_id of this Video.


        :param play_id: The play_id of this Video.  # noqa: E501
        :type: str
        """

        self._play_id = play_id

    @property
    def playback_groups(self):
        """Gets the playback_groups of this Video.  # noqa: E501


        :return: The playback_groups of this Video.  # noqa: E501
        :rtype: JsonNode
        """
        return self._playback_groups

    @playback_groups.setter
    def playback_groups(self, playback_groups):
        """Sets the playback_groups of this Video.


        :param playback_groups: The playback_groups of this Video.  # noqa: E501
        :type: JsonNode
        """

        self._playback_groups = playback_groups

    @property
    def at_bat_number(self):
        """Gets the at_bat_number of this Video.  # noqa: E501


        :return: The at_bat_number of this Video.  # noqa: E501
        :rtype: int
        """
        return self._at_bat_number

    @at_bat_number.setter
    def at_bat_number(self, at_bat_number):
        """Sets the at_bat_number of this Video.


        :param at_bat_number: The at_bat_number of this Video.  # noqa: E501
        :type: int
        """

        self._at_bat_number = at_bat_number

    @property
    def pitch_number(self):
        """Gets the pitch_number of this Video.  # noqa: E501


        :return: The pitch_number of this Video.  # noqa: E501
        :rtype: int
        """
        return self._pitch_number

    @pitch_number.setter
    def pitch_number(self, pitch_number):
        """Sets the pitch_number of this Video.


        :param pitch_number: The pitch_number of this Video.  # noqa: E501
        :type: int
        """

        self._pitch_number = pitch_number

    @property
    def _date(self):
        """Gets the _date of this Video.  # noqa: E501


        :return: The _date of this Video.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Video.


        :param _date: The _date of this Video.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

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
        if issubclass(Video, dict):
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
        if not isinstance(other, Video):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
