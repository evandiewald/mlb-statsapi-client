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

class BroadcasterXrefId(object):
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
        'xref_id': 'str',
        'xref_type': 'str',
        'xref_id_two': 'str',
        'season': 'str',
        'broadcaster_id': 'int'
    }

    attribute_map = {
        'xref_id': 'xrefId',
        'xref_type': 'xrefType',
        'xref_id_two': 'xrefIdTwo',
        'season': 'season',
        'broadcaster_id': 'broadcasterId'
    }

    def __init__(self, xref_id=None, xref_type=None, xref_id_two=None, season=None, broadcaster_id=None):  # noqa: E501
        """BroadcasterXrefId - a model defined in Swagger"""  # noqa: E501
        self._xref_id = None
        self._xref_type = None
        self._xref_id_two = None
        self._season = None
        self._broadcaster_id = None
        self.discriminator = None
        if xref_id is not None:
            self.xref_id = xref_id
        if xref_type is not None:
            self.xref_type = xref_type
        if xref_id_two is not None:
            self.xref_id_two = xref_id_two
        if season is not None:
            self.season = season
        if broadcaster_id is not None:
            self.broadcaster_id = broadcaster_id

    @property
    def xref_id(self):
        """Gets the xref_id of this BroadcasterXrefId.  # noqa: E501


        :return: The xref_id of this BroadcasterXrefId.  # noqa: E501
        :rtype: str
        """
        return self._xref_id

    @xref_id.setter
    def xref_id(self, xref_id):
        """Sets the xref_id of this BroadcasterXrefId.


        :param xref_id: The xref_id of this BroadcasterXrefId.  # noqa: E501
        :type: str
        """

        self._xref_id = xref_id

    @property
    def xref_type(self):
        """Gets the xref_type of this BroadcasterXrefId.  # noqa: E501


        :return: The xref_type of this BroadcasterXrefId.  # noqa: E501
        :rtype: str
        """
        return self._xref_type

    @xref_type.setter
    def xref_type(self, xref_type):
        """Sets the xref_type of this BroadcasterXrefId.


        :param xref_type: The xref_type of this BroadcasterXrefId.  # noqa: E501
        :type: str
        """

        self._xref_type = xref_type

    @property
    def xref_id_two(self):
        """Gets the xref_id_two of this BroadcasterXrefId.  # noqa: E501


        :return: The xref_id_two of this BroadcasterXrefId.  # noqa: E501
        :rtype: str
        """
        return self._xref_id_two

    @xref_id_two.setter
    def xref_id_two(self, xref_id_two):
        """Sets the xref_id_two of this BroadcasterXrefId.


        :param xref_id_two: The xref_id_two of this BroadcasterXrefId.  # noqa: E501
        :type: str
        """

        self._xref_id_two = xref_id_two

    @property
    def season(self):
        """Gets the season of this BroadcasterXrefId.  # noqa: E501


        :return: The season of this BroadcasterXrefId.  # noqa: E501
        :rtype: str
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this BroadcasterXrefId.


        :param season: The season of this BroadcasterXrefId.  # noqa: E501
        :type: str
        """

        self._season = season

    @property
    def broadcaster_id(self):
        """Gets the broadcaster_id of this BroadcasterXrefId.  # noqa: E501


        :return: The broadcaster_id of this BroadcasterXrefId.  # noqa: E501
        :rtype: int
        """
        return self._broadcaster_id

    @broadcaster_id.setter
    def broadcaster_id(self, broadcaster_id):
        """Sets the broadcaster_id of this BroadcasterXrefId.


        :param broadcaster_id: The broadcaster_id of this BroadcasterXrefId.  # noqa: E501
        :type: int
        """

        self._broadcaster_id = broadcaster_id

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
        if issubclass(BroadcasterXrefId, dict):
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
        if not isinstance(other, BroadcasterXrefId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
