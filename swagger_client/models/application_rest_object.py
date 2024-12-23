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

class ApplicationRestObject(object):
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
        'android_package': 'str',
        'icon': 'str',
        'intent': 'str',
        'name': 'str',
        'android_url': 'str',
        'ios_url': 'str',
        'ios_package': 'str',
        'primary': 'bool'
    }

    attribute_map = {
        'copyright': 'copyright',
        'android_package': 'androidPackage',
        'icon': 'icon',
        'intent': 'intent',
        'name': 'name',
        'android_url': 'androidUrl',
        'ios_url': 'iosUrl',
        'ios_package': 'iosPackage',
        'primary': 'primary'
    }

    def __init__(self, copyright=None, android_package=None, icon=None, intent=None, name=None, android_url=None, ios_url=None, ios_package=None, primary=None):  # noqa: E501
        """ApplicationRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._android_package = None
        self._icon = None
        self._intent = None
        self._name = None
        self._android_url = None
        self._ios_url = None
        self._ios_package = None
        self._primary = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if android_package is not None:
            self.android_package = android_package
        if icon is not None:
            self.icon = icon
        if intent is not None:
            self.intent = intent
        if name is not None:
            self.name = name
        if android_url is not None:
            self.android_url = android_url
        if ios_url is not None:
            self.ios_url = ios_url
        if ios_package is not None:
            self.ios_package = ios_package
        if primary is not None:
            self.primary = primary

    @property
    def copyright(self):
        """Gets the copyright of this ApplicationRestObject.  # noqa: E501


        :return: The copyright of this ApplicationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this ApplicationRestObject.


        :param copyright: The copyright of this ApplicationRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def android_package(self):
        """Gets the android_package of this ApplicationRestObject.  # noqa: E501


        :return: The android_package of this ApplicationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._android_package

    @android_package.setter
    def android_package(self, android_package):
        """Sets the android_package of this ApplicationRestObject.


        :param android_package: The android_package of this ApplicationRestObject.  # noqa: E501
        :type: str
        """

        self._android_package = android_package

    @property
    def icon(self):
        """Gets the icon of this ApplicationRestObject.  # noqa: E501


        :return: The icon of this ApplicationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ApplicationRestObject.


        :param icon: The icon of this ApplicationRestObject.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def intent(self):
        """Gets the intent of this ApplicationRestObject.  # noqa: E501


        :return: The intent of this ApplicationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        """Sets the intent of this ApplicationRestObject.


        :param intent: The intent of this ApplicationRestObject.  # noqa: E501
        :type: str
        """

        self._intent = intent

    @property
    def name(self):
        """Gets the name of this ApplicationRestObject.  # noqa: E501


        :return: The name of this ApplicationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationRestObject.


        :param name: The name of this ApplicationRestObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def android_url(self):
        """Gets the android_url of this ApplicationRestObject.  # noqa: E501


        :return: The android_url of this ApplicationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._android_url

    @android_url.setter
    def android_url(self, android_url):
        """Sets the android_url of this ApplicationRestObject.


        :param android_url: The android_url of this ApplicationRestObject.  # noqa: E501
        :type: str
        """

        self._android_url = android_url

    @property
    def ios_url(self):
        """Gets the ios_url of this ApplicationRestObject.  # noqa: E501


        :return: The ios_url of this ApplicationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._ios_url

    @ios_url.setter
    def ios_url(self, ios_url):
        """Sets the ios_url of this ApplicationRestObject.


        :param ios_url: The ios_url of this ApplicationRestObject.  # noqa: E501
        :type: str
        """

        self._ios_url = ios_url

    @property
    def ios_package(self):
        """Gets the ios_package of this ApplicationRestObject.  # noqa: E501


        :return: The ios_package of this ApplicationRestObject.  # noqa: E501
        :rtype: str
        """
        return self._ios_package

    @ios_package.setter
    def ios_package(self, ios_package):
        """Sets the ios_package of this ApplicationRestObject.


        :param ios_package: The ios_package of this ApplicationRestObject.  # noqa: E501
        :type: str
        """

        self._ios_package = ios_package

    @property
    def primary(self):
        """Gets the primary of this ApplicationRestObject.  # noqa: E501


        :return: The primary of this ApplicationRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this ApplicationRestObject.


        :param primary: The primary of this ApplicationRestObject.  # noqa: E501
        :type: bool
        """

        self._primary = primary

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
        if issubclass(ApplicationRestObject, dict):
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
        if not isinstance(other, ApplicationRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
