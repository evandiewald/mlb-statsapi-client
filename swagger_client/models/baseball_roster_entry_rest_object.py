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

class BaseballRosterEntryRestObject(object):
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
        'person': 'BaseballPersonRestObject',
        'jersey_number': 'str',
        'position': 'PositionRestObject',
        'alternate_captain': 'bool',
        'captain': 'bool',
        'note': 'str',
        'status': 'DynamicEnumRestObject',
        'job': 'str',
        'job_id': 'str',
        'title': 'str',
        'parent_team_id': 'int',
        'team': 'BaseballTeamRestObject',
        'is_active': 'bool',
        'start_date': 'date',
        'end_date': 'date',
        'status_date': 'date',
        'is_active_forty_man': 'bool',
        'batting_order': 'str',
        'stats': 'StatsRestObject',
        'season_stats': 'StatsRestObject',
        'game_status': 'GameStatusRestObject',
        'all_positions': 'list[PositionRestObject]'
    }

    attribute_map = {
        'person': 'person',
        'jersey_number': 'jerseyNumber',
        'position': 'position',
        'alternate_captain': 'alternateCaptain',
        'captain': 'captain',
        'note': 'note',
        'status': 'status',
        'job': 'job',
        'job_id': 'jobId',
        'title': 'title',
        'parent_team_id': 'parentTeamId',
        'team': 'team',
        'is_active': 'isActive',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'status_date': 'statusDate',
        'is_active_forty_man': 'isActiveFortyMan',
        'batting_order': 'battingOrder',
        'stats': 'stats',
        'season_stats': 'seasonStats',
        'game_status': 'gameStatus',
        'all_positions': 'allPositions'
    }

    def __init__(self, person=None, jersey_number=None, position=None, alternate_captain=None, captain=None, note=None, status=None, job=None, job_id=None, title=None, parent_team_id=None, team=None, is_active=None, start_date=None, end_date=None, status_date=None, is_active_forty_man=None, batting_order=None, stats=None, season_stats=None, game_status=None, all_positions=None):  # noqa: E501
        """BaseballRosterEntryRestObject - a model defined in Swagger"""  # noqa: E501
        self._person = None
        self._jersey_number = None
        self._position = None
        self._alternate_captain = None
        self._captain = None
        self._note = None
        self._status = None
        self._job = None
        self._job_id = None
        self._title = None
        self._parent_team_id = None
        self._team = None
        self._is_active = None
        self._start_date = None
        self._end_date = None
        self._status_date = None
        self._is_active_forty_man = None
        self._batting_order = None
        self._stats = None
        self._season_stats = None
        self._game_status = None
        self._all_positions = None
        self.discriminator = None
        if person is not None:
            self.person = person
        if jersey_number is not None:
            self.jersey_number = jersey_number
        if position is not None:
            self.position = position
        if alternate_captain is not None:
            self.alternate_captain = alternate_captain
        if captain is not None:
            self.captain = captain
        if note is not None:
            self.note = note
        if status is not None:
            self.status = status
        if job is not None:
            self.job = job
        if job_id is not None:
            self.job_id = job_id
        if title is not None:
            self.title = title
        if parent_team_id is not None:
            self.parent_team_id = parent_team_id
        if team is not None:
            self.team = team
        if is_active is not None:
            self.is_active = is_active
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if status_date is not None:
            self.status_date = status_date
        if is_active_forty_man is not None:
            self.is_active_forty_man = is_active_forty_man
        if batting_order is not None:
            self.batting_order = batting_order
        if stats is not None:
            self.stats = stats
        if season_stats is not None:
            self.season_stats = season_stats
        if game_status is not None:
            self.game_status = game_status
        if all_positions is not None:
            self.all_positions = all_positions

    @property
    def person(self):
        """Gets the person of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The person of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: BaseballPersonRestObject
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this BaseballRosterEntryRestObject.


        :param person: The person of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: BaseballPersonRestObject
        """

        self._person = person

    @property
    def jersey_number(self):
        """Gets the jersey_number of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The jersey_number of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: str
        """
        return self._jersey_number

    @jersey_number.setter
    def jersey_number(self, jersey_number):
        """Sets the jersey_number of this BaseballRosterEntryRestObject.


        :param jersey_number: The jersey_number of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: str
        """

        self._jersey_number = jersey_number

    @property
    def position(self):
        """Gets the position of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The position of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: PositionRestObject
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this BaseballRosterEntryRestObject.


        :param position: The position of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: PositionRestObject
        """

        self._position = position

    @property
    def alternate_captain(self):
        """Gets the alternate_captain of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The alternate_captain of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._alternate_captain

    @alternate_captain.setter
    def alternate_captain(self, alternate_captain):
        """Sets the alternate_captain of this BaseballRosterEntryRestObject.


        :param alternate_captain: The alternate_captain of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: bool
        """

        self._alternate_captain = alternate_captain

    @property
    def captain(self):
        """Gets the captain of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The captain of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._captain

    @captain.setter
    def captain(self, captain):
        """Sets the captain of this BaseballRosterEntryRestObject.


        :param captain: The captain of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: bool
        """

        self._captain = captain

    @property
    def note(self):
        """Gets the note of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The note of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this BaseballRosterEntryRestObject.


        :param note: The note of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def status(self):
        """Gets the status of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The status of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: DynamicEnumRestObject
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BaseballRosterEntryRestObject.


        :param status: The status of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: DynamicEnumRestObject
        """

        self._status = status

    @property
    def job(self):
        """Gets the job of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The job of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: str
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this BaseballRosterEntryRestObject.


        :param job: The job of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: str
        """

        self._job = job

    @property
    def job_id(self):
        """Gets the job_id of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The job_id of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BaseballRosterEntryRestObject.


        :param job_id: The job_id of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def title(self):
        """Gets the title of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The title of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BaseballRosterEntryRestObject.


        :param title: The title of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def parent_team_id(self):
        """Gets the parent_team_id of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The parent_team_id of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: int
        """
        return self._parent_team_id

    @parent_team_id.setter
    def parent_team_id(self, parent_team_id):
        """Sets the parent_team_id of this BaseballRosterEntryRestObject.


        :param parent_team_id: The parent_team_id of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: int
        """

        self._parent_team_id = parent_team_id

    @property
    def team(self):
        """Gets the team of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The team of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: BaseballTeamRestObject
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BaseballRosterEntryRestObject.


        :param team: The team of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: BaseballTeamRestObject
        """

        self._team = team

    @property
    def is_active(self):
        """Gets the is_active of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The is_active of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this BaseballRosterEntryRestObject.


        :param is_active: The is_active of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def start_date(self):
        """Gets the start_date of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The start_date of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this BaseballRosterEntryRestObject.


        :param start_date: The start_date of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The end_date of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this BaseballRosterEntryRestObject.


        :param end_date: The end_date of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def status_date(self):
        """Gets the status_date of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The status_date of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: date
        """
        return self._status_date

    @status_date.setter
    def status_date(self, status_date):
        """Sets the status_date of this BaseballRosterEntryRestObject.


        :param status_date: The status_date of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: date
        """

        self._status_date = status_date

    @property
    def is_active_forty_man(self):
        """Gets the is_active_forty_man of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The is_active_forty_man of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_active_forty_man

    @is_active_forty_man.setter
    def is_active_forty_man(self, is_active_forty_man):
        """Sets the is_active_forty_man of this BaseballRosterEntryRestObject.


        :param is_active_forty_man: The is_active_forty_man of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: bool
        """

        self._is_active_forty_man = is_active_forty_man

    @property
    def batting_order(self):
        """Gets the batting_order of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The batting_order of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: str
        """
        return self._batting_order

    @batting_order.setter
    def batting_order(self, batting_order):
        """Sets the batting_order of this BaseballRosterEntryRestObject.


        :param batting_order: The batting_order of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: str
        """

        self._batting_order = batting_order

    @property
    def stats(self):
        """Gets the stats of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The stats of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: StatsRestObject
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this BaseballRosterEntryRestObject.


        :param stats: The stats of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: StatsRestObject
        """

        self._stats = stats

    @property
    def season_stats(self):
        """Gets the season_stats of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The season_stats of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: StatsRestObject
        """
        return self._season_stats

    @season_stats.setter
    def season_stats(self, season_stats):
        """Sets the season_stats of this BaseballRosterEntryRestObject.


        :param season_stats: The season_stats of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: StatsRestObject
        """

        self._season_stats = season_stats

    @property
    def game_status(self):
        """Gets the game_status of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The game_status of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: GameStatusRestObject
        """
        return self._game_status

    @game_status.setter
    def game_status(self, game_status):
        """Sets the game_status of this BaseballRosterEntryRestObject.


        :param game_status: The game_status of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: GameStatusRestObject
        """

        self._game_status = game_status

    @property
    def all_positions(self):
        """Gets the all_positions of this BaseballRosterEntryRestObject.  # noqa: E501


        :return: The all_positions of this BaseballRosterEntryRestObject.  # noqa: E501
        :rtype: list[PositionRestObject]
        """
        return self._all_positions

    @all_positions.setter
    def all_positions(self, all_positions):
        """Sets the all_positions of this BaseballRosterEntryRestObject.


        :param all_positions: The all_positions of this BaseballRosterEntryRestObject.  # noqa: E501
        :type: list[PositionRestObject]
        """

        self._all_positions = all_positions

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
        if issubclass(BaseballRosterEntryRestObject, dict):
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
        if not isinstance(other, BaseballRosterEntryRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
