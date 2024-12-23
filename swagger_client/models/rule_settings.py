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

class RuleSettings(object):
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
        'play_setting_id': 'int',
        'setting_id': 'int',
        'setting_name': 'str',
        'setting_display_name': 'str',
        'setting_category_id': 'int',
        'setting_category': 'str',
        'setting_category_code': 'str',
        'setting_description': 'str',
        'setting_is_public': 'bool',
        'value_type': 'str',
        'setting_value': 'object',
        'setting_scope': 'str',
        'setting_options': 'list[RuleSettingsOption]',
        'priority_override': 'int',
        'start_date': 'date',
        'end_date': 'date',
        'inherited': 'bool',
        'game_type': 'str',
        'all_game_type_status': 'bool',
        'sport': 'Sport',
        'league': 'League',
        'venue': 'Venue',
        'game_pk': 'int',
        'schedule_event': 'ScheduleEvent',
        'sort_order': 'int',
        'user_has_permission': 'bool'
    }

    attribute_map = {
        'play_setting_id': 'playSettingId',
        'setting_id': 'settingId',
        'setting_name': 'settingName',
        'setting_display_name': 'settingDisplayName',
        'setting_category_id': 'settingCategoryId',
        'setting_category': 'settingCategory',
        'setting_category_code': 'settingCategoryCode',
        'setting_description': 'settingDescription',
        'setting_is_public': 'settingIsPublic',
        'value_type': 'valueType',
        'setting_value': 'settingValue',
        'setting_scope': 'settingScope',
        'setting_options': 'settingOptions',
        'priority_override': 'priorityOverride',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'inherited': 'inherited',
        'game_type': 'gameType',
        'all_game_type_status': 'allGameTypeStatus',
        'sport': 'sport',
        'league': 'league',
        'venue': 'venue',
        'game_pk': 'gamePk',
        'schedule_event': 'scheduleEvent',
        'sort_order': 'sortOrder',
        'user_has_permission': 'userHasPermission'
    }

    def __init__(self, play_setting_id=None, setting_id=None, setting_name=None, setting_display_name=None, setting_category_id=None, setting_category=None, setting_category_code=None, setting_description=None, setting_is_public=None, value_type=None, setting_value=None, setting_scope=None, setting_options=None, priority_override=None, start_date=None, end_date=None, inherited=None, game_type=None, all_game_type_status=None, sport=None, league=None, venue=None, game_pk=None, schedule_event=None, sort_order=None, user_has_permission=None):  # noqa: E501
        """RuleSettings - a model defined in Swagger"""  # noqa: E501
        self._play_setting_id = None
        self._setting_id = None
        self._setting_name = None
        self._setting_display_name = None
        self._setting_category_id = None
        self._setting_category = None
        self._setting_category_code = None
        self._setting_description = None
        self._setting_is_public = None
        self._value_type = None
        self._setting_value = None
        self._setting_scope = None
        self._setting_options = None
        self._priority_override = None
        self._start_date = None
        self._end_date = None
        self._inherited = None
        self._game_type = None
        self._all_game_type_status = None
        self._sport = None
        self._league = None
        self._venue = None
        self._game_pk = None
        self._schedule_event = None
        self._sort_order = None
        self._user_has_permission = None
        self.discriminator = None
        if play_setting_id is not None:
            self.play_setting_id = play_setting_id
        if setting_id is not None:
            self.setting_id = setting_id
        if setting_name is not None:
            self.setting_name = setting_name
        if setting_display_name is not None:
            self.setting_display_name = setting_display_name
        if setting_category_id is not None:
            self.setting_category_id = setting_category_id
        if setting_category is not None:
            self.setting_category = setting_category
        if setting_category_code is not None:
            self.setting_category_code = setting_category_code
        if setting_description is not None:
            self.setting_description = setting_description
        if setting_is_public is not None:
            self.setting_is_public = setting_is_public
        if value_type is not None:
            self.value_type = value_type
        if setting_value is not None:
            self.setting_value = setting_value
        if setting_scope is not None:
            self.setting_scope = setting_scope
        if setting_options is not None:
            self.setting_options = setting_options
        if priority_override is not None:
            self.priority_override = priority_override
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if inherited is not None:
            self.inherited = inherited
        if game_type is not None:
            self.game_type = game_type
        if all_game_type_status is not None:
            self.all_game_type_status = all_game_type_status
        if sport is not None:
            self.sport = sport
        if league is not None:
            self.league = league
        if venue is not None:
            self.venue = venue
        if game_pk is not None:
            self.game_pk = game_pk
        if schedule_event is not None:
            self.schedule_event = schedule_event
        if sort_order is not None:
            self.sort_order = sort_order
        if user_has_permission is not None:
            self.user_has_permission = user_has_permission

    @property
    def play_setting_id(self):
        """Gets the play_setting_id of this RuleSettings.  # noqa: E501


        :return: The play_setting_id of this RuleSettings.  # noqa: E501
        :rtype: int
        """
        return self._play_setting_id

    @play_setting_id.setter
    def play_setting_id(self, play_setting_id):
        """Sets the play_setting_id of this RuleSettings.


        :param play_setting_id: The play_setting_id of this RuleSettings.  # noqa: E501
        :type: int
        """

        self._play_setting_id = play_setting_id

    @property
    def setting_id(self):
        """Gets the setting_id of this RuleSettings.  # noqa: E501


        :return: The setting_id of this RuleSettings.  # noqa: E501
        :rtype: int
        """
        return self._setting_id

    @setting_id.setter
    def setting_id(self, setting_id):
        """Sets the setting_id of this RuleSettings.


        :param setting_id: The setting_id of this RuleSettings.  # noqa: E501
        :type: int
        """

        self._setting_id = setting_id

    @property
    def setting_name(self):
        """Gets the setting_name of this RuleSettings.  # noqa: E501


        :return: The setting_name of this RuleSettings.  # noqa: E501
        :rtype: str
        """
        return self._setting_name

    @setting_name.setter
    def setting_name(self, setting_name):
        """Sets the setting_name of this RuleSettings.


        :param setting_name: The setting_name of this RuleSettings.  # noqa: E501
        :type: str
        """

        self._setting_name = setting_name

    @property
    def setting_display_name(self):
        """Gets the setting_display_name of this RuleSettings.  # noqa: E501


        :return: The setting_display_name of this RuleSettings.  # noqa: E501
        :rtype: str
        """
        return self._setting_display_name

    @setting_display_name.setter
    def setting_display_name(self, setting_display_name):
        """Sets the setting_display_name of this RuleSettings.


        :param setting_display_name: The setting_display_name of this RuleSettings.  # noqa: E501
        :type: str
        """

        self._setting_display_name = setting_display_name

    @property
    def setting_category_id(self):
        """Gets the setting_category_id of this RuleSettings.  # noqa: E501


        :return: The setting_category_id of this RuleSettings.  # noqa: E501
        :rtype: int
        """
        return self._setting_category_id

    @setting_category_id.setter
    def setting_category_id(self, setting_category_id):
        """Sets the setting_category_id of this RuleSettings.


        :param setting_category_id: The setting_category_id of this RuleSettings.  # noqa: E501
        :type: int
        """

        self._setting_category_id = setting_category_id

    @property
    def setting_category(self):
        """Gets the setting_category of this RuleSettings.  # noqa: E501


        :return: The setting_category of this RuleSettings.  # noqa: E501
        :rtype: str
        """
        return self._setting_category

    @setting_category.setter
    def setting_category(self, setting_category):
        """Sets the setting_category of this RuleSettings.


        :param setting_category: The setting_category of this RuleSettings.  # noqa: E501
        :type: str
        """

        self._setting_category = setting_category

    @property
    def setting_category_code(self):
        """Gets the setting_category_code of this RuleSettings.  # noqa: E501


        :return: The setting_category_code of this RuleSettings.  # noqa: E501
        :rtype: str
        """
        return self._setting_category_code

    @setting_category_code.setter
    def setting_category_code(self, setting_category_code):
        """Sets the setting_category_code of this RuleSettings.


        :param setting_category_code: The setting_category_code of this RuleSettings.  # noqa: E501
        :type: str
        """

        self._setting_category_code = setting_category_code

    @property
    def setting_description(self):
        """Gets the setting_description of this RuleSettings.  # noqa: E501


        :return: The setting_description of this RuleSettings.  # noqa: E501
        :rtype: str
        """
        return self._setting_description

    @setting_description.setter
    def setting_description(self, setting_description):
        """Sets the setting_description of this RuleSettings.


        :param setting_description: The setting_description of this RuleSettings.  # noqa: E501
        :type: str
        """

        self._setting_description = setting_description

    @property
    def setting_is_public(self):
        """Gets the setting_is_public of this RuleSettings.  # noqa: E501


        :return: The setting_is_public of this RuleSettings.  # noqa: E501
        :rtype: bool
        """
        return self._setting_is_public

    @setting_is_public.setter
    def setting_is_public(self, setting_is_public):
        """Sets the setting_is_public of this RuleSettings.


        :param setting_is_public: The setting_is_public of this RuleSettings.  # noqa: E501
        :type: bool
        """

        self._setting_is_public = setting_is_public

    @property
    def value_type(self):
        """Gets the value_type of this RuleSettings.  # noqa: E501


        :return: The value_type of this RuleSettings.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this RuleSettings.


        :param value_type: The value_type of this RuleSettings.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

    @property
    def setting_value(self):
        """Gets the setting_value of this RuleSettings.  # noqa: E501


        :return: The setting_value of this RuleSettings.  # noqa: E501
        :rtype: object
        """
        return self._setting_value

    @setting_value.setter
    def setting_value(self, setting_value):
        """Sets the setting_value of this RuleSettings.


        :param setting_value: The setting_value of this RuleSettings.  # noqa: E501
        :type: object
        """

        self._setting_value = setting_value

    @property
    def setting_scope(self):
        """Gets the setting_scope of this RuleSettings.  # noqa: E501


        :return: The setting_scope of this RuleSettings.  # noqa: E501
        :rtype: str
        """
        return self._setting_scope

    @setting_scope.setter
    def setting_scope(self, setting_scope):
        """Sets the setting_scope of this RuleSettings.


        :param setting_scope: The setting_scope of this RuleSettings.  # noqa: E501
        :type: str
        """

        self._setting_scope = setting_scope

    @property
    def setting_options(self):
        """Gets the setting_options of this RuleSettings.  # noqa: E501


        :return: The setting_options of this RuleSettings.  # noqa: E501
        :rtype: list[RuleSettingsOption]
        """
        return self._setting_options

    @setting_options.setter
    def setting_options(self, setting_options):
        """Sets the setting_options of this RuleSettings.


        :param setting_options: The setting_options of this RuleSettings.  # noqa: E501
        :type: list[RuleSettingsOption]
        """

        self._setting_options = setting_options

    @property
    def priority_override(self):
        """Gets the priority_override of this RuleSettings.  # noqa: E501


        :return: The priority_override of this RuleSettings.  # noqa: E501
        :rtype: int
        """
        return self._priority_override

    @priority_override.setter
    def priority_override(self, priority_override):
        """Sets the priority_override of this RuleSettings.


        :param priority_override: The priority_override of this RuleSettings.  # noqa: E501
        :type: int
        """

        self._priority_override = priority_override

    @property
    def start_date(self):
        """Gets the start_date of this RuleSettings.  # noqa: E501


        :return: The start_date of this RuleSettings.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this RuleSettings.


        :param start_date: The start_date of this RuleSettings.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this RuleSettings.  # noqa: E501


        :return: The end_date of this RuleSettings.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this RuleSettings.


        :param end_date: The end_date of this RuleSettings.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def inherited(self):
        """Gets the inherited of this RuleSettings.  # noqa: E501


        :return: The inherited of this RuleSettings.  # noqa: E501
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """Sets the inherited of this RuleSettings.


        :param inherited: The inherited of this RuleSettings.  # noqa: E501
        :type: bool
        """

        self._inherited = inherited

    @property
    def game_type(self):
        """Gets the game_type of this RuleSettings.  # noqa: E501


        :return: The game_type of this RuleSettings.  # noqa: E501
        :rtype: str
        """
        return self._game_type

    @game_type.setter
    def game_type(self, game_type):
        """Sets the game_type of this RuleSettings.


        :param game_type: The game_type of this RuleSettings.  # noqa: E501
        :type: str
        """

        self._game_type = game_type

    @property
    def all_game_type_status(self):
        """Gets the all_game_type_status of this RuleSettings.  # noqa: E501


        :return: The all_game_type_status of this RuleSettings.  # noqa: E501
        :rtype: bool
        """
        return self._all_game_type_status

    @all_game_type_status.setter
    def all_game_type_status(self, all_game_type_status):
        """Sets the all_game_type_status of this RuleSettings.


        :param all_game_type_status: The all_game_type_status of this RuleSettings.  # noqa: E501
        :type: bool
        """

        self._all_game_type_status = all_game_type_status

    @property
    def sport(self):
        """Gets the sport of this RuleSettings.  # noqa: E501


        :return: The sport of this RuleSettings.  # noqa: E501
        :rtype: Sport
        """
        return self._sport

    @sport.setter
    def sport(self, sport):
        """Sets the sport of this RuleSettings.


        :param sport: The sport of this RuleSettings.  # noqa: E501
        :type: Sport
        """

        self._sport = sport

    @property
    def league(self):
        """Gets the league of this RuleSettings.  # noqa: E501


        :return: The league of this RuleSettings.  # noqa: E501
        :rtype: League
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this RuleSettings.


        :param league: The league of this RuleSettings.  # noqa: E501
        :type: League
        """

        self._league = league

    @property
    def venue(self):
        """Gets the venue of this RuleSettings.  # noqa: E501


        :return: The venue of this RuleSettings.  # noqa: E501
        :rtype: Venue
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this RuleSettings.


        :param venue: The venue of this RuleSettings.  # noqa: E501
        :type: Venue
        """

        self._venue = venue

    @property
    def game_pk(self):
        """Gets the game_pk of this RuleSettings.  # noqa: E501


        :return: The game_pk of this RuleSettings.  # noqa: E501
        :rtype: int
        """
        return self._game_pk

    @game_pk.setter
    def game_pk(self, game_pk):
        """Sets the game_pk of this RuleSettings.


        :param game_pk: The game_pk of this RuleSettings.  # noqa: E501
        :type: int
        """

        self._game_pk = game_pk

    @property
    def schedule_event(self):
        """Gets the schedule_event of this RuleSettings.  # noqa: E501


        :return: The schedule_event of this RuleSettings.  # noqa: E501
        :rtype: ScheduleEvent
        """
        return self._schedule_event

    @schedule_event.setter
    def schedule_event(self, schedule_event):
        """Sets the schedule_event of this RuleSettings.


        :param schedule_event: The schedule_event of this RuleSettings.  # noqa: E501
        :type: ScheduleEvent
        """

        self._schedule_event = schedule_event

    @property
    def sort_order(self):
        """Gets the sort_order of this RuleSettings.  # noqa: E501


        :return: The sort_order of this RuleSettings.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this RuleSettings.


        :param sort_order: The sort_order of this RuleSettings.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def user_has_permission(self):
        """Gets the user_has_permission of this RuleSettings.  # noqa: E501


        :return: The user_has_permission of this RuleSettings.  # noqa: E501
        :rtype: bool
        """
        return self._user_has_permission

    @user_has_permission.setter
    def user_has_permission(self, user_has_permission):
        """Sets the user_has_permission of this RuleSettings.


        :param user_has_permission: The user_has_permission of this RuleSettings.  # noqa: E501
        :type: bool
        """

        self._user_has_permission = user_has_permission

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
        if issubclass(RuleSettings, dict):
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
        if not isinstance(other, RuleSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other