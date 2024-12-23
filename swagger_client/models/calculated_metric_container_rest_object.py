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

class CalculatedMetricContainerRestObject(object):
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
        'metrics': 'list[CalculatedMetricRestObject]',
        'warnings': 'list[MetricWarningRestObject]',
        'invalid_metrics': 'list[CalculatedMetricRestObject]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'metrics': 'metrics',
        'warnings': 'warnings',
        'invalid_metrics': 'invalidMetrics'
    }

    def __init__(self, copyright=None, metrics=None, warnings=None, invalid_metrics=None):  # noqa: E501
        """CalculatedMetricContainerRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._metrics = None
        self._warnings = None
        self._invalid_metrics = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if metrics is not None:
            self.metrics = metrics
        if warnings is not None:
            self.warnings = warnings
        if invalid_metrics is not None:
            self.invalid_metrics = invalid_metrics

    @property
    def copyright(self):
        """Gets the copyright of this CalculatedMetricContainerRestObject.  # noqa: E501


        :return: The copyright of this CalculatedMetricContainerRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this CalculatedMetricContainerRestObject.


        :param copyright: The copyright of this CalculatedMetricContainerRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def metrics(self):
        """Gets the metrics of this CalculatedMetricContainerRestObject.  # noqa: E501


        :return: The metrics of this CalculatedMetricContainerRestObject.  # noqa: E501
        :rtype: list[CalculatedMetricRestObject]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this CalculatedMetricContainerRestObject.


        :param metrics: The metrics of this CalculatedMetricContainerRestObject.  # noqa: E501
        :type: list[CalculatedMetricRestObject]
        """

        self._metrics = metrics

    @property
    def warnings(self):
        """Gets the warnings of this CalculatedMetricContainerRestObject.  # noqa: E501


        :return: The warnings of this CalculatedMetricContainerRestObject.  # noqa: E501
        :rtype: list[MetricWarningRestObject]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this CalculatedMetricContainerRestObject.


        :param warnings: The warnings of this CalculatedMetricContainerRestObject.  # noqa: E501
        :type: list[MetricWarningRestObject]
        """

        self._warnings = warnings

    @property
    def invalid_metrics(self):
        """Gets the invalid_metrics of this CalculatedMetricContainerRestObject.  # noqa: E501


        :return: The invalid_metrics of this CalculatedMetricContainerRestObject.  # noqa: E501
        :rtype: list[CalculatedMetricRestObject]
        """
        return self._invalid_metrics

    @invalid_metrics.setter
    def invalid_metrics(self, invalid_metrics):
        """Sets the invalid_metrics of this CalculatedMetricContainerRestObject.


        :param invalid_metrics: The invalid_metrics of this CalculatedMetricContainerRestObject.  # noqa: E501
        :type: list[CalculatedMetricRestObject]
        """

        self._invalid_metrics = invalid_metrics

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
        if issubclass(CalculatedMetricContainerRestObject, dict):
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
        if not isinstance(other, CalculatedMetricContainerRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other