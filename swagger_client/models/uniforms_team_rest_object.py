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

class UniformsTeamRestObject(object):
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
        'team_id': 'int',
        'uniform_assets': 'list[UniformRestObject]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'team_id': 'teamId',
        'uniform_assets': 'uniformAssets'
    }

    def __init__(self, copyright=None, team_id=None, uniform_assets=None):  # noqa: E501
        """UniformsTeamRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._team_id = None
        self._uniform_assets = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if team_id is not None:
            self.team_id = team_id
        if uniform_assets is not None:
            self.uniform_assets = uniform_assets

    @property
    def copyright(self):
        """Gets the copyright of this UniformsTeamRestObject.  # noqa: E501


        :return: The copyright of this UniformsTeamRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this UniformsTeamRestObject.


        :param copyright: The copyright of this UniformsTeamRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def team_id(self):
        """Gets the team_id of this UniformsTeamRestObject.  # noqa: E501


        :return: The team_id of this UniformsTeamRestObject.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this UniformsTeamRestObject.


        :param team_id: The team_id of this UniformsTeamRestObject.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def uniform_assets(self):
        """Gets the uniform_assets of this UniformsTeamRestObject.  # noqa: E501


        :return: The uniform_assets of this UniformsTeamRestObject.  # noqa: E501
        :rtype: list[UniformRestObject]
        """
        return self._uniform_assets

    @uniform_assets.setter
    def uniform_assets(self, uniform_assets):
        """Sets the uniform_assets of this UniformsTeamRestObject.


        :param uniform_assets: The uniform_assets of this UniformsTeamRestObject.  # noqa: E501
        :type: list[UniformRestObject]
        """

        self._uniform_assets = uniform_assets

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
        if issubclass(UniformsTeamRestObject, dict):
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
        if not isinstance(other, UniformsTeamRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
