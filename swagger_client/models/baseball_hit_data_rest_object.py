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

class BaseballHitDataRestObject(object):
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
        'launch_speed': 'float',
        'launch_angle': 'float',
        'total_distance': 'float',
        'trajectory': 'str',
        'hardness': 'str',
        'location': 'str',
        'coordinates': 'Coordinates',
        'is_barrel': 'bool',
        'hit_probability': 'float',
        'bat_speed': 'float',
        'is_sword_swing': 'bool',
        'launch_data': 'LaunchDataRestObject',
        'trajectory_data': 'HitTrajectoryDataRestObject',
        'landing_data': 'StartEndDataRestObject',
        'last_measured_data': 'StartEndDataRestObject',
        'reduced_confidence': 'list[str]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'launch_speed': 'launchSpeed',
        'launch_angle': 'launchAngle',
        'total_distance': 'totalDistance',
        'trajectory': 'trajectory',
        'hardness': 'hardness',
        'location': 'location',
        'coordinates': 'coordinates',
        'is_barrel': 'isBarrel',
        'hit_probability': 'hitProbability',
        'bat_speed': 'batSpeed',
        'is_sword_swing': 'isSwordSwing',
        'launch_data': 'launchData',
        'trajectory_data': 'trajectoryData',
        'landing_data': 'landingData',
        'last_measured_data': 'lastMeasuredData',
        'reduced_confidence': 'reducedConfidence'
    }

    def __init__(self, copyright=None, launch_speed=None, launch_angle=None, total_distance=None, trajectory=None, hardness=None, location=None, coordinates=None, is_barrel=None, hit_probability=None, bat_speed=None, is_sword_swing=None, launch_data=None, trajectory_data=None, landing_data=None, last_measured_data=None, reduced_confidence=None):  # noqa: E501
        """BaseballHitDataRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._launch_speed = None
        self._launch_angle = None
        self._total_distance = None
        self._trajectory = None
        self._hardness = None
        self._location = None
        self._coordinates = None
        self._is_barrel = None
        self._hit_probability = None
        self._bat_speed = None
        self._is_sword_swing = None
        self._launch_data = None
        self._trajectory_data = None
        self._landing_data = None
        self._last_measured_data = None
        self._reduced_confidence = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if launch_speed is not None:
            self.launch_speed = launch_speed
        if launch_angle is not None:
            self.launch_angle = launch_angle
        if total_distance is not None:
            self.total_distance = total_distance
        if trajectory is not None:
            self.trajectory = trajectory
        if hardness is not None:
            self.hardness = hardness
        if location is not None:
            self.location = location
        if coordinates is not None:
            self.coordinates = coordinates
        if is_barrel is not None:
            self.is_barrel = is_barrel
        if hit_probability is not None:
            self.hit_probability = hit_probability
        if bat_speed is not None:
            self.bat_speed = bat_speed
        if is_sword_swing is not None:
            self.is_sword_swing = is_sword_swing
        if launch_data is not None:
            self.launch_data = launch_data
        if trajectory_data is not None:
            self.trajectory_data = trajectory_data
        if landing_data is not None:
            self.landing_data = landing_data
        if last_measured_data is not None:
            self.last_measured_data = last_measured_data
        if reduced_confidence is not None:
            self.reduced_confidence = reduced_confidence

    @property
    def copyright(self):
        """Gets the copyright of this BaseballHitDataRestObject.  # noqa: E501


        :return: The copyright of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this BaseballHitDataRestObject.


        :param copyright: The copyright of this BaseballHitDataRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def launch_speed(self):
        """Gets the launch_speed of this BaseballHitDataRestObject.  # noqa: E501


        :return: The launch_speed of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._launch_speed

    @launch_speed.setter
    def launch_speed(self, launch_speed):
        """Sets the launch_speed of this BaseballHitDataRestObject.


        :param launch_speed: The launch_speed of this BaseballHitDataRestObject.  # noqa: E501
        :type: float
        """

        self._launch_speed = launch_speed

    @property
    def launch_angle(self):
        """Gets the launch_angle of this BaseballHitDataRestObject.  # noqa: E501


        :return: The launch_angle of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._launch_angle

    @launch_angle.setter
    def launch_angle(self, launch_angle):
        """Sets the launch_angle of this BaseballHitDataRestObject.


        :param launch_angle: The launch_angle of this BaseballHitDataRestObject.  # noqa: E501
        :type: float
        """

        self._launch_angle = launch_angle

    @property
    def total_distance(self):
        """Gets the total_distance of this BaseballHitDataRestObject.  # noqa: E501


        :return: The total_distance of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._total_distance

    @total_distance.setter
    def total_distance(self, total_distance):
        """Sets the total_distance of this BaseballHitDataRestObject.


        :param total_distance: The total_distance of this BaseballHitDataRestObject.  # noqa: E501
        :type: float
        """

        self._total_distance = total_distance

    @property
    def trajectory(self):
        """Gets the trajectory of this BaseballHitDataRestObject.  # noqa: E501


        :return: The trajectory of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._trajectory

    @trajectory.setter
    def trajectory(self, trajectory):
        """Sets the trajectory of this BaseballHitDataRestObject.


        :param trajectory: The trajectory of this BaseballHitDataRestObject.  # noqa: E501
        :type: str
        """

        self._trajectory = trajectory

    @property
    def hardness(self):
        """Gets the hardness of this BaseballHitDataRestObject.  # noqa: E501


        :return: The hardness of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._hardness

    @hardness.setter
    def hardness(self, hardness):
        """Sets the hardness of this BaseballHitDataRestObject.


        :param hardness: The hardness of this BaseballHitDataRestObject.  # noqa: E501
        :type: str
        """

        self._hardness = hardness

    @property
    def location(self):
        """Gets the location of this BaseballHitDataRestObject.  # noqa: E501


        :return: The location of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this BaseballHitDataRestObject.


        :param location: The location of this BaseballHitDataRestObject.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def coordinates(self):
        """Gets the coordinates of this BaseballHitDataRestObject.  # noqa: E501


        :return: The coordinates of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this BaseballHitDataRestObject.


        :param coordinates: The coordinates of this BaseballHitDataRestObject.  # noqa: E501
        :type: Coordinates
        """

        self._coordinates = coordinates

    @property
    def is_barrel(self):
        """Gets the is_barrel of this BaseballHitDataRestObject.  # noqa: E501


        :return: The is_barrel of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_barrel

    @is_barrel.setter
    def is_barrel(self, is_barrel):
        """Sets the is_barrel of this BaseballHitDataRestObject.


        :param is_barrel: The is_barrel of this BaseballHitDataRestObject.  # noqa: E501
        :type: bool
        """

        self._is_barrel = is_barrel

    @property
    def hit_probability(self):
        """Gets the hit_probability of this BaseballHitDataRestObject.  # noqa: E501


        :return: The hit_probability of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._hit_probability

    @hit_probability.setter
    def hit_probability(self, hit_probability):
        """Sets the hit_probability of this BaseballHitDataRestObject.


        :param hit_probability: The hit_probability of this BaseballHitDataRestObject.  # noqa: E501
        :type: float
        """

        self._hit_probability = hit_probability

    @property
    def bat_speed(self):
        """Gets the bat_speed of this BaseballHitDataRestObject.  # noqa: E501


        :return: The bat_speed of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: float
        """
        return self._bat_speed

    @bat_speed.setter
    def bat_speed(self, bat_speed):
        """Sets the bat_speed of this BaseballHitDataRestObject.


        :param bat_speed: The bat_speed of this BaseballHitDataRestObject.  # noqa: E501
        :type: float
        """

        self._bat_speed = bat_speed

    @property
    def is_sword_swing(self):
        """Gets the is_sword_swing of this BaseballHitDataRestObject.  # noqa: E501


        :return: The is_sword_swing of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_sword_swing

    @is_sword_swing.setter
    def is_sword_swing(self, is_sword_swing):
        """Sets the is_sword_swing of this BaseballHitDataRestObject.


        :param is_sword_swing: The is_sword_swing of this BaseballHitDataRestObject.  # noqa: E501
        :type: bool
        """

        self._is_sword_swing = is_sword_swing

    @property
    def launch_data(self):
        """Gets the launch_data of this BaseballHitDataRestObject.  # noqa: E501


        :return: The launch_data of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: LaunchDataRestObject
        """
        return self._launch_data

    @launch_data.setter
    def launch_data(self, launch_data):
        """Sets the launch_data of this BaseballHitDataRestObject.


        :param launch_data: The launch_data of this BaseballHitDataRestObject.  # noqa: E501
        :type: LaunchDataRestObject
        """

        self._launch_data = launch_data

    @property
    def trajectory_data(self):
        """Gets the trajectory_data of this BaseballHitDataRestObject.  # noqa: E501


        :return: The trajectory_data of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: HitTrajectoryDataRestObject
        """
        return self._trajectory_data

    @trajectory_data.setter
    def trajectory_data(self, trajectory_data):
        """Sets the trajectory_data of this BaseballHitDataRestObject.


        :param trajectory_data: The trajectory_data of this BaseballHitDataRestObject.  # noqa: E501
        :type: HitTrajectoryDataRestObject
        """

        self._trajectory_data = trajectory_data

    @property
    def landing_data(self):
        """Gets the landing_data of this BaseballHitDataRestObject.  # noqa: E501


        :return: The landing_data of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: StartEndDataRestObject
        """
        return self._landing_data

    @landing_data.setter
    def landing_data(self, landing_data):
        """Sets the landing_data of this BaseballHitDataRestObject.


        :param landing_data: The landing_data of this BaseballHitDataRestObject.  # noqa: E501
        :type: StartEndDataRestObject
        """

        self._landing_data = landing_data

    @property
    def last_measured_data(self):
        """Gets the last_measured_data of this BaseballHitDataRestObject.  # noqa: E501


        :return: The last_measured_data of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: StartEndDataRestObject
        """
        return self._last_measured_data

    @last_measured_data.setter
    def last_measured_data(self, last_measured_data):
        """Sets the last_measured_data of this BaseballHitDataRestObject.


        :param last_measured_data: The last_measured_data of this BaseballHitDataRestObject.  # noqa: E501
        :type: StartEndDataRestObject
        """

        self._last_measured_data = last_measured_data

    @property
    def reduced_confidence(self):
        """Gets the reduced_confidence of this BaseballHitDataRestObject.  # noqa: E501


        :return: The reduced_confidence of this BaseballHitDataRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._reduced_confidence

    @reduced_confidence.setter
    def reduced_confidence(self, reduced_confidence):
        """Sets the reduced_confidence of this BaseballHitDataRestObject.


        :param reduced_confidence: The reduced_confidence of this BaseballHitDataRestObject.  # noqa: E501
        :type: list[str]
        """

        self._reduced_confidence = reduced_confidence

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
        if issubclass(BaseballHitDataRestObject, dict):
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
        if not isinstance(other, BaseballHitDataRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
