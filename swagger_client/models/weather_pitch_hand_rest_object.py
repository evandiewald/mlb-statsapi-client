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

class WeatherPitchHandRestObject(object):
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
        'pitch_hand': 'PitchHandTypeRestObject',
        'calm': 'WeatherDeviationRestObject',
        'indoor': 'WeatherDeviationRestObject'
    }

    attribute_map = {
        'copyright': 'copyright',
        'pitch_hand': 'pitchHand',
        'calm': 'calm',
        'indoor': 'indoor'
    }

    def __init__(self, copyright=None, pitch_hand=None, calm=None, indoor=None):  # noqa: E501
        """WeatherPitchHandRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._pitch_hand = None
        self._calm = None
        self._indoor = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if pitch_hand is not None:
            self.pitch_hand = pitch_hand
        if calm is not None:
            self.calm = calm
        if indoor is not None:
            self.indoor = indoor

    @property
    def copyright(self):
        """Gets the copyright of this WeatherPitchHandRestObject.  # noqa: E501


        :return: The copyright of this WeatherPitchHandRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this WeatherPitchHandRestObject.


        :param copyright: The copyright of this WeatherPitchHandRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def pitch_hand(self):
        """Gets the pitch_hand of this WeatherPitchHandRestObject.  # noqa: E501


        :return: The pitch_hand of this WeatherPitchHandRestObject.  # noqa: E501
        :rtype: PitchHandTypeRestObject
        """
        return self._pitch_hand

    @pitch_hand.setter
    def pitch_hand(self, pitch_hand):
        """Sets the pitch_hand of this WeatherPitchHandRestObject.


        :param pitch_hand: The pitch_hand of this WeatherPitchHandRestObject.  # noqa: E501
        :type: PitchHandTypeRestObject
        """

        self._pitch_hand = pitch_hand

    @property
    def calm(self):
        """Gets the calm of this WeatherPitchHandRestObject.  # noqa: E501


        :return: The calm of this WeatherPitchHandRestObject.  # noqa: E501
        :rtype: WeatherDeviationRestObject
        """
        return self._calm

    @calm.setter
    def calm(self, calm):
        """Sets the calm of this WeatherPitchHandRestObject.


        :param calm: The calm of this WeatherPitchHandRestObject.  # noqa: E501
        :type: WeatherDeviationRestObject
        """

        self._calm = calm

    @property
    def indoor(self):
        """Gets the indoor of this WeatherPitchHandRestObject.  # noqa: E501


        :return: The indoor of this WeatherPitchHandRestObject.  # noqa: E501
        :rtype: WeatherDeviationRestObject
        """
        return self._indoor

    @indoor.setter
    def indoor(self, indoor):
        """Sets the indoor of this WeatherPitchHandRestObject.


        :param indoor: The indoor of this WeatherPitchHandRestObject.  # noqa: E501
        :type: WeatherDeviationRestObject
        """

        self._indoor = indoor

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
        if issubclass(WeatherPitchHandRestObject, dict):
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
        if not isinstance(other, WeatherPitchHandRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
