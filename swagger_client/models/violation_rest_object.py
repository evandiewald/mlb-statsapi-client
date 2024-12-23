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

class ViolationRestObject(object):
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
        'type': 'str',
        'description': 'str',
        'player': 'BaseballPersonRestObject',
        'subtype': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'type': 'type',
        'description': 'description',
        'player': 'player',
        'subtype': 'subtype'
    }

    def __init__(self, copyright=None, type=None, description=None, player=None, subtype=None):  # noqa: E501
        """ViolationRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._type = None
        self._description = None
        self._player = None
        self._subtype = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if player is not None:
            self.player = player
        if subtype is not None:
            self.subtype = subtype

    @property
    def copyright(self):
        """Gets the copyright of this ViolationRestObject.  # noqa: E501


        :return: The copyright of this ViolationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this ViolationRestObject.


        :param copyright: The copyright of this ViolationRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def type(self):
        """Gets the type of this ViolationRestObject.  # noqa: E501


        :return: The type of this ViolationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ViolationRestObject.


        :param type: The type of this ViolationRestObject.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this ViolationRestObject.  # noqa: E501


        :return: The description of this ViolationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ViolationRestObject.


        :param description: The description of this ViolationRestObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def player(self):
        """Gets the player of this ViolationRestObject.  # noqa: E501


        :return: The player of this ViolationRestObject.  # noqa: E501
        :rtype: BaseballPersonRestObject
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this ViolationRestObject.


        :param player: The player of this ViolationRestObject.  # noqa: E501
        :type: BaseballPersonRestObject
        """

        self._player = player

    @property
    def subtype(self):
        """Gets the subtype of this ViolationRestObject.  # noqa: E501


        :return: The subtype of this ViolationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this ViolationRestObject.


        :param subtype: The subtype of this ViolationRestObject.  # noqa: E501
        :type: str
        """

        self._subtype = subtype

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
        if issubclass(ViolationRestObject, dict):
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
        if not isinstance(other, ViolationRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other