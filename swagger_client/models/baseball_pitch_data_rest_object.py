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

class BaseballPitchDataRestObject(object):
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
        'start_speed': 'float',
        'end_speed': 'float',
        'nasty_factor': 'float',
        'strike_zone_top': 'float',
        'strike_zone_bottom': 'float',
        'strike_zone_width': 'float',
        'strike_zone_depth': 'float',
        'coordinates': 'Coordinates',
        'breaks': 'Breaks',
        'zone': 'int',
        'type_confidence': 'float',
        'plate_time': 'float',
        'extension': 'float'
    }

    attribute_map = {
        'copyright': 'copyright',
        'start_speed': 'startSpeed',
        'end_speed': 'endSpeed',
        'nasty_factor': 'nastyFactor',
        'strike_zone_top': 'strikeZoneTop',
        'strike_zone_bottom': 'strikeZoneBottom',
        'strike_zone_width': 'strikeZoneWidth',
        'strike_zone_depth': 'strikeZoneDepth',
        'coordinates': 'coordinates',
        'breaks': 'breaks',
        'zone': 'zone',
        'type_confidence': 'typeConfidence',
        'plate_time': 'plateTime',
        'extension': 'extension'
    }

    def __init__(self, copyright=None, start_speed=None, end_speed=None, nasty_factor=None, strike_zone_top=None, strike_zone_bottom=None, strike_zone_width=None, strike_zone_depth=None, coordinates=None, breaks=None, zone=None, type_confidence=None, plate_time=None, extension=None):  # noqa: E501
        """BaseballPitchDataRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._start_speed = None
        self._end_speed = None
        self._nasty_factor = None
        self._strike_zone_top = None
        self._strike_zone_bottom = None
        self._strike_zone_width = None
        self._strike_zone_depth = None
        self._coordinates = None
        self._breaks = None
        self._zone = None
        self._type_confidence = None
        self._plate_time = None
        self._extension = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if start_speed is not None:
            self.start_speed = start_speed
        if end_speed is not None:
            self.end_speed = end_speed
        if nasty_factor is not None:
            self.nasty_factor = nasty_factor
        if strike_zone_top is not None:
            self.strike_zone_top = strike_zone_top
        if strike_zone_bottom is not None:
            self.strike_zone_bottom = strike_zone_bottom
        if strike_zone_width is not None:
            self.strike_zone_width = strike_zone_width
        if strike_zone_depth is not None:
            self.strike_zone_depth = strike_zone_depth
        if coordinates is not None:
            self.coordinates = coordinates
        if breaks is not None:
            self.breaks = breaks
        if zone is not None:
            self.zone = zone
        if type_confidence is not None:
            self.type_confidence = type_confidence
        if plate_time is not None:
            self.plate_time = plate_time
        if extension is not None:
            self.extension = extension

    @property
    def copyright(self):
        """Gets the copyright of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The copyright of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this BaseballPitchDataRestObject.


        :param copyright: The copyright of this BaseballPitchDataRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def start_speed(self):
        """Gets the start_speed of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The start_speed of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._start_speed

    @start_speed.setter
    def start_speed(self, start_speed):
        """Sets the start_speed of this BaseballPitchDataRestObject.


        :param start_speed: The start_speed of this BaseballPitchDataRestObject.  # noqa: E501
        :type: float
        """

        self._start_speed = start_speed

    @property
    def end_speed(self):
        """Gets the end_speed of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The end_speed of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._end_speed

    @end_speed.setter
    def end_speed(self, end_speed):
        """Sets the end_speed of this BaseballPitchDataRestObject.


        :param end_speed: The end_speed of this BaseballPitchDataRestObject.  # noqa: E501
        :type: float
        """

        self._end_speed = end_speed

    @property
    def nasty_factor(self):
        """Gets the nasty_factor of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The nasty_factor of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._nasty_factor

    @nasty_factor.setter
    def nasty_factor(self, nasty_factor):
        """Sets the nasty_factor of this BaseballPitchDataRestObject.


        :param nasty_factor: The nasty_factor of this BaseballPitchDataRestObject.  # noqa: E501
        :type: float
        """

        self._nasty_factor = nasty_factor

    @property
    def strike_zone_top(self):
        """Gets the strike_zone_top of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The strike_zone_top of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._strike_zone_top

    @strike_zone_top.setter
    def strike_zone_top(self, strike_zone_top):
        """Sets the strike_zone_top of this BaseballPitchDataRestObject.


        :param strike_zone_top: The strike_zone_top of this BaseballPitchDataRestObject.  # noqa: E501
        :type: float
        """

        self._strike_zone_top = strike_zone_top

    @property
    def strike_zone_bottom(self):
        """Gets the strike_zone_bottom of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The strike_zone_bottom of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._strike_zone_bottom

    @strike_zone_bottom.setter
    def strike_zone_bottom(self, strike_zone_bottom):
        """Sets the strike_zone_bottom of this BaseballPitchDataRestObject.


        :param strike_zone_bottom: The strike_zone_bottom of this BaseballPitchDataRestObject.  # noqa: E501
        :type: float
        """

        self._strike_zone_bottom = strike_zone_bottom

    @property
    def strike_zone_width(self):
        """Gets the strike_zone_width of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The strike_zone_width of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._strike_zone_width

    @strike_zone_width.setter
    def strike_zone_width(self, strike_zone_width):
        """Sets the strike_zone_width of this BaseballPitchDataRestObject.


        :param strike_zone_width: The strike_zone_width of this BaseballPitchDataRestObject.  # noqa: E501
        :type: float
        """

        self._strike_zone_width = strike_zone_width

    @property
    def strike_zone_depth(self):
        """Gets the strike_zone_depth of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The strike_zone_depth of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._strike_zone_depth

    @strike_zone_depth.setter
    def strike_zone_depth(self, strike_zone_depth):
        """Sets the strike_zone_depth of this BaseballPitchDataRestObject.


        :param strike_zone_depth: The strike_zone_depth of this BaseballPitchDataRestObject.  # noqa: E501
        :type: float
        """

        self._strike_zone_depth = strike_zone_depth

    @property
    def coordinates(self):
        """Gets the coordinates of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The coordinates of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this BaseballPitchDataRestObject.


        :param coordinates: The coordinates of this BaseballPitchDataRestObject.  # noqa: E501
        :type: Coordinates
        """

        self._coordinates = coordinates

    @property
    def breaks(self):
        """Gets the breaks of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The breaks of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: Breaks
        """
        return self._breaks

    @breaks.setter
    def breaks(self, breaks):
        """Sets the breaks of this BaseballPitchDataRestObject.


        :param breaks: The breaks of this BaseballPitchDataRestObject.  # noqa: E501
        :type: Breaks
        """

        self._breaks = breaks

    @property
    def zone(self):
        """Gets the zone of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The zone of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: int
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this BaseballPitchDataRestObject.


        :param zone: The zone of this BaseballPitchDataRestObject.  # noqa: E501
        :type: int
        """

        self._zone = zone

    @property
    def type_confidence(self):
        """Gets the type_confidence of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The type_confidence of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._type_confidence

    @type_confidence.setter
    def type_confidence(self, type_confidence):
        """Sets the type_confidence of this BaseballPitchDataRestObject.


        :param type_confidence: The type_confidence of this BaseballPitchDataRestObject.  # noqa: E501
        :type: float
        """

        self._type_confidence = type_confidence

    @property
    def plate_time(self):
        """Gets the plate_time of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The plate_time of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._plate_time

    @plate_time.setter
    def plate_time(self, plate_time):
        """Sets the plate_time of this BaseballPitchDataRestObject.


        :param plate_time: The plate_time of this BaseballPitchDataRestObject.  # noqa: E501
        :type: float
        """

        self._plate_time = plate_time

    @property
    def extension(self):
        """Gets the extension of this BaseballPitchDataRestObject.  # noqa: E501


        :return: The extension of this BaseballPitchDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this BaseballPitchDataRestObject.


        :param extension: The extension of this BaseballPitchDataRestObject.  # noqa: E501
        :type: float
        """

        self._extension = extension

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
        if issubclass(BaseballPitchDataRestObject, dict):
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
        if not isinstance(other, BaseballPitchDataRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
