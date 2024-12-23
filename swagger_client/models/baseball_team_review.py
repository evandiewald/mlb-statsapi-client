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

class BaseballTeamReview(object):
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
        'used_successful': 'int',
        'used_failed': 'int',
        'remaining': 'int'
    }

    attribute_map = {
        'copyright': 'copyright',
        'used_successful': 'usedSuccessful',
        'used_failed': 'usedFailed',
        'remaining': 'remaining'
    }

    def __init__(self, copyright=None, used_successful=None, used_failed=None, remaining=None):  # noqa: E501
        """BaseballTeamReview - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._used_successful = None
        self._used_failed = None
        self._remaining = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if used_successful is not None:
            self.used_successful = used_successful
        if used_failed is not None:
            self.used_failed = used_failed
        if remaining is not None:
            self.remaining = remaining

    @property
    def copyright(self):
        """Gets the copyright of this BaseballTeamReview.  # noqa: E501


        :return: The copyright of this BaseballTeamReview.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this BaseballTeamReview.


        :param copyright: The copyright of this BaseballTeamReview.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def used_successful(self):
        """Gets the used_successful of this BaseballTeamReview.  # noqa: E501


        :return: The used_successful of this BaseballTeamReview.  # noqa: E501
        :rtype: int
        """
        return self._used_successful

    @used_successful.setter
    def used_successful(self, used_successful):
        """Sets the used_successful of this BaseballTeamReview.


        :param used_successful: The used_successful of this BaseballTeamReview.  # noqa: E501
        :type: int
        """

        self._used_successful = used_successful

    @property
    def used_failed(self):
        """Gets the used_failed of this BaseballTeamReview.  # noqa: E501


        :return: The used_failed of this BaseballTeamReview.  # noqa: E501
        :rtype: int
        """
        return self._used_failed

    @used_failed.setter
    def used_failed(self, used_failed):
        """Sets the used_failed of this BaseballTeamReview.


        :param used_failed: The used_failed of this BaseballTeamReview.  # noqa: E501
        :type: int
        """

        self._used_failed = used_failed

    @property
    def remaining(self):
        """Gets the remaining of this BaseballTeamReview.  # noqa: E501


        :return: The remaining of this BaseballTeamReview.  # noqa: E501
        :rtype: int
        """
        return self._remaining

    @remaining.setter
    def remaining(self, remaining):
        """Sets the remaining of this BaseballTeamReview.


        :param remaining: The remaining of this BaseballTeamReview.  # noqa: E501
        :type: int
        """

        self._remaining = remaining

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
        if issubclass(BaseballTeamReview, dict):
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
        if not isinstance(other, BaseballTeamReview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
