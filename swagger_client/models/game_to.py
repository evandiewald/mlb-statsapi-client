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

class GameTO(object):
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
        'game_status_detail': 'str',
        'away_holds': 'list[int]',
        'home_holds': 'list[int]',
        'away_blown_saves': 'list[int]',
        'home_blown_saves': 'list[int]',
        'game_minutes': 'int',
        'first_pitch_time_utc': 'datetime',
        'first_pitch_time': 'str',
        'total_minutes': 'int',
        'delay_minutes': 'int',
        'game_pk': 'int',
        'attendance': 'int',
        'wind_direction': 'str',
        'wind_speed': 'str',
        'sky': 'str',
        'temperature': 'str',
        'game_status_ind': 'str',
        'delay_reason': 'str',
        'official_scorer': 'int',
        'primary_datacaster': 'int',
        'secondary_datacaster': 'int'
    }

    attribute_map = {
        'game_status_detail': 'gameStatusDetail',
        'away_holds': 'awayHolds',
        'home_holds': 'homeHolds',
        'away_blown_saves': 'awayBlownSaves',
        'home_blown_saves': 'homeBlownSaves',
        'game_minutes': 'gameMinutes',
        'first_pitch_time_utc': 'firstPitchTimeUTC',
        'first_pitch_time': 'firstPitchTime',
        'total_minutes': 'totalMinutes',
        'delay_minutes': 'delayMinutes',
        'game_pk': 'game_pk',
        'attendance': 'attendance',
        'wind_direction': 'wind_direction',
        'wind_speed': 'wind_speed',
        'sky': 'sky',
        'temperature': 'temperature',
        'game_status_ind': 'game_status_ind',
        'delay_reason': 'delay_reason',
        'official_scorer': 'official_scorer',
        'primary_datacaster': 'primary_datacaster',
        'secondary_datacaster': 'secondary_datacaster'
    }

    def __init__(self, game_status_detail=None, away_holds=None, home_holds=None, away_blown_saves=None, home_blown_saves=None, game_minutes=None, first_pitch_time_utc=None, first_pitch_time=None, total_minutes=None, delay_minutes=None, game_pk=None, attendance=None, wind_direction=None, wind_speed=None, sky=None, temperature=None, game_status_ind=None, delay_reason=None, official_scorer=None, primary_datacaster=None, secondary_datacaster=None):  # noqa: E501
        """GameTO - a model defined in Swagger"""  # noqa: E501
        self._game_status_detail = None
        self._away_holds = None
        self._home_holds = None
        self._away_blown_saves = None
        self._home_blown_saves = None
        self._game_minutes = None
        self._first_pitch_time_utc = None
        self._first_pitch_time = None
        self._total_minutes = None
        self._delay_minutes = None
        self._game_pk = None
        self._attendance = None
        self._wind_direction = None
        self._wind_speed = None
        self._sky = None
        self._temperature = None
        self._game_status_ind = None
        self._delay_reason = None
        self._official_scorer = None
        self._primary_datacaster = None
        self._secondary_datacaster = None
        self.discriminator = None
        if game_status_detail is not None:
            self.game_status_detail = game_status_detail
        if away_holds is not None:
            self.away_holds = away_holds
        if home_holds is not None:
            self.home_holds = home_holds
        if away_blown_saves is not None:
            self.away_blown_saves = away_blown_saves
        if home_blown_saves is not None:
            self.home_blown_saves = home_blown_saves
        if game_minutes is not None:
            self.game_minutes = game_minutes
        if first_pitch_time_utc is not None:
            self.first_pitch_time_utc = first_pitch_time_utc
        if first_pitch_time is not None:
            self.first_pitch_time = first_pitch_time
        if total_minutes is not None:
            self.total_minutes = total_minutes
        if delay_minutes is not None:
            self.delay_minutes = delay_minutes
        if game_pk is not None:
            self.game_pk = game_pk
        if attendance is not None:
            self.attendance = attendance
        if wind_direction is not None:
            self.wind_direction = wind_direction
        if wind_speed is not None:
            self.wind_speed = wind_speed
        if sky is not None:
            self.sky = sky
        if temperature is not None:
            self.temperature = temperature
        if game_status_ind is not None:
            self.game_status_ind = game_status_ind
        if delay_reason is not None:
            self.delay_reason = delay_reason
        if official_scorer is not None:
            self.official_scorer = official_scorer
        if primary_datacaster is not None:
            self.primary_datacaster = primary_datacaster
        if secondary_datacaster is not None:
            self.secondary_datacaster = secondary_datacaster

    @property
    def game_status_detail(self):
        """Gets the game_status_detail of this GameTO.  # noqa: E501


        :return: The game_status_detail of this GameTO.  # noqa: E501
        :rtype: str
        """
        return self._game_status_detail

    @game_status_detail.setter
    def game_status_detail(self, game_status_detail):
        """Sets the game_status_detail of this GameTO.


        :param game_status_detail: The game_status_detail of this GameTO.  # noqa: E501
        :type: str
        """

        self._game_status_detail = game_status_detail

    @property
    def away_holds(self):
        """Gets the away_holds of this GameTO.  # noqa: E501


        :return: The away_holds of this GameTO.  # noqa: E501
        :rtype: list[int]
        """
        return self._away_holds

    @away_holds.setter
    def away_holds(self, away_holds):
        """Sets the away_holds of this GameTO.


        :param away_holds: The away_holds of this GameTO.  # noqa: E501
        :type: list[int]
        """

        self._away_holds = away_holds

    @property
    def home_holds(self):
        """Gets the home_holds of this GameTO.  # noqa: E501


        :return: The home_holds of this GameTO.  # noqa: E501
        :rtype: list[int]
        """
        return self._home_holds

    @home_holds.setter
    def home_holds(self, home_holds):
        """Sets the home_holds of this GameTO.


        :param home_holds: The home_holds of this GameTO.  # noqa: E501
        :type: list[int]
        """

        self._home_holds = home_holds

    @property
    def away_blown_saves(self):
        """Gets the away_blown_saves of this GameTO.  # noqa: E501


        :return: The away_blown_saves of this GameTO.  # noqa: E501
        :rtype: list[int]
        """
        return self._away_blown_saves

    @away_blown_saves.setter
    def away_blown_saves(self, away_blown_saves):
        """Sets the away_blown_saves of this GameTO.


        :param away_blown_saves: The away_blown_saves of this GameTO.  # noqa: E501
        :type: list[int]
        """

        self._away_blown_saves = away_blown_saves

    @property
    def home_blown_saves(self):
        """Gets the home_blown_saves of this GameTO.  # noqa: E501


        :return: The home_blown_saves of this GameTO.  # noqa: E501
        :rtype: list[int]
        """
        return self._home_blown_saves

    @home_blown_saves.setter
    def home_blown_saves(self, home_blown_saves):
        """Sets the home_blown_saves of this GameTO.


        :param home_blown_saves: The home_blown_saves of this GameTO.  # noqa: E501
        :type: list[int]
        """

        self._home_blown_saves = home_blown_saves

    @property
    def game_minutes(self):
        """Gets the game_minutes of this GameTO.  # noqa: E501


        :return: The game_minutes of this GameTO.  # noqa: E501
        :rtype: int
        """
        return self._game_minutes

    @game_minutes.setter
    def game_minutes(self, game_minutes):
        """Sets the game_minutes of this GameTO.


        :param game_minutes: The game_minutes of this GameTO.  # noqa: E501
        :type: int
        """

        self._game_minutes = game_minutes

    @property
    def first_pitch_time_utc(self):
        """Gets the first_pitch_time_utc of this GameTO.  # noqa: E501


        :return: The first_pitch_time_utc of this GameTO.  # noqa: E501
        :rtype: datetime
        """
        return self._first_pitch_time_utc

    @first_pitch_time_utc.setter
    def first_pitch_time_utc(self, first_pitch_time_utc):
        """Sets the first_pitch_time_utc of this GameTO.


        :param first_pitch_time_utc: The first_pitch_time_utc of this GameTO.  # noqa: E501
        :type: datetime
        """

        self._first_pitch_time_utc = first_pitch_time_utc

    @property
    def first_pitch_time(self):
        """Gets the first_pitch_time of this GameTO.  # noqa: E501


        :return: The first_pitch_time of this GameTO.  # noqa: E501
        :rtype: str
        """
        return self._first_pitch_time

    @first_pitch_time.setter
    def first_pitch_time(self, first_pitch_time):
        """Sets the first_pitch_time of this GameTO.


        :param first_pitch_time: The first_pitch_time of this GameTO.  # noqa: E501
        :type: str
        """

        self._first_pitch_time = first_pitch_time

    @property
    def total_minutes(self):
        """Gets the total_minutes of this GameTO.  # noqa: E501


        :return: The total_minutes of this GameTO.  # noqa: E501
        :rtype: int
        """
        return self._total_minutes

    @total_minutes.setter
    def total_minutes(self, total_minutes):
        """Sets the total_minutes of this GameTO.


        :param total_minutes: The total_minutes of this GameTO.  # noqa: E501
        :type: int
        """

        self._total_minutes = total_minutes

    @property
    def delay_minutes(self):
        """Gets the delay_minutes of this GameTO.  # noqa: E501


        :return: The delay_minutes of this GameTO.  # noqa: E501
        :rtype: int
        """
        return self._delay_minutes

    @delay_minutes.setter
    def delay_minutes(self, delay_minutes):
        """Sets the delay_minutes of this GameTO.


        :param delay_minutes: The delay_minutes of this GameTO.  # noqa: E501
        :type: int
        """

        self._delay_minutes = delay_minutes

    @property
    def game_pk(self):
        """Gets the game_pk of this GameTO.  # noqa: E501


        :return: The game_pk of this GameTO.  # noqa: E501
        :rtype: int
        """
        return self._game_pk

    @game_pk.setter
    def game_pk(self, game_pk):
        """Sets the game_pk of this GameTO.


        :param game_pk: The game_pk of this GameTO.  # noqa: E501
        :type: int
        """

        self._game_pk = game_pk

    @property
    def attendance(self):
        """Gets the attendance of this GameTO.  # noqa: E501


        :return: The attendance of this GameTO.  # noqa: E501
        :rtype: int
        """
        return self._attendance

    @attendance.setter
    def attendance(self, attendance):
        """Sets the attendance of this GameTO.


        :param attendance: The attendance of this GameTO.  # noqa: E501
        :type: int
        """

        self._attendance = attendance

    @property
    def wind_direction(self):
        """Gets the wind_direction of this GameTO.  # noqa: E501


        :return: The wind_direction of this GameTO.  # noqa: E501
        :rtype: str
        """
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, wind_direction):
        """Sets the wind_direction of this GameTO.


        :param wind_direction: The wind_direction of this GameTO.  # noqa: E501
        :type: str
        """

        self._wind_direction = wind_direction

    @property
    def wind_speed(self):
        """Gets the wind_speed of this GameTO.  # noqa: E501


        :return: The wind_speed of this GameTO.  # noqa: E501
        :rtype: str
        """
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, wind_speed):
        """Sets the wind_speed of this GameTO.


        :param wind_speed: The wind_speed of this GameTO.  # noqa: E501
        :type: str
        """

        self._wind_speed = wind_speed

    @property
    def sky(self):
        """Gets the sky of this GameTO.  # noqa: E501


        :return: The sky of this GameTO.  # noqa: E501
        :rtype: str
        """
        return self._sky

    @sky.setter
    def sky(self, sky):
        """Sets the sky of this GameTO.


        :param sky: The sky of this GameTO.  # noqa: E501
        :type: str
        """

        self._sky = sky

    @property
    def temperature(self):
        """Gets the temperature of this GameTO.  # noqa: E501


        :return: The temperature of this GameTO.  # noqa: E501
        :rtype: str
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this GameTO.


        :param temperature: The temperature of this GameTO.  # noqa: E501
        :type: str
        """

        self._temperature = temperature

    @property
    def game_status_ind(self):
        """Gets the game_status_ind of this GameTO.  # noqa: E501


        :return: The game_status_ind of this GameTO.  # noqa: E501
        :rtype: str
        """
        return self._game_status_ind

    @game_status_ind.setter
    def game_status_ind(self, game_status_ind):
        """Sets the game_status_ind of this GameTO.


        :param game_status_ind: The game_status_ind of this GameTO.  # noqa: E501
        :type: str
        """

        self._game_status_ind = game_status_ind

    @property
    def delay_reason(self):
        """Gets the delay_reason of this GameTO.  # noqa: E501


        :return: The delay_reason of this GameTO.  # noqa: E501
        :rtype: str
        """
        return self._delay_reason

    @delay_reason.setter
    def delay_reason(self, delay_reason):
        """Sets the delay_reason of this GameTO.


        :param delay_reason: The delay_reason of this GameTO.  # noqa: E501
        :type: str
        """

        self._delay_reason = delay_reason

    @property
    def official_scorer(self):
        """Gets the official_scorer of this GameTO.  # noqa: E501


        :return: The official_scorer of this GameTO.  # noqa: E501
        :rtype: int
        """
        return self._official_scorer

    @official_scorer.setter
    def official_scorer(self, official_scorer):
        """Sets the official_scorer of this GameTO.


        :param official_scorer: The official_scorer of this GameTO.  # noqa: E501
        :type: int
        """

        self._official_scorer = official_scorer

    @property
    def primary_datacaster(self):
        """Gets the primary_datacaster of this GameTO.  # noqa: E501


        :return: The primary_datacaster of this GameTO.  # noqa: E501
        :rtype: int
        """
        return self._primary_datacaster

    @primary_datacaster.setter
    def primary_datacaster(self, primary_datacaster):
        """Sets the primary_datacaster of this GameTO.


        :param primary_datacaster: The primary_datacaster of this GameTO.  # noqa: E501
        :type: int
        """

        self._primary_datacaster = primary_datacaster

    @property
    def secondary_datacaster(self):
        """Gets the secondary_datacaster of this GameTO.  # noqa: E501


        :return: The secondary_datacaster of this GameTO.  # noqa: E501
        :rtype: int
        """
        return self._secondary_datacaster

    @secondary_datacaster.setter
    def secondary_datacaster(self, secondary_datacaster):
        """Sets the secondary_datacaster of this GameTO.


        :param secondary_datacaster: The secondary_datacaster of this GameTO.  # noqa: E501
        :type: int
        """

        self._secondary_datacaster = secondary_datacaster

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
        if issubclass(GameTO, dict):
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
        if not isinstance(other, GameTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
