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

class BaseballTeamUniformRestObject(object):
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
        'id': 'int',
        'team_name': 'str',
        'uniform_assets': 'list[UniformRestObject]',
        'link': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'id': 'id',
        'team_name': 'teamName',
        'uniform_assets': 'uniformAssets',
        'link': 'link'
    }

    def __init__(self, copyright=None, id=None, team_name=None, uniform_assets=None, link=None):  # noqa: E501
        """BaseballTeamUniformRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._id = None
        self._team_name = None
        self._uniform_assets = None
        self._link = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if id is not None:
            self.id = id
        if team_name is not None:
            self.team_name = team_name
        if uniform_assets is not None:
            self.uniform_assets = uniform_assets
        if link is not None:
            self.link = link

    @property
    def copyright(self):
        """Gets the copyright of this BaseballTeamUniformRestObject.  # noqa: E501


        :return: The copyright of this BaseballTeamUniformRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this BaseballTeamUniformRestObject.


        :param copyright: The copyright of this BaseballTeamUniformRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def id(self):
        """Gets the id of this BaseballTeamUniformRestObject.  # noqa: E501


        :return: The id of this BaseballTeamUniformRestObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseballTeamUniformRestObject.


        :param id: The id of this BaseballTeamUniformRestObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def team_name(self):
        """Gets the team_name of this BaseballTeamUniformRestObject.  # noqa: E501


        :return: The team_name of this BaseballTeamUniformRestObject.  # noqa: E501
        :rtype: str
        """
        return self._team_name

    @team_name.setter
    def team_name(self, team_name):
        """Sets the team_name of this BaseballTeamUniformRestObject.


        :param team_name: The team_name of this BaseballTeamUniformRestObject.  # noqa: E501
        :type: str
        """

        self._team_name = team_name

    @property
    def uniform_assets(self):
        """Gets the uniform_assets of this BaseballTeamUniformRestObject.  # noqa: E501


        :return: The uniform_assets of this BaseballTeamUniformRestObject.  # noqa: E501
        :rtype: list[UniformRestObject]
        """
        return self._uniform_assets

    @uniform_assets.setter
    def uniform_assets(self, uniform_assets):
        """Sets the uniform_assets of this BaseballTeamUniformRestObject.


        :param uniform_assets: The uniform_assets of this BaseballTeamUniformRestObject.  # noqa: E501
        :type: list[UniformRestObject]
        """

        self._uniform_assets = uniform_assets

    @property
    def link(self):
        """Gets the link of this BaseballTeamUniformRestObject.  # noqa: E501


        :return: The link of this BaseballTeamUniformRestObject.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this BaseballTeamUniformRestObject.


        :param link: The link of this BaseballTeamUniformRestObject.  # noqa: E501
        :type: str
        """

        self._link = link

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
        if issubclass(BaseballTeamUniformRestObject, dict):
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
        if not isinstance(other, BaseballTeamUniformRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other