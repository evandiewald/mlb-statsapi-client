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

class CoordinateRestObject(object):
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
        'latitude': 'float',
        'longitude': 'float',
        'coordinates': 'list[str]',
        'type': 'str',
        'label': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'coordinates': 'coordinates',
        'type': 'type',
        'label': 'label'
    }

    def __init__(self, copyright=None, latitude=None, longitude=None, coordinates=None, type=None, label=None):  # noqa: E501
        """CoordinateRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._latitude = None
        self._longitude = None
        self._coordinates = None
        self._type = None
        self._label = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if coordinates is not None:
            self.coordinates = coordinates
        if type is not None:
            self.type = type
        if label is not None:
            self.label = label

    @property
    def copyright(self):
        """Gets the copyright of this CoordinateRestObject.  # noqa: E501


        :return: The copyright of this CoordinateRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this CoordinateRestObject.


        :param copyright: The copyright of this CoordinateRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def latitude(self):
        """Gets the latitude of this CoordinateRestObject.  # noqa: E501


        :return: The latitude of this CoordinateRestObject.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this CoordinateRestObject.


        :param latitude: The latitude of this CoordinateRestObject.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this CoordinateRestObject.  # noqa: E501


        :return: The longitude of this CoordinateRestObject.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this CoordinateRestObject.


        :param longitude: The longitude of this CoordinateRestObject.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def coordinates(self):
        """Gets the coordinates of this CoordinateRestObject.  # noqa: E501


        :return: The coordinates of this CoordinateRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this CoordinateRestObject.


        :param coordinates: The coordinates of this CoordinateRestObject.  # noqa: E501
        :type: list[str]
        """

        self._coordinates = coordinates

    @property
    def type(self):
        """Gets the type of this CoordinateRestObject.  # noqa: E501


        :return: The type of this CoordinateRestObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CoordinateRestObject.


        :param type: The type of this CoordinateRestObject.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def label(self):
        """Gets the label of this CoordinateRestObject.  # noqa: E501


        :return: The label of this CoordinateRestObject.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CoordinateRestObject.


        :param label: The label of this CoordinateRestObject.  # noqa: E501
        :type: str
        """

        self._label = label

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
        if issubclass(CoordinateRestObject, dict):
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
        if not isinstance(other, CoordinateRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other