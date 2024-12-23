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

class AnalyticsGameMetadataRestObject(object):
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
        'game_pk': 'str',
        'updated_at': 'str',
        'audit_updated_at': 'str',
        'metrics_updated_at': 'str',
        'video_updated_at': 'str',
        'link': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'game_pk': 'gamePk',
        'updated_at': 'updatedAt',
        'audit_updated_at': 'auditUpdatedAt',
        'metrics_updated_at': 'metricsUpdatedAt',
        'video_updated_at': 'videoUpdatedAt',
        'link': 'link'
    }

    def __init__(self, copyright=None, game_pk=None, updated_at=None, audit_updated_at=None, metrics_updated_at=None, video_updated_at=None, link=None):  # noqa: E501
        """AnalyticsGameMetadataRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._game_pk = None
        self._updated_at = None
        self._audit_updated_at = None
        self._metrics_updated_at = None
        self._video_updated_at = None
        self._link = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if game_pk is not None:
            self.game_pk = game_pk
        if updated_at is not None:
            self.updated_at = updated_at
        if audit_updated_at is not None:
            self.audit_updated_at = audit_updated_at
        if metrics_updated_at is not None:
            self.metrics_updated_at = metrics_updated_at
        if video_updated_at is not None:
            self.video_updated_at = video_updated_at
        if link is not None:
            self.link = link

    @property
    def copyright(self):
        """Gets the copyright of this AnalyticsGameMetadataRestObject.  # noqa: E501


        :return: The copyright of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this AnalyticsGameMetadataRestObject.


        :param copyright: The copyright of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def game_pk(self):
        """Gets the game_pk of this AnalyticsGameMetadataRestObject.  # noqa: E501


        :return: The game_pk of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._game_pk

    @game_pk.setter
    def game_pk(self, game_pk):
        """Sets the game_pk of this AnalyticsGameMetadataRestObject.


        :param game_pk: The game_pk of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :type: str
        """

        self._game_pk = game_pk

    @property
    def updated_at(self):
        """Gets the updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501


        :return: The updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AnalyticsGameMetadataRestObject.


        :param updated_at: The updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def audit_updated_at(self):
        """Gets the audit_updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501


        :return: The audit_updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._audit_updated_at

    @audit_updated_at.setter
    def audit_updated_at(self, audit_updated_at):
        """Sets the audit_updated_at of this AnalyticsGameMetadataRestObject.


        :param audit_updated_at: The audit_updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :type: str
        """

        self._audit_updated_at = audit_updated_at

    @property
    def metrics_updated_at(self):
        """Gets the metrics_updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501


        :return: The metrics_updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._metrics_updated_at

    @metrics_updated_at.setter
    def metrics_updated_at(self, metrics_updated_at):
        """Sets the metrics_updated_at of this AnalyticsGameMetadataRestObject.


        :param metrics_updated_at: The metrics_updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :type: str
        """

        self._metrics_updated_at = metrics_updated_at

    @property
    def video_updated_at(self):
        """Gets the video_updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501


        :return: The video_updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._video_updated_at

    @video_updated_at.setter
    def video_updated_at(self, video_updated_at):
        """Sets the video_updated_at of this AnalyticsGameMetadataRestObject.


        :param video_updated_at: The video_updated_at of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :type: str
        """

        self._video_updated_at = video_updated_at

    @property
    def link(self):
        """Gets the link of this AnalyticsGameMetadataRestObject.  # noqa: E501


        :return: The link of this AnalyticsGameMetadataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this AnalyticsGameMetadataRestObject.


        :param link: The link of this AnalyticsGameMetadataRestObject.  # noqa: E501
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
        if issubclass(AnalyticsGameMetadataRestObject, dict):
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
        if not isinstance(other, AnalyticsGameMetadataRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other