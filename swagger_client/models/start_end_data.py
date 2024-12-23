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

class StartEndData(object):
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
        'velocity': 'Coordinates',
        'position': 'Coordinates',
        'time': 'float',
        'confidence': 'str',
        'speed': 'float',
        'bearing': 'float',
        'distance': 'float'
    }

    attribute_map = {
        'velocity': 'velocity',
        'position': 'position',
        'time': 'time',
        'confidence': 'confidence',
        'speed': 'speed',
        'bearing': 'bearing',
        'distance': 'distance'
    }

    def __init__(self, velocity=None, position=None, time=None, confidence=None, speed=None, bearing=None, distance=None):  # noqa: E501
        """StartEndData - a model defined in Swagger"""  # noqa: E501
        self._velocity = None
        self._position = None
        self._time = None
        self._confidence = None
        self._speed = None
        self._bearing = None
        self._distance = None
        self.discriminator = None
        if velocity is not None:
            self.velocity = velocity
        if position is not None:
            self.position = position
        if time is not None:
            self.time = time
        if confidence is not None:
            self.confidence = confidence
        if speed is not None:
            self.speed = speed
        if bearing is not None:
            self.bearing = bearing
        if distance is not None:
            self.distance = distance

    @property
    def velocity(self):
        """Gets the velocity of this StartEndData.  # noqa: E501


        :return: The velocity of this StartEndData.  # noqa: E501
        :rtype: Coordinates
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """Sets the velocity of this StartEndData.


        :param velocity: The velocity of this StartEndData.  # noqa: E501
        :type: Coordinates
        """

        self._velocity = velocity

    @property
    def position(self):
        """Gets the position of this StartEndData.  # noqa: E501


        :return: The position of this StartEndData.  # noqa: E501
        :rtype: Coordinates
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this StartEndData.


        :param position: The position of this StartEndData.  # noqa: E501
        :type: Coordinates
        """

        self._position = position

    @property
    def time(self):
        """Gets the time of this StartEndData.  # noqa: E501


        :return: The time of this StartEndData.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StartEndData.


        :param time: The time of this StartEndData.  # noqa: E501
        :type: float
        """

        self._time = time

    @property
    def confidence(self):
        """Gets the confidence of this StartEndData.  # noqa: E501


        :return: The confidence of this StartEndData.  # noqa: E501
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this StartEndData.


        :param confidence: The confidence of this StartEndData.  # noqa: E501
        :type: str
        """

        self._confidence = confidence

    @property
    def speed(self):
        """Gets the speed of this StartEndData.  # noqa: E501


        :return: The speed of this StartEndData.  # noqa: E501
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this StartEndData.


        :param speed: The speed of this StartEndData.  # noqa: E501
        :type: float
        """

        self._speed = speed

    @property
    def bearing(self):
        """Gets the bearing of this StartEndData.  # noqa: E501


        :return: The bearing of this StartEndData.  # noqa: E501
        :rtype: float
        """
        return self._bearing

    @bearing.setter
    def bearing(self, bearing):
        """Sets the bearing of this StartEndData.


        :param bearing: The bearing of this StartEndData.  # noqa: E501
        :type: float
        """

        self._bearing = bearing

    @property
    def distance(self):
        """Gets the distance of this StartEndData.  # noqa: E501


        :return: The distance of this StartEndData.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this StartEndData.


        :param distance: The distance of this StartEndData.  # noqa: E501
        :type: float
        """

        self._distance = distance

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
        if issubclass(StartEndData, dict):
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
        if not isinstance(other, StartEndData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
