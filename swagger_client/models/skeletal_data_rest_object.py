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

class SkeletalDataRestObject(object):
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
        'frames': 'list[FrameRestObject]',
        'joint_meta_data': 'dict(str, str)',
        'system': 'SystemRestObject'
    }

    attribute_map = {
        'copyright': 'copyright',
        'frames': 'frames',
        'joint_meta_data': 'jointMetaData',
        'system': 'system'
    }

    def __init__(self, copyright=None, frames=None, joint_meta_data=None, system=None):  # noqa: E501
        """SkeletalDataRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._frames = None
        self._joint_meta_data = None
        self._system = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if frames is not None:
            self.frames = frames
        if joint_meta_data is not None:
            self.joint_meta_data = joint_meta_data
        if system is not None:
            self.system = system

    @property
    def copyright(self):
        """Gets the copyright of this SkeletalDataRestObject.  # noqa: E501


        :return: The copyright of this SkeletalDataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this SkeletalDataRestObject.


        :param copyright: The copyright of this SkeletalDataRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def frames(self):
        """Gets the frames of this SkeletalDataRestObject.  # noqa: E501


        :return: The frames of this SkeletalDataRestObject.  # noqa: E501
        :rtype: list[FrameRestObject]
        """
        return self._frames

    @frames.setter
    def frames(self, frames):
        """Sets the frames of this SkeletalDataRestObject.


        :param frames: The frames of this SkeletalDataRestObject.  # noqa: E501
        :type: list[FrameRestObject]
        """

        self._frames = frames

    @property
    def joint_meta_data(self):
        """Gets the joint_meta_data of this SkeletalDataRestObject.  # noqa: E501


        :return: The joint_meta_data of this SkeletalDataRestObject.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._joint_meta_data

    @joint_meta_data.setter
    def joint_meta_data(self, joint_meta_data):
        """Sets the joint_meta_data of this SkeletalDataRestObject.


        :param joint_meta_data: The joint_meta_data of this SkeletalDataRestObject.  # noqa: E501
        :type: dict(str, str)
        """

        self._joint_meta_data = joint_meta_data

    @property
    def system(self):
        """Gets the system of this SkeletalDataRestObject.  # noqa: E501


        :return: The system of this SkeletalDataRestObject.  # noqa: E501
        :rtype: SystemRestObject
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this SkeletalDataRestObject.


        :param system: The system of this SkeletalDataRestObject.  # noqa: E501
        :type: SystemRestObject
        """

        self._system = system

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
        if issubclass(SkeletalDataRestObject, dict):
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
        if not isinstance(other, SkeletalDataRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
