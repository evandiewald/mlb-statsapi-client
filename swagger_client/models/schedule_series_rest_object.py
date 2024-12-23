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

class ScheduleSeriesRestObject(object):
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
        'series': 'PostseasonSeriesRestObject',
        'total_items': 'int',
        'total_games': 'int',
        'total_games_in_progress': 'int',
        'games': 'list[BaseballScheduleItemRestObject]',
        'sort_order': 'int'
    }

    attribute_map = {
        'copyright': 'copyright',
        'series': 'series',
        'total_items': 'totalItems',
        'total_games': 'totalGames',
        'total_games_in_progress': 'totalGamesInProgress',
        'games': 'games',
        'sort_order': 'sortOrder'
    }

    def __init__(self, copyright=None, series=None, total_items=None, total_games=None, total_games_in_progress=None, games=None, sort_order=None):  # noqa: E501
        """ScheduleSeriesRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._series = None
        self._total_items = None
        self._total_games = None
        self._total_games_in_progress = None
        self._games = None
        self._sort_order = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if series is not None:
            self.series = series
        if total_items is not None:
            self.total_items = total_items
        if total_games is not None:
            self.total_games = total_games
        if total_games_in_progress is not None:
            self.total_games_in_progress = total_games_in_progress
        if games is not None:
            self.games = games
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def copyright(self):
        """Gets the copyright of this ScheduleSeriesRestObject.  # noqa: E501


        :return: The copyright of this ScheduleSeriesRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this ScheduleSeriesRestObject.


        :param copyright: The copyright of this ScheduleSeriesRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def series(self):
        """Gets the series of this ScheduleSeriesRestObject.  # noqa: E501


        :return: The series of this ScheduleSeriesRestObject.  # noqa: E501
        :rtype: PostseasonSeriesRestObject
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this ScheduleSeriesRestObject.


        :param series: The series of this ScheduleSeriesRestObject.  # noqa: E501
        :type: PostseasonSeriesRestObject
        """

        self._series = series

    @property
    def total_items(self):
        """Gets the total_items of this ScheduleSeriesRestObject.  # noqa: E501


        :return: The total_items of this ScheduleSeriesRestObject.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this ScheduleSeriesRestObject.


        :param total_items: The total_items of this ScheduleSeriesRestObject.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def total_games(self):
        """Gets the total_games of this ScheduleSeriesRestObject.  # noqa: E501


        :return: The total_games of this ScheduleSeriesRestObject.  # noqa: E501
        :rtype: int
        """
        return self._total_games

    @total_games.setter
    def total_games(self, total_games):
        """Sets the total_games of this ScheduleSeriesRestObject.


        :param total_games: The total_games of this ScheduleSeriesRestObject.  # noqa: E501
        :type: int
        """

        self._total_games = total_games

    @property
    def total_games_in_progress(self):
        """Gets the total_games_in_progress of this ScheduleSeriesRestObject.  # noqa: E501


        :return: The total_games_in_progress of this ScheduleSeriesRestObject.  # noqa: E501
        :rtype: int
        """
        return self._total_games_in_progress

    @total_games_in_progress.setter
    def total_games_in_progress(self, total_games_in_progress):
        """Sets the total_games_in_progress of this ScheduleSeriesRestObject.


        :param total_games_in_progress: The total_games_in_progress of this ScheduleSeriesRestObject.  # noqa: E501
        :type: int
        """

        self._total_games_in_progress = total_games_in_progress

    @property
    def games(self):
        """Gets the games of this ScheduleSeriesRestObject.  # noqa: E501


        :return: The games of this ScheduleSeriesRestObject.  # noqa: E501
        :rtype: list[BaseballScheduleItemRestObject]
        """
        return self._games

    @games.setter
    def games(self, games):
        """Sets the games of this ScheduleSeriesRestObject.


        :param games: The games of this ScheduleSeriesRestObject.  # noqa: E501
        :type: list[BaseballScheduleItemRestObject]
        """

        self._games = games

    @property
    def sort_order(self):
        """Gets the sort_order of this ScheduleSeriesRestObject.  # noqa: E501


        :return: The sort_order of this ScheduleSeriesRestObject.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ScheduleSeriesRestObject.


        :param sort_order: The sort_order of this ScheduleSeriesRestObject.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

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
        if issubclass(ScheduleSeriesRestObject, dict):
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
        if not isinstance(other, ScheduleSeriesRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other