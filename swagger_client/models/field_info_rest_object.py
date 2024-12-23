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

class FieldInfoRestObject(object):
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
        'capacity': 'int',
        'turf_type': 'str',
        'roof_type': 'str',
        'left_line': 'int',
        'left': 'int',
        'left_center': 'int',
        'center': 'int',
        'right_center': 'int',
        'right': 'int',
        'right_line': 'int'
    }

    attribute_map = {
        'copyright': 'copyright',
        'capacity': 'capacity',
        'turf_type': 'turfType',
        'roof_type': 'roofType',
        'left_line': 'leftLine',
        'left': 'left',
        'left_center': 'leftCenter',
        'center': 'center',
        'right_center': 'rightCenter',
        'right': 'right',
        'right_line': 'rightLine'
    }

    def __init__(self, copyright=None, capacity=None, turf_type=None, roof_type=None, left_line=None, left=None, left_center=None, center=None, right_center=None, right=None, right_line=None):  # noqa: E501
        """FieldInfoRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._capacity = None
        self._turf_type = None
        self._roof_type = None
        self._left_line = None
        self._left = None
        self._left_center = None
        self._center = None
        self._right_center = None
        self._right = None
        self._right_line = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if capacity is not None:
            self.capacity = capacity
        if turf_type is not None:
            self.turf_type = turf_type
        if roof_type is not None:
            self.roof_type = roof_type
        if left_line is not None:
            self.left_line = left_line
        if left is not None:
            self.left = left
        if left_center is not None:
            self.left_center = left_center
        if center is not None:
            self.center = center
        if right_center is not None:
            self.right_center = right_center
        if right is not None:
            self.right = right
        if right_line is not None:
            self.right_line = right_line

    @property
    def copyright(self):
        """Gets the copyright of this FieldInfoRestObject.  # noqa: E501


        :return: The copyright of this FieldInfoRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this FieldInfoRestObject.


        :param copyright: The copyright of this FieldInfoRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def capacity(self):
        """Gets the capacity of this FieldInfoRestObject.  # noqa: E501


        :return: The capacity of this FieldInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this FieldInfoRestObject.


        :param capacity: The capacity of this FieldInfoRestObject.  # noqa: E501
        :type: int
        """

        self._capacity = capacity

    @property
    def turf_type(self):
        """Gets the turf_type of this FieldInfoRestObject.  # noqa: E501


        :return: The turf_type of this FieldInfoRestObject.  # noqa: E501
        :rtype: str
        """
        return self._turf_type

    @turf_type.setter
    def turf_type(self, turf_type):
        """Sets the turf_type of this FieldInfoRestObject.


        :param turf_type: The turf_type of this FieldInfoRestObject.  # noqa: E501
        :type: str
        """

        self._turf_type = turf_type

    @property
    def roof_type(self):
        """Gets the roof_type of this FieldInfoRestObject.  # noqa: E501


        :return: The roof_type of this FieldInfoRestObject.  # noqa: E501
        :rtype: str
        """
        return self._roof_type

    @roof_type.setter
    def roof_type(self, roof_type):
        """Sets the roof_type of this FieldInfoRestObject.


        :param roof_type: The roof_type of this FieldInfoRestObject.  # noqa: E501
        :type: str
        """

        self._roof_type = roof_type

    @property
    def left_line(self):
        """Gets the left_line of this FieldInfoRestObject.  # noqa: E501


        :return: The left_line of this FieldInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._left_line

    @left_line.setter
    def left_line(self, left_line):
        """Sets the left_line of this FieldInfoRestObject.


        :param left_line: The left_line of this FieldInfoRestObject.  # noqa: E501
        :type: int
        """

        self._left_line = left_line

    @property
    def left(self):
        """Gets the left of this FieldInfoRestObject.  # noqa: E501


        :return: The left of this FieldInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this FieldInfoRestObject.


        :param left: The left of this FieldInfoRestObject.  # noqa: E501
        :type: int
        """

        self._left = left

    @property
    def left_center(self):
        """Gets the left_center of this FieldInfoRestObject.  # noqa: E501


        :return: The left_center of this FieldInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._left_center

    @left_center.setter
    def left_center(self, left_center):
        """Sets the left_center of this FieldInfoRestObject.


        :param left_center: The left_center of this FieldInfoRestObject.  # noqa: E501
        :type: int
        """

        self._left_center = left_center

    @property
    def center(self):
        """Gets the center of this FieldInfoRestObject.  # noqa: E501


        :return: The center of this FieldInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._center

    @center.setter
    def center(self, center):
        """Sets the center of this FieldInfoRestObject.


        :param center: The center of this FieldInfoRestObject.  # noqa: E501
        :type: int
        """

        self._center = center

    @property
    def right_center(self):
        """Gets the right_center of this FieldInfoRestObject.  # noqa: E501


        :return: The right_center of this FieldInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._right_center

    @right_center.setter
    def right_center(self, right_center):
        """Sets the right_center of this FieldInfoRestObject.


        :param right_center: The right_center of this FieldInfoRestObject.  # noqa: E501
        :type: int
        """

        self._right_center = right_center

    @property
    def right(self):
        """Gets the right of this FieldInfoRestObject.  # noqa: E501


        :return: The right of this FieldInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this FieldInfoRestObject.


        :param right: The right of this FieldInfoRestObject.  # noqa: E501
        :type: int
        """

        self._right = right

    @property
    def right_line(self):
        """Gets the right_line of this FieldInfoRestObject.  # noqa: E501


        :return: The right_line of this FieldInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._right_line

    @right_line.setter
    def right_line(self, right_line):
        """Sets the right_line of this FieldInfoRestObject.


        :param right_line: The right_line of this FieldInfoRestObject.  # noqa: E501
        :type: int
        """

        self._right_line = right_line

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
        if issubclass(FieldInfoRestObject, dict):
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
        if not isinstance(other, FieldInfoRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other