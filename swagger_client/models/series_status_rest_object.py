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

class SeriesStatusRestObject(object):
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
        'game_number': 'int',
        'total_games': 'int',
        'is_tied': 'bool',
        'is_over': 'bool',
        'wins': 'int',
        'losses': 'int',
        'winning_team': 'BaseballTeamRestObject',
        'losing_team': 'BaseballTeamRestObject',
        'description': 'str',
        'short_description': 'str',
        'result': 'str',
        'short_name': 'str',
        'abbreviation': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'game_number': 'gameNumber',
        'total_games': 'totalGames',
        'is_tied': 'isTied',
        'is_over': 'isOver',
        'wins': 'wins',
        'losses': 'losses',
        'winning_team': 'winningTeam',
        'losing_team': 'losingTeam',
        'description': 'description',
        'short_description': 'shortDescription',
        'result': 'result',
        'short_name': 'shortName',
        'abbreviation': 'abbreviation'
    }

    def __init__(self, copyright=None, game_number=None, total_games=None, is_tied=None, is_over=None, wins=None, losses=None, winning_team=None, losing_team=None, description=None, short_description=None, result=None, short_name=None, abbreviation=None):  # noqa: E501
        """SeriesStatusRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._game_number = None
        self._total_games = None
        self._is_tied = None
        self._is_over = None
        self._wins = None
        self._losses = None
        self._winning_team = None
        self._losing_team = None
        self._description = None
        self._short_description = None
        self._result = None
        self._short_name = None
        self._abbreviation = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if game_number is not None:
            self.game_number = game_number
        if total_games is not None:
            self.total_games = total_games
        if is_tied is not None:
            self.is_tied = is_tied
        if is_over is not None:
            self.is_over = is_over
        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if winning_team is not None:
            self.winning_team = winning_team
        if losing_team is not None:
            self.losing_team = losing_team
        if description is not None:
            self.description = description
        if short_description is not None:
            self.short_description = short_description
        if result is not None:
            self.result = result
        if short_name is not None:
            self.short_name = short_name
        if abbreviation is not None:
            self.abbreviation = abbreviation

    @property
    def copyright(self):
        """Gets the copyright of this SeriesStatusRestObject.  # noqa: E501


        :return: The copyright of this SeriesStatusRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this SeriesStatusRestObject.


        :param copyright: The copyright of this SeriesStatusRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def game_number(self):
        """Gets the game_number of this SeriesStatusRestObject.  # noqa: E501


        :return: The game_number of this SeriesStatusRestObject.  # noqa: E501
        :rtype: int
        """
        return self._game_number

    @game_number.setter
    def game_number(self, game_number):
        """Sets the game_number of this SeriesStatusRestObject.


        :param game_number: The game_number of this SeriesStatusRestObject.  # noqa: E501
        :type: int
        """

        self._game_number = game_number

    @property
    def total_games(self):
        """Gets the total_games of this SeriesStatusRestObject.  # noqa: E501


        :return: The total_games of this SeriesStatusRestObject.  # noqa: E501
        :rtype: int
        """
        return self._total_games

    @total_games.setter
    def total_games(self, total_games):
        """Sets the total_games of this SeriesStatusRestObject.


        :param total_games: The total_games of this SeriesStatusRestObject.  # noqa: E501
        :type: int
        """

        self._total_games = total_games

    @property
    def is_tied(self):
        """Gets the is_tied of this SeriesStatusRestObject.  # noqa: E501


        :return: The is_tied of this SeriesStatusRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_tied

    @is_tied.setter
    def is_tied(self, is_tied):
        """Sets the is_tied of this SeriesStatusRestObject.


        :param is_tied: The is_tied of this SeriesStatusRestObject.  # noqa: E501
        :type: bool
        """

        self._is_tied = is_tied

    @property
    def is_over(self):
        """Gets the is_over of this SeriesStatusRestObject.  # noqa: E501


        :return: The is_over of this SeriesStatusRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_over

    @is_over.setter
    def is_over(self, is_over):
        """Sets the is_over of this SeriesStatusRestObject.


        :param is_over: The is_over of this SeriesStatusRestObject.  # noqa: E501
        :type: bool
        """

        self._is_over = is_over

    @property
    def wins(self):
        """Gets the wins of this SeriesStatusRestObject.  # noqa: E501


        :return: The wins of this SeriesStatusRestObject.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this SeriesStatusRestObject.


        :param wins: The wins of this SeriesStatusRestObject.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this SeriesStatusRestObject.  # noqa: E501


        :return: The losses of this SeriesStatusRestObject.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this SeriesStatusRestObject.


        :param losses: The losses of this SeriesStatusRestObject.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def winning_team(self):
        """Gets the winning_team of this SeriesStatusRestObject.  # noqa: E501


        :return: The winning_team of this SeriesStatusRestObject.  # noqa: E501
        :rtype: BaseballTeamRestObject
        """
        return self._winning_team

    @winning_team.setter
    def winning_team(self, winning_team):
        """Sets the winning_team of this SeriesStatusRestObject.


        :param winning_team: The winning_team of this SeriesStatusRestObject.  # noqa: E501
        :type: BaseballTeamRestObject
        """

        self._winning_team = winning_team

    @property
    def losing_team(self):
        """Gets the losing_team of this SeriesStatusRestObject.  # noqa: E501


        :return: The losing_team of this SeriesStatusRestObject.  # noqa: E501
        :rtype: BaseballTeamRestObject
        """
        return self._losing_team

    @losing_team.setter
    def losing_team(self, losing_team):
        """Sets the losing_team of this SeriesStatusRestObject.


        :param losing_team: The losing_team of this SeriesStatusRestObject.  # noqa: E501
        :type: BaseballTeamRestObject
        """

        self._losing_team = losing_team

    @property
    def description(self):
        """Gets the description of this SeriesStatusRestObject.  # noqa: E501


        :return: The description of this SeriesStatusRestObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SeriesStatusRestObject.


        :param description: The description of this SeriesStatusRestObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def short_description(self):
        """Gets the short_description of this SeriesStatusRestObject.  # noqa: E501


        :return: The short_description of this SeriesStatusRestObject.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this SeriesStatusRestObject.


        :param short_description: The short_description of this SeriesStatusRestObject.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def result(self):
        """Gets the result of this SeriesStatusRestObject.  # noqa: E501


        :return: The result of this SeriesStatusRestObject.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this SeriesStatusRestObject.


        :param result: The result of this SeriesStatusRestObject.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def short_name(self):
        """Gets the short_name of this SeriesStatusRestObject.  # noqa: E501


        :return: The short_name of this SeriesStatusRestObject.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this SeriesStatusRestObject.


        :param short_name: The short_name of this SeriesStatusRestObject.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this SeriesStatusRestObject.  # noqa: E501


        :return: The abbreviation of this SeriesStatusRestObject.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this SeriesStatusRestObject.


        :param abbreviation: The abbreviation of this SeriesStatusRestObject.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

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
        if issubclass(SeriesStatusRestObject, dict):
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
        if not isinstance(other, SeriesStatusRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
