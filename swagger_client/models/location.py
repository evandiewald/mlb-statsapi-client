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

class Location(object):
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
        'address1': 'str',
        'address2': 'str',
        'address3': 'str',
        'address4': 'str',
        'attention': 'str',
        'phone': 'str',
        'city': 'str',
        'state': 'str',
        'country': 'str',
        'state_abbrev': 'str',
        'postal_code': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'azimuth_angle': 'float',
        'elevation': 'int'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'address4': 'address4',
        'attention': 'attention',
        'phone': 'phone',
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'state_abbrev': 'stateAbbrev',
        'postal_code': 'postalCode',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'azimuth_angle': 'azimuthAngle',
        'elevation': 'elevation'
    }

    def __init__(self, address1=None, address2=None, address3=None, address4=None, attention=None, phone=None, city=None, state=None, country=None, state_abbrev=None, postal_code=None, latitude=None, longitude=None, azimuth_angle=None, elevation=None):  # noqa: E501
        """Location - a model defined in Swagger"""  # noqa: E501
        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._address4 = None
        self._attention = None
        self._phone = None
        self._city = None
        self._state = None
        self._country = None
        self._state_abbrev = None
        self._postal_code = None
        self._latitude = None
        self._longitude = None
        self._azimuth_angle = None
        self._elevation = None
        self.discriminator = None
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if address3 is not None:
            self.address3 = address3
        if address4 is not None:
            self.address4 = address4
        if attention is not None:
            self.attention = attention
        if phone is not None:
            self.phone = phone
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country
        if state_abbrev is not None:
            self.state_abbrev = state_abbrev
        if postal_code is not None:
            self.postal_code = postal_code
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if azimuth_angle is not None:
            self.azimuth_angle = azimuth_angle
        if elevation is not None:
            self.elevation = elevation

    @property
    def address1(self):
        """Gets the address1 of this Location.  # noqa: E501


        :return: The address1 of this Location.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this Location.


        :param address1: The address1 of this Location.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this Location.  # noqa: E501


        :return: The address2 of this Location.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Location.


        :param address2: The address2 of this Location.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def address3(self):
        """Gets the address3 of this Location.  # noqa: E501


        :return: The address3 of this Location.  # noqa: E501
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """Sets the address3 of this Location.


        :param address3: The address3 of this Location.  # noqa: E501
        :type: str
        """

        self._address3 = address3

    @property
    def address4(self):
        """Gets the address4 of this Location.  # noqa: E501


        :return: The address4 of this Location.  # noqa: E501
        :rtype: str
        """
        return self._address4

    @address4.setter
    def address4(self, address4):
        """Sets the address4 of this Location.


        :param address4: The address4 of this Location.  # noqa: E501
        :type: str
        """

        self._address4 = address4

    @property
    def attention(self):
        """Gets the attention of this Location.  # noqa: E501


        :return: The attention of this Location.  # noqa: E501
        :rtype: str
        """
        return self._attention

    @attention.setter
    def attention(self, attention):
        """Sets the attention of this Location.


        :param attention: The attention of this Location.  # noqa: E501
        :type: str
        """

        self._attention = attention

    @property
    def phone(self):
        """Gets the phone of this Location.  # noqa: E501


        :return: The phone of this Location.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Location.


        :param phone: The phone of this Location.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def city(self):
        """Gets the city of this Location.  # noqa: E501


        :return: The city of this Location.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Location.


        :param city: The city of this Location.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Location.  # noqa: E501


        :return: The state of this Location.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Location.


        :param state: The state of this Location.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """Gets the country of this Location.  # noqa: E501


        :return: The country of this Location.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Location.


        :param country: The country of this Location.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def state_abbrev(self):
        """Gets the state_abbrev of this Location.  # noqa: E501


        :return: The state_abbrev of this Location.  # noqa: E501
        :rtype: str
        """
        return self._state_abbrev

    @state_abbrev.setter
    def state_abbrev(self, state_abbrev):
        """Sets the state_abbrev of this Location.


        :param state_abbrev: The state_abbrev of this Location.  # noqa: E501
        :type: str
        """

        self._state_abbrev = state_abbrev

    @property
    def postal_code(self):
        """Gets the postal_code of this Location.  # noqa: E501


        :return: The postal_code of this Location.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Location.


        :param postal_code: The postal_code of this Location.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def latitude(self):
        """Gets the latitude of this Location.  # noqa: E501


        :return: The latitude of this Location.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Location.


        :param latitude: The latitude of this Location.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Location.  # noqa: E501


        :return: The longitude of this Location.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Location.


        :param longitude: The longitude of this Location.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def azimuth_angle(self):
        """Gets the azimuth_angle of this Location.  # noqa: E501


        :return: The azimuth_angle of this Location.  # noqa: E501
        :rtype: float
        """
        return self._azimuth_angle

    @azimuth_angle.setter
    def azimuth_angle(self, azimuth_angle):
        """Sets the azimuth_angle of this Location.


        :param azimuth_angle: The azimuth_angle of this Location.  # noqa: E501
        :type: float
        """

        self._azimuth_angle = azimuth_angle

    @property
    def elevation(self):
        """Gets the elevation of this Location.  # noqa: E501


        :return: The elevation of this Location.  # noqa: E501
        :rtype: int
        """
        return self._elevation

    @elevation.setter
    def elevation(self, elevation):
        """Sets the elevation of this Location.


        :param elevation: The elevation of this Location.  # noqa: E501
        :type: int
        """

        self._elevation = elevation

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
        if issubclass(Location, dict):
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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
