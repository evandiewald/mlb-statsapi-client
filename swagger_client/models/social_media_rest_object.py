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

class SocialMediaRestObject(object):
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
        'twitter': 'list[str]',
        'facebook': 'list[str]',
        'instagram': 'list[str]',
        'vine': 'list[str]',
        'periscope': 'list[str]',
        'tumblr': 'list[str]',
        'youtube': 'list[str]',
        'pinterest': 'list[str]',
        'googleplus': 'list[str]',
        'snapchat': 'list[str]',
        'website': 'list[str]',
        'hashtags': 'list[str]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'twitter': 'twitter',
        'facebook': 'facebook',
        'instagram': 'instagram',
        'vine': 'vine',
        'periscope': 'periscope',
        'tumblr': 'tumblr',
        'youtube': 'youtube',
        'pinterest': 'pinterest',
        'googleplus': 'googleplus',
        'snapchat': 'snapchat',
        'website': 'website',
        'hashtags': 'hashtags'
    }

    def __init__(self, copyright=None, twitter=None, facebook=None, instagram=None, vine=None, periscope=None, tumblr=None, youtube=None, pinterest=None, googleplus=None, snapchat=None, website=None, hashtags=None):  # noqa: E501
        """SocialMediaRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._twitter = None
        self._facebook = None
        self._instagram = None
        self._vine = None
        self._periscope = None
        self._tumblr = None
        self._youtube = None
        self._pinterest = None
        self._googleplus = None
        self._snapchat = None
        self._website = None
        self._hashtags = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if twitter is not None:
            self.twitter = twitter
        if facebook is not None:
            self.facebook = facebook
        if instagram is not None:
            self.instagram = instagram
        if vine is not None:
            self.vine = vine
        if periscope is not None:
            self.periscope = periscope
        if tumblr is not None:
            self.tumblr = tumblr
        if youtube is not None:
            self.youtube = youtube
        if pinterest is not None:
            self.pinterest = pinterest
        if googleplus is not None:
            self.googleplus = googleplus
        if snapchat is not None:
            self.snapchat = snapchat
        if website is not None:
            self.website = website
        if hashtags is not None:
            self.hashtags = hashtags

    @property
    def copyright(self):
        """Gets the copyright of this SocialMediaRestObject.  # noqa: E501


        :return: The copyright of this SocialMediaRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this SocialMediaRestObject.


        :param copyright: The copyright of this SocialMediaRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def twitter(self):
        """Gets the twitter of this SocialMediaRestObject.  # noqa: E501


        :return: The twitter of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """Sets the twitter of this SocialMediaRestObject.


        :param twitter: The twitter of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._twitter = twitter

    @property
    def facebook(self):
        """Gets the facebook of this SocialMediaRestObject.  # noqa: E501


        :return: The facebook of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """Sets the facebook of this SocialMediaRestObject.


        :param facebook: The facebook of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._facebook = facebook

    @property
    def instagram(self):
        """Gets the instagram of this SocialMediaRestObject.  # noqa: E501


        :return: The instagram of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._instagram

    @instagram.setter
    def instagram(self, instagram):
        """Sets the instagram of this SocialMediaRestObject.


        :param instagram: The instagram of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._instagram = instagram

    @property
    def vine(self):
        """Gets the vine of this SocialMediaRestObject.  # noqa: E501


        :return: The vine of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._vine

    @vine.setter
    def vine(self, vine):
        """Sets the vine of this SocialMediaRestObject.


        :param vine: The vine of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._vine = vine

    @property
    def periscope(self):
        """Gets the periscope of this SocialMediaRestObject.  # noqa: E501


        :return: The periscope of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._periscope

    @periscope.setter
    def periscope(self, periscope):
        """Sets the periscope of this SocialMediaRestObject.


        :param periscope: The periscope of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._periscope = periscope

    @property
    def tumblr(self):
        """Gets the tumblr of this SocialMediaRestObject.  # noqa: E501


        :return: The tumblr of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._tumblr

    @tumblr.setter
    def tumblr(self, tumblr):
        """Sets the tumblr of this SocialMediaRestObject.


        :param tumblr: The tumblr of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._tumblr = tumblr

    @property
    def youtube(self):
        """Gets the youtube of this SocialMediaRestObject.  # noqa: E501


        :return: The youtube of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._youtube

    @youtube.setter
    def youtube(self, youtube):
        """Sets the youtube of this SocialMediaRestObject.


        :param youtube: The youtube of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._youtube = youtube

    @property
    def pinterest(self):
        """Gets the pinterest of this SocialMediaRestObject.  # noqa: E501


        :return: The pinterest of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._pinterest

    @pinterest.setter
    def pinterest(self, pinterest):
        """Sets the pinterest of this SocialMediaRestObject.


        :param pinterest: The pinterest of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._pinterest = pinterest

    @property
    def googleplus(self):
        """Gets the googleplus of this SocialMediaRestObject.  # noqa: E501


        :return: The googleplus of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._googleplus

    @googleplus.setter
    def googleplus(self, googleplus):
        """Sets the googleplus of this SocialMediaRestObject.


        :param googleplus: The googleplus of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._googleplus = googleplus

    @property
    def snapchat(self):
        """Gets the snapchat of this SocialMediaRestObject.  # noqa: E501


        :return: The snapchat of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._snapchat

    @snapchat.setter
    def snapchat(self, snapchat):
        """Sets the snapchat of this SocialMediaRestObject.


        :param snapchat: The snapchat of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._snapchat = snapchat

    @property
    def website(self):
        """Gets the website of this SocialMediaRestObject.  # noqa: E501


        :return: The website of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this SocialMediaRestObject.


        :param website: The website of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._website = website

    @property
    def hashtags(self):
        """Gets the hashtags of this SocialMediaRestObject.  # noqa: E501


        :return: The hashtags of this SocialMediaRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._hashtags

    @hashtags.setter
    def hashtags(self, hashtags):
        """Sets the hashtags of this SocialMediaRestObject.


        :param hashtags: The hashtags of this SocialMediaRestObject.  # noqa: E501
        :type: list[str]
        """

        self._hashtags = hashtags

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
        if issubclass(SocialMediaRestObject, dict):
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
        if not isinstance(other, SocialMediaRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
