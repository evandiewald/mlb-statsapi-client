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

class Sport(object):
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
        'id': 'int',
        'code': 'str',
        'name': 'str',
        'abbreviation': 'str',
        'sort_order': 'int',
        'device_properties': 'JsonNode',
        'rule_settings': 'list[RuleSettings]',
        'season_state': 'str',
        'season_date_info': 'Season',
        'hydrated_rule_settings': 'dict(str, object)',
        'hydrated_season': 'dict(str, object)',
        'active_status': 'str',
        'affiliated': 'bool',
        'sport_active': 'bool',
        'hydrated_device_properties': 'dict(str, object)',
        'user_privileges': 'list[Privilege]'
    }

    attribute_map = {
        'requesting_user_role': 'requestingUserRole',
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'abbreviation': 'abbreviation',
        'sort_order': 'sortOrder',
        'device_properties': 'deviceProperties',
        'rule_settings': 'ruleSettings',
        'season_state': 'seasonState',
        'season_date_info': 'seasonDateInfo',
        'hydrated_rule_settings': 'hydratedRuleSettings',
        'hydrated_season': 'hydratedSeason',
        'active_status': 'activeStatus',
        'affiliated': 'affiliated',
        'sport_active': 'sportActive',
        'hydrated_device_properties': 'hydratedDeviceProperties',
        'user_privileges': 'userPrivileges'
    }

    def __init__(self, requesting_user_role=None, id=None, code=None, name=None, abbreviation=None, sort_order=None, device_properties=None, rule_settings=None, season_state=None, season_date_info=None, hydrated_rule_settings=None, hydrated_season=None, active_status=None, affiliated=None, sport_active=None, hydrated_device_properties=None, user_privileges=None):  # noqa: E501
        """Sport - a model defined in Swagger"""  # noqa: E501
        self._requesting_user_role = None
        self._id = None
        self._code = None
        self._name = None
        self._abbreviation = None
        self._sort_order = None
        self._device_properties = None
        self._rule_settings = None
        self._season_state = None
        self._season_date_info = None
        self._hydrated_rule_settings = None
        self._hydrated_season = None
        self._active_status = None
        self._affiliated = None
        self._sport_active = None
        self._hydrated_device_properties = None
        self._user_privileges = None
        self.discriminator = None
        if requesting_user_role is not None:
            self.requesting_user_role = requesting_user_role
        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if sort_order is not None:
            self.sort_order = sort_order
        if device_properties is not None:
            self.device_properties = device_properties
        if rule_settings is not None:
            self.rule_settings = rule_settings
        if season_state is not None:
            self.season_state = season_state
        if season_date_info is not None:
            self.season_date_info = season_date_info
        if hydrated_rule_settings is not None:
            self.hydrated_rule_settings = hydrated_rule_settings
        if hydrated_season is not None:
            self.hydrated_season = hydrated_season
        if active_status is not None:
            self.active_status = active_status
        if affiliated is not None:
            self.affiliated = affiliated
        if sport_active is not None:
            self.sport_active = sport_active
        if hydrated_device_properties is not None:
            self.hydrated_device_properties = hydrated_device_properties
        if user_privileges is not None:
            self.user_privileges = user_privileges

    @property
    def requesting_user_role(self):
        """Gets the requesting_user_role of this Sport.  # noqa: E501


        :return: The requesting_user_role of this Sport.  # noqa: E501
        :rtype: Role
        """
        return self._requesting_user_role

    @requesting_user_role.setter
    def requesting_user_role(self, requesting_user_role):
        """Sets the requesting_user_role of this Sport.


        :param requesting_user_role: The requesting_user_role of this Sport.  # noqa: E501
        :type: Role
        """

        self._requesting_user_role = requesting_user_role

    @property
    def id(self):
        """Gets the id of this Sport.  # noqa: E501


        :return: The id of this Sport.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Sport.


        :param id: The id of this Sport.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this Sport.  # noqa: E501


        :return: The code of this Sport.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Sport.


        :param code: The code of this Sport.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this Sport.  # noqa: E501


        :return: The name of this Sport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sport.


        :param name: The name of this Sport.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this Sport.  # noqa: E501


        :return: The abbreviation of this Sport.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this Sport.


        :param abbreviation: The abbreviation of this Sport.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def sort_order(self):
        """Gets the sort_order of this Sport.  # noqa: E501


        :return: The sort_order of this Sport.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this Sport.


        :param sort_order: The sort_order of this Sport.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def device_properties(self):
        """Gets the device_properties of this Sport.  # noqa: E501


        :return: The device_properties of this Sport.  # noqa: E501
        :rtype: JsonNode
        """
        return self._device_properties

    @device_properties.setter
    def device_properties(self, device_properties):
        """Sets the device_properties of this Sport.


        :param device_properties: The device_properties of this Sport.  # noqa: E501
        :type: JsonNode
        """

        self._device_properties = device_properties

    @property
    def rule_settings(self):
        """Gets the rule_settings of this Sport.  # noqa: E501


        :return: The rule_settings of this Sport.  # noqa: E501
        :rtype: list[RuleSettings]
        """
        return self._rule_settings

    @rule_settings.setter
    def rule_settings(self, rule_settings):
        """Sets the rule_settings of this Sport.


        :param rule_settings: The rule_settings of this Sport.  # noqa: E501
        :type: list[RuleSettings]
        """

        self._rule_settings = rule_settings

    @property
    def season_state(self):
        """Gets the season_state of this Sport.  # noqa: E501


        :return: The season_state of this Sport.  # noqa: E501
        :rtype: str
        """
        return self._season_state

    @season_state.setter
    def season_state(self, season_state):
        """Sets the season_state of this Sport.


        :param season_state: The season_state of this Sport.  # noqa: E501
        :type: str
        """

        self._season_state = season_state

    @property
    def season_date_info(self):
        """Gets the season_date_info of this Sport.  # noqa: E501


        :return: The season_date_info of this Sport.  # noqa: E501
        :rtype: Season
        """
        return self._season_date_info

    @season_date_info.setter
    def season_date_info(self, season_date_info):
        """Sets the season_date_info of this Sport.


        :param season_date_info: The season_date_info of this Sport.  # noqa: E501
        :type: Season
        """

        self._season_date_info = season_date_info

    @property
    def hydrated_rule_settings(self):
        """Gets the hydrated_rule_settings of this Sport.  # noqa: E501


        :return: The hydrated_rule_settings of this Sport.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._hydrated_rule_settings

    @hydrated_rule_settings.setter
    def hydrated_rule_settings(self, hydrated_rule_settings):
        """Sets the hydrated_rule_settings of this Sport.


        :param hydrated_rule_settings: The hydrated_rule_settings of this Sport.  # noqa: E501
        :type: dict(str, object)
        """

        self._hydrated_rule_settings = hydrated_rule_settings

    @property
    def hydrated_season(self):
        """Gets the hydrated_season of this Sport.  # noqa: E501


        :return: The hydrated_season of this Sport.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._hydrated_season

    @hydrated_season.setter
    def hydrated_season(self, hydrated_season):
        """Sets the hydrated_season of this Sport.


        :param hydrated_season: The hydrated_season of this Sport.  # noqa: E501
        :type: dict(str, object)
        """

        self._hydrated_season = hydrated_season

    @property
    def active_status(self):
        """Gets the active_status of this Sport.  # noqa: E501


        :return: The active_status of this Sport.  # noqa: E501
        :rtype: str
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this Sport.


        :param active_status: The active_status of this Sport.  # noqa: E501
        :type: str
        """

        self._active_status = active_status

    @property
    def affiliated(self):
        """Gets the affiliated of this Sport.  # noqa: E501


        :return: The affiliated of this Sport.  # noqa: E501
        :rtype: bool
        """
        return self._affiliated

    @affiliated.setter
    def affiliated(self, affiliated):
        """Sets the affiliated of this Sport.


        :param affiliated: The affiliated of this Sport.  # noqa: E501
        :type: bool
        """

        self._affiliated = affiliated

    @property
    def sport_active(self):
        """Gets the sport_active of this Sport.  # noqa: E501


        :return: The sport_active of this Sport.  # noqa: E501
        :rtype: bool
        """
        return self._sport_active

    @sport_active.setter
    def sport_active(self, sport_active):
        """Sets the sport_active of this Sport.


        :param sport_active: The sport_active of this Sport.  # noqa: E501
        :type: bool
        """

        self._sport_active = sport_active

    @property
    def hydrated_device_properties(self):
        """Gets the hydrated_device_properties of this Sport.  # noqa: E501


        :return: The hydrated_device_properties of this Sport.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._hydrated_device_properties

    @hydrated_device_properties.setter
    def hydrated_device_properties(self, hydrated_device_properties):
        """Sets the hydrated_device_properties of this Sport.


        :param hydrated_device_properties: The hydrated_device_properties of this Sport.  # noqa: E501
        :type: dict(str, object)
        """

        self._hydrated_device_properties = hydrated_device_properties

    @property
    def user_privileges(self):
        """Gets the user_privileges of this Sport.  # noqa: E501


        :return: The user_privileges of this Sport.  # noqa: E501
        :rtype: list[Privilege]
        """
        return self._user_privileges

    @user_privileges.setter
    def user_privileges(self, user_privileges):
        """Sets the user_privileges of this Sport.


        :param user_privileges: The user_privileges of this Sport.  # noqa: E501
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
        if issubclass(Sport, dict):
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
        if not isinstance(other, Sport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other