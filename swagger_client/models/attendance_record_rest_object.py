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

class AttendanceRecordRestObject(object):
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
        'openings_total7day': 'int',
        'openings_total': 'int',
        'openings_total_away': 'int',
        'openings_total_home': 'int',
        'openings_total_lost': 'int',
        'openings_total_ytd': 'int',
        'games_total': 'int',
        'games_away_total': 'int',
        'games_home_total': 'int',
        'year': 'str',
        'attendance_average_away': 'int',
        'attendance_average_home': 'int',
        'attendance_average_ytd': 'int',
        'attendance_high': 'int',
        'attendance_high_date': 'str',
        'attendance_high_game': 'BaseballScheduleItemRestObject',
        'attendance_low': 'int',
        'attendance_low_date': 'str',
        'attendance_low_game': 'BaseballScheduleItemRestObject',
        'attendance_opening7day_avg': 'int',
        'attendance_opening_average': 'int',
        'attendance_total7day': 'int',
        'attendance_total': 'int',
        'attendance_total_away': 'int',
        'attendance_total_home': 'int',
        'attendance_total_yesterday': 'int',
        'attendance_total_ytd': 'int',
        'game_type': 'GameTypeEnum',
        'team': 'BaseballTeamRestObject'
    }

    attribute_map = {
        'copyright': 'copyright',
        'openings_total7day': 'openingsTotal7day',
        'openings_total': 'openingsTotal',
        'openings_total_away': 'openingsTotalAway',
        'openings_total_home': 'openingsTotalHome',
        'openings_total_lost': 'openingsTotalLost',
        'openings_total_ytd': 'openingsTotalYtd',
        'games_total': 'gamesTotal',
        'games_away_total': 'gamesAwayTotal',
        'games_home_total': 'gamesHomeTotal',
        'year': 'year',
        'attendance_average_away': 'attendanceAverageAway',
        'attendance_average_home': 'attendanceAverageHome',
        'attendance_average_ytd': 'attendanceAverageYtd',
        'attendance_high': 'attendanceHigh',
        'attendance_high_date': 'attendanceHighDate',
        'attendance_high_game': 'attendanceHighGame',
        'attendance_low': 'attendanceLow',
        'attendance_low_date': 'attendanceLowDate',
        'attendance_low_game': 'attendanceLowGame',
        'attendance_opening7day_avg': 'attendanceOpening7dayAvg',
        'attendance_opening_average': 'attendanceOpeningAverage',
        'attendance_total7day': 'attendanceTotal7day',
        'attendance_total': 'attendanceTotal',
        'attendance_total_away': 'attendanceTotalAway',
        'attendance_total_home': 'attendanceTotalHome',
        'attendance_total_yesterday': 'attendanceTotalYesterday',
        'attendance_total_ytd': 'attendanceTotalYtd',
        'game_type': 'gameType',
        'team': 'team'
    }

    def __init__(self, copyright=None, openings_total7day=None, openings_total=None, openings_total_away=None, openings_total_home=None, openings_total_lost=None, openings_total_ytd=None, games_total=None, games_away_total=None, games_home_total=None, year=None, attendance_average_away=None, attendance_average_home=None, attendance_average_ytd=None, attendance_high=None, attendance_high_date=None, attendance_high_game=None, attendance_low=None, attendance_low_date=None, attendance_low_game=None, attendance_opening7day_avg=None, attendance_opening_average=None, attendance_total7day=None, attendance_total=None, attendance_total_away=None, attendance_total_home=None, attendance_total_yesterday=None, attendance_total_ytd=None, game_type=None, team=None):  # noqa: E501
        """AttendanceRecordRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._openings_total7day = None
        self._openings_total = None
        self._openings_total_away = None
        self._openings_total_home = None
        self._openings_total_lost = None
        self._openings_total_ytd = None
        self._games_total = None
        self._games_away_total = None
        self._games_home_total = None
        self._year = None
        self._attendance_average_away = None
        self._attendance_average_home = None
        self._attendance_average_ytd = None
        self._attendance_high = None
        self._attendance_high_date = None
        self._attendance_high_game = None
        self._attendance_low = None
        self._attendance_low_date = None
        self._attendance_low_game = None
        self._attendance_opening7day_avg = None
        self._attendance_opening_average = None
        self._attendance_total7day = None
        self._attendance_total = None
        self._attendance_total_away = None
        self._attendance_total_home = None
        self._attendance_total_yesterday = None
        self._attendance_total_ytd = None
        self._game_type = None
        self._team = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if openings_total7day is not None:
            self.openings_total7day = openings_total7day
        if openings_total is not None:
            self.openings_total = openings_total
        if openings_total_away is not None:
            self.openings_total_away = openings_total_away
        if openings_total_home is not None:
            self.openings_total_home = openings_total_home
        if openings_total_lost is not None:
            self.openings_total_lost = openings_total_lost
        if openings_total_ytd is not None:
            self.openings_total_ytd = openings_total_ytd
        if games_total is not None:
            self.games_total = games_total
        if games_away_total is not None:
            self.games_away_total = games_away_total
        if games_home_total is not None:
            self.games_home_total = games_home_total
        if year is not None:
            self.year = year
        if attendance_average_away is not None:
            self.attendance_average_away = attendance_average_away
        if attendance_average_home is not None:
            self.attendance_average_home = attendance_average_home
        if attendance_average_ytd is not None:
            self.attendance_average_ytd = attendance_average_ytd
        if attendance_high is not None:
            self.attendance_high = attendance_high
        if attendance_high_date is not None:
            self.attendance_high_date = attendance_high_date
        if attendance_high_game is not None:
            self.attendance_high_game = attendance_high_game
        if attendance_low is not None:
            self.attendance_low = attendance_low
        if attendance_low_date is not None:
            self.attendance_low_date = attendance_low_date
        if attendance_low_game is not None:
            self.attendance_low_game = attendance_low_game
        if attendance_opening7day_avg is not None:
            self.attendance_opening7day_avg = attendance_opening7day_avg
        if attendance_opening_average is not None:
            self.attendance_opening_average = attendance_opening_average
        if attendance_total7day is not None:
            self.attendance_total7day = attendance_total7day
        if attendance_total is not None:
            self.attendance_total = attendance_total
        if attendance_total_away is not None:
            self.attendance_total_away = attendance_total_away
        if attendance_total_home is not None:
            self.attendance_total_home = attendance_total_home
        if attendance_total_yesterday is not None:
            self.attendance_total_yesterday = attendance_total_yesterday
        if attendance_total_ytd is not None:
            self.attendance_total_ytd = attendance_total_ytd
        if game_type is not None:
            self.game_type = game_type
        if team is not None:
            self.team = team

    @property
    def copyright(self):
        """Gets the copyright of this AttendanceRecordRestObject.  # noqa: E501


        :return: The copyright of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this AttendanceRecordRestObject.


        :param copyright: The copyright of this AttendanceRecordRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def openings_total7day(self):
        """Gets the openings_total7day of this AttendanceRecordRestObject.  # noqa: E501


        :return: The openings_total7day of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._openings_total7day

    @openings_total7day.setter
    def openings_total7day(self, openings_total7day):
        """Sets the openings_total7day of this AttendanceRecordRestObject.


        :param openings_total7day: The openings_total7day of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._openings_total7day = openings_total7day

    @property
    def openings_total(self):
        """Gets the openings_total of this AttendanceRecordRestObject.  # noqa: E501


        :return: The openings_total of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._openings_total

    @openings_total.setter
    def openings_total(self, openings_total):
        """Sets the openings_total of this AttendanceRecordRestObject.


        :param openings_total: The openings_total of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._openings_total = openings_total

    @property
    def openings_total_away(self):
        """Gets the openings_total_away of this AttendanceRecordRestObject.  # noqa: E501


        :return: The openings_total_away of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._openings_total_away

    @openings_total_away.setter
    def openings_total_away(self, openings_total_away):
        """Sets the openings_total_away of this AttendanceRecordRestObject.


        :param openings_total_away: The openings_total_away of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._openings_total_away = openings_total_away

    @property
    def openings_total_home(self):
        """Gets the openings_total_home of this AttendanceRecordRestObject.  # noqa: E501


        :return: The openings_total_home of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._openings_total_home

    @openings_total_home.setter
    def openings_total_home(self, openings_total_home):
        """Sets the openings_total_home of this AttendanceRecordRestObject.


        :param openings_total_home: The openings_total_home of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._openings_total_home = openings_total_home

    @property
    def openings_total_lost(self):
        """Gets the openings_total_lost of this AttendanceRecordRestObject.  # noqa: E501


        :return: The openings_total_lost of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._openings_total_lost

    @openings_total_lost.setter
    def openings_total_lost(self, openings_total_lost):
        """Sets the openings_total_lost of this AttendanceRecordRestObject.


        :param openings_total_lost: The openings_total_lost of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._openings_total_lost = openings_total_lost

    @property
    def openings_total_ytd(self):
        """Gets the openings_total_ytd of this AttendanceRecordRestObject.  # noqa: E501


        :return: The openings_total_ytd of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._openings_total_ytd

    @openings_total_ytd.setter
    def openings_total_ytd(self, openings_total_ytd):
        """Sets the openings_total_ytd of this AttendanceRecordRestObject.


        :param openings_total_ytd: The openings_total_ytd of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._openings_total_ytd = openings_total_ytd

    @property
    def games_total(self):
        """Gets the games_total of this AttendanceRecordRestObject.  # noqa: E501


        :return: The games_total of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._games_total

    @games_total.setter
    def games_total(self, games_total):
        """Sets the games_total of this AttendanceRecordRestObject.


        :param games_total: The games_total of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._games_total = games_total

    @property
    def games_away_total(self):
        """Gets the games_away_total of this AttendanceRecordRestObject.  # noqa: E501


        :return: The games_away_total of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._games_away_total

    @games_away_total.setter
    def games_away_total(self, games_away_total):
        """Sets the games_away_total of this AttendanceRecordRestObject.


        :param games_away_total: The games_away_total of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._games_away_total = games_away_total

    @property
    def games_home_total(self):
        """Gets the games_home_total of this AttendanceRecordRestObject.  # noqa: E501


        :return: The games_home_total of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._games_home_total

    @games_home_total.setter
    def games_home_total(self, games_home_total):
        """Sets the games_home_total of this AttendanceRecordRestObject.


        :param games_home_total: The games_home_total of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._games_home_total = games_home_total

    @property
    def year(self):
        """Gets the year of this AttendanceRecordRestObject.  # noqa: E501


        :return: The year of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this AttendanceRecordRestObject.


        :param year: The year of this AttendanceRecordRestObject.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def attendance_average_away(self):
        """Gets the attendance_average_away of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_average_away of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_average_away

    @attendance_average_away.setter
    def attendance_average_away(self, attendance_average_away):
        """Sets the attendance_average_away of this AttendanceRecordRestObject.


        :param attendance_average_away: The attendance_average_away of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_average_away = attendance_average_away

    @property
    def attendance_average_home(self):
        """Gets the attendance_average_home of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_average_home of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_average_home

    @attendance_average_home.setter
    def attendance_average_home(self, attendance_average_home):
        """Sets the attendance_average_home of this AttendanceRecordRestObject.


        :param attendance_average_home: The attendance_average_home of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_average_home = attendance_average_home

    @property
    def attendance_average_ytd(self):
        """Gets the attendance_average_ytd of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_average_ytd of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_average_ytd

    @attendance_average_ytd.setter
    def attendance_average_ytd(self, attendance_average_ytd):
        """Sets the attendance_average_ytd of this AttendanceRecordRestObject.


        :param attendance_average_ytd: The attendance_average_ytd of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_average_ytd = attendance_average_ytd

    @property
    def attendance_high(self):
        """Gets the attendance_high of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_high of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_high

    @attendance_high.setter
    def attendance_high(self, attendance_high):
        """Sets the attendance_high of this AttendanceRecordRestObject.


        :param attendance_high: The attendance_high of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_high = attendance_high

    @property
    def attendance_high_date(self):
        """Gets the attendance_high_date of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_high_date of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: str
        """
        return self._attendance_high_date

    @attendance_high_date.setter
    def attendance_high_date(self, attendance_high_date):
        """Sets the attendance_high_date of this AttendanceRecordRestObject.


        :param attendance_high_date: The attendance_high_date of this AttendanceRecordRestObject.  # noqa: E501
        :type: str
        """

        self._attendance_high_date = attendance_high_date

    @property
    def attendance_high_game(self):
        """Gets the attendance_high_game of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_high_game of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: BaseballScheduleItemRestObject
        """
        return self._attendance_high_game

    @attendance_high_game.setter
    def attendance_high_game(self, attendance_high_game):
        """Sets the attendance_high_game of this AttendanceRecordRestObject.


        :param attendance_high_game: The attendance_high_game of this AttendanceRecordRestObject.  # noqa: E501
        :type: BaseballScheduleItemRestObject
        """

        self._attendance_high_game = attendance_high_game

    @property
    def attendance_low(self):
        """Gets the attendance_low of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_low of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_low

    @attendance_low.setter
    def attendance_low(self, attendance_low):
        """Sets the attendance_low of this AttendanceRecordRestObject.


        :param attendance_low: The attendance_low of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_low = attendance_low

    @property
    def attendance_low_date(self):
        """Gets the attendance_low_date of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_low_date of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: str
        """
        return self._attendance_low_date

    @attendance_low_date.setter
    def attendance_low_date(self, attendance_low_date):
        """Sets the attendance_low_date of this AttendanceRecordRestObject.


        :param attendance_low_date: The attendance_low_date of this AttendanceRecordRestObject.  # noqa: E501
        :type: str
        """

        self._attendance_low_date = attendance_low_date

    @property
    def attendance_low_game(self):
        """Gets the attendance_low_game of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_low_game of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: BaseballScheduleItemRestObject
        """
        return self._attendance_low_game

    @attendance_low_game.setter
    def attendance_low_game(self, attendance_low_game):
        """Sets the attendance_low_game of this AttendanceRecordRestObject.


        :param attendance_low_game: The attendance_low_game of this AttendanceRecordRestObject.  # noqa: E501
        :type: BaseballScheduleItemRestObject
        """

        self._attendance_low_game = attendance_low_game

    @property
    def attendance_opening7day_avg(self):
        """Gets the attendance_opening7day_avg of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_opening7day_avg of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_opening7day_avg

    @attendance_opening7day_avg.setter
    def attendance_opening7day_avg(self, attendance_opening7day_avg):
        """Sets the attendance_opening7day_avg of this AttendanceRecordRestObject.


        :param attendance_opening7day_avg: The attendance_opening7day_avg of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_opening7day_avg = attendance_opening7day_avg

    @property
    def attendance_opening_average(self):
        """Gets the attendance_opening_average of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_opening_average of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_opening_average

    @attendance_opening_average.setter
    def attendance_opening_average(self, attendance_opening_average):
        """Sets the attendance_opening_average of this AttendanceRecordRestObject.


        :param attendance_opening_average: The attendance_opening_average of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_opening_average = attendance_opening_average

    @property
    def attendance_total7day(self):
        """Gets the attendance_total7day of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_total7day of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_total7day

    @attendance_total7day.setter
    def attendance_total7day(self, attendance_total7day):
        """Sets the attendance_total7day of this AttendanceRecordRestObject.


        :param attendance_total7day: The attendance_total7day of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_total7day = attendance_total7day

    @property
    def attendance_total(self):
        """Gets the attendance_total of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_total of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_total

    @attendance_total.setter
    def attendance_total(self, attendance_total):
        """Sets the attendance_total of this AttendanceRecordRestObject.


        :param attendance_total: The attendance_total of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_total = attendance_total

    @property
    def attendance_total_away(self):
        """Gets the attendance_total_away of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_total_away of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_total_away

    @attendance_total_away.setter
    def attendance_total_away(self, attendance_total_away):
        """Sets the attendance_total_away of this AttendanceRecordRestObject.


        :param attendance_total_away: The attendance_total_away of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_total_away = attendance_total_away

    @property
    def attendance_total_home(self):
        """Gets the attendance_total_home of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_total_home of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_total_home

    @attendance_total_home.setter
    def attendance_total_home(self, attendance_total_home):
        """Sets the attendance_total_home of this AttendanceRecordRestObject.


        :param attendance_total_home: The attendance_total_home of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_total_home = attendance_total_home

    @property
    def attendance_total_yesterday(self):
        """Gets the attendance_total_yesterday of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_total_yesterday of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_total_yesterday

    @attendance_total_yesterday.setter
    def attendance_total_yesterday(self, attendance_total_yesterday):
        """Sets the attendance_total_yesterday of this AttendanceRecordRestObject.


        :param attendance_total_yesterday: The attendance_total_yesterday of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_total_yesterday = attendance_total_yesterday

    @property
    def attendance_total_ytd(self):
        """Gets the attendance_total_ytd of this AttendanceRecordRestObject.  # noqa: E501


        :return: The attendance_total_ytd of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: int
        """
        return self._attendance_total_ytd

    @attendance_total_ytd.setter
    def attendance_total_ytd(self, attendance_total_ytd):
        """Sets the attendance_total_ytd of this AttendanceRecordRestObject.


        :param attendance_total_ytd: The attendance_total_ytd of this AttendanceRecordRestObject.  # noqa: E501
        :type: int
        """

        self._attendance_total_ytd = attendance_total_ytd

    @property
    def game_type(self):
        """Gets the game_type of this AttendanceRecordRestObject.  # noqa: E501


        :return: The game_type of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: GameTypeEnum
        """
        return self._game_type

    @game_type.setter
    def game_type(self, game_type):
        """Sets the game_type of this AttendanceRecordRestObject.


        :param game_type: The game_type of this AttendanceRecordRestObject.  # noqa: E501
        :type: GameTypeEnum
        """

        self._game_type = game_type

    @property
    def team(self):
        """Gets the team of this AttendanceRecordRestObject.  # noqa: E501


        :return: The team of this AttendanceRecordRestObject.  # noqa: E501
        :rtype: BaseballTeamRestObject
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this AttendanceRecordRestObject.


        :param team: The team of this AttendanceRecordRestObject.  # noqa: E501
        :type: BaseballTeamRestObject
        """

        self._team = team

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
        if issubclass(AttendanceRecordRestObject, dict):
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
        if not isinstance(other, AttendanceRecordRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
