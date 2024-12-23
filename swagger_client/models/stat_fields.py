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

class StatFields(object):
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
        'standard': 'bool',
        'advanced': 'bool',
        'tracking': 'bool',
        'expected': 'bool'
    }

    attribute_map = {
        'copyright': 'copyright',
        'standard': 'standard',
        'advanced': 'advanced',
        'tracking': 'tracking',
        'expected': 'expected'
    }

    def __init__(self, copyright=None, standard=None, advanced=None, tracking=None, expected=None):  # noqa: E501
        """StatFields - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._standard = None
        self._advanced = None
        self._tracking = None
        self._expected = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if standard is not None:
            self.standard = standard
        if advanced is not None:
            self.advanced = advanced
        if tracking is not None:
            self.tracking = tracking
        if expected is not None:
            self.expected = expected

    @property
    def copyright(self):
        """Gets the copyright of this StatFields.  # noqa: E501


        :return: The copyright of this StatFields.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this StatFields.


        :param copyright: The copyright of this StatFields.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def standard(self):
        """Gets the standard of this StatFields.  # noqa: E501


        :return: The standard of this StatFields.  # noqa: E501
        :rtype: bool
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this StatFields.


        :param standard: The standard of this StatFields.  # noqa: E501
        :type: bool
        """

        self._standard = standard

    @property
    def advanced(self):
        """Gets the advanced of this StatFields.  # noqa: E501


        :return: The advanced of this StatFields.  # noqa: E501
        :rtype: bool
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this StatFields.


        :param advanced: The advanced of this StatFields.  # noqa: E501
        :type: bool
        """

        self._advanced = advanced

    @property
    def tracking(self):
        """Gets the tracking of this StatFields.  # noqa: E501


        :return: The tracking of this StatFields.  # noqa: E501
        :rtype: bool
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this StatFields.


        :param tracking: The tracking of this StatFields.  # noqa: E501
        :type: bool
        """

        self._tracking = tracking

    @property
    def expected(self):
        """Gets the expected of this StatFields.  # noqa: E501


        :return: The expected of this StatFields.  # noqa: E501
        :rtype: bool
        """
        return self._expected

    @expected.setter
    def expected(self, expected):
        """Sets the expected of this StatFields.


        :param expected: The expected of this StatFields.  # noqa: E501
        :type: bool
        """

        self._expected = expected

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
        if issubclass(StatFields, dict):
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
        if not isinstance(other, StatFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
