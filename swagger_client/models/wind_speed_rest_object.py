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

class WindSpeedRestObject(object):
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
        'side': 'float',
        'tail': 'float',
        'vertical': 'float'
    }

    attribute_map = {
        'copyright': 'copyright',
        'side': 'side',
        'tail': 'tail',
        'vertical': 'vertical'
    }

    def __init__(self, copyright=None, side=None, tail=None, vertical=None):  # noqa: E501
        """WindSpeedRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._side = None
        self._tail = None
        self._vertical = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if side is not None:
            self.side = side
        if tail is not None:
            self.tail = tail
        if vertical is not None:
            self.vertical = vertical

    @property
    def copyright(self):
        """Gets the copyright of this WindSpeedRestObject.  # noqa: E501


        :return: The copyright of this WindSpeedRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this WindSpeedRestObject.


        :param copyright: The copyright of this WindSpeedRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def side(self):
        """Gets the side of this WindSpeedRestObject.  # noqa: E501

        Mean wind speed calculated at a right angle (transverse) to the trajectory of the ball in the horizontal direction.  # noqa: E501

        :return: The side of this WindSpeedRestObject.  # noqa: E501
        :rtype: float
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this WindSpeedRestObject.

        Mean wind speed calculated at a right angle (transverse) to the trajectory of the ball in the horizontal direction.  # noqa: E501

        :param side: The side of this WindSpeedRestObject.  # noqa: E501
        :type: float
        """

        self._side = side

    @property
    def tail(self):
        """Gets the tail of this WindSpeedRestObject.  # noqa: E501

        Mean wind speed calculated along the trajectory of the ball. A tail wind is positive and a headwind is negative.  # noqa: E501

        :return: The tail of this WindSpeedRestObject.  # noqa: E501
        :rtype: float
        """
        return self._tail

    @tail.setter
    def tail(self, tail):
        """Sets the tail of this WindSpeedRestObject.

        Mean wind speed calculated along the trajectory of the ball. A tail wind is positive and a headwind is negative.  # noqa: E501

        :param tail: The tail of this WindSpeedRestObject.  # noqa: E501
        :type: float
        """

        self._tail = tail

    @property
    def vertical(self):
        """Gets the vertical of this WindSpeedRestObject.  # noqa: E501

        Mean wind speed component affecting the pitch trajectory in the vertical (z) direction.  # noqa: E501

        :return: The vertical of this WindSpeedRestObject.  # noqa: E501
        :rtype: float
        """
        return self._vertical

    @vertical.setter
    def vertical(self, vertical):
        """Sets the vertical of this WindSpeedRestObject.

        Mean wind speed component affecting the pitch trajectory in the vertical (z) direction.  # noqa: E501

        :param vertical: The vertical of this WindSpeedRestObject.  # noqa: E501
        :type: float
        """

        self._vertical = vertical

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
        if issubclass(WindSpeedRestObject, dict):
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
        if not isinstance(other, WindSpeedRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
