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

class OtherNamesRestObject(object):
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
        'slug': 'str',
        'first_initial_last_name': 'str',
        'last_name_first_initial': 'str',
        'last_first_name': 'str',
        'phonetic_name': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'slug': 'slug',
        'first_initial_last_name': 'firstInitialLastName',
        'last_name_first_initial': 'lastNameFirstInitial',
        'last_first_name': 'lastFirstName',
        'phonetic_name': 'phoneticName'
    }

    def __init__(self, copyright=None, slug=None, first_initial_last_name=None, last_name_first_initial=None, last_first_name=None, phonetic_name=None):  # noqa: E501
        """OtherNamesRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._slug = None
        self._first_initial_last_name = None
        self._last_name_first_initial = None
        self._last_first_name = None
        self._phonetic_name = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if slug is not None:
            self.slug = slug
        if first_initial_last_name is not None:
            self.first_initial_last_name = first_initial_last_name
        if last_name_first_initial is not None:
            self.last_name_first_initial = last_name_first_initial
        if last_first_name is not None:
            self.last_first_name = last_first_name
        if phonetic_name is not None:
            self.phonetic_name = phonetic_name

    @property
    def copyright(self):
        """Gets the copyright of this OtherNamesRestObject.  # noqa: E501


        :return: The copyright of this OtherNamesRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this OtherNamesRestObject.


        :param copyright: The copyright of this OtherNamesRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def slug(self):
        """Gets the slug of this OtherNamesRestObject.  # noqa: E501


        :return: The slug of this OtherNamesRestObject.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this OtherNamesRestObject.


        :param slug: The slug of this OtherNamesRestObject.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def first_initial_last_name(self):
        """Gets the first_initial_last_name of this OtherNamesRestObject.  # noqa: E501


        :return: The first_initial_last_name of this OtherNamesRestObject.  # noqa: E501
        :rtype: str
        """
        return self._first_initial_last_name

    @first_initial_last_name.setter
    def first_initial_last_name(self, first_initial_last_name):
        """Sets the first_initial_last_name of this OtherNamesRestObject.


        :param first_initial_last_name: The first_initial_last_name of this OtherNamesRestObject.  # noqa: E501
        :type: str
        """

        self._first_initial_last_name = first_initial_last_name

    @property
    def last_name_first_initial(self):
        """Gets the last_name_first_initial of this OtherNamesRestObject.  # noqa: E501


        :return: The last_name_first_initial of this OtherNamesRestObject.  # noqa: E501
        :rtype: str
        """
        return self._last_name_first_initial

    @last_name_first_initial.setter
    def last_name_first_initial(self, last_name_first_initial):
        """Sets the last_name_first_initial of this OtherNamesRestObject.


        :param last_name_first_initial: The last_name_first_initial of this OtherNamesRestObject.  # noqa: E501
        :type: str
        """

        self._last_name_first_initial = last_name_first_initial

    @property
    def last_first_name(self):
        """Gets the last_first_name of this OtherNamesRestObject.  # noqa: E501


        :return: The last_first_name of this OtherNamesRestObject.  # noqa: E501
        :rtype: str
        """
        return self._last_first_name

    @last_first_name.setter
    def last_first_name(self, last_first_name):
        """Sets the last_first_name of this OtherNamesRestObject.


        :param last_first_name: The last_first_name of this OtherNamesRestObject.  # noqa: E501
        :type: str
        """

        self._last_first_name = last_first_name

    @property
    def phonetic_name(self):
        """Gets the phonetic_name of this OtherNamesRestObject.  # noqa: E501


        :return: The phonetic_name of this OtherNamesRestObject.  # noqa: E501
        :rtype: str
        """
        return self._phonetic_name

    @phonetic_name.setter
    def phonetic_name(self, phonetic_name):
        """Sets the phonetic_name of this OtherNamesRestObject.


        :param phonetic_name: The phonetic_name of this OtherNamesRestObject.  # noqa: E501
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
        if issubclass(OtherNamesRestObject, dict):
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
        if not isinstance(other, OtherNamesRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
