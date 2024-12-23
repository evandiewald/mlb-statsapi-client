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

class Split(object):
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
        'batter': 'str',
        'pitcher': 'str',
        'men_on_base': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'batter': 'batter',
        'pitcher': 'pitcher',
        'men_on_base': 'menOnBase'
    }

    def __init__(self, copyright=None, batter=None, pitcher=None, men_on_base=None):  # noqa: E501
        """Split - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._batter = None
        self._pitcher = None
        self._men_on_base = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if batter is not None:
            self.batter = batter
        if pitcher is not None:
            self.pitcher = pitcher
        if men_on_base is not None:
            self.men_on_base = men_on_base

    @property
    def copyright(self):
        """Gets the copyright of this Split.  # noqa: E501


        :return: The copyright of this Split.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this Split.


        :param copyright: The copyright of this Split.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def batter(self):
        """Gets the batter of this Split.  # noqa: E501


        :return: The batter of this Split.  # noqa: E501
        :rtype: str
        """
        return self._batter

    @batter.setter
    def batter(self, batter):
        """Sets the batter of this Split.


        :param batter: The batter of this Split.  # noqa: E501
        :type: str
        """

        self._batter = batter

    @property
    def pitcher(self):
        """Gets the pitcher of this Split.  # noqa: E501


        :return: The pitcher of this Split.  # noqa: E501
        :rtype: str
        """
        return self._pitcher

    @pitcher.setter
    def pitcher(self, pitcher):
        """Sets the pitcher of this Split.


        :param pitcher: The pitcher of this Split.  # noqa: E501
        :type: str
        """

        self._pitcher = pitcher

    @property
    def men_on_base(self):
        """Gets the men_on_base of this Split.  # noqa: E501


        :return: The men_on_base of this Split.  # noqa: E501
        :rtype: str
        """
        return self._men_on_base

    @men_on_base.setter
    def men_on_base(self, men_on_base):
        """Sets the men_on_base of this Split.


        :param men_on_base: The men_on_base of this Split.  # noqa: E501
        :type: str
        """

        self._men_on_base = men_on_base

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
        if issubclass(Split, dict):
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
        if not isinstance(other, Split):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
