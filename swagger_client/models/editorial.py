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

class Editorial(object):
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
        'probables': 'JsonNode',
        'preview': 'JsonNode',
        'recap': 'JsonNode',
        'articles': 'JsonNode',
        'wrap': 'JsonNode'
    }

    attribute_map = {
        'probables': 'probables',
        'preview': 'preview',
        'recap': 'recap',
        'articles': 'articles',
        'wrap': 'wrap'
    }

    def __init__(self, probables=None, preview=None, recap=None, articles=None, wrap=None):  # noqa: E501
        """Editorial - a model defined in Swagger"""  # noqa: E501
        self._probables = None
        self._preview = None
        self._recap = None
        self._articles = None
        self._wrap = None
        self.discriminator = None
        if probables is not None:
            self.probables = probables
        if preview is not None:
            self.preview = preview
        if recap is not None:
            self.recap = recap
        if articles is not None:
            self.articles = articles
        if wrap is not None:
            self.wrap = wrap

    @property
    def probables(self):
        """Gets the probables of this Editorial.  # noqa: E501


        :return: The probables of this Editorial.  # noqa: E501
        :rtype: JsonNode
        """
        return self._probables

    @probables.setter
    def probables(self, probables):
        """Sets the probables of this Editorial.


        :param probables: The probables of this Editorial.  # noqa: E501
        :type: JsonNode
        """

        self._probables = probables

    @property
    def preview(self):
        """Gets the preview of this Editorial.  # noqa: E501


        :return: The preview of this Editorial.  # noqa: E501
        :rtype: JsonNode
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this Editorial.


        :param preview: The preview of this Editorial.  # noqa: E501
        :type: JsonNode
        """

        self._preview = preview

    @property
    def recap(self):
        """Gets the recap of this Editorial.  # noqa: E501


        :return: The recap of this Editorial.  # noqa: E501
        :rtype: JsonNode
        """
        return self._recap

    @recap.setter
    def recap(self, recap):
        """Sets the recap of this Editorial.


        :param recap: The recap of this Editorial.  # noqa: E501
        :type: JsonNode
        """

        self._recap = recap

    @property
    def articles(self):
        """Gets the articles of this Editorial.  # noqa: E501


        :return: The articles of this Editorial.  # noqa: E501
        :rtype: JsonNode
        """
        return self._articles

    @articles.setter
    def articles(self, articles):
        """Sets the articles of this Editorial.


        :param articles: The articles of this Editorial.  # noqa: E501
        :type: JsonNode
        """

        self._articles = articles

    @property
    def wrap(self):
        """Gets the wrap of this Editorial.  # noqa: E501


        :return: The wrap of this Editorial.  # noqa: E501
        :rtype: JsonNode
        """
        return self._wrap

    @wrap.setter
    def wrap(self, wrap):
        """Sets the wrap of this Editorial.


        :param wrap: The wrap of this Editorial.  # noqa: E501
        :type: JsonNode
        """

        self._wrap = wrap

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
        if issubclass(Editorial, dict):
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
        if not isinstance(other, Editorial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
