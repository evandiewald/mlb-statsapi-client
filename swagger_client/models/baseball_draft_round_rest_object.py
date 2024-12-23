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

class BaseballDraftRoundRestObject(object):
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
        'round': 'str',
        'picks': 'list[BaseballDraftProspectRestObject]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'round': 'round',
        'picks': 'picks'
    }

    def __init__(self, copyright=None, round=None, picks=None):  # noqa: E501
        """BaseballDraftRoundRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._round = None
        self._picks = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if round is not None:
            self.round = round
        if picks is not None:
            self.picks = picks

    @property
    def copyright(self):
        """Gets the copyright of this BaseballDraftRoundRestObject.  # noqa: E501


        :return: The copyright of this BaseballDraftRoundRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this BaseballDraftRoundRestObject.


        :param copyright: The copyright of this BaseballDraftRoundRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def round(self):
        """Gets the round of this BaseballDraftRoundRestObject.  # noqa: E501


        :return: The round of this BaseballDraftRoundRestObject.  # noqa: E501
        :rtype: str
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this BaseballDraftRoundRestObject.


        :param round: The round of this BaseballDraftRoundRestObject.  # noqa: E501
        :type: str
        """

        self._round = round

    @property
    def picks(self):
        """Gets the picks of this BaseballDraftRoundRestObject.  # noqa: E501


        :return: The picks of this BaseballDraftRoundRestObject.  # noqa: E501
        :rtype: list[BaseballDraftProspectRestObject]
        """
        return self._picks

    @picks.setter
    def picks(self, picks):
        """Sets the picks of this BaseballDraftRoundRestObject.


        :param picks: The picks of this BaseballDraftRoundRestObject.  # noqa: E501
        :type: list[BaseballDraftProspectRestObject]
        """

        self._picks = picks

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
        if issubclass(BaseballDraftRoundRestObject, dict):
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
        if not isinstance(other, BaseballDraftRoundRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
