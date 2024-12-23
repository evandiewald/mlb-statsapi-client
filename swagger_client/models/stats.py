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

class Stats(object):
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
        'all_stats': 'list[StatContainer]'
    }

    attribute_map = {
        'all_stats': 'allStats'
    }

    def __init__(self, all_stats=None):  # noqa: E501
        """Stats - a model defined in Swagger"""  # noqa: E501
        self._all_stats = None
        self.discriminator = None
        if all_stats is not None:
            self.all_stats = all_stats

    @property
    def all_stats(self):
        """Gets the all_stats of this Stats.  # noqa: E501


        :return: The all_stats of this Stats.  # noqa: E501
        :rtype: list[StatContainer]
        """
        return self._all_stats

    @all_stats.setter
    def all_stats(self, all_stats):
        """Sets the all_stats of this Stats.


        :param all_stats: The all_stats of this Stats.  # noqa: E501
        :type: list[StatContainer]
        """

        self._all_stats = all_stats

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
        if issubclass(Stats, dict):
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
        if not isinstance(other, Stats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other