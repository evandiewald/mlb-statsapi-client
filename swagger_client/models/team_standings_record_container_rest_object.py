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

class TeamStandingsRecordContainerRestObject(object):
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
        'hydrations': 'list[str]',
        'standings_type': 'str',
        'league': 'LeagueRestObject',
        'division': 'DivisionRestObject',
        'conference': 'ConferenceRestObject',
        'sport': 'SportRestObject',
        'organization': 'BaseballTeamRestObject',
        'last_updated': 'datetime',
        'aggregate_record': 'TeamStandingsRecordRestObject',
        'team_records': 'list[TeamStandingsRecordRestObject]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'hydrations': 'hydrations',
        'standings_type': 'standingsType',
        'league': 'league',
        'division': 'division',
        'conference': 'conference',
        'sport': 'sport',
        'organization': 'organization',
        'last_updated': 'lastUpdated',
        'aggregate_record': 'aggregateRecord',
        'team_records': 'teamRecords'
    }

    def __init__(self, copyright=None, hydrations=None, standings_type=None, league=None, division=None, conference=None, sport=None, organization=None, last_updated=None, aggregate_record=None, team_records=None):  # noqa: E501
        """TeamStandingsRecordContainerRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._hydrations = None
        self._standings_type = None
        self._league = None
        self._division = None
        self._conference = None
        self._sport = None
        self._organization = None
        self._last_updated = None
        self._aggregate_record = None
        self._team_records = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if hydrations is not None:
            self.hydrations = hydrations
        if standings_type is not None:
            self.standings_type = standings_type
        if league is not None:
            self.league = league
        if division is not None:
            self.division = division
        if conference is not None:
            self.conference = conference
        if sport is not None:
            self.sport = sport
        if organization is not None:
            self.organization = organization
        if last_updated is not None:
            self.last_updated = last_updated
        if aggregate_record is not None:
            self.aggregate_record = aggregate_record
        if team_records is not None:
            self.team_records = team_records

    @property
    def copyright(self):
        """Gets the copyright of this TeamStandingsRecordContainerRestObject.  # noqa: E501


        :return: The copyright of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this TeamStandingsRecordContainerRestObject.


        :param copyright: The copyright of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def hydrations(self):
        """Gets the hydrations of this TeamStandingsRecordContainerRestObject.  # noqa: E501


        :return: The hydrations of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._hydrations

    @hydrations.setter
    def hydrations(self, hydrations):
        """Sets the hydrations of this TeamStandingsRecordContainerRestObject.


        :param hydrations: The hydrations of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :type: list[str]
        """

        self._hydrations = hydrations

    @property
    def standings_type(self):
        """Gets the standings_type of this TeamStandingsRecordContainerRestObject.  # noqa: E501


        :return: The standings_type of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :rtype: str
        """
        return self._standings_type

    @standings_type.setter
    def standings_type(self, standings_type):
        """Sets the standings_type of this TeamStandingsRecordContainerRestObject.


        :param standings_type: The standings_type of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :type: str
        """

        self._standings_type = standings_type

    @property
    def league(self):
        """Gets the league of this TeamStandingsRecordContainerRestObject.  # noqa: E501


        :return: The league of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :rtype: LeagueRestObject
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this TeamStandingsRecordContainerRestObject.


        :param league: The league of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :type: LeagueRestObject
        """

        self._league = league

    @property
    def division(self):
        """Gets the division of this TeamStandingsRecordContainerRestObject.  # noqa: E501


        :return: The division of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :rtype: DivisionRestObject
        """
        return self._division

    @division.setter
    def division(self, division):
        """Sets the division of this TeamStandingsRecordContainerRestObject.


        :param division: The division of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :type: DivisionRestObject
        """

        self._division = division

    @property
    def conference(self):
        """Gets the conference of this TeamStandingsRecordContainerRestObject.  # noqa: E501


        :return: The conference of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :rtype: ConferenceRestObject
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this TeamStandingsRecordContainerRestObject.


        :param conference: The conference of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :type: ConferenceRestObject
        """

        self._conference = conference

    @property
    def sport(self):
        """Gets the sport of this TeamStandingsRecordContainerRestObject.  # noqa: E501


        :return: The sport of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :rtype: SportRestObject
        """
        return self._sport

    @sport.setter
    def sport(self, sport):
        """Sets the sport of this TeamStandingsRecordContainerRestObject.


        :param sport: The sport of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :type: SportRestObject
        """

        self._sport = sport

    @property
    def organization(self):
        """Gets the organization of this TeamStandingsRecordContainerRestObject.  # noqa: E501


        :return: The organization of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :rtype: BaseballTeamRestObject
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this TeamStandingsRecordContainerRestObject.


        :param organization: The organization of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :type: BaseballTeamRestObject
        """

        self._organization = organization

    @property
    def last_updated(self):
        """Gets the last_updated of this TeamStandingsRecordContainerRestObject.  # noqa: E501


        :return: The last_updated of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this TeamStandingsRecordContainerRestObject.


        :param last_updated: The last_updated of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def aggregate_record(self):
        """Gets the aggregate_record of this TeamStandingsRecordContainerRestObject.  # noqa: E501


        :return: The aggregate_record of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :rtype: TeamStandingsRecordRestObject
        """
        return self._aggregate_record

    @aggregate_record.setter
    def aggregate_record(self, aggregate_record):
        """Sets the aggregate_record of this TeamStandingsRecordContainerRestObject.


        :param aggregate_record: The aggregate_record of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :type: TeamStandingsRecordRestObject
        """

        self._aggregate_record = aggregate_record

    @property
    def team_records(self):
        """Gets the team_records of this TeamStandingsRecordContainerRestObject.  # noqa: E501


        :return: The team_records of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :rtype: list[TeamStandingsRecordRestObject]
        """
        return self._team_records

    @team_records.setter
    def team_records(self, team_records):
        """Sets the team_records of this TeamStandingsRecordContainerRestObject.


        :param team_records: The team_records of this TeamStandingsRecordContainerRestObject.  # noqa: E501
        :type: list[TeamStandingsRecordRestObject]
        """

        self._team_records = team_records

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
        if issubclass(TeamStandingsRecordContainerRestObject, dict):
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
        if not isinstance(other, TeamStandingsRecordContainerRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
