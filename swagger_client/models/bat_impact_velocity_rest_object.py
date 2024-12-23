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

class BatImpactVelocityRestObject(object):
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
        'before': 'BatImpactVelocityRestObjectBefore',
        'after': 'BatImpactVelocityRestObjectAfter'
    }

    attribute_map = {
        'copyright': 'copyright',
        'before': 'before',
        'after': 'after'
    }

    def __init__(self, copyright=None, before=None, after=None):  # noqa: E501
        """BatImpactVelocityRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._before = None
        self._after = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if before is not None:
            self.before = before
        if after is not None:
            self.after = after

    @property
    def copyright(self):
        """Gets the copyright of this BatImpactVelocityRestObject.  # noqa: E501


        :return: The copyright of this BatImpactVelocityRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this BatImpactVelocityRestObject.


        :param copyright: The copyright of this BatImpactVelocityRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def before(self):
        """Gets the before of this BatImpactVelocityRestObject.  # noqa: E501


        :return: The before of this BatImpactVelocityRestObject.  # noqa: E501
        :rtype: BatImpactVelocityRestObjectBefore
        """
        return self._before

    @before.setter
    def before(self, before):
        """Sets the before of this BatImpactVelocityRestObject.


        :param before: The before of this BatImpactVelocityRestObject.  # noqa: E501
        :type: BatImpactVelocityRestObjectBefore
        """

        self._before = before

    @property
    def after(self):
        """Gets the after of this BatImpactVelocityRestObject.  # noqa: E501


        :return: The after of this BatImpactVelocityRestObject.  # noqa: E501
        :rtype: BatImpactVelocityRestObjectAfter
        """
        return self._after

    @after.setter
    def after(self, after):
        """Sets the after of this BatImpactVelocityRestObject.


        :param after: The after of this BatImpactVelocityRestObject.  # noqa: E501
        :type: BatImpactVelocityRestObjectAfter
        """

        self._after = after

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
        if issubclass(BatImpactVelocityRestObject, dict):
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
        if not isinstance(other, BatImpactVelocityRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
