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

class MilestoneRuleRestObject(object):
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
        'milestone_rule_id': 'int',
        'milestone_value': 'int',
        'milestone_rank': 'int',
        'game_type_code': 'str',
        'org_type': 'OrganizationTypeRestObject',
        'milestone_type': 'MilestoneTypeRestObject',
        'milestone_duration': 'MilestoneDurationRestObject',
        'milestone_statistic': 'MilestoneStatisticRestObject'
    }

    attribute_map = {
        'copyright': 'copyright',
        'milestone_rule_id': 'milestoneRuleId',
        'milestone_value': 'milestoneValue',
        'milestone_rank': 'milestoneRank',
        'game_type_code': 'gameTypeCode',
        'org_type': 'orgType',
        'milestone_type': 'milestoneType',
        'milestone_duration': 'milestoneDuration',
        'milestone_statistic': 'milestoneStatistic'
    }

    def __init__(self, copyright=None, milestone_rule_id=None, milestone_value=None, milestone_rank=None, game_type_code=None, org_type=None, milestone_type=None, milestone_duration=None, milestone_statistic=None):  # noqa: E501
        """MilestoneRuleRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._milestone_rule_id = None
        self._milestone_value = None
        self._milestone_rank = None
        self._game_type_code = None
        self._org_type = None
        self._milestone_type = None
        self._milestone_duration = None
        self._milestone_statistic = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if milestone_rule_id is not None:
            self.milestone_rule_id = milestone_rule_id
        if milestone_value is not None:
            self.milestone_value = milestone_value
        if milestone_rank is not None:
            self.milestone_rank = milestone_rank
        if game_type_code is not None:
            self.game_type_code = game_type_code
        if org_type is not None:
            self.org_type = org_type
        if milestone_type is not None:
            self.milestone_type = milestone_type
        if milestone_duration is not None:
            self.milestone_duration = milestone_duration
        if milestone_statistic is not None:
            self.milestone_statistic = milestone_statistic

    @property
    def copyright(self):
        """Gets the copyright of this MilestoneRuleRestObject.  # noqa: E501


        :return: The copyright of this MilestoneRuleRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this MilestoneRuleRestObject.


        :param copyright: The copyright of this MilestoneRuleRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def milestone_rule_id(self):
        """Gets the milestone_rule_id of this MilestoneRuleRestObject.  # noqa: E501


        :return: The milestone_rule_id of this MilestoneRuleRestObject.  # noqa: E501
        :rtype: int
        """
        return self._milestone_rule_id

    @milestone_rule_id.setter
    def milestone_rule_id(self, milestone_rule_id):
        """Sets the milestone_rule_id of this MilestoneRuleRestObject.


        :param milestone_rule_id: The milestone_rule_id of this MilestoneRuleRestObject.  # noqa: E501
        :type: int
        """

        self._milestone_rule_id = milestone_rule_id

    @property
    def milestone_value(self):
        """Gets the milestone_value of this MilestoneRuleRestObject.  # noqa: E501


        :return: The milestone_value of this MilestoneRuleRestObject.  # noqa: E501
        :rtype: int
        """
        return self._milestone_value

    @milestone_value.setter
    def milestone_value(self, milestone_value):
        """Sets the milestone_value of this MilestoneRuleRestObject.


        :param milestone_value: The milestone_value of this MilestoneRuleRestObject.  # noqa: E501
        :type: int
        """

        self._milestone_value = milestone_value

    @property
    def milestone_rank(self):
        """Gets the milestone_rank of this MilestoneRuleRestObject.  # noqa: E501


        :return: The milestone_rank of this MilestoneRuleRestObject.  # noqa: E501
        :rtype: int
        """
        return self._milestone_rank

    @milestone_rank.setter
    def milestone_rank(self, milestone_rank):
        """Sets the milestone_rank of this MilestoneRuleRestObject.


        :param milestone_rank: The milestone_rank of this MilestoneRuleRestObject.  # noqa: E501
        :type: int
        """

        self._milestone_rank = milestone_rank

    @property
    def game_type_code(self):
        """Gets the game_type_code of this MilestoneRuleRestObject.  # noqa: E501


        :return: The game_type_code of this MilestoneRuleRestObject.  # noqa: E501
        :rtype: str
        """
        return self._game_type_code

    @game_type_code.setter
    def game_type_code(self, game_type_code):
        """Sets the game_type_code of this MilestoneRuleRestObject.


        :param game_type_code: The game_type_code of this MilestoneRuleRestObject.  # noqa: E501
        :type: str
        """

        self._game_type_code = game_type_code

    @property
    def org_type(self):
        """Gets the org_type of this MilestoneRuleRestObject.  # noqa: E501


        :return: The org_type of this MilestoneRuleRestObject.  # noqa: E501
        :rtype: OrganizationTypeRestObject
        """
        return self._org_type

    @org_type.setter
    def org_type(self, org_type):
        """Sets the org_type of this MilestoneRuleRestObject.


        :param org_type: The org_type of this MilestoneRuleRestObject.  # noqa: E501
        :type: OrganizationTypeRestObject
        """

        self._org_type = org_type

    @property
    def milestone_type(self):
        """Gets the milestone_type of this MilestoneRuleRestObject.  # noqa: E501


        :return: The milestone_type of this MilestoneRuleRestObject.  # noqa: E501
        :rtype: MilestoneTypeRestObject
        """
        return self._milestone_type

    @milestone_type.setter
    def milestone_type(self, milestone_type):
        """Sets the milestone_type of this MilestoneRuleRestObject.


        :param milestone_type: The milestone_type of this MilestoneRuleRestObject.  # noqa: E501
        :type: MilestoneTypeRestObject
        """

        self._milestone_type = milestone_type

    @property
    def milestone_duration(self):
        """Gets the milestone_duration of this MilestoneRuleRestObject.  # noqa: E501


        :return: The milestone_duration of this MilestoneRuleRestObject.  # noqa: E501
        :rtype: MilestoneDurationRestObject
        """
        return self._milestone_duration

    @milestone_duration.setter
    def milestone_duration(self, milestone_duration):
        """Sets the milestone_duration of this MilestoneRuleRestObject.


        :param milestone_duration: The milestone_duration of this MilestoneRuleRestObject.  # noqa: E501
        :type: MilestoneDurationRestObject
        """

        self._milestone_duration = milestone_duration

    @property
    def milestone_statistic(self):
        """Gets the milestone_statistic of this MilestoneRuleRestObject.  # noqa: E501


        :return: The milestone_statistic of this MilestoneRuleRestObject.  # noqa: E501
        :rtype: MilestoneStatisticRestObject
        """
        return self._milestone_statistic

    @milestone_statistic.setter
    def milestone_statistic(self, milestone_statistic):
        """Sets the milestone_statistic of this MilestoneRuleRestObject.


        :param milestone_statistic: The milestone_statistic of this MilestoneRuleRestObject.  # noqa: E501
        :type: MilestoneStatisticRestObject
        """

        self._milestone_statistic = milestone_statistic

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
        if issubclass(MilestoneRuleRestObject, dict):
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
        if not isinstance(other, MilestoneRuleRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
