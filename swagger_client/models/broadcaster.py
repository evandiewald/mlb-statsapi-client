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

class Broadcaster(object):
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
        'broadcaster_id': 'int',
        'broadcaster_text': 'str',
        'broadcaster_desc': 'str',
        'call_sign': 'str',
        'broadcaster_type_id': 'int',
        'broadcaster_type_code': 'str',
        'broadcaster_type_text': 'str',
        'broadcaster_type_desc': 'str',
        'broadcaster_comment': 'str',
        'primary_team_id': 'int',
        'broadcast_availability': 'BroadcastAvailability',
        'active_status': 'bool',
        'is_national_status': 'bool',
        'sort_order': 'int',
        'mvpd_auth_broadcast': 'bool',
        'language': 'Language'
    }

    attribute_map = {
        'broadcaster_id': 'broadcasterId',
        'broadcaster_text': 'broadcasterText',
        'broadcaster_desc': 'broadcasterDesc',
        'call_sign': 'callSign',
        'broadcaster_type_id': 'broadcasterTypeId',
        'broadcaster_type_code': 'broadcasterTypeCode',
        'broadcaster_type_text': 'broadcasterTypeText',
        'broadcaster_type_desc': 'broadcasterTypeDesc',
        'broadcaster_comment': 'broadcasterComment',
        'primary_team_id': 'primaryTeamId',
        'broadcast_availability': 'broadcastAvailability',
        'active_status': 'activeStatus',
        'is_national_status': 'isNationalStatus',
        'sort_order': 'sortOrder',
        'mvpd_auth_broadcast': 'mvpdAuthBroadcast',
        'language': 'language'
    }

    def __init__(self, broadcaster_id=None, broadcaster_text=None, broadcaster_desc=None, call_sign=None, broadcaster_type_id=None, broadcaster_type_code=None, broadcaster_type_text=None, broadcaster_type_desc=None, broadcaster_comment=None, primary_team_id=None, broadcast_availability=None, active_status=None, is_national_status=None, sort_order=None, mvpd_auth_broadcast=None, language=None):  # noqa: E501
        """Broadcaster - a model defined in Swagger"""  # noqa: E501
        self._broadcaster_id = None
        self._broadcaster_text = None
        self._broadcaster_desc = None
        self._call_sign = None
        self._broadcaster_type_id = None
        self._broadcaster_type_code = None
        self._broadcaster_type_text = None
        self._broadcaster_type_desc = None
        self._broadcaster_comment = None
        self._primary_team_id = None
        self._broadcast_availability = None
        self._active_status = None
        self._is_national_status = None
        self._sort_order = None
        self._mvpd_auth_broadcast = None
        self._language = None
        self.discriminator = None
        if broadcaster_id is not None:
            self.broadcaster_id = broadcaster_id
        if broadcaster_text is not None:
            self.broadcaster_text = broadcaster_text
        if broadcaster_desc is not None:
            self.broadcaster_desc = broadcaster_desc
        if call_sign is not None:
            self.call_sign = call_sign
        if broadcaster_type_id is not None:
            self.broadcaster_type_id = broadcaster_type_id
        if broadcaster_type_code is not None:
            self.broadcaster_type_code = broadcaster_type_code
        if broadcaster_type_text is not None:
            self.broadcaster_type_text = broadcaster_type_text
        if broadcaster_type_desc is not None:
            self.broadcaster_type_desc = broadcaster_type_desc
        if broadcaster_comment is not None:
            self.broadcaster_comment = broadcaster_comment
        if primary_team_id is not None:
            self.primary_team_id = primary_team_id
        if broadcast_availability is not None:
            self.broadcast_availability = broadcast_availability
        if active_status is not None:
            self.active_status = active_status
        if is_national_status is not None:
            self.is_national_status = is_national_status
        if sort_order is not None:
            self.sort_order = sort_order
        if mvpd_auth_broadcast is not None:
            self.mvpd_auth_broadcast = mvpd_auth_broadcast
        if language is not None:
            self.language = language

    @property
    def broadcaster_id(self):
        """Gets the broadcaster_id of this Broadcaster.  # noqa: E501


        :return: The broadcaster_id of this Broadcaster.  # noqa: E501
        :rtype: int
        """
        return self._broadcaster_id

    @broadcaster_id.setter
    def broadcaster_id(self, broadcaster_id):
        """Sets the broadcaster_id of this Broadcaster.


        :param broadcaster_id: The broadcaster_id of this Broadcaster.  # noqa: E501
        :type: int
        """

        self._broadcaster_id = broadcaster_id

    @property
    def broadcaster_text(self):
        """Gets the broadcaster_text of this Broadcaster.  # noqa: E501


        :return: The broadcaster_text of this Broadcaster.  # noqa: E501
        :rtype: str
        """
        return self._broadcaster_text

    @broadcaster_text.setter
    def broadcaster_text(self, broadcaster_text):
        """Sets the broadcaster_text of this Broadcaster.


        :param broadcaster_text: The broadcaster_text of this Broadcaster.  # noqa: E501
        :type: str
        """

        self._broadcaster_text = broadcaster_text

    @property
    def broadcaster_desc(self):
        """Gets the broadcaster_desc of this Broadcaster.  # noqa: E501


        :return: The broadcaster_desc of this Broadcaster.  # noqa: E501
        :rtype: str
        """
        return self._broadcaster_desc

    @broadcaster_desc.setter
    def broadcaster_desc(self, broadcaster_desc):
        """Sets the broadcaster_desc of this Broadcaster.


        :param broadcaster_desc: The broadcaster_desc of this Broadcaster.  # noqa: E501
        :type: str
        """

        self._broadcaster_desc = broadcaster_desc

    @property
    def call_sign(self):
        """Gets the call_sign of this Broadcaster.  # noqa: E501


        :return: The call_sign of this Broadcaster.  # noqa: E501
        :rtype: str
        """
        return self._call_sign

    @call_sign.setter
    def call_sign(self, call_sign):
        """Sets the call_sign of this Broadcaster.


        :param call_sign: The call_sign of this Broadcaster.  # noqa: E501
        :type: str
        """

        self._call_sign = call_sign

    @property
    def broadcaster_type_id(self):
        """Gets the broadcaster_type_id of this Broadcaster.  # noqa: E501


        :return: The broadcaster_type_id of this Broadcaster.  # noqa: E501
        :rtype: int
        """
        return self._broadcaster_type_id

    @broadcaster_type_id.setter
    def broadcaster_type_id(self, broadcaster_type_id):
        """Sets the broadcaster_type_id of this Broadcaster.


        :param broadcaster_type_id: The broadcaster_type_id of this Broadcaster.  # noqa: E501
        :type: int
        """

        self._broadcaster_type_id = broadcaster_type_id

    @property
    def broadcaster_type_code(self):
        """Gets the broadcaster_type_code of this Broadcaster.  # noqa: E501


        :return: The broadcaster_type_code of this Broadcaster.  # noqa: E501
        :rtype: str
        """
        return self._broadcaster_type_code

    @broadcaster_type_code.setter
    def broadcaster_type_code(self, broadcaster_type_code):
        """Sets the broadcaster_type_code of this Broadcaster.


        :param broadcaster_type_code: The broadcaster_type_code of this Broadcaster.  # noqa: E501
        :type: str
        """

        self._broadcaster_type_code = broadcaster_type_code

    @property
    def broadcaster_type_text(self):
        """Gets the broadcaster_type_text of this Broadcaster.  # noqa: E501


        :return: The broadcaster_type_text of this Broadcaster.  # noqa: E501
        :rtype: str
        """
        return self._broadcaster_type_text

    @broadcaster_type_text.setter
    def broadcaster_type_text(self, broadcaster_type_text):
        """Sets the broadcaster_type_text of this Broadcaster.


        :param broadcaster_type_text: The broadcaster_type_text of this Broadcaster.  # noqa: E501
        :type: str
        """

        self._broadcaster_type_text = broadcaster_type_text

    @property
    def broadcaster_type_desc(self):
        """Gets the broadcaster_type_desc of this Broadcaster.  # noqa: E501


        :return: The broadcaster_type_desc of this Broadcaster.  # noqa: E501
        :rtype: str
        """
        return self._broadcaster_type_desc

    @broadcaster_type_desc.setter
    def broadcaster_type_desc(self, broadcaster_type_desc):
        """Sets the broadcaster_type_desc of this Broadcaster.


        :param broadcaster_type_desc: The broadcaster_type_desc of this Broadcaster.  # noqa: E501
        :type: str
        """

        self._broadcaster_type_desc = broadcaster_type_desc

    @property
    def broadcaster_comment(self):
        """Gets the broadcaster_comment of this Broadcaster.  # noqa: E501


        :return: The broadcaster_comment of this Broadcaster.  # noqa: E501
        :rtype: str
        """
        return self._broadcaster_comment

    @broadcaster_comment.setter
    def broadcaster_comment(self, broadcaster_comment):
        """Sets the broadcaster_comment of this Broadcaster.


        :param broadcaster_comment: The broadcaster_comment of this Broadcaster.  # noqa: E501
        :type: str
        """

        self._broadcaster_comment = broadcaster_comment

    @property
    def primary_team_id(self):
        """Gets the primary_team_id of this Broadcaster.  # noqa: E501


        :return: The primary_team_id of this Broadcaster.  # noqa: E501
        :rtype: int
        """
        return self._primary_team_id

    @primary_team_id.setter
    def primary_team_id(self, primary_team_id):
        """Sets the primary_team_id of this Broadcaster.


        :param primary_team_id: The primary_team_id of this Broadcaster.  # noqa: E501
        :type: int
        """

        self._primary_team_id = primary_team_id

    @property
    def broadcast_availability(self):
        """Gets the broadcast_availability of this Broadcaster.  # noqa: E501


        :return: The broadcast_availability of this Broadcaster.  # noqa: E501
        :rtype: BroadcastAvailability
        """
        return self._broadcast_availability

    @broadcast_availability.setter
    def broadcast_availability(self, broadcast_availability):
        """Sets the broadcast_availability of this Broadcaster.


        :param broadcast_availability: The broadcast_availability of this Broadcaster.  # noqa: E501
        :type: BroadcastAvailability
        """

        self._broadcast_availability = broadcast_availability

    @property
    def active_status(self):
        """Gets the active_status of this Broadcaster.  # noqa: E501


        :return: The active_status of this Broadcaster.  # noqa: E501
        :rtype: bool
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this Broadcaster.


        :param active_status: The active_status of this Broadcaster.  # noqa: E501
        :type: bool
        """

        self._active_status = active_status

    @property
    def is_national_status(self):
        """Gets the is_national_status of this Broadcaster.  # noqa: E501


        :return: The is_national_status of this Broadcaster.  # noqa: E501
        :rtype: bool
        """
        return self._is_national_status

    @is_national_status.setter
    def is_national_status(self, is_national_status):
        """Sets the is_national_status of this Broadcaster.


        :param is_national_status: The is_national_status of this Broadcaster.  # noqa: E501
        :type: bool
        """

        self._is_national_status = is_national_status

    @property
    def sort_order(self):
        """Gets the sort_order of this Broadcaster.  # noqa: E501


        :return: The sort_order of this Broadcaster.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this Broadcaster.


        :param sort_order: The sort_order of this Broadcaster.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def mvpd_auth_broadcast(self):
        """Gets the mvpd_auth_broadcast of this Broadcaster.  # noqa: E501


        :return: The mvpd_auth_broadcast of this Broadcaster.  # noqa: E501
        :rtype: bool
        """
        return self._mvpd_auth_broadcast

    @mvpd_auth_broadcast.setter
    def mvpd_auth_broadcast(self, mvpd_auth_broadcast):
        """Sets the mvpd_auth_broadcast of this Broadcaster.


        :param mvpd_auth_broadcast: The mvpd_auth_broadcast of this Broadcaster.  # noqa: E501
        :type: bool
        """

        self._mvpd_auth_broadcast = mvpd_auth_broadcast

    @property
    def language(self):
        """Gets the language of this Broadcaster.  # noqa: E501


        :return: The language of this Broadcaster.  # noqa: E501
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Broadcaster.


        :param language: The language of this Broadcaster.  # noqa: E501
        :type: Language
        """

        self._language = language

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
        if issubclass(Broadcaster, dict):
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
        if not isinstance(other, Broadcaster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other