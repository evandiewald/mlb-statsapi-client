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

class GameContentRestObject(object):
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
        'link': 'str',
        'editorial': 'GameEditorialRestObject',
        'media': 'GameMediaRestObject',
        'highlights': 'GameHighlightsRestObject',
        'summary': 'GameContentSummaryRestObject',
        'game_notes': 'GameNotesRestObject'
    }

    attribute_map = {
        'copyright': 'copyright',
        'link': 'link',
        'editorial': 'editorial',
        'media': 'media',
        'highlights': 'highlights',
        'summary': 'summary',
        'game_notes': 'gameNotes'
    }

    def __init__(self, copyright=None, link=None, editorial=None, media=None, highlights=None, summary=None, game_notes=None):  # noqa: E501
        """GameContentRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._link = None
        self._editorial = None
        self._media = None
        self._highlights = None
        self._summary = None
        self._game_notes = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if link is not None:
            self.link = link
        if editorial is not None:
            self.editorial = editorial
        if media is not None:
            self.media = media
        if highlights is not None:
            self.highlights = highlights
        if summary is not None:
            self.summary = summary
        if game_notes is not None:
            self.game_notes = game_notes

    @property
    def copyright(self):
        """Gets the copyright of this GameContentRestObject.  # noqa: E501


        :return: The copyright of this GameContentRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this GameContentRestObject.


        :param copyright: The copyright of this GameContentRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def link(self):
        """Gets the link of this GameContentRestObject.  # noqa: E501


        :return: The link of this GameContentRestObject.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this GameContentRestObject.


        :param link: The link of this GameContentRestObject.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def editorial(self):
        """Gets the editorial of this GameContentRestObject.  # noqa: E501


        :return: The editorial of this GameContentRestObject.  # noqa: E501
        :rtype: GameEditorialRestObject
        """
        return self._editorial

    @editorial.setter
    def editorial(self, editorial):
        """Sets the editorial of this GameContentRestObject.


        :param editorial: The editorial of this GameContentRestObject.  # noqa: E501
        :type: GameEditorialRestObject
        """

        self._editorial = editorial

    @property
    def media(self):
        """Gets the media of this GameContentRestObject.  # noqa: E501


        :return: The media of this GameContentRestObject.  # noqa: E501
        :rtype: GameMediaRestObject
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this GameContentRestObject.


        :param media: The media of this GameContentRestObject.  # noqa: E501
        :type: GameMediaRestObject
        """

        self._media = media

    @property
    def highlights(self):
        """Gets the highlights of this GameContentRestObject.  # noqa: E501


        :return: The highlights of this GameContentRestObject.  # noqa: E501
        :rtype: GameHighlightsRestObject
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """Sets the highlights of this GameContentRestObject.


        :param highlights: The highlights of this GameContentRestObject.  # noqa: E501
        :type: GameHighlightsRestObject
        """

        self._highlights = highlights

    @property
    def summary(self):
        """Gets the summary of this GameContentRestObject.  # noqa: E501


        :return: The summary of this GameContentRestObject.  # noqa: E501
        :rtype: GameContentSummaryRestObject
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this GameContentRestObject.


        :param summary: The summary of this GameContentRestObject.  # noqa: E501
        :type: GameContentSummaryRestObject
        """

        self._summary = summary

    @property
    def game_notes(self):
        """Gets the game_notes of this GameContentRestObject.  # noqa: E501


        :return: The game_notes of this GameContentRestObject.  # noqa: E501
        :rtype: GameNotesRestObject
        """
        return self._game_notes

    @game_notes.setter
    def game_notes(self, game_notes):
        """Sets the game_notes of this GameContentRestObject.


        :param game_notes: The game_notes of this GameContentRestObject.  # noqa: E501
        :type: GameNotesRestObject
        """

        self._game_notes = game_notes

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
        if issubclass(GameContentRestObject, dict):
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
        if not isinstance(other, GameContentRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other