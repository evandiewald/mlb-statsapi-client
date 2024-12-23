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

class LiveLookin(object):
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
        'game_pk': 'int',
        'media_playback_id': 'int',
        'kicker': 'str',
        'headline': 'str',
        'playbacks': 'list[LiveLookinPlayback]'
    }

    attribute_map = {
        'game_pk': 'gamePk',
        'media_playback_id': 'mediaPlaybackId',
        'kicker': 'kicker',
        'headline': 'headline',
        'playbacks': 'playbacks'
    }

    def __init__(self, game_pk=None, media_playback_id=None, kicker=None, headline=None, playbacks=None):  # noqa: E501
        """LiveLookin - a model defined in Swagger"""  # noqa: E501
        self._game_pk = None
        self._media_playback_id = None
        self._kicker = None
        self._headline = None
        self._playbacks = None
        self.discriminator = None
        if game_pk is not None:
            self.game_pk = game_pk
        if media_playback_id is not None:
            self.media_playback_id = media_playback_id
        if kicker is not None:
            self.kicker = kicker
        if headline is not None:
            self.headline = headline
        if playbacks is not None:
            self.playbacks = playbacks

    @property
    def game_pk(self):
        """Gets the game_pk of this LiveLookin.  # noqa: E501


        :return: The game_pk of this LiveLookin.  # noqa: E501
        :rtype: int
        """
        return self._game_pk

    @game_pk.setter
    def game_pk(self, game_pk):
        """Sets the game_pk of this LiveLookin.


        :param game_pk: The game_pk of this LiveLookin.  # noqa: E501
        :type: int
        """

        self._game_pk = game_pk

    @property
    def media_playback_id(self):
        """Gets the media_playback_id of this LiveLookin.  # noqa: E501


        :return: The media_playback_id of this LiveLookin.  # noqa: E501
        :rtype: int
        """
        return self._media_playback_id

    @media_playback_id.setter
    def media_playback_id(self, media_playback_id):
        """Sets the media_playback_id of this LiveLookin.


        :param media_playback_id: The media_playback_id of this LiveLookin.  # noqa: E501
        :type: int
        """

        self._media_playback_id = media_playback_id

    @property
    def kicker(self):
        """Gets the kicker of this LiveLookin.  # noqa: E501


        :return: The kicker of this LiveLookin.  # noqa: E501
        :rtype: str
        """
        return self._kicker

    @kicker.setter
    def kicker(self, kicker):
        """Sets the kicker of this LiveLookin.


        :param kicker: The kicker of this LiveLookin.  # noqa: E501
        :type: str
        """

        self._kicker = kicker

    @property
    def headline(self):
        """Gets the headline of this LiveLookin.  # noqa: E501


        :return: The headline of this LiveLookin.  # noqa: E501
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """Sets the headline of this LiveLookin.


        :param headline: The headline of this LiveLookin.  # noqa: E501
        :type: str
        """

        self._headline = headline

    @property
    def playbacks(self):
        """Gets the playbacks of this LiveLookin.  # noqa: E501


        :return: The playbacks of this LiveLookin.  # noqa: E501
        :rtype: list[LiveLookinPlayback]
        """
        return self._playbacks

    @playbacks.setter
    def playbacks(self, playbacks):
        """Sets the playbacks of this LiveLookin.


        :param playbacks: The playbacks of this LiveLookin.  # noqa: E501
        :type: list[LiveLookinPlayback]
        """

        self._playbacks = playbacks

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
        if issubclass(LiveLookin, dict):
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
        if not isinstance(other, LiveLookin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
