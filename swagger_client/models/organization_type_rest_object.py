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

class OrganizationTypeRestObject(object):
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
        'org_type_id': 'int',
        'org_type_code': 'str',
        'org_type_text': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'org_type_id': 'orgTypeId',
        'org_type_code': 'orgTypeCode',
        'org_type_text': 'orgTypeText'
    }

    def __init__(self, copyright=None, org_type_id=None, org_type_code=None, org_type_text=None):  # noqa: E501
        """OrganizationTypeRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._org_type_id = None
        self._org_type_code = None
        self._org_type_text = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if org_type_id is not None:
            self.org_type_id = org_type_id
        if org_type_code is not None:
            self.org_type_code = org_type_code
        if org_type_text is not None:
            self.org_type_text = org_type_text

    @property
    def copyright(self):
        """Gets the copyright of this OrganizationTypeRestObject.  # noqa: E501


        :return: The copyright of this OrganizationTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this OrganizationTypeRestObject.


        :param copyright: The copyright of this OrganizationTypeRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def org_type_id(self):
        """Gets the org_type_id of this OrganizationTypeRestObject.  # noqa: E501


        :return: The org_type_id of this OrganizationTypeRestObject.  # noqa: E501
        :rtype: int
        """
        return self._org_type_id

    @org_type_id.setter
    def org_type_id(self, org_type_id):
        """Sets the org_type_id of this OrganizationTypeRestObject.


        :param org_type_id: The org_type_id of this OrganizationTypeRestObject.  # noqa: E501
        :type: int
        """

        self._org_type_id = org_type_id

    @property
    def org_type_code(self):
        """Gets the org_type_code of this OrganizationTypeRestObject.  # noqa: E501


        :return: The org_type_code of this OrganizationTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._org_type_code

    @org_type_code.setter
    def org_type_code(self, org_type_code):
        """Sets the org_type_code of this OrganizationTypeRestObject.


        :param org_type_code: The org_type_code of this OrganizationTypeRestObject.  # noqa: E501
        :type: str
        """

        self._org_type_code = org_type_code

    @property
    def org_type_text(self):
        """Gets the org_type_text of this OrganizationTypeRestObject.  # noqa: E501


        :return: The org_type_text of this OrganizationTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._org_type_text

    @org_type_text.setter
    def org_type_text(self, org_type_text):
        """Sets the org_type_text of this OrganizationTypeRestObject.


        :param org_type_text: The org_type_text of this OrganizationTypeRestObject.  # noqa: E501
        :type: str
        """

        self._org_type_text = org_type_text

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
        if issubclass(OrganizationTypeRestObject, dict):
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
        if not isinstance(other, OrganizationTypeRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other