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

class WeatherDeviationsRestObject(object):
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
        'hit': 'WeatherHitRestObject',
        'pitch': 'WeatherPitchRestObject'
    }

    attribute_map = {
        'copyright': 'copyright',
        'hit': 'hit',
        'pitch': 'pitch'
    }

    def __init__(self, copyright=None, hit=None, pitch=None):  # noqa: E501
        """WeatherDeviationsRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._hit = None
        self._pitch = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if hit is not None:
            self.hit = hit
        if pitch is not None:
            self.pitch = pitch

    @property
    def copyright(self):
        """Gets the copyright of this WeatherDeviationsRestObject.  # noqa: E501


        :return: The copyright of this WeatherDeviationsRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this WeatherDeviationsRestObject.


        :param copyright: The copyright of this WeatherDeviationsRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def hit(self):
        """Gets the hit of this WeatherDeviationsRestObject.  # noqa: E501


        :return: The hit of this WeatherDeviationsRestObject.  # noqa: E501
        :rtype: WeatherHitRestObject
        """
        return self._hit

    @hit.setter
    def hit(self, hit):
        """Sets the hit of this WeatherDeviationsRestObject.


        :param hit: The hit of this WeatherDeviationsRestObject.  # noqa: E501
        :type: WeatherHitRestObject
        """

        self._hit = hit

    @property
    def pitch(self):
        """Gets the pitch of this WeatherDeviationsRestObject.  # noqa: E501


        :return: The pitch of this WeatherDeviationsRestObject.  # noqa: E501
        :rtype: WeatherPitchRestObject
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        """Sets the pitch of this WeatherDeviationsRestObject.


        :param pitch: The pitch of this WeatherDeviationsRestObject.  # noqa: E501
        :type: WeatherPitchRestObject
        """

        self._pitch = pitch

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
        if issubclass(WeatherDeviationsRestObject, dict):
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
        if not isinstance(other, WeatherDeviationsRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
