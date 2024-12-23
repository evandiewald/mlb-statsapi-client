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

class UniformAssetTypeRestObject(object):
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
        'uniform_asset_type_desc': 'str',
        'uniform_asset_type_code': 'str',
        'uniform_asset_type_text': 'str',
        'uniform_asset_type_id': 'int'
    }

    attribute_map = {
        'copyright': 'copyright',
        'uniform_asset_type_desc': 'uniformAssetTypeDesc',
        'uniform_asset_type_code': 'uniformAssetTypeCode',
        'uniform_asset_type_text': 'uniformAssetTypeText',
        'uniform_asset_type_id': 'uniformAssetTypeId'
    }

    def __init__(self, copyright=None, uniform_asset_type_desc=None, uniform_asset_type_code=None, uniform_asset_type_text=None, uniform_asset_type_id=None):  # noqa: E501
        """UniformAssetTypeRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._uniform_asset_type_desc = None
        self._uniform_asset_type_code = None
        self._uniform_asset_type_text = None
        self._uniform_asset_type_id = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if uniform_asset_type_desc is not None:
            self.uniform_asset_type_desc = uniform_asset_type_desc
        if uniform_asset_type_code is not None:
            self.uniform_asset_type_code = uniform_asset_type_code
        if uniform_asset_type_text is not None:
            self.uniform_asset_type_text = uniform_asset_type_text
        if uniform_asset_type_id is not None:
            self.uniform_asset_type_id = uniform_asset_type_id

    @property
    def copyright(self):
        """Gets the copyright of this UniformAssetTypeRestObject.  # noqa: E501


        :return: The copyright of this UniformAssetTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this UniformAssetTypeRestObject.


        :param copyright: The copyright of this UniformAssetTypeRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def uniform_asset_type_desc(self):
        """Gets the uniform_asset_type_desc of this UniformAssetTypeRestObject.  # noqa: E501


        :return: The uniform_asset_type_desc of this UniformAssetTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._uniform_asset_type_desc

    @uniform_asset_type_desc.setter
    def uniform_asset_type_desc(self, uniform_asset_type_desc):
        """Sets the uniform_asset_type_desc of this UniformAssetTypeRestObject.


        :param uniform_asset_type_desc: The uniform_asset_type_desc of this UniformAssetTypeRestObject.  # noqa: E501
        :type: str
        """

        self._uniform_asset_type_desc = uniform_asset_type_desc

    @property
    def uniform_asset_type_code(self):
        """Gets the uniform_asset_type_code of this UniformAssetTypeRestObject.  # noqa: E501


        :return: The uniform_asset_type_code of this UniformAssetTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._uniform_asset_type_code

    @uniform_asset_type_code.setter
    def uniform_asset_type_code(self, uniform_asset_type_code):
        """Sets the uniform_asset_type_code of this UniformAssetTypeRestObject.


        :param uniform_asset_type_code: The uniform_asset_type_code of this UniformAssetTypeRestObject.  # noqa: E501
        :type: str
        """

        self._uniform_asset_type_code = uniform_asset_type_code

    @property
    def uniform_asset_type_text(self):
        """Gets the uniform_asset_type_text of this UniformAssetTypeRestObject.  # noqa: E501


        :return: The uniform_asset_type_text of this UniformAssetTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._uniform_asset_type_text

    @uniform_asset_type_text.setter
    def uniform_asset_type_text(self, uniform_asset_type_text):
        """Sets the uniform_asset_type_text of this UniformAssetTypeRestObject.


        :param uniform_asset_type_text: The uniform_asset_type_text of this UniformAssetTypeRestObject.  # noqa: E501
        :type: str
        """

        self._uniform_asset_type_text = uniform_asset_type_text

    @property
    def uniform_asset_type_id(self):
        """Gets the uniform_asset_type_id of this UniformAssetTypeRestObject.  # noqa: E501


        :return: The uniform_asset_type_id of this UniformAssetTypeRestObject.  # noqa: E501
        :rtype: int
        """
        return self._uniform_asset_type_id

    @uniform_asset_type_id.setter
    def uniform_asset_type_id(self, uniform_asset_type_id):
        """Sets the uniform_asset_type_id of this UniformAssetTypeRestObject.


        :param uniform_asset_type_id: The uniform_asset_type_id of this UniformAssetTypeRestObject.  # noqa: E501
        :type: int
        """

        self._uniform_asset_type_id = uniform_asset_type_id

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
        if issubclass(UniformAssetTypeRestObject, dict):
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
        if not isinstance(other, UniformAssetTypeRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other