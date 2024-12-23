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

class StatSearchConfigRestObject(object):
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
        'parameters': 'list[StatSearchParamRestObject]',
        'group_by_types': 'list[StatSearchGroupByRestObject]',
        'compare_over_types': 'list[StatSearchGroupByRestObject]',
        'situation_codes': 'list[StatSearchSitCodeRestObject]',
        'stats': 'list[StatSearchStatRestObject]',
        'aggregations': 'list[AggregateSortTypeRestObject]',
        'filter_levels': 'list[FilterLevelEnumRestObject]',
        'person_filters': 'list[StatSearchPersonFilterRestObject]'
    }

    attribute_map = {
        'parameters': 'parameters',
        'group_by_types': 'groupByTypes',
        'compare_over_types': 'compareOverTypes',
        'situation_codes': 'situationCodes',
        'stats': 'stats',
        'aggregations': 'aggregations',
        'filter_levels': 'filterLevels',
        'person_filters': 'personFilters'
    }

    def __init__(self, parameters=None, group_by_types=None, compare_over_types=None, situation_codes=None, stats=None, aggregations=None, filter_levels=None, person_filters=None):  # noqa: E501
        """StatSearchConfigRestObject - a model defined in Swagger"""  # noqa: E501
        self._parameters = None
        self._group_by_types = None
        self._compare_over_types = None
        self._situation_codes = None
        self._stats = None
        self._aggregations = None
        self._filter_levels = None
        self._person_filters = None
        self.discriminator = None
        if parameters is not None:
            self.parameters = parameters
        if group_by_types is not None:
            self.group_by_types = group_by_types
        if compare_over_types is not None:
            self.compare_over_types = compare_over_types
        if situation_codes is not None:
            self.situation_codes = situation_codes
        if stats is not None:
            self.stats = stats
        if aggregations is not None:
            self.aggregations = aggregations
        if filter_levels is not None:
            self.filter_levels = filter_levels
        if person_filters is not None:
            self.person_filters = person_filters

    @property
    def parameters(self):
        """Gets the parameters of this StatSearchConfigRestObject.  # noqa: E501


        :return: The parameters of this StatSearchConfigRestObject.  # noqa: E501
        :rtype: list[StatSearchParamRestObject]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this StatSearchConfigRestObject.


        :param parameters: The parameters of this StatSearchConfigRestObject.  # noqa: E501
        :type: list[StatSearchParamRestObject]
        """

        self._parameters = parameters

    @property
    def group_by_types(self):
        """Gets the group_by_types of this StatSearchConfigRestObject.  # noqa: E501


        :return: The group_by_types of this StatSearchConfigRestObject.  # noqa: E501
        :rtype: list[StatSearchGroupByRestObject]
        """
        return self._group_by_types

    @group_by_types.setter
    def group_by_types(self, group_by_types):
        """Sets the group_by_types of this StatSearchConfigRestObject.


        :param group_by_types: The group_by_types of this StatSearchConfigRestObject.  # noqa: E501
        :type: list[StatSearchGroupByRestObject]
        """

        self._group_by_types = group_by_types

    @property
    def compare_over_types(self):
        """Gets the compare_over_types of this StatSearchConfigRestObject.  # noqa: E501


        :return: The compare_over_types of this StatSearchConfigRestObject.  # noqa: E501
        :rtype: list[StatSearchGroupByRestObject]
        """
        return self._compare_over_types

    @compare_over_types.setter
    def compare_over_types(self, compare_over_types):
        """Sets the compare_over_types of this StatSearchConfigRestObject.


        :param compare_over_types: The compare_over_types of this StatSearchConfigRestObject.  # noqa: E501
        :type: list[StatSearchGroupByRestObject]
        """

        self._compare_over_types = compare_over_types

    @property
    def situation_codes(self):
        """Gets the situation_codes of this StatSearchConfigRestObject.  # noqa: E501


        :return: The situation_codes of this StatSearchConfigRestObject.  # noqa: E501
        :rtype: list[StatSearchSitCodeRestObject]
        """
        return self._situation_codes

    @situation_codes.setter
    def situation_codes(self, situation_codes):
        """Sets the situation_codes of this StatSearchConfigRestObject.


        :param situation_codes: The situation_codes of this StatSearchConfigRestObject.  # noqa: E501
        :type: list[StatSearchSitCodeRestObject]
        """

        self._situation_codes = situation_codes

    @property
    def stats(self):
        """Gets the stats of this StatSearchConfigRestObject.  # noqa: E501


        :return: The stats of this StatSearchConfigRestObject.  # noqa: E501
        :rtype: list[StatSearchStatRestObject]
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this StatSearchConfigRestObject.


        :param stats: The stats of this StatSearchConfigRestObject.  # noqa: E501
        :type: list[StatSearchStatRestObject]
        """

        self._stats = stats

    @property
    def aggregations(self):
        """Gets the aggregations of this StatSearchConfigRestObject.  # noqa: E501


        :return: The aggregations of this StatSearchConfigRestObject.  # noqa: E501
        :rtype: list[AggregateSortTypeRestObject]
        """
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggregations):
        """Sets the aggregations of this StatSearchConfigRestObject.


        :param aggregations: The aggregations of this StatSearchConfigRestObject.  # noqa: E501
        :type: list[AggregateSortTypeRestObject]
        """

        self._aggregations = aggregations

    @property
    def filter_levels(self):
        """Gets the filter_levels of this StatSearchConfigRestObject.  # noqa: E501


        :return: The filter_levels of this StatSearchConfigRestObject.  # noqa: E501
        :rtype: list[FilterLevelEnumRestObject]
        """
        return self._filter_levels

    @filter_levels.setter
    def filter_levels(self, filter_levels):
        """Sets the filter_levels of this StatSearchConfigRestObject.


        :param filter_levels: The filter_levels of this StatSearchConfigRestObject.  # noqa: E501
        :type: list[FilterLevelEnumRestObject]
        """

        self._filter_levels = filter_levels

    @property
    def person_filters(self):
        """Gets the person_filters of this StatSearchConfigRestObject.  # noqa: E501


        :return: The person_filters of this StatSearchConfigRestObject.  # noqa: E501
        :rtype: list[StatSearchPersonFilterRestObject]
        """
        return self._person_filters

    @person_filters.setter
    def person_filters(self, person_filters):
        """Sets the person_filters of this StatSearchConfigRestObject.


        :param person_filters: The person_filters of this StatSearchConfigRestObject.  # noqa: E501
        :type: list[StatSearchPersonFilterRestObject]
        """

        self._person_filters = person_filters

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
        if issubclass(StatSearchConfigRestObject, dict):
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
        if not isinstance(other, StatSearchConfigRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
