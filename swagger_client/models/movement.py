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

class Movement(object):
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
        'origin_base': 'str',
        'start': 'str',
        'end': 'str',
        'out_base': 'str',
        'is_out': 'bool',
        'out_number': 'int'
    }

    attribute_map = {
        'origin_base': 'originBase',
        'start': 'start',
        'end': 'end',
        'out_base': 'outBase',
        'is_out': 'isOut',
        'out_number': 'outNumber'
    }

    def __init__(self, origin_base=None, start=None, end=None, out_base=None, is_out=None, out_number=None):  # noqa: E501
        """Movement - a model defined in Swagger"""  # noqa: E501
        self._origin_base = None
        self._start = None
        self._end = None
        self._out_base = None
        self._is_out = None
        self._out_number = None
        self.discriminator = None
        if origin_base is not None:
            self.origin_base = origin_base
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if out_base is not None:
            self.out_base = out_base
        if is_out is not None:
            self.is_out = is_out
        if out_number is not None:
            self.out_number = out_number

    @property
    def origin_base(self):
        """Gets the origin_base of this Movement.  # noqa: E501


        :return: The origin_base of this Movement.  # noqa: E501
        :rtype: str
        """
        return self._origin_base

    @origin_base.setter
    def origin_base(self, origin_base):
        """Sets the origin_base of this Movement.


        :param origin_base: The origin_base of this Movement.  # noqa: E501
        :type: str
        """

        self._origin_base = origin_base

    @property
    def start(self):
        """Gets the start of this Movement.  # noqa: E501


        :return: The start of this Movement.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Movement.


        :param start: The start of this Movement.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this Movement.  # noqa: E501


        :return: The end of this Movement.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this Movement.


        :param end: The end of this Movement.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def out_base(self):
        """Gets the out_base of this Movement.  # noqa: E501


        :return: The out_base of this Movement.  # noqa: E501
        :rtype: str
        """
        return self._out_base

    @out_base.setter
    def out_base(self, out_base):
        """Sets the out_base of this Movement.


        :param out_base: The out_base of this Movement.  # noqa: E501
        :type: str
        """

        self._out_base = out_base

    @property
    def is_out(self):
        """Gets the is_out of this Movement.  # noqa: E501


        :return: The is_out of this Movement.  # noqa: E501
        :rtype: bool
        """
        return self._is_out

    @is_out.setter
    def is_out(self, is_out):
        """Sets the is_out of this Movement.


        :param is_out: The is_out of this Movement.  # noqa: E501
        :type: bool
        """

        self._is_out = is_out

    @property
    def out_number(self):
        """Gets the out_number of this Movement.  # noqa: E501


        :return: The out_number of this Movement.  # noqa: E501
        :rtype: int
        """
        return self._out_number

    @out_number.setter
    def out_number(self, out_number):
        """Sets the out_number of this Movement.


        :param out_number: The out_number of this Movement.  # noqa: E501
        :type: int
        """

        self._out_number = out_number

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
        if issubclass(Movement, dict):
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
        if not isinstance(other, Movement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
