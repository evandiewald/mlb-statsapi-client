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

class VideoResolutionEnumRestObject(object):
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
        'code': 'str',
        'resolution_short': 'str',
        'resolution_full': 'str'
    }

    attribute_map = {
        'code': 'code',
        'resolution_short': 'resolutionShort',
        'resolution_full': 'resolutionFull'
    }

    def __init__(self, code=None, resolution_short=None, resolution_full=None):  # noqa: E501
        """VideoResolutionEnumRestObject - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._resolution_short = None
        self._resolution_full = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if resolution_short is not None:
            self.resolution_short = resolution_short
        if resolution_full is not None:
            self.resolution_full = resolution_full

    @property
    def code(self):
        """Gets the code of this VideoResolutionEnumRestObject.  # noqa: E501


        :return: The code of this VideoResolutionEnumRestObject.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this VideoResolutionEnumRestObject.


        :param code: The code of this VideoResolutionEnumRestObject.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def resolution_short(self):
        """Gets the resolution_short of this VideoResolutionEnumRestObject.  # noqa: E501


        :return: The resolution_short of this VideoResolutionEnumRestObject.  # noqa: E501
        :rtype: str
        """
        return self._resolution_short

    @resolution_short.setter
    def resolution_short(self, resolution_short):
        """Sets the resolution_short of this VideoResolutionEnumRestObject.


        :param resolution_short: The resolution_short of this VideoResolutionEnumRestObject.  # noqa: E501
        :type: str
        """

        self._resolution_short = resolution_short

    @property
    def resolution_full(self):
        """Gets the resolution_full of this VideoResolutionEnumRestObject.  # noqa: E501


        :return: The resolution_full of this VideoResolutionEnumRestObject.  # noqa: E501
        :rtype: str
        """
        return self._resolution_full

    @resolution_full.setter
    def resolution_full(self, resolution_full):
        """Sets the resolution_full of this VideoResolutionEnumRestObject.


        :param resolution_full: The resolution_full of this VideoResolutionEnumRestObject.  # noqa: E501
        :type: str
        """

        self._resolution_full = resolution_full

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
        if issubclass(VideoResolutionEnumRestObject, dict):
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
        if not isinstance(other, VideoResolutionEnumRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
