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

class HomeRunDerbyRoundBatterRestObject(object):
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
        'started': 'bool',
        'complete': 'bool',
        'winner': 'bool',
        'player': 'BaseballPersonRestObject',
        'top_derby_hit_data': 'BaseballHitDataRestObject',
        'hits': 'list[HomeRunDerbyBatterHitRestObject]',
        'seed': 'int',
        'order': 'int',
        'is_winner': 'bool',
        'is_complete': 'bool',
        'is_started': 'bool',
        'num_home_runs': 'int'
    }

    attribute_map = {
        'copyright': 'copyright',
        'started': 'started',
        'complete': 'complete',
        'winner': 'winner',
        'player': 'player',
        'top_derby_hit_data': 'topDerbyHitData',
        'hits': 'hits',
        'seed': 'seed',
        'order': 'order',
        'is_winner': 'isWinner',
        'is_complete': 'isComplete',
        'is_started': 'isStarted',
        'num_home_runs': 'numHomeRuns'
    }

    def __init__(self, copyright=None, started=None, complete=None, winner=None, player=None, top_derby_hit_data=None, hits=None, seed=None, order=None, is_winner=None, is_complete=None, is_started=None, num_home_runs=None):  # noqa: E501
        """HomeRunDerbyRoundBatterRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._started = None
        self._complete = None
        self._winner = None
        self._player = None
        self._top_derby_hit_data = None
        self._hits = None
        self._seed = None
        self._order = None
        self._is_winner = None
        self._is_complete = None
        self._is_started = None
        self._num_home_runs = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if started is not None:
            self.started = started
        if complete is not None:
            self.complete = complete
        if winner is not None:
            self.winner = winner
        if player is not None:
            self.player = player
        if top_derby_hit_data is not None:
            self.top_derby_hit_data = top_derby_hit_data
        if hits is not None:
            self.hits = hits
        if seed is not None:
            self.seed = seed
        if order is not None:
            self.order = order
        if is_winner is not None:
            self.is_winner = is_winner
        if is_complete is not None:
            self.is_complete = is_complete
        if is_started is not None:
            self.is_started = is_started
        if num_home_runs is not None:
            self.num_home_runs = num_home_runs

    @property
    def copyright(self):
        """Gets the copyright of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The copyright of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this HomeRunDerbyRoundBatterRestObject.


        :param copyright: The copyright of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def started(self):
        """Gets the started of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The started of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this HomeRunDerbyRoundBatterRestObject.


        :param started: The started of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: bool
        """

        self._started = started

    @property
    def complete(self):
        """Gets the complete of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The complete of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this HomeRunDerbyRoundBatterRestObject.


        :param complete: The complete of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: bool
        """

        self._complete = complete

    @property
    def winner(self):
        """Gets the winner of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The winner of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._winner

    @winner.setter
    def winner(self, winner):
        """Sets the winner of this HomeRunDerbyRoundBatterRestObject.


        :param winner: The winner of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: bool
        """

        self._winner = winner

    @property
    def player(self):
        """Gets the player of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The player of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: BaseballPersonRestObject
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this HomeRunDerbyRoundBatterRestObject.


        :param player: The player of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: BaseballPersonRestObject
        """

        self._player = player

    @property
    def top_derby_hit_data(self):
        """Gets the top_derby_hit_data of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The top_derby_hit_data of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: BaseballHitDataRestObject
        """
        return self._top_derby_hit_data

    @top_derby_hit_data.setter
    def top_derby_hit_data(self, top_derby_hit_data):
        """Sets the top_derby_hit_data of this HomeRunDerbyRoundBatterRestObject.


        :param top_derby_hit_data: The top_derby_hit_data of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: BaseballHitDataRestObject
        """

        self._top_derby_hit_data = top_derby_hit_data

    @property
    def hits(self):
        """Gets the hits of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The hits of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: list[HomeRunDerbyBatterHitRestObject]
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this HomeRunDerbyRoundBatterRestObject.


        :param hits: The hits of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: list[HomeRunDerbyBatterHitRestObject]
        """

        self._hits = hits

    @property
    def seed(self):
        """Gets the seed of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The seed of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: int
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """Sets the seed of this HomeRunDerbyRoundBatterRestObject.


        :param seed: The seed of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: int
        """

        self._seed = seed

    @property
    def order(self):
        """Gets the order of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The order of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this HomeRunDerbyRoundBatterRestObject.


        :param order: The order of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def is_winner(self):
        """Gets the is_winner of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The is_winner of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_winner

    @is_winner.setter
    def is_winner(self, is_winner):
        """Sets the is_winner of this HomeRunDerbyRoundBatterRestObject.


        :param is_winner: The is_winner of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: bool
        """

        self._is_winner = is_winner

    @property
    def is_complete(self):
        """Gets the is_complete of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The is_complete of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        """Sets the is_complete of this HomeRunDerbyRoundBatterRestObject.


        :param is_complete: The is_complete of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: bool
        """

        self._is_complete = is_complete

    @property
    def is_started(self):
        """Gets the is_started of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The is_started of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_started

    @is_started.setter
    def is_started(self, is_started):
        """Sets the is_started of this HomeRunDerbyRoundBatterRestObject.


        :param is_started: The is_started of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: bool
        """

        self._is_started = is_started

    @property
    def num_home_runs(self):
        """Gets the num_home_runs of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501


        :return: The num_home_runs of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :rtype: int
        """
        return self._num_home_runs

    @num_home_runs.setter
    def num_home_runs(self, num_home_runs):
        """Sets the num_home_runs of this HomeRunDerbyRoundBatterRestObject.


        :param num_home_runs: The num_home_runs of this HomeRunDerbyRoundBatterRestObject.  # noqa: E501
        :type: int
        """

        self._num_home_runs = num_home_runs

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
        if issubclass(HomeRunDerbyRoundBatterRestObject, dict):
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
        if not isinstance(other, HomeRunDerbyRoundBatterRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
