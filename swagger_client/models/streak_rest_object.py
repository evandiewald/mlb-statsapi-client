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

class StreakRestObject(object):
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
        'streak_type': 'str',
        'streak_number': 'int',
        'streak_code': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'streak_type': 'streakType',
        'streak_number': 'streakNumber',
        'streak_code': 'streakCode'
    }

    def __init__(self, copyright=None, streak_type=None, streak_number=None, streak_code=None):  # noqa: E501
        """StreakRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._streak_type = None
        self._streak_number = None
        self._streak_code = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if streak_type is not None:
            self.streak_type = streak_type
        if streak_number is not None:
            self.streak_number = streak_number
        if streak_code is not None:
            self.streak_code = streak_code

    @property
    def copyright(self):
        """Gets the copyright of this StreakRestObject.  # noqa: E501


        :return: The copyright of this StreakRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this StreakRestObject.


        :param copyright: The copyright of this StreakRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def streak_type(self):
        """Gets the streak_type of this StreakRestObject.  # noqa: E501


        :return: The streak_type of this StreakRestObject.  # noqa: E501
        :rtype: str
        """
        return self._streak_type

    @streak_type.setter
    def streak_type(self, streak_type):
        """Sets the streak_type of this StreakRestObject.


        :param streak_type: The streak_type of this StreakRestObject.  # noqa: E501
        :type: str
        """

        self._streak_type = streak_type

    @property
    def streak_number(self):
        """Gets the streak_number of this StreakRestObject.  # noqa: E501


        :return: The streak_number of this StreakRestObject.  # noqa: E501
        :rtype: int
        """
        return self._streak_number

    @streak_number.setter
    def streak_number(self, streak_number):
        """Sets the streak_number of this StreakRestObject.


        :param streak_number: The streak_number of this StreakRestObject.  # noqa: E501
        :type: int
        """

        self._streak_number = streak_number

    @property
    def streak_code(self):
        """Gets the streak_code of this StreakRestObject.  # noqa: E501


        :return: The streak_code of this StreakRestObject.  # noqa: E501
        :rtype: str
        """
        return self._streak_code

    @streak_code.setter
    def streak_code(self, streak_code):
        """Sets the streak_code of this StreakRestObject.


        :param streak_code: The streak_code of this StreakRestObject.  # noqa: E501
        :type: str
        """

        self._streak_code = streak_code

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
        if issubclass(StreakRestObject, dict):
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
        if not isinstance(other, StreakRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
