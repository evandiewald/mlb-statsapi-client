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

class BaseballViolation(object):
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
        'violation_type': 'str',
        'violation_sub_type': 'str',
        'violation_description': 'str',
        'violation_player': 'BaseballPerson'
    }

    attribute_map = {
        'violation_type': 'violationType',
        'violation_sub_type': 'violationSubType',
        'violation_description': 'violationDescription',
        'violation_player': 'violationPlayer'
    }

    def __init__(self, violation_type=None, violation_sub_type=None, violation_description=None, violation_player=None):  # noqa: E501
        """BaseballViolation - a model defined in Swagger"""  # noqa: E501
        self._violation_type = None
        self._violation_sub_type = None
        self._violation_description = None
        self._violation_player = None
        self.discriminator = None
        if violation_type is not None:
            self.violation_type = violation_type
        if violation_sub_type is not None:
            self.violation_sub_type = violation_sub_type
        if violation_description is not None:
            self.violation_description = violation_description
        if violation_player is not None:
            self.violation_player = violation_player

    @property
    def violation_type(self):
        """Gets the violation_type of this BaseballViolation.  # noqa: E501


        :return: The violation_type of this BaseballViolation.  # noqa: E501
        :rtype: str
        """
        return self._violation_type

    @violation_type.setter
    def violation_type(self, violation_type):
        """Sets the violation_type of this BaseballViolation.


        :param violation_type: The violation_type of this BaseballViolation.  # noqa: E501
        :type: str
        """

        self._violation_type = violation_type

    @property
    def violation_sub_type(self):
        """Gets the violation_sub_type of this BaseballViolation.  # noqa: E501


        :return: The violation_sub_type of this BaseballViolation.  # noqa: E501
        :rtype: str
        """
        return self._violation_sub_type

    @violation_sub_type.setter
    def violation_sub_type(self, violation_sub_type):
        """Sets the violation_sub_type of this BaseballViolation.


        :param violation_sub_type: The violation_sub_type of this BaseballViolation.  # noqa: E501
        :type: str
        """

        self._violation_sub_type = violation_sub_type

    @property
    def violation_description(self):
        """Gets the violation_description of this BaseballViolation.  # noqa: E501


        :return: The violation_description of this BaseballViolation.  # noqa: E501
        :rtype: str
        """
        return self._violation_description

    @violation_description.setter
    def violation_description(self, violation_description):
        """Sets the violation_description of this BaseballViolation.


        :param violation_description: The violation_description of this BaseballViolation.  # noqa: E501
        :type: str
        """

        self._violation_description = violation_description

    @property
    def violation_player(self):
        """Gets the violation_player of this BaseballViolation.  # noqa: E501


        :return: The violation_player of this BaseballViolation.  # noqa: E501
        :rtype: BaseballPerson
        """
        return self._violation_player

    @violation_player.setter
    def violation_player(self, violation_player):
        """Sets the violation_player of this BaseballViolation.


        :param violation_player: The violation_player of this BaseballViolation.  # noqa: E501
        :type: BaseballPerson
        """

        self._violation_player = violation_player

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
        if issubclass(BaseballViolation, dict):
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
        if not isinstance(other, BaseballViolation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
