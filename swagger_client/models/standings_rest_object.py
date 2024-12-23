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

class StandingsRestObject(object):
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
        'last_updated': 'datetime',
        'records': 'list[TeamStandingsRecordContainerRestObject]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'last_updated': 'lastUpdated',
        'records': 'records'
    }

    def __init__(self, copyright=None, last_updated=None, records=None):  # noqa: E501
        """StandingsRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._last_updated = None
        self._records = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if last_updated is not None:
            self.last_updated = last_updated
        if records is not None:
            self.records = records

    @property
    def copyright(self):
        """Gets the copyright of this StandingsRestObject.  # noqa: E501


        :return: The copyright of this StandingsRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this StandingsRestObject.


        :param copyright: The copyright of this StandingsRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def last_updated(self):
        """Gets the last_updated of this StandingsRestObject.  # noqa: E501


        :return: The last_updated of this StandingsRestObject.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this StandingsRestObject.


        :param last_updated: The last_updated of this StandingsRestObject.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def records(self):
        """Gets the records of this StandingsRestObject.  # noqa: E501


        :return: The records of this StandingsRestObject.  # noqa: E501
        :rtype: list[TeamStandingsRecordContainerRestObject]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this StandingsRestObject.


        :param records: The records of this StandingsRestObject.  # noqa: E501
        :type: list[TeamStandingsRecordContainerRestObject]
        """

        self._records = records

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
        if issubclass(StandingsRestObject, dict):
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
        if not isinstance(other, StandingsRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other