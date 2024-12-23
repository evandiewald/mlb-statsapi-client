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

class StatcastPositionRestObject(object):
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
        'position_id': 'int',
        'description': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'position_id': 'positionId',
        'description': 'description'
    }

    def __init__(self, copyright=None, position_id=None, description=None):  # noqa: E501
        """StatcastPositionRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._position_id = None
        self._description = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if position_id is not None:
            self.position_id = position_id
        if description is not None:
            self.description = description

    @property
    def copyright(self):
        """Gets the copyright of this StatcastPositionRestObject.  # noqa: E501


        :return: The copyright of this StatcastPositionRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this StatcastPositionRestObject.


        :param copyright: The copyright of this StatcastPositionRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def position_id(self):
        """Gets the position_id of this StatcastPositionRestObject.  # noqa: E501


        :return: The position_id of this StatcastPositionRestObject.  # noqa: E501
        :rtype: int
        """
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        """Sets the position_id of this StatcastPositionRestObject.


        :param position_id: The position_id of this StatcastPositionRestObject.  # noqa: E501
        :type: int
        """

        self._position_id = position_id

    @property
    def description(self):
        """Gets the description of this StatcastPositionRestObject.  # noqa: E501


        :return: The description of this StatcastPositionRestObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StatcastPositionRestObject.


        :param description: The description of this StatcastPositionRestObject.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(StatcastPositionRestObject, dict):
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
        if not isinstance(other, StatcastPositionRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
