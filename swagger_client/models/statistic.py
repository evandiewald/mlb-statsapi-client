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

class Statistic(object):
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
        'statistic_id': 'int',
        'statistic_text': 'str',
        'statistic_desc': 'str',
        'category': 'str',
        'is_statcast_status': 'bool',
        'is_standard_status': 'bool',
        'sort_order': 'int'
    }

    attribute_map = {
        'statistic_id': 'statisticId',
        'statistic_text': 'statisticText',
        'statistic_desc': 'statisticDesc',
        'category': 'category',
        'is_statcast_status': 'isStatcastStatus',
        'is_standard_status': 'isStandardStatus',
        'sort_order': 'sortOrder'
    }

    def __init__(self, statistic_id=None, statistic_text=None, statistic_desc=None, category=None, is_statcast_status=None, is_standard_status=None, sort_order=None):  # noqa: E501
        """Statistic - a model defined in Swagger"""  # noqa: E501
        self._statistic_id = None
        self._statistic_text = None
        self._statistic_desc = None
        self._category = None
        self._is_statcast_status = None
        self._is_standard_status = None
        self._sort_order = None
        self.discriminator = None
        if statistic_id is not None:
            self.statistic_id = statistic_id
        if statistic_text is not None:
            self.statistic_text = statistic_text
        if statistic_desc is not None:
            self.statistic_desc = statistic_desc
        if category is not None:
            self.category = category
        if is_statcast_status is not None:
            self.is_statcast_status = is_statcast_status
        if is_standard_status is not None:
            self.is_standard_status = is_standard_status
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def statistic_id(self):
        """Gets the statistic_id of this Statistic.  # noqa: E501


        :return: The statistic_id of this Statistic.  # noqa: E501
        :rtype: int
        """
        return self._statistic_id

    @statistic_id.setter
    def statistic_id(self, statistic_id):
        """Sets the statistic_id of this Statistic.


        :param statistic_id: The statistic_id of this Statistic.  # noqa: E501
        :type: int
        """

        self._statistic_id = statistic_id

    @property
    def statistic_text(self):
        """Gets the statistic_text of this Statistic.  # noqa: E501


        :return: The statistic_text of this Statistic.  # noqa: E501
        :rtype: str
        """
        return self._statistic_text

    @statistic_text.setter
    def statistic_text(self, statistic_text):
        """Sets the statistic_text of this Statistic.


        :param statistic_text: The statistic_text of this Statistic.  # noqa: E501
        :type: str
        """

        self._statistic_text = statistic_text

    @property
    def statistic_desc(self):
        """Gets the statistic_desc of this Statistic.  # noqa: E501


        :return: The statistic_desc of this Statistic.  # noqa: E501
        :rtype: str
        """
        return self._statistic_desc

    @statistic_desc.setter
    def statistic_desc(self, statistic_desc):
        """Sets the statistic_desc of this Statistic.


        :param statistic_desc: The statistic_desc of this Statistic.  # noqa: E501
        :type: str
        """

        self._statistic_desc = statistic_desc

    @property
    def category(self):
        """Gets the category of this Statistic.  # noqa: E501


        :return: The category of this Statistic.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Statistic.


        :param category: The category of this Statistic.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def is_statcast_status(self):
        """Gets the is_statcast_status of this Statistic.  # noqa: E501


        :return: The is_statcast_status of this Statistic.  # noqa: E501
        :rtype: bool
        """
        return self._is_statcast_status

    @is_statcast_status.setter
    def is_statcast_status(self, is_statcast_status):
        """Sets the is_statcast_status of this Statistic.


        :param is_statcast_status: The is_statcast_status of this Statistic.  # noqa: E501
        :type: bool
        """

        self._is_statcast_status = is_statcast_status

    @property
    def is_standard_status(self):
        """Gets the is_standard_status of this Statistic.  # noqa: E501


        :return: The is_standard_status of this Statistic.  # noqa: E501
        :rtype: bool
        """
        return self._is_standard_status

    @is_standard_status.setter
    def is_standard_status(self, is_standard_status):
        """Sets the is_standard_status of this Statistic.


        :param is_standard_status: The is_standard_status of this Statistic.  # noqa: E501
        :type: bool
        """

        self._is_standard_status = is_standard_status

    @property
    def sort_order(self):
        """Gets the sort_order of this Statistic.  # noqa: E501


        :return: The sort_order of this Statistic.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this Statistic.


        :param sort_order: The sort_order of this Statistic.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

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
        if issubclass(Statistic, dict):
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
        if not isinstance(other, Statistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other