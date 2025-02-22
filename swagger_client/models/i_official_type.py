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

class IOfficialType(object):
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
        'display_name': 'str',
        'short_name': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'short_name': 'shortName'
    }

    def __init__(self, display_name=None, short_name=None):  # noqa: E501
        """IOfficialType - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._short_name = None
        self.discriminator = None
        if display_name is not None:
            self.display_name = display_name
        if short_name is not None:
            self.short_name = short_name

    @property
    def display_name(self):
        """Gets the display_name of this IOfficialType.  # noqa: E501


        :return: The display_name of this IOfficialType.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IOfficialType.


        :param display_name: The display_name of this IOfficialType.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def short_name(self):
        """Gets the short_name of this IOfficialType.  # noqa: E501


        :return: The short_name of this IOfficialType.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this IOfficialType.


        :param short_name: The short_name of this IOfficialType.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

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
        if issubclass(IOfficialType, dict):
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
        if not isinstance(other, IOfficialType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
