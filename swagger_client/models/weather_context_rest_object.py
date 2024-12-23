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

class WeatherContextRestObject(object):
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
        'condition_type': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'condition_type': 'conditionType'
    }

    def __init__(self, copyright=None, condition_type=None):  # noqa: E501
        """WeatherContextRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._condition_type = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if condition_type is not None:
            self.condition_type = condition_type

    @property
    def copyright(self):
        """Gets the copyright of this WeatherContextRestObject.  # noqa: E501


        :return: The copyright of this WeatherContextRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this WeatherContextRestObject.


        :param copyright: The copyright of this WeatherContextRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def condition_type(self):
        """Gets the condition_type of this WeatherContextRestObject.  # noqa: E501


        :return: The condition_type of this WeatherContextRestObject.  # noqa: E501
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """Sets the condition_type of this WeatherContextRestObject.


        :param condition_type: The condition_type of this WeatherContextRestObject.  # noqa: E501
        :type: str
        """

        self._condition_type = condition_type

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
        if issubclass(WeatherContextRestObject, dict):
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
        if not isinstance(other, WeatherContextRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
