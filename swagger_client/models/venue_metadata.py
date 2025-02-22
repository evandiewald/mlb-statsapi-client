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

class VenueMetadata(object):
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
        'active': 'bool',
        'capacity': 'int',
        'start_year': 'int',
        'end_year': 'int',
        'types': 'list[VenueTypeEnum]'
    }

    attribute_map = {
        'active': 'active',
        'capacity': 'capacity',
        'start_year': 'startYear',
        'end_year': 'endYear',
        'types': 'types'
    }

    def __init__(self, active=None, capacity=None, start_year=None, end_year=None, types=None):  # noqa: E501
        """VenueMetadata - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._capacity = None
        self._start_year = None
        self._end_year = None
        self._types = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if capacity is not None:
            self.capacity = capacity
        if start_year is not None:
            self.start_year = start_year
        if end_year is not None:
            self.end_year = end_year
        if types is not None:
            self.types = types

    @property
    def active(self):
        """Gets the active of this VenueMetadata.  # noqa: E501


        :return: The active of this VenueMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this VenueMetadata.


        :param active: The active of this VenueMetadata.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def capacity(self):
        """Gets the capacity of this VenueMetadata.  # noqa: E501


        :return: The capacity of this VenueMetadata.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this VenueMetadata.


        :param capacity: The capacity of this VenueMetadata.  # noqa: E501
        :type: int
        """

        self._capacity = capacity

    @property
    def start_year(self):
        """Gets the start_year of this VenueMetadata.  # noqa: E501


        :return: The start_year of this VenueMetadata.  # noqa: E501
        :rtype: int
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """Sets the start_year of this VenueMetadata.


        :param start_year: The start_year of this VenueMetadata.  # noqa: E501
        :type: int
        """

        self._start_year = start_year

    @property
    def end_year(self):
        """Gets the end_year of this VenueMetadata.  # noqa: E501


        :return: The end_year of this VenueMetadata.  # noqa: E501
        :rtype: int
        """
        return self._end_year

    @end_year.setter
    def end_year(self, end_year):
        """Sets the end_year of this VenueMetadata.


        :param end_year: The end_year of this VenueMetadata.  # noqa: E501
        :type: int
        """

        self._end_year = end_year

    @property
    def types(self):
        """Gets the types of this VenueMetadata.  # noqa: E501


        :return: The types of this VenueMetadata.  # noqa: E501
        :rtype: list[VenueTypeEnum]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this VenueMetadata.


        :param types: The types of this VenueMetadata.  # noqa: E501
        :type: list[VenueTypeEnum]
        """

        self._types = types

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
        if issubclass(VenueMetadata, dict):
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
        if not isinstance(other, VenueMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
