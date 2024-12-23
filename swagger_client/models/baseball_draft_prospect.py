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

class BaseballDraftProspect(object):
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
        'requesting_user_role': 'Role',
        'bis_player_id': 'int',
        'bis_school_id': 'int',
        'draft_player_id': 'int',
        'pick_round': 'str',
        'pick_round_label': 'str',
        'pick_number': 'int',
        'display_pick_number': 'int',
        'round_pick_number': 'int',
        'english_blurb': 'str',
        'spanish_blurb': 'str',
        'rank': 'int',
        'picked_team_code': 'str',
        'home': 'Location',
        'scouting_report': 'str',
        'photo_flag': 'bool',
        'school': 'School',
        'comments': 'str',
        'headshot_link': 'str',
        'pick_value': 'str',
        'signing_bonus': 'str',
        'person': 'BaseballPerson',
        'team': 'BaseballTeam',
        'draft_type': 'DraftTypeEnum',
        'draft_status': 'DraftStatusEnum',
        'was_passed': 'bool',
        'was_last_pick': 'bool',
        'was_selected': 'bool',
        'year': 'str',
        'user_privileges': 'list[Privilege]'
    }

    attribute_map = {
        'requesting_user_role': 'requestingUserRole',
        'bis_player_id': 'bisPlayerId',
        'bis_school_id': 'bisSchoolId',
        'draft_player_id': 'draftPlayerId',
        'pick_round': 'pickRound',
        'pick_round_label': 'pickRoundLabel',
        'pick_number': 'pickNumber',
        'display_pick_number': 'displayPickNumber',
        'round_pick_number': 'roundPickNumber',
        'english_blurb': 'englishBlurb',
        'spanish_blurb': 'spanishBlurb',
        'rank': 'rank',
        'picked_team_code': 'pickedTeamCode',
        'home': 'home',
        'scouting_report': 'scoutingReport',
        'photo_flag': 'photoFlag',
        'school': 'school',
        'comments': 'comments',
        'headshot_link': 'headshotLink',
        'pick_value': 'pickValue',
        'signing_bonus': 'signingBonus',
        'person': 'person',
        'team': 'team',
        'draft_type': 'draftType',
        'draft_status': 'draftStatus',
        'was_passed': 'wasPassed',
        'was_last_pick': 'wasLastPick',
        'was_selected': 'wasSelected',
        'year': 'year',
        'user_privileges': 'userPrivileges'
    }

    def __init__(self, requesting_user_role=None, bis_player_id=None, bis_school_id=None, draft_player_id=None, pick_round=None, pick_round_label=None, pick_number=None, display_pick_number=None, round_pick_number=None, english_blurb=None, spanish_blurb=None, rank=None, picked_team_code=None, home=None, scouting_report=None, photo_flag=None, school=None, comments=None, headshot_link=None, pick_value=None, signing_bonus=None, person=None, team=None, draft_type=None, draft_status=None, was_passed=None, was_last_pick=None, was_selected=None, year=None, user_privileges=None):  # noqa: E501
        """BaseballDraftProspect - a model defined in Swagger"""  # noqa: E501
        self._requesting_user_role = None
        self._bis_player_id = None
        self._bis_school_id = None
        self._draft_player_id = None
        self._pick_round = None
        self._pick_round_label = None
        self._pick_number = None
        self._display_pick_number = None
        self._round_pick_number = None
        self._english_blurb = None
        self._spanish_blurb = None
        self._rank = None
        self._picked_team_code = None
        self._home = None
        self._scouting_report = None
        self._photo_flag = None
        self._school = None
        self._comments = None
        self._headshot_link = None
        self._pick_value = None
        self._signing_bonus = None
        self._person = None
        self._team = None
        self._draft_type = None
        self._draft_status = None
        self._was_passed = None
        self._was_last_pick = None
        self._was_selected = None
        self._year = None
        self._user_privileges = None
        self.discriminator = None
        if requesting_user_role is not None:
            self.requesting_user_role = requesting_user_role
        if bis_player_id is not None:
            self.bis_player_id = bis_player_id
        if bis_school_id is not None:
            self.bis_school_id = bis_school_id
        if draft_player_id is not None:
            self.draft_player_id = draft_player_id
        if pick_round is not None:
            self.pick_round = pick_round
        if pick_round_label is not None:
            self.pick_round_label = pick_round_label
        if pick_number is not None:
            self.pick_number = pick_number
        if display_pick_number is not None:
            self.display_pick_number = display_pick_number
        if round_pick_number is not None:
            self.round_pick_number = round_pick_number
        if english_blurb is not None:
            self.english_blurb = english_blurb
        if spanish_blurb is not None:
            self.spanish_blurb = spanish_blurb
        if rank is not None:
            self.rank = rank
        if picked_team_code is not None:
            self.picked_team_code = picked_team_code
        if home is not None:
            self.home = home
        if scouting_report is not None:
            self.scouting_report = scouting_report
        if photo_flag is not None:
            self.photo_flag = photo_flag
        if school is not None:
            self.school = school
        if comments is not None:
            self.comments = comments
        if headshot_link is not None:
            self.headshot_link = headshot_link
        if pick_value is not None:
            self.pick_value = pick_value
        if signing_bonus is not None:
            self.signing_bonus = signing_bonus
        if person is not None:
            self.person = person
        if team is not None:
            self.team = team
        if draft_type is not None:
            self.draft_type = draft_type
        if draft_status is not None:
            self.draft_status = draft_status
        if was_passed is not None:
            self.was_passed = was_passed
        if was_last_pick is not None:
            self.was_last_pick = was_last_pick
        if was_selected is not None:
            self.was_selected = was_selected
        if year is not None:
            self.year = year
        if user_privileges is not None:
            self.user_privileges = user_privileges

    @property
    def requesting_user_role(self):
        """Gets the requesting_user_role of this BaseballDraftProspect.  # noqa: E501


        :return: The requesting_user_role of this BaseballDraftProspect.  # noqa: E501
        :rtype: Role
        """
        return self._requesting_user_role

    @requesting_user_role.setter
    def requesting_user_role(self, requesting_user_role):
        """Sets the requesting_user_role of this BaseballDraftProspect.


        :param requesting_user_role: The requesting_user_role of this BaseballDraftProspect.  # noqa: E501
        :type: Role
        """

        self._requesting_user_role = requesting_user_role

    @property
    def bis_player_id(self):
        """Gets the bis_player_id of this BaseballDraftProspect.  # noqa: E501


        :return: The bis_player_id of this BaseballDraftProspect.  # noqa: E501
        :rtype: int
        """
        return self._bis_player_id

    @bis_player_id.setter
    def bis_player_id(self, bis_player_id):
        """Sets the bis_player_id of this BaseballDraftProspect.


        :param bis_player_id: The bis_player_id of this BaseballDraftProspect.  # noqa: E501
        :type: int
        """

        self._bis_player_id = bis_player_id

    @property
    def bis_school_id(self):
        """Gets the bis_school_id of this BaseballDraftProspect.  # noqa: E501


        :return: The bis_school_id of this BaseballDraftProspect.  # noqa: E501
        :rtype: int
        """
        return self._bis_school_id

    @bis_school_id.setter
    def bis_school_id(self, bis_school_id):
        """Sets the bis_school_id of this BaseballDraftProspect.


        :param bis_school_id: The bis_school_id of this BaseballDraftProspect.  # noqa: E501
        :type: int
        """

        self._bis_school_id = bis_school_id

    @property
    def draft_player_id(self):
        """Gets the draft_player_id of this BaseballDraftProspect.  # noqa: E501


        :return: The draft_player_id of this BaseballDraftProspect.  # noqa: E501
        :rtype: int
        """
        return self._draft_player_id

    @draft_player_id.setter
    def draft_player_id(self, draft_player_id):
        """Sets the draft_player_id of this BaseballDraftProspect.


        :param draft_player_id: The draft_player_id of this BaseballDraftProspect.  # noqa: E501
        :type: int
        """

        self._draft_player_id = draft_player_id

    @property
    def pick_round(self):
        """Gets the pick_round of this BaseballDraftProspect.  # noqa: E501


        :return: The pick_round of this BaseballDraftProspect.  # noqa: E501
        :rtype: str
        """
        return self._pick_round

    @pick_round.setter
    def pick_round(self, pick_round):
        """Sets the pick_round of this BaseballDraftProspect.


        :param pick_round: The pick_round of this BaseballDraftProspect.  # noqa: E501
        :type: str
        """

        self._pick_round = pick_round

    @property
    def pick_round_label(self):
        """Gets the pick_round_label of this BaseballDraftProspect.  # noqa: E501


        :return: The pick_round_label of this BaseballDraftProspect.  # noqa: E501
        :rtype: str
        """
        return self._pick_round_label

    @pick_round_label.setter
    def pick_round_label(self, pick_round_label):
        """Sets the pick_round_label of this BaseballDraftProspect.


        :param pick_round_label: The pick_round_label of this BaseballDraftProspect.  # noqa: E501
        :type: str
        """

        self._pick_round_label = pick_round_label

    @property
    def pick_number(self):
        """Gets the pick_number of this BaseballDraftProspect.  # noqa: E501


        :return: The pick_number of this BaseballDraftProspect.  # noqa: E501
        :rtype: int
        """
        return self._pick_number

    @pick_number.setter
    def pick_number(self, pick_number):
        """Sets the pick_number of this BaseballDraftProspect.


        :param pick_number: The pick_number of this BaseballDraftProspect.  # noqa: E501
        :type: int
        """

        self._pick_number = pick_number

    @property
    def display_pick_number(self):
        """Gets the display_pick_number of this BaseballDraftProspect.  # noqa: E501


        :return: The display_pick_number of this BaseballDraftProspect.  # noqa: E501
        :rtype: int
        """
        return self._display_pick_number

    @display_pick_number.setter
    def display_pick_number(self, display_pick_number):
        """Sets the display_pick_number of this BaseballDraftProspect.


        :param display_pick_number: The display_pick_number of this BaseballDraftProspect.  # noqa: E501
        :type: int
        """

        self._display_pick_number = display_pick_number

    @property
    def round_pick_number(self):
        """Gets the round_pick_number of this BaseballDraftProspect.  # noqa: E501


        :return: The round_pick_number of this BaseballDraftProspect.  # noqa: E501
        :rtype: int
        """
        return self._round_pick_number

    @round_pick_number.setter
    def round_pick_number(self, round_pick_number):
        """Sets the round_pick_number of this BaseballDraftProspect.


        :param round_pick_number: The round_pick_number of this BaseballDraftProspect.  # noqa: E501
        :type: int
        """

        self._round_pick_number = round_pick_number

    @property
    def english_blurb(self):
        """Gets the english_blurb of this BaseballDraftProspect.  # noqa: E501


        :return: The english_blurb of this BaseballDraftProspect.  # noqa: E501
        :rtype: str
        """
        return self._english_blurb

    @english_blurb.setter
    def english_blurb(self, english_blurb):
        """Sets the english_blurb of this BaseballDraftProspect.


        :param english_blurb: The english_blurb of this BaseballDraftProspect.  # noqa: E501
        :type: str
        """

        self._english_blurb = english_blurb

    @property
    def spanish_blurb(self):
        """Gets the spanish_blurb of this BaseballDraftProspect.  # noqa: E501


        :return: The spanish_blurb of this BaseballDraftProspect.  # noqa: E501
        :rtype: str
        """
        return self._spanish_blurb

    @spanish_blurb.setter
    def spanish_blurb(self, spanish_blurb):
        """Sets the spanish_blurb of this BaseballDraftProspect.


        :param spanish_blurb: The spanish_blurb of this BaseballDraftProspect.  # noqa: E501
        :type: str
        """

        self._spanish_blurb = spanish_blurb

    @property
    def rank(self):
        """Gets the rank of this BaseballDraftProspect.  # noqa: E501


        :return: The rank of this BaseballDraftProspect.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this BaseballDraftProspect.


        :param rank: The rank of this BaseballDraftProspect.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def picked_team_code(self):
        """Gets the picked_team_code of this BaseballDraftProspect.  # noqa: E501


        :return: The picked_team_code of this BaseballDraftProspect.  # noqa: E501
        :rtype: str
        """
        return self._picked_team_code

    @picked_team_code.setter
    def picked_team_code(self, picked_team_code):
        """Sets the picked_team_code of this BaseballDraftProspect.


        :param picked_team_code: The picked_team_code of this BaseballDraftProspect.  # noqa: E501
        :type: str
        """

        self._picked_team_code = picked_team_code

    @property
    def home(self):
        """Gets the home of this BaseballDraftProspect.  # noqa: E501


        :return: The home of this BaseballDraftProspect.  # noqa: E501
        :rtype: Location
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this BaseballDraftProspect.


        :param home: The home of this BaseballDraftProspect.  # noqa: E501
        :type: Location
        """

        self._home = home

    @property
    def scouting_report(self):
        """Gets the scouting_report of this BaseballDraftProspect.  # noqa: E501


        :return: The scouting_report of this BaseballDraftProspect.  # noqa: E501
        :rtype: str
        """
        return self._scouting_report

    @scouting_report.setter
    def scouting_report(self, scouting_report):
        """Sets the scouting_report of this BaseballDraftProspect.


        :param scouting_report: The scouting_report of this BaseballDraftProspect.  # noqa: E501
        :type: str
        """

        self._scouting_report = scouting_report

    @property
    def photo_flag(self):
        """Gets the photo_flag of this BaseballDraftProspect.  # noqa: E501


        :return: The photo_flag of this BaseballDraftProspect.  # noqa: E501
        :rtype: bool
        """
        return self._photo_flag

    @photo_flag.setter
    def photo_flag(self, photo_flag):
        """Sets the photo_flag of this BaseballDraftProspect.


        :param photo_flag: The photo_flag of this BaseballDraftProspect.  # noqa: E501
        :type: bool
        """

        self._photo_flag = photo_flag

    @property
    def school(self):
        """Gets the school of this BaseballDraftProspect.  # noqa: E501


        :return: The school of this BaseballDraftProspect.  # noqa: E501
        :rtype: School
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this BaseballDraftProspect.


        :param school: The school of this BaseballDraftProspect.  # noqa: E501
        :type: School
        """

        self._school = school

    @property
    def comments(self):
        """Gets the comments of this BaseballDraftProspect.  # noqa: E501


        :return: The comments of this BaseballDraftProspect.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this BaseballDraftProspect.


        :param comments: The comments of this BaseballDraftProspect.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def headshot_link(self):
        """Gets the headshot_link of this BaseballDraftProspect.  # noqa: E501


        :return: The headshot_link of this BaseballDraftProspect.  # noqa: E501
        :rtype: str
        """
        return self._headshot_link

    @headshot_link.setter
    def headshot_link(self, headshot_link):
        """Sets the headshot_link of this BaseballDraftProspect.


        :param headshot_link: The headshot_link of this BaseballDraftProspect.  # noqa: E501
        :type: str
        """

        self._headshot_link = headshot_link

    @property
    def pick_value(self):
        """Gets the pick_value of this BaseballDraftProspect.  # noqa: E501


        :return: The pick_value of this BaseballDraftProspect.  # noqa: E501
        :rtype: str
        """
        return self._pick_value

    @pick_value.setter
    def pick_value(self, pick_value):
        """Sets the pick_value of this BaseballDraftProspect.


        :param pick_value: The pick_value of this BaseballDraftProspect.  # noqa: E501
        :type: str
        """

        self._pick_value = pick_value

    @property
    def signing_bonus(self):
        """Gets the signing_bonus of this BaseballDraftProspect.  # noqa: E501


        :return: The signing_bonus of this BaseballDraftProspect.  # noqa: E501
        :rtype: str
        """
        return self._signing_bonus

    @signing_bonus.setter
    def signing_bonus(self, signing_bonus):
        """Sets the signing_bonus of this BaseballDraftProspect.


        :param signing_bonus: The signing_bonus of this BaseballDraftProspect.  # noqa: E501
        :type: str
        """

        self._signing_bonus = signing_bonus

    @property
    def person(self):
        """Gets the person of this BaseballDraftProspect.  # noqa: E501


        :return: The person of this BaseballDraftProspect.  # noqa: E501
        :rtype: BaseballPerson
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this BaseballDraftProspect.


        :param person: The person of this BaseballDraftProspect.  # noqa: E501
        :type: BaseballPerson
        """

        self._person = person

    @property
    def team(self):
        """Gets the team of this BaseballDraftProspect.  # noqa: E501


        :return: The team of this BaseballDraftProspect.  # noqa: E501
        :rtype: BaseballTeam
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BaseballDraftProspect.


        :param team: The team of this BaseballDraftProspect.  # noqa: E501
        :type: BaseballTeam
        """

        self._team = team

    @property
    def draft_type(self):
        """Gets the draft_type of this BaseballDraftProspect.  # noqa: E501


        :return: The draft_type of this BaseballDraftProspect.  # noqa: E501
        :rtype: DraftTypeEnum
        """
        return self._draft_type

    @draft_type.setter
    def draft_type(self, draft_type):
        """Sets the draft_type of this BaseballDraftProspect.


        :param draft_type: The draft_type of this BaseballDraftProspect.  # noqa: E501
        :type: DraftTypeEnum
        """

        self._draft_type = draft_type

    @property
    def draft_status(self):
        """Gets the draft_status of this BaseballDraftProspect.  # noqa: E501


        :return: The draft_status of this BaseballDraftProspect.  # noqa: E501
        :rtype: DraftStatusEnum
        """
        return self._draft_status

    @draft_status.setter
    def draft_status(self, draft_status):
        """Sets the draft_status of this BaseballDraftProspect.


        :param draft_status: The draft_status of this BaseballDraftProspect.  # noqa: E501
        :type: DraftStatusEnum
        """

        self._draft_status = draft_status

    @property
    def was_passed(self):
        """Gets the was_passed of this BaseballDraftProspect.  # noqa: E501


        :return: The was_passed of this BaseballDraftProspect.  # noqa: E501
        :rtype: bool
        """
        return self._was_passed

    @was_passed.setter
    def was_passed(self, was_passed):
        """Sets the was_passed of this BaseballDraftProspect.


        :param was_passed: The was_passed of this BaseballDraftProspect.  # noqa: E501
        :type: bool
        """

        self._was_passed = was_passed

    @property
    def was_last_pick(self):
        """Gets the was_last_pick of this BaseballDraftProspect.  # noqa: E501


        :return: The was_last_pick of this BaseballDraftProspect.  # noqa: E501
        :rtype: bool
        """
        return self._was_last_pick

    @was_last_pick.setter
    def was_last_pick(self, was_last_pick):
        """Sets the was_last_pick of this BaseballDraftProspect.


        :param was_last_pick: The was_last_pick of this BaseballDraftProspect.  # noqa: E501
        :type: bool
        """

        self._was_last_pick = was_last_pick

    @property
    def was_selected(self):
        """Gets the was_selected of this BaseballDraftProspect.  # noqa: E501


        :return: The was_selected of this BaseballDraftProspect.  # noqa: E501
        :rtype: bool
        """
        return self._was_selected

    @was_selected.setter
    def was_selected(self, was_selected):
        """Sets the was_selected of this BaseballDraftProspect.


        :param was_selected: The was_selected of this BaseballDraftProspect.  # noqa: E501
        :type: bool
        """

        self._was_selected = was_selected

    @property
    def year(self):
        """Gets the year of this BaseballDraftProspect.  # noqa: E501


        :return: The year of this BaseballDraftProspect.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this BaseballDraftProspect.


        :param year: The year of this BaseballDraftProspect.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def user_privileges(self):
        """Gets the user_privileges of this BaseballDraftProspect.  # noqa: E501


        :return: The user_privileges of this BaseballDraftProspect.  # noqa: E501
        :rtype: list[Privilege]
        """
        return self._user_privileges

    @user_privileges.setter
    def user_privileges(self, user_privileges):
        """Sets the user_privileges of this BaseballDraftProspect.


        :param user_privileges: The user_privileges of this BaseballDraftProspect.  # noqa: E501
        :type: list[Privilege]
        """

        self._user_privileges = user_privileges

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
        if issubclass(BaseballDraftProspect, dict):
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
        if not isinstance(other, BaseballDraftProspect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other