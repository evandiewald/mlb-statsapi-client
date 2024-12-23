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

class BaseballHotColdZone(object):
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
        'zone': 'str',
        'sweetness': 'str',
        'temp': 'str',
        'color': 'str',
        'value': 'str'
    }

    attribute_map = {
        'zone': 'zone',
        'sweetness': 'sweetness',
        'temp': 'temp',
        'color': 'color',
        'value': 'value'
    }

    def __init__(self, zone=None, sweetness=None, temp=None, color=None, value=None):  # noqa: E501
        """BaseballHotColdZone - a model defined in Swagger"""  # noqa: E501
        self._zone = None
        self._sweetness = None
        self._temp = None
        self._color = None
        self._value = None
        self.discriminator = None
        if zone is not None:
            self.zone = zone
        if sweetness is not None:
            self.sweetness = sweetness
        if temp is not None:
            self.temp = temp
        if color is not None:
            self.color = color
        if value is not None:
            self.value = value

    @property
    def zone(self):
        """Gets the zone of this BaseballHotColdZone.  # noqa: E501


        :return: The zone of this BaseballHotColdZone.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this BaseballHotColdZone.


        :param zone: The zone of this BaseballHotColdZone.  # noqa: E501
        :type: str
        """

        self._zone = zone

    @property
    def sweetness(self):
        """Gets the sweetness of this BaseballHotColdZone.  # noqa: E501


        :return: The sweetness of this BaseballHotColdZone.  # noqa: E501
        :rtype: str
        """
        return self._sweetness

    @sweetness.setter
    def sweetness(self, sweetness):
        """Sets the sweetness of this BaseballHotColdZone.


        :param sweetness: The sweetness of this BaseballHotColdZone.  # noqa: E501
        :type: str
        """

        self._sweetness = sweetness

    @property
    def temp(self):
        """Gets the temp of this BaseballHotColdZone.  # noqa: E501


        :return: The temp of this BaseballHotColdZone.  # noqa: E501
        :rtype: str
        """
        return self._temp

    @temp.setter
    def temp(self, temp):
        """Sets the temp of this BaseballHotColdZone.


        :param temp: The temp of this BaseballHotColdZone.  # noqa: E501
        :type: str
        """

        self._temp = temp

    @property
    def color(self):
        """Gets the color of this BaseballHotColdZone.  # noqa: E501


        :return: The color of this BaseballHotColdZone.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this BaseballHotColdZone.


        :param color: The color of this BaseballHotColdZone.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def value(self):
        """Gets the value of this BaseballHotColdZone.  # noqa: E501


        :return: The value of this BaseballHotColdZone.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BaseballHotColdZone.


        :param value: The value of this BaseballHotColdZone.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(BaseballHotColdZone, dict):
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
        if not isinstance(other, BaseballHotColdZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
