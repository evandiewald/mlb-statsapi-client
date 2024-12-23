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

class BatSweetSpotRestObject(object):
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
        'axial_offset': 'float',
        'distance_from_head': 'float',
        'speed_before_impact': 'float',
        'radial_offset': 'float',
        'velocity': 'BatImpactVelocityRestObject'
    }

    attribute_map = {
        'copyright': 'copyright',
        'axial_offset': 'axialOffset',
        'distance_from_head': 'distanceFromHead',
        'speed_before_impact': 'speedBeforeImpact',
        'radial_offset': 'radialOffset',
        'velocity': 'velocity'
    }

    def __init__(self, copyright=None, axial_offset=None, distance_from_head=None, speed_before_impact=None, radial_offset=None, velocity=None):  # noqa: E501
        """BatSweetSpotRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._axial_offset = None
        self._distance_from_head = None
        self._speed_before_impact = None
        self._radial_offset = None
        self._velocity = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if axial_offset is not None:
            self.axial_offset = axial_offset
        if distance_from_head is not None:
            self.distance_from_head = distance_from_head
        if speed_before_impact is not None:
            self.speed_before_impact = speed_before_impact
        if radial_offset is not None:
            self.radial_offset = radial_offset
        if velocity is not None:
            self.velocity = velocity

    @property
    def copyright(self):
        """Gets the copyright of this BatSweetSpotRestObject.  # noqa: E501


        :return: The copyright of this BatSweetSpotRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this BatSweetSpotRestObject.


        :param copyright: The copyright of this BatSweetSpotRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def axial_offset(self):
        """Gets the axial_offset of this BatSweetSpotRestObject.  # noqa: E501

        Distance from the sweetSpot to the impact point along the bat. Negative is towards the handle of the bat, positive towards the head.  # noqa: E501

        :return: The axial_offset of this BatSweetSpotRestObject.  # noqa: E501
        :rtype: float
        """
        return self._axial_offset

    @axial_offset.setter
    def axial_offset(self, axial_offset):
        """Sets the axial_offset of this BatSweetSpotRestObject.

        Distance from the sweetSpot to the impact point along the bat. Negative is towards the handle of the bat, positive towards the head.  # noqa: E501

        :param axial_offset: The axial_offset of this BatSweetSpotRestObject.  # noqa: E501
        :type: float
        """

        self._axial_offset = axial_offset

    @property
    def distance_from_head(self):
        """Gets the distance_from_head of this BatSweetSpotRestObject.  # noqa: E501

        Distance along the bat from the sweetSpot towards the head. Will be constant for all swings.  # noqa: E501

        :return: The distance_from_head of this BatSweetSpotRestObject.  # noqa: E501
        :rtype: float
        """
        return self._distance_from_head

    @distance_from_head.setter
    def distance_from_head(self, distance_from_head):
        """Sets the distance_from_head of this BatSweetSpotRestObject.

        Distance along the bat from the sweetSpot towards the head. Will be constant for all swings.  # noqa: E501

        :param distance_from_head: The distance_from_head of this BatSweetSpotRestObject.  # noqa: E501
        :type: float
        """

        self._distance_from_head = distance_from_head

    @property
    def speed_before_impact(self):
        """Gets the speed_before_impact of this BatSweetSpotRestObject.  # noqa: E501

        The speed of the sweetSpot right before contact.  # noqa: E501

        :return: The speed_before_impact of this BatSweetSpotRestObject.  # noqa: E501
        :rtype: float
        """
        return self._speed_before_impact

    @speed_before_impact.setter
    def speed_before_impact(self, speed_before_impact):
        """Sets the speed_before_impact of this BatSweetSpotRestObject.

        The speed of the sweetSpot right before contact.  # noqa: E501

        :param speed_before_impact: The speed_before_impact of this BatSweetSpotRestObject.  # noqa: E501
        :type: float
        """

        self._speed_before_impact = speed_before_impact

    @property
    def radial_offset(self):
        """Gets the radial_offset of this BatSweetSpotRestObject.  # noqa: E501

        Distance from the sweetSpot to the impact point perpendicular to the bat. Negative is below the center of the bat, positive is above.  # noqa: E501

        :return: The radial_offset of this BatSweetSpotRestObject.  # noqa: E501
        :rtype: float
        """
        return self._radial_offset

    @radial_offset.setter
    def radial_offset(self, radial_offset):
        """Sets the radial_offset of this BatSweetSpotRestObject.

        Distance from the sweetSpot to the impact point perpendicular to the bat. Negative is below the center of the bat, positive is above.  # noqa: E501

        :param radial_offset: The radial_offset of this BatSweetSpotRestObject.  # noqa: E501
        :type: float
        """

        self._radial_offset = radial_offset

    @property
    def velocity(self):
        """Gets the velocity of this BatSweetSpotRestObject.  # noqa: E501


        :return: The velocity of this BatSweetSpotRestObject.  # noqa: E501
        :rtype: BatImpactVelocityRestObject
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """Sets the velocity of this BatSweetSpotRestObject.


        :param velocity: The velocity of this BatSweetSpotRestObject.  # noqa: E501
        :type: BatImpactVelocityRestObject
        """

        self._velocity = velocity

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
        if issubclass(BatSweetSpotRestObject, dict):
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
        if not isinstance(other, BatSweetSpotRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
