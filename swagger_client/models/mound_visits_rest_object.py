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

class MoundVisitsRestObject(object):
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
        'away': 'UsedRemainingRestObject',
        'home': 'UsedRemainingRestObject'
    }

    attribute_map = {
        'copyright': 'copyright',
        'away': 'away',
        'home': 'home'
    }

    def __init__(self, copyright=None, away=None, home=None):  # noqa: E501
        """MoundVisitsRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._away = None
        self._home = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if away is not None:
            self.away = away
        if home is not None:
            self.home = home

    @property
    def copyright(self):
        """Gets the copyright of this MoundVisitsRestObject.  # noqa: E501


        :return: The copyright of this MoundVisitsRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this MoundVisitsRestObject.


        :param copyright: The copyright of this MoundVisitsRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def away(self):
        """Gets the away of this MoundVisitsRestObject.  # noqa: E501


        :return: The away of this MoundVisitsRestObject.  # noqa: E501
        :rtype: UsedRemainingRestObject
        """
        return self._away

    @away.setter
    def away(self, away):
        """Sets the away of this MoundVisitsRestObject.


        :param away: The away of this MoundVisitsRestObject.  # noqa: E501
        :type: UsedRemainingRestObject
        """

        self._away = away

    @property
    def home(self):
        """Gets the home of this MoundVisitsRestObject.  # noqa: E501


        :return: The home of this MoundVisitsRestObject.  # noqa: E501
        :rtype: UsedRemainingRestObject
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this MoundVisitsRestObject.


        :param home: The home of this MoundVisitsRestObject.  # noqa: E501
        :type: UsedRemainingRestObject
        """

        self._home = home

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
        if issubclass(MoundVisitsRestObject, dict):
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
        if not isinstance(other, MoundVisitsRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
