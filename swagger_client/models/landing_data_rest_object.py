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

class LandingDataRestObject(object):
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
        'time': 'float',
        'position': 'LandingPositionRestObject',
        'distance': 'float',
        'offset_spin': 'float',
        'offset_wind': 'float'
    }

    attribute_map = {
        'copyright': 'copyright',
        'time': 'time',
        'position': 'position',
        'distance': 'distance',
        'offset_spin': 'offsetSpin',
        'offset_wind': 'offsetWind'
    }

    def __init__(self, copyright=None, time=None, position=None, distance=None, offset_spin=None, offset_wind=None):  # noqa: E501
        """LandingDataRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._time = None
        self._position = None
        self._distance = None
        self._offset_spin = None
        self._offset_wind = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if time is not None:
            self.time = time
        if position is not None:
            self.position = position
        if distance is not None:
            self.distance = distance
        if offset_spin is not None:
            self.offset_spin = offset_spin
        if offset_wind is not None:
            self.offset_wind = offset_wind

    @property
    def copyright(self):
        """Gets the copyright of this LandingDataRestObject.  # noqa: E501


        :return: The copyright of this LandingDataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this LandingDataRestObject.


        :param copyright: The copyright of this LandingDataRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def time(self):
        """Gets the time of this LandingDataRestObject.  # noqa: E501

        Hang time of the ball's trajectory.  # noqa: E501

        :return: The time of this LandingDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this LandingDataRestObject.

        Hang time of the ball's trajectory.  # noqa: E501

        :param time: The time of this LandingDataRestObject.  # noqa: E501
        :type: float
        """

        self._time = time

    @property
    def position(self):
        """Gets the position of this LandingDataRestObject.  # noqa: E501


        :return: The position of this LandingDataRestObject.  # noqa: E501
        :rtype: LandingPositionRestObject
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this LandingDataRestObject.


        :param position: The position of this LandingDataRestObject.  # noqa: E501
        :type: LandingPositionRestObject
        """

        self._position = position

    @property
    def distance(self):
        """Gets the distance of this LandingDataRestObject.  # noqa: E501

        Straight-line distance to the landing point of the ball's trajectory. If the ball hits above z=0 this distance is projected down to z=0.  # noqa: E501

        :return: The distance of this LandingDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this LandingDataRestObject.

        Straight-line distance to the landing point of the ball's trajectory. If the ball hits above z=0 this distance is projected down to z=0.  # noqa: E501

        :param distance: The distance of this LandingDataRestObject.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def offset_spin(self):
        """Gets the offset_spin of this LandingDataRestObject.  # noqa: E501

        Additional distance attributed to the ball's spin.  # noqa: E501

        :return: The offset_spin of this LandingDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._offset_spin

    @offset_spin.setter
    def offset_spin(self, offset_spin):
        """Sets the offset_spin of this LandingDataRestObject.

        Additional distance attributed to the ball's spin.  # noqa: E501

        :param offset_spin: The offset_spin of this LandingDataRestObject.  # noqa: E501
        :type: float
        """

        self._offset_spin = offset_spin

    @property
    def offset_wind(self):
        """Gets the offset_wind of this LandingDataRestObject.  # noqa: E501

        Landing position offset attributed to the wind's impact on the ball's trajectory.  # noqa: E501

        :return: The offset_wind of this LandingDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._offset_wind

    @offset_wind.setter
    def offset_wind(self, offset_wind):
        """Sets the offset_wind of this LandingDataRestObject.

        Landing position offset attributed to the wind's impact on the ball's trajectory.  # noqa: E501

        :param offset_wind: The offset_wind of this LandingDataRestObject.  # noqa: E501
        :type: float
        """

        self._offset_wind = offset_wind

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
        if issubclass(LandingDataRestObject, dict):
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
        if not isinstance(other, LandingDataRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
