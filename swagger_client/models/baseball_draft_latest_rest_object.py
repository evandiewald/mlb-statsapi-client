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

class BaseballDraftLatestRestObject(object):
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
        'pick': 'BaseballDraftProspectRestObject',
        'number': 'int',
        'next_up': 'list[BaseballDraftProspectRestObject]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'pick': 'pick',
        'number': 'number',
        'next_up': 'nextUp'
    }

    def __init__(self, copyright=None, pick=None, number=None, next_up=None):  # noqa: E501
        """BaseballDraftLatestRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._pick = None
        self._number = None
        self._next_up = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if pick is not None:
            self.pick = pick
        if number is not None:
            self.number = number
        if next_up is not None:
            self.next_up = next_up

    @property
    def copyright(self):
        """Gets the copyright of this BaseballDraftLatestRestObject.  # noqa: E501


        :return: The copyright of this BaseballDraftLatestRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this BaseballDraftLatestRestObject.


        :param copyright: The copyright of this BaseballDraftLatestRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def pick(self):
        """Gets the pick of this BaseballDraftLatestRestObject.  # noqa: E501


        :return: The pick of this BaseballDraftLatestRestObject.  # noqa: E501
        :rtype: BaseballDraftProspectRestObject
        """
        return self._pick

    @pick.setter
    def pick(self, pick):
        """Sets the pick of this BaseballDraftLatestRestObject.


        :param pick: The pick of this BaseballDraftLatestRestObject.  # noqa: E501
        :type: BaseballDraftProspectRestObject
        """

        self._pick = pick

    @property
    def number(self):
        """Gets the number of this BaseballDraftLatestRestObject.  # noqa: E501


        :return: The number of this BaseballDraftLatestRestObject.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this BaseballDraftLatestRestObject.


        :param number: The number of this BaseballDraftLatestRestObject.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def next_up(self):
        """Gets the next_up of this BaseballDraftLatestRestObject.  # noqa: E501


        :return: The next_up of this BaseballDraftLatestRestObject.  # noqa: E501
        :rtype: list[BaseballDraftProspectRestObject]
        """
        return self._next_up

    @next_up.setter
    def next_up(self, next_up):
        """Sets the next_up of this BaseballDraftLatestRestObject.


        :param next_up: The next_up of this BaseballDraftLatestRestObject.  # noqa: E501
        :type: list[BaseballDraftProspectRestObject]
        """

        self._next_up = next_up

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
        if issubclass(BaseballDraftLatestRestObject, dict):
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
        if not isinstance(other, BaseballDraftLatestRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
