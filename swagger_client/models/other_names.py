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

class OtherNames(object):
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
        'id': 'int',
        'first_name': 'str',
        'last_name': 'str',
        'slug': 'str',
        'phonetic_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'slug': 'slug',
        'phonetic_name': 'phoneticName'
    }

    def __init__(self, id=None, first_name=None, last_name=None, slug=None, phonetic_name=None):  # noqa: E501
        """OtherNames - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._first_name = None
        self._last_name = None
        self._slug = None
        self._phonetic_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if slug is not None:
            self.slug = slug
        if phonetic_name is not None:
            self.phonetic_name = phonetic_name

    @property
    def id(self):
        """Gets the id of this OtherNames.  # noqa: E501


        :return: The id of this OtherNames.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OtherNames.


        :param id: The id of this OtherNames.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this OtherNames.  # noqa: E501


        :return: The first_name of this OtherNames.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this OtherNames.


        :param first_name: The first_name of this OtherNames.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this OtherNames.  # noqa: E501


        :return: The last_name of this OtherNames.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this OtherNames.


        :param last_name: The last_name of this OtherNames.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def slug(self):
        """Gets the slug of this OtherNames.  # noqa: E501


        :return: The slug of this OtherNames.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this OtherNames.


        :param slug: The slug of this OtherNames.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def phonetic_name(self):
        """Gets the phonetic_name of this OtherNames.  # noqa: E501


        :return: The phonetic_name of this OtherNames.  # noqa: E501
        :rtype: str
        """
        return self._phonetic_name

    @phonetic_name.setter
    def phonetic_name(self, phonetic_name):
        """Sets the phonetic_name of this OtherNames.


        :param phonetic_name: The phonetic_name of this OtherNames.  # noqa: E501
        :type: str
        """

        self._phonetic_name = phonetic_name

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
        if issubclass(OtherNames, dict):
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
        if not isinstance(other, OtherNames):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other