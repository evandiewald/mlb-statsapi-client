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

class GameNotesRestObject(object):
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
        'notes': 'JsonNode'
    }

    attribute_map = {
        'copyright': 'copyright',
        'notes': 'notes'
    }

    def __init__(self, copyright=None, notes=None):  # noqa: E501
        """GameNotesRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._notes = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if notes is not None:
            self.notes = notes

    @property
    def copyright(self):
        """Gets the copyright of this GameNotesRestObject.  # noqa: E501


        :return: The copyright of this GameNotesRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this GameNotesRestObject.


        :param copyright: The copyright of this GameNotesRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def notes(self):
        """Gets the notes of this GameNotesRestObject.  # noqa: E501


        :return: The notes of this GameNotesRestObject.  # noqa: E501
        :rtype: JsonNode
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this GameNotesRestObject.


        :param notes: The notes of this GameNotesRestObject.  # noqa: E501
        :type: JsonNode
        """

        self._notes = notes

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
        if issubclass(GameNotesRestObject, dict):
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
        if not isinstance(other, GameNotesRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
