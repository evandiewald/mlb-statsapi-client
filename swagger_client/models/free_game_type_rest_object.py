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

class FreeGameTypeRestObject(object):
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
        'free_game_type_code': 'str',
        'free_game_type_text': 'str',
        'free_game_type_desc': 'str',
        'free_game_type_id': 'int'
    }

    attribute_map = {
        'copyright': 'copyright',
        'free_game_type_code': 'freeGameTypeCode',
        'free_game_type_text': 'freeGameTypeText',
        'free_game_type_desc': 'freeGameTypeDesc',
        'free_game_type_id': 'freeGameTypeId'
    }

    def __init__(self, copyright=None, free_game_type_code=None, free_game_type_text=None, free_game_type_desc=None, free_game_type_id=None):  # noqa: E501
        """FreeGameTypeRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._free_game_type_code = None
        self._free_game_type_text = None
        self._free_game_type_desc = None
        self._free_game_type_id = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if free_game_type_code is not None:
            self.free_game_type_code = free_game_type_code
        if free_game_type_text is not None:
            self.free_game_type_text = free_game_type_text
        if free_game_type_desc is not None:
            self.free_game_type_desc = free_game_type_desc
        if free_game_type_id is not None:
            self.free_game_type_id = free_game_type_id

    @property
    def copyright(self):
        """Gets the copyright of this FreeGameTypeRestObject.  # noqa: E501


        :return: The copyright of this FreeGameTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this FreeGameTypeRestObject.


        :param copyright: The copyright of this FreeGameTypeRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def free_game_type_code(self):
        """Gets the free_game_type_code of this FreeGameTypeRestObject.  # noqa: E501


        :return: The free_game_type_code of this FreeGameTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._free_game_type_code

    @free_game_type_code.setter
    def free_game_type_code(self, free_game_type_code):
        """Sets the free_game_type_code of this FreeGameTypeRestObject.


        :param free_game_type_code: The free_game_type_code of this FreeGameTypeRestObject.  # noqa: E501
        :type: str
        """

        self._free_game_type_code = free_game_type_code

    @property
    def free_game_type_text(self):
        """Gets the free_game_type_text of this FreeGameTypeRestObject.  # noqa: E501


        :return: The free_game_type_text of this FreeGameTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._free_game_type_text

    @free_game_type_text.setter
    def free_game_type_text(self, free_game_type_text):
        """Sets the free_game_type_text of this FreeGameTypeRestObject.


        :param free_game_type_text: The free_game_type_text of this FreeGameTypeRestObject.  # noqa: E501
        :type: str
        """

        self._free_game_type_text = free_game_type_text

    @property
    def free_game_type_desc(self):
        """Gets the free_game_type_desc of this FreeGameTypeRestObject.  # noqa: E501


        :return: The free_game_type_desc of this FreeGameTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._free_game_type_desc

    @free_game_type_desc.setter
    def free_game_type_desc(self, free_game_type_desc):
        """Sets the free_game_type_desc of this FreeGameTypeRestObject.


        :param free_game_type_desc: The free_game_type_desc of this FreeGameTypeRestObject.  # noqa: E501
        :type: str
        """

        self._free_game_type_desc = free_game_type_desc

    @property
    def free_game_type_id(self):
        """Gets the free_game_type_id of this FreeGameTypeRestObject.  # noqa: E501


        :return: The free_game_type_id of this FreeGameTypeRestObject.  # noqa: E501
        :rtype: int
        """
        return self._free_game_type_id

    @free_game_type_id.setter
    def free_game_type_id(self, free_game_type_id):
        """Sets the free_game_type_id of this FreeGameTypeRestObject.


        :param free_game_type_id: The free_game_type_id of this FreeGameTypeRestObject.  # noqa: E501
        :type: int
        """

        self._free_game_type_id = free_game_type_id

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
        if issubclass(FreeGameTypeRestObject, dict):
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
        if not isinstance(other, FreeGameTypeRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other