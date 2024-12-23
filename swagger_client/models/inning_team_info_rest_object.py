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

class InningTeamInfoRestObject(object):
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
        'runs': 'int',
        'hits': 'int',
        'errors': 'int',
        'left_on_base': 'int'
    }

    attribute_map = {
        'copyright': 'copyright',
        'runs': 'runs',
        'hits': 'hits',
        'errors': 'errors',
        'left_on_base': 'leftOnBase'
    }

    def __init__(self, copyright=None, runs=None, hits=None, errors=None, left_on_base=None):  # noqa: E501
        """InningTeamInfoRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._runs = None
        self._hits = None
        self._errors = None
        self._left_on_base = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if runs is not None:
            self.runs = runs
        if hits is not None:
            self.hits = hits
        if errors is not None:
            self.errors = errors
        if left_on_base is not None:
            self.left_on_base = left_on_base

    @property
    def copyright(self):
        """Gets the copyright of this InningTeamInfoRestObject.  # noqa: E501


        :return: The copyright of this InningTeamInfoRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this InningTeamInfoRestObject.


        :param copyright: The copyright of this InningTeamInfoRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def runs(self):
        """Gets the runs of this InningTeamInfoRestObject.  # noqa: E501


        :return: The runs of this InningTeamInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """Sets the runs of this InningTeamInfoRestObject.


        :param runs: The runs of this InningTeamInfoRestObject.  # noqa: E501
        :type: int
        """

        self._runs = runs

    @property
    def hits(self):
        """Gets the hits of this InningTeamInfoRestObject.  # noqa: E501


        :return: The hits of this InningTeamInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this InningTeamInfoRestObject.


        :param hits: The hits of this InningTeamInfoRestObject.  # noqa: E501
        :type: int
        """

        self._hits = hits

    @property
    def errors(self):
        """Gets the errors of this InningTeamInfoRestObject.  # noqa: E501


        :return: The errors of this InningTeamInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InningTeamInfoRestObject.


        :param errors: The errors of this InningTeamInfoRestObject.  # noqa: E501
        :type: int
        """

        self._errors = errors

    @property
    def left_on_base(self):
        """Gets the left_on_base of this InningTeamInfoRestObject.  # noqa: E501


        :return: The left_on_base of this InningTeamInfoRestObject.  # noqa: E501
        :rtype: int
        """
        return self._left_on_base

    @left_on_base.setter
    def left_on_base(self, left_on_base):
        """Sets the left_on_base of this InningTeamInfoRestObject.


        :param left_on_base: The left_on_base of this InningTeamInfoRestObject.  # noqa: E501
        :type: int
        """

        self._left_on_base = left_on_base

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
        if issubclass(InningTeamInfoRestObject, dict):
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
        if not isinstance(other, InningTeamInfoRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
