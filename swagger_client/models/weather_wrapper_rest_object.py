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

class WeatherWrapperRestObject(object):
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
        'units': 'JsonNode',
        'data': 'RestObject'
    }

    attribute_map = {
        'copyright': 'copyright',
        'units': 'units',
        'data': 'data'
    }

    def __init__(self, copyright=None, units=None, data=None):  # noqa: E501
        """WeatherWrapperRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._units = None
        self._data = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if units is not None:
            self.units = units
        if data is not None:
            self.data = data

    @property
    def copyright(self):
        """Gets the copyright of this WeatherWrapperRestObject.  # noqa: E501


        :return: The copyright of this WeatherWrapperRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this WeatherWrapperRestObject.


        :param copyright: The copyright of this WeatherWrapperRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def units(self):
        """Gets the units of this WeatherWrapperRestObject.  # noqa: E501


        :return: The units of this WeatherWrapperRestObject.  # noqa: E501
        :rtype: JsonNode
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this WeatherWrapperRestObject.


        :param units: The units of this WeatherWrapperRestObject.  # noqa: E501
        :type: JsonNode
        """

        self._units = units

    @property
    def data(self):
        """Gets the data of this WeatherWrapperRestObject.  # noqa: E501


        :return: The data of this WeatherWrapperRestObject.  # noqa: E501
        :rtype: RestObject
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this WeatherWrapperRestObject.


        :param data: The data of this WeatherWrapperRestObject.  # noqa: E501
        :type: RestObject
        """

        self._data = data

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
        if issubclass(WeatherWrapperRestObject, dict):
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
        if not isinstance(other, WeatherWrapperRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other