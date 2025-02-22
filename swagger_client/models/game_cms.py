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

class GameCms(object):
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
        'editorial': 'Editorial',
        'media': 'Media',
        'highlights': 'Highlights',
        'game_notes': 'GameNotes',
        'content_summary': 'ContentSummary',
        'lineup': 'Lineup'
    }

    attribute_map = {
        'editorial': 'editorial',
        'media': 'media',
        'highlights': 'highlights',
        'game_notes': 'gameNotes',
        'content_summary': 'contentSummary',
        'lineup': 'lineup'
    }

    def __init__(self, editorial=None, media=None, highlights=None, game_notes=None, content_summary=None, lineup=None):  # noqa: E501
        """GameCms - a model defined in Swagger"""  # noqa: E501
        self._editorial = None
        self._media = None
        self._highlights = None
        self._game_notes = None
        self._content_summary = None
        self._lineup = None
        self.discriminator = None
        if editorial is not None:
            self.editorial = editorial
        if media is not None:
            self.media = media
        if highlights is not None:
            self.highlights = highlights
        if game_notes is not None:
            self.game_notes = game_notes
        if content_summary is not None:
            self.content_summary = content_summary
        if lineup is not None:
            self.lineup = lineup

    @property
    def editorial(self):
        """Gets the editorial of this GameCms.  # noqa: E501


        :return: The editorial of this GameCms.  # noqa: E501
        :rtype: Editorial
        """
        return self._editorial

    @editorial.setter
    def editorial(self, editorial):
        """Sets the editorial of this GameCms.


        :param editorial: The editorial of this GameCms.  # noqa: E501
        :type: Editorial
        """

        self._editorial = editorial

    @property
    def media(self):
        """Gets the media of this GameCms.  # noqa: E501


        :return: The media of this GameCms.  # noqa: E501
        :rtype: Media
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this GameCms.


        :param media: The media of this GameCms.  # noqa: E501
        :type: Media
        """

        self._media = media

    @property
    def highlights(self):
        """Gets the highlights of this GameCms.  # noqa: E501


        :return: The highlights of this GameCms.  # noqa: E501
        :rtype: Highlights
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """Sets the highlights of this GameCms.


        :param highlights: The highlights of this GameCms.  # noqa: E501
        :type: Highlights
        """

        self._highlights = highlights

    @property
    def game_notes(self):
        """Gets the game_notes of this GameCms.  # noqa: E501


        :return: The game_notes of this GameCms.  # noqa: E501
        :rtype: GameNotes
        """
        return self._game_notes

    @game_notes.setter
    def game_notes(self, game_notes):
        """Sets the game_notes of this GameCms.


        :param game_notes: The game_notes of this GameCms.  # noqa: E501
        :type: GameNotes
        """

        self._game_notes = game_notes

    @property
    def content_summary(self):
        """Gets the content_summary of this GameCms.  # noqa: E501


        :return: The content_summary of this GameCms.  # noqa: E501
        :rtype: ContentSummary
        """
        return self._content_summary

    @content_summary.setter
    def content_summary(self, content_summary):
        """Sets the content_summary of this GameCms.


        :param content_summary: The content_summary of this GameCms.  # noqa: E501
        :type: ContentSummary
        """

        self._content_summary = content_summary

    @property
    def lineup(self):
        """Gets the lineup of this GameCms.  # noqa: E501


        :return: The lineup of this GameCms.  # noqa: E501
        :rtype: Lineup
        """
        return self._lineup

    @lineup.setter
    def lineup(self, lineup):
        """Sets the lineup of this GameCms.


        :param lineup: The lineup of this GameCms.  # noqa: E501
        :type: Lineup
        """

        self._lineup = lineup

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
        if issubclass(GameCms, dict):
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
        if not isinstance(other, GameCms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
