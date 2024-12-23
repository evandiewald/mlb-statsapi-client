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

class BaseballGameMetaDataRestObject(object):
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
        'wait': 'int',
        'time_stamp': 'str',
        'game_events': 'list[str]',
        'logical_events': 'list[str]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'wait': 'wait',
        'time_stamp': 'timeStamp',
        'game_events': 'gameEvents',
        'logical_events': 'logicalEvents'
    }

    def __init__(self, copyright=None, wait=None, time_stamp=None, game_events=None, logical_events=None):  # noqa: E501
        """BaseballGameMetaDataRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._wait = None
        self._time_stamp = None
        self._game_events = None
        self._logical_events = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if wait is not None:
            self.wait = wait
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if game_events is not None:
            self.game_events = game_events
        if logical_events is not None:
            self.logical_events = logical_events

    @property
    def copyright(self):
        """Gets the copyright of this BaseballGameMetaDataRestObject.  # noqa: E501


        :return: The copyright of this BaseballGameMetaDataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this BaseballGameMetaDataRestObject.


        :param copyright: The copyright of this BaseballGameMetaDataRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def wait(self):
        """Gets the wait of this BaseballGameMetaDataRestObject.  # noqa: E501


        :return: The wait of this BaseballGameMetaDataRestObject.  # noqa: E501
        :rtype: int
        """
        return self._wait

    @wait.setter
    def wait(self, wait):
        """Sets the wait of this BaseballGameMetaDataRestObject.


        :param wait: The wait of this BaseballGameMetaDataRestObject.  # noqa: E501
        :type: int
        """

        self._wait = wait

    @property
    def time_stamp(self):
        """Gets the time_stamp of this BaseballGameMetaDataRestObject.  # noqa: E501


        :return: The time_stamp of this BaseballGameMetaDataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this BaseballGameMetaDataRestObject.


        :param time_stamp: The time_stamp of this BaseballGameMetaDataRestObject.  # noqa: E501
        :type: str
        """

        self._time_stamp = time_stamp

    @property
    def game_events(self):
        """Gets the game_events of this BaseballGameMetaDataRestObject.  # noqa: E501


        :return: The game_events of this BaseballGameMetaDataRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._game_events

    @game_events.setter
    def game_events(self, game_events):
        """Sets the game_events of this BaseballGameMetaDataRestObject.


        :param game_events: The game_events of this BaseballGameMetaDataRestObject.  # noqa: E501
        :type: list[str]
        """

        self._game_events = game_events

    @property
    def logical_events(self):
        """Gets the logical_events of this BaseballGameMetaDataRestObject.  # noqa: E501


        :return: The logical_events of this BaseballGameMetaDataRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._logical_events

    @logical_events.setter
    def logical_events(self, logical_events):
        """Sets the logical_events of this BaseballGameMetaDataRestObject.


        :param logical_events: The logical_events of this BaseballGameMetaDataRestObject.  # noqa: E501
        :type: list[str]
        """

        self._logical_events = logical_events

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
        if issubclass(BaseballGameMetaDataRestObject, dict):
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
        if not isinstance(other, BaseballGameMetaDataRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
