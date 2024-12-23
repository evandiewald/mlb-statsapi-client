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

class MilestoneTypeRestObject(object):
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
        'milestone_type_id': 'int',
        'milestone_type_code': 'str',
        'milestone_type_text': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'milestone_type_id': 'milestoneTypeId',
        'milestone_type_code': 'milestoneTypeCode',
        'milestone_type_text': 'milestoneTypeText'
    }

    def __init__(self, copyright=None, milestone_type_id=None, milestone_type_code=None, milestone_type_text=None):  # noqa: E501
        """MilestoneTypeRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._milestone_type_id = None
        self._milestone_type_code = None
        self._milestone_type_text = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if milestone_type_id is not None:
            self.milestone_type_id = milestone_type_id
        if milestone_type_code is not None:
            self.milestone_type_code = milestone_type_code
        if milestone_type_text is not None:
            self.milestone_type_text = milestone_type_text

    @property
    def copyright(self):
        """Gets the copyright of this MilestoneTypeRestObject.  # noqa: E501


        :return: The copyright of this MilestoneTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this MilestoneTypeRestObject.


        :param copyright: The copyright of this MilestoneTypeRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def milestone_type_id(self):
        """Gets the milestone_type_id of this MilestoneTypeRestObject.  # noqa: E501


        :return: The milestone_type_id of this MilestoneTypeRestObject.  # noqa: E501
        :rtype: int
        """
        return self._milestone_type_id

    @milestone_type_id.setter
    def milestone_type_id(self, milestone_type_id):
        """Sets the milestone_type_id of this MilestoneTypeRestObject.


        :param milestone_type_id: The milestone_type_id of this MilestoneTypeRestObject.  # noqa: E501
        :type: int
        """

        self._milestone_type_id = milestone_type_id

    @property
    def milestone_type_code(self):
        """Gets the milestone_type_code of this MilestoneTypeRestObject.  # noqa: E501


        :return: The milestone_type_code of this MilestoneTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._milestone_type_code

    @milestone_type_code.setter
    def milestone_type_code(self, milestone_type_code):
        """Sets the milestone_type_code of this MilestoneTypeRestObject.


        :param milestone_type_code: The milestone_type_code of this MilestoneTypeRestObject.  # noqa: E501
        :type: str
        """

        self._milestone_type_code = milestone_type_code

    @property
    def milestone_type_text(self):
        """Gets the milestone_type_text of this MilestoneTypeRestObject.  # noqa: E501


        :return: The milestone_type_text of this MilestoneTypeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._milestone_type_text

    @milestone_type_text.setter
    def milestone_type_text(self, milestone_type_text):
        """Sets the milestone_type_text of this MilestoneTypeRestObject.


        :param milestone_type_text: The milestone_type_text of this MilestoneTypeRestObject.  # noqa: E501
        :type: str
        """

        self._milestone_type_text = milestone_type_text

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
        if issubclass(MilestoneTypeRestObject, dict):
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
        if not isinstance(other, MilestoneTypeRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
