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

class BaseballGameLiveLookinRestObject(object):
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
        'game_pk': 'int',
        'media_playback_id': 'int',
        'headline': 'str',
        'kicker': 'str',
        'playbacks': 'list[LiveLookinPlayback]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'game_pk': 'gamePk',
        'media_playback_id': 'mediaPlaybackId',
        'headline': 'headline',
        'kicker': 'kicker',
        'playbacks': 'playbacks'
    }

    def __init__(self, copyright=None, game_pk=None, media_playback_id=None, headline=None, kicker=None, playbacks=None):  # noqa: E501
        """BaseballGameLiveLookinRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._game_pk = None
        self._media_playback_id = None
        self._headline = None
        self._kicker = None
        self._playbacks = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if game_pk is not None:
            self.game_pk = game_pk
        if media_playback_id is not None:
            self.media_playback_id = media_playback_id
        if headline is not None:
            self.headline = headline
        if kicker is not None:
            self.kicker = kicker
        if playbacks is not None:
            self.playbacks = playbacks

    @property
    def copyright(self):
        """Gets the copyright of this BaseballGameLiveLookinRestObject.  # noqa: E501


        :return: The copyright of this BaseballGameLiveLookinRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this BaseballGameLiveLookinRestObject.


        :param copyright: The copyright of this BaseballGameLiveLookinRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def game_pk(self):
        """Gets the game_pk of this BaseballGameLiveLookinRestObject.  # noqa: E501


        :return: The game_pk of this BaseballGameLiveLookinRestObject.  # noqa: E501
        :rtype: int
        """
        return self._game_pk

    @game_pk.setter
    def game_pk(self, game_pk):
        """Sets the game_pk of this BaseballGameLiveLookinRestObject.


        :param game_pk: The game_pk of this BaseballGameLiveLookinRestObject.  # noqa: E501
        :type: int
        """

        self._game_pk = game_pk

    @property
    def media_playback_id(self):
        """Gets the media_playback_id of this BaseballGameLiveLookinRestObject.  # noqa: E501


        :return: The media_playback_id of this BaseballGameLiveLookinRestObject.  # noqa: E501
        :rtype: int
        """
        return self._media_playback_id

    @media_playback_id.setter
    def media_playback_id(self, media_playback_id):
        """Sets the media_playback_id of this BaseballGameLiveLookinRestObject.


        :param media_playback_id: The media_playback_id of this BaseballGameLiveLookinRestObject.  # noqa: E501
        :type: int
        """

        self._media_playback_id = media_playback_id

    @property
    def headline(self):
        """Gets the headline of this BaseballGameLiveLookinRestObject.  # noqa: E501


        :return: The headline of this BaseballGameLiveLookinRestObject.  # noqa: E501
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """Sets the headline of this BaseballGameLiveLookinRestObject.


        :param headline: The headline of this BaseballGameLiveLookinRestObject.  # noqa: E501
        :type: str
        """

        self._headline = headline

    @property
    def kicker(self):
        """Gets the kicker of this BaseballGameLiveLookinRestObject.  # noqa: E501


        :return: The kicker of this BaseballGameLiveLookinRestObject.  # noqa: E501
        :rtype: str
        """
        return self._kicker

    @kicker.setter
    def kicker(self, kicker):
        """Sets the kicker of this BaseballGameLiveLookinRestObject.


        :param kicker: The kicker of this BaseballGameLiveLookinRestObject.  # noqa: E501
        :type: str
        """

        self._kicker = kicker

    @property
    def playbacks(self):
        """Gets the playbacks of this BaseballGameLiveLookinRestObject.  # noqa: E501


        :return: The playbacks of this BaseballGameLiveLookinRestObject.  # noqa: E501
        :rtype: list[LiveLookinPlayback]
        """
        return self._playbacks

    @playbacks.setter
    def playbacks(self, playbacks):
        """Sets the playbacks of this BaseballGameLiveLookinRestObject.


        :param playbacks: The playbacks of this BaseballGameLiveLookinRestObject.  # noqa: E501
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
        if issubclass(BaseballGameLiveLookinRestObject, dict):
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
        if not isinstance(other, BaseballGameLiveLookinRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
