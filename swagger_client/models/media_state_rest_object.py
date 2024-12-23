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

class MediaStateRestObject(object):
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
        'media_state_id': 'int',
        'media_state_code': 'str',
        'media_state_text': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'media_state_id': 'mediaStateId',
        'media_state_code': 'mediaStateCode',
        'media_state_text': 'mediaStateText'
    }

    def __init__(self, copyright=None, media_state_id=None, media_state_code=None, media_state_text=None):  # noqa: E501
        """MediaStateRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._media_state_id = None
        self._media_state_code = None
        self._media_state_text = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if media_state_id is not None:
            self.media_state_id = media_state_id
        if media_state_code is not None:
            self.media_state_code = media_state_code
        if media_state_text is not None:
            self.media_state_text = media_state_text

    @property
    def copyright(self):
        """Gets the copyright of this MediaStateRestObject.  # noqa: E501


        :return: The copyright of this MediaStateRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this MediaStateRestObject.


        :param copyright: The copyright of this MediaStateRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def media_state_id(self):
        """Gets the media_state_id of this MediaStateRestObject.  # noqa: E501


        :return: The media_state_id of this MediaStateRestObject.  # noqa: E501
        :rtype: int
        """
        return self._media_state_id

    @media_state_id.setter
    def media_state_id(self, media_state_id):
        """Sets the media_state_id of this MediaStateRestObject.


        :param media_state_id: The media_state_id of this MediaStateRestObject.  # noqa: E501
        :type: int
        """

        self._media_state_id = media_state_id

    @property
    def media_state_code(self):
        """Gets the media_state_code of this MediaStateRestObject.  # noqa: E501


        :return: The media_state_code of this MediaStateRestObject.  # noqa: E501
        :rtype: str
        """
        return self._media_state_code

    @media_state_code.setter
    def media_state_code(self, media_state_code):
        """Sets the media_state_code of this MediaStateRestObject.


        :param media_state_code: The media_state_code of this MediaStateRestObject.  # noqa: E501
        :type: str
        """

        self._media_state_code = media_state_code

    @property
    def media_state_text(self):
        """Gets the media_state_text of this MediaStateRestObject.  # noqa: E501


        :return: The media_state_text of this MediaStateRestObject.  # noqa: E501
        :rtype: str
        """
        return self._media_state_text

    @media_state_text.setter
    def media_state_text(self, media_state_text):
        """Sets the media_state_text of this MediaStateRestObject.


        :param media_state_text: The media_state_text of this MediaStateRestObject.  # noqa: E501
        :type: str
        """

        self._media_state_text = media_state_text

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
        if issubclass(MediaStateRestObject, dict):
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
        if not isinstance(other, MediaStateRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
