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

class StatSearchGroupByRestObject(object):
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
        'code': 'str',
        'description': 'str',
        'filter_level': 'str',
        'hitting': 'bool',
        'pitching': 'bool',
        'fielding': 'bool',
        'catching': 'bool',
        'running': 'bool'
    }

    attribute_map = {
        'copyright': 'copyright',
        'code': 'code',
        'description': 'description',
        'filter_level': 'filterLevel',
        'hitting': 'hitting',
        'pitching': 'pitching',
        'fielding': 'fielding',
        'catching': 'catching',
        'running': 'running'
    }

    def __init__(self, copyright=None, code=None, description=None, filter_level=None, hitting=None, pitching=None, fielding=None, catching=None, running=None):  # noqa: E501
        """StatSearchGroupByRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._code = None
        self._description = None
        self._filter_level = None
        self._hitting = None
        self._pitching = None
        self._fielding = None
        self._catching = None
        self._running = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if filter_level is not None:
            self.filter_level = filter_level
        if hitting is not None:
            self.hitting = hitting
        if pitching is not None:
            self.pitching = pitching
        if fielding is not None:
            self.fielding = fielding
        if catching is not None:
            self.catching = catching
        if running is not None:
            self.running = running

    @property
    def copyright(self):
        """Gets the copyright of this StatSearchGroupByRestObject.  # noqa: E501


        :return: The copyright of this StatSearchGroupByRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this StatSearchGroupByRestObject.


        :param copyright: The copyright of this StatSearchGroupByRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def code(self):
        """Gets the code of this StatSearchGroupByRestObject.  # noqa: E501


        :return: The code of this StatSearchGroupByRestObject.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StatSearchGroupByRestObject.


        :param code: The code of this StatSearchGroupByRestObject.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this StatSearchGroupByRestObject.  # noqa: E501


        :return: The description of this StatSearchGroupByRestObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StatSearchGroupByRestObject.


        :param description: The description of this StatSearchGroupByRestObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def filter_level(self):
        """Gets the filter_level of this StatSearchGroupByRestObject.  # noqa: E501


        :return: The filter_level of this StatSearchGroupByRestObject.  # noqa: E501
        :rtype: str
        """
        return self._filter_level

    @filter_level.setter
    def filter_level(self, filter_level):
        """Sets the filter_level of this StatSearchGroupByRestObject.


        :param filter_level: The filter_level of this StatSearchGroupByRestObject.  # noqa: E501
        :type: str
        """

        self._filter_level = filter_level

    @property
    def hitting(self):
        """Gets the hitting of this StatSearchGroupByRestObject.  # noqa: E501


        :return: The hitting of this StatSearchGroupByRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._hitting

    @hitting.setter
    def hitting(self, hitting):
        """Sets the hitting of this StatSearchGroupByRestObject.


        :param hitting: The hitting of this StatSearchGroupByRestObject.  # noqa: E501
        :type: bool
        """

        self._hitting = hitting

    @property
    def pitching(self):
        """Gets the pitching of this StatSearchGroupByRestObject.  # noqa: E501


        :return: The pitching of this StatSearchGroupByRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._pitching

    @pitching.setter
    def pitching(self, pitching):
        """Sets the pitching of this StatSearchGroupByRestObject.


        :param pitching: The pitching of this StatSearchGroupByRestObject.  # noqa: E501
        :type: bool
        """

        self._pitching = pitching

    @property
    def fielding(self):
        """Gets the fielding of this StatSearchGroupByRestObject.  # noqa: E501


        :return: The fielding of this StatSearchGroupByRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._fielding

    @fielding.setter
    def fielding(self, fielding):
        """Sets the fielding of this StatSearchGroupByRestObject.


        :param fielding: The fielding of this StatSearchGroupByRestObject.  # noqa: E501
        :type: bool
        """

        self._fielding = fielding

    @property
    def catching(self):
        """Gets the catching of this StatSearchGroupByRestObject.  # noqa: E501


        :return: The catching of this StatSearchGroupByRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._catching

    @catching.setter
    def catching(self, catching):
        """Sets the catching of this StatSearchGroupByRestObject.


        :param catching: The catching of this StatSearchGroupByRestObject.  # noqa: E501
        :type: bool
        """

        self._catching = catching

    @property
    def running(self):
        """Gets the running of this StatSearchGroupByRestObject.  # noqa: E501


        :return: The running of this StatSearchGroupByRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this StatSearchGroupByRestObject.


        :param running: The running of this StatSearchGroupByRestObject.  # noqa: E501
        :type: bool
        """

        self._running = running

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
        if issubclass(StatSearchGroupByRestObject, dict):
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
        if not isinstance(other, StatSearchGroupByRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
