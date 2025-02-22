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

class ContactPointPositionRestObject(object):
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
        'x': 'float',
        'y': 'float',
        'z': 'float',
        'time_stamp': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'x': 'x',
        'y': 'y',
        'z': 'z',
        'time_stamp': 'timeStamp'
    }

    def __init__(self, copyright=None, x=None, y=None, z=None, time_stamp=None):  # noqa: E501
        """ContactPointPositionRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._x = None
        self._y = None
        self._z = None
        self._time_stamp = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z
        if time_stamp is not None:
            self.time_stamp = time_stamp

    @property
    def copyright(self):
        """Gets the copyright of this ContactPointPositionRestObject.  # noqa: E501


        :return: The copyright of this ContactPointPositionRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this ContactPointPositionRestObject.


        :param copyright: The copyright of this ContactPointPositionRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def x(self):
        """Gets the x of this ContactPointPositionRestObject.  # noqa: E501

        Location in the horizontal dimension, negative toward third base, positive toward first base.  # noqa: E501

        :return: The x of this ContactPointPositionRestObject.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this ContactPointPositionRestObject.

        Location in the horizontal dimension, negative toward third base, positive toward first base.  # noqa: E501

        :param x: The x of this ContactPointPositionRestObject.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this ContactPointPositionRestObject.  # noqa: E501

        Location in the depth dimension, negative toward the backstop, positive toward pitcher’s mound.  # noqa: E501

        :return: The y of this ContactPointPositionRestObject.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this ContactPointPositionRestObject.

        Location in the depth dimension, negative toward the backstop, positive toward pitcher’s mound.  # noqa: E501

        :param y: The y of this ContactPointPositionRestObject.  # noqa: E501
        :type: float
        """

        self._y = y

    @property
    def z(self):
        """Gets the z of this ContactPointPositionRestObject.  # noqa: E501

        Location in the vertical dimension, from the ground upward.  # noqa: E501

        :return: The z of this ContactPointPositionRestObject.  # noqa: E501
        :rtype: float
        """
        return self._z

    @z.setter
    def z(self, z):
        """Sets the z of this ContactPointPositionRestObject.

        Location in the vertical dimension, from the ground upward.  # noqa: E501

        :param z: The z of this ContactPointPositionRestObject.  # noqa: E501
        :type: float
        """

        self._z = z

    @property
    def time_stamp(self):
        """Gets the time_stamp of this ContactPointPositionRestObject.  # noqa: E501


        :return: The time_stamp of this ContactPointPositionRestObject.  # noqa: E501
        :rtype: str
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this ContactPointPositionRestObject.


        :param time_stamp: The time_stamp of this ContactPointPositionRestObject.  # noqa: E501
        :type: str
        """

        self._time_stamp = time_stamp

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
        if issubclass(ContactPointPositionRestObject, dict):
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
        if not isinstance(other, ContactPointPositionRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
