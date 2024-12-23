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

class PitchCodeRestObject(object):
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
        'code': 'str',
        'description': 'str',
        'swing_status': 'bool',
        'swing_miss_status': 'bool',
        'swing_contact_status': 'bool',
        'sort_order': 'int',
        'strike_status': 'bool',
        'ball_status': 'bool',
        'pitch_status': 'bool',
        'pitch_result_text': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'code': 'code',
        'description': 'description',
        'swing_status': 'swingStatus',
        'swing_miss_status': 'swingMissStatus',
        'swing_contact_status': 'swingContactStatus',
        'sort_order': 'sortOrder',
        'strike_status': 'strikeStatus',
        'ball_status': 'ballStatus',
        'pitch_status': 'pitchStatus',
        'pitch_result_text': 'pitchResultText'
    }

    def __init__(self, copyright=None, code=None, description=None, swing_status=None, swing_miss_status=None, swing_contact_status=None, sort_order=None, strike_status=None, ball_status=None, pitch_status=None, pitch_result_text=None):  # noqa: E501
        """PitchCodeRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._code = None
        self._description = None
        self._swing_status = None
        self._swing_miss_status = None
        self._swing_contact_status = None
        self._sort_order = None
        self._strike_status = None
        self._ball_status = None
        self._pitch_status = None
        self._pitch_result_text = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if swing_status is not None:
            self.swing_status = swing_status
        if swing_miss_status is not None:
            self.swing_miss_status = swing_miss_status
        if swing_contact_status is not None:
            self.swing_contact_status = swing_contact_status
        if sort_order is not None:
            self.sort_order = sort_order
        if strike_status is not None:
            self.strike_status = strike_status
        if ball_status is not None:
            self.ball_status = ball_status
        if pitch_status is not None:
            self.pitch_status = pitch_status
        if pitch_result_text is not None:
            self.pitch_result_text = pitch_result_text

    @property
    def copyright(self):
        """Gets the copyright of this PitchCodeRestObject.  # noqa: E501


        :return: The copyright of this PitchCodeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this PitchCodeRestObject.


        :param copyright: The copyright of this PitchCodeRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def code(self):
        """Gets the code of this PitchCodeRestObject.  # noqa: E501


        :return: The code of this PitchCodeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PitchCodeRestObject.


        :param code: The code of this PitchCodeRestObject.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this PitchCodeRestObject.  # noqa: E501


        :return: The description of this PitchCodeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PitchCodeRestObject.


        :param description: The description of this PitchCodeRestObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def swing_status(self):
        """Gets the swing_status of this PitchCodeRestObject.  # noqa: E501


        :return: The swing_status of this PitchCodeRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._swing_status

    @swing_status.setter
    def swing_status(self, swing_status):
        """Sets the swing_status of this PitchCodeRestObject.


        :param swing_status: The swing_status of this PitchCodeRestObject.  # noqa: E501
        :type: bool
        """

        self._swing_status = swing_status

    @property
    def swing_miss_status(self):
        """Gets the swing_miss_status of this PitchCodeRestObject.  # noqa: E501


        :return: The swing_miss_status of this PitchCodeRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._swing_miss_status

    @swing_miss_status.setter
    def swing_miss_status(self, swing_miss_status):
        """Sets the swing_miss_status of this PitchCodeRestObject.


        :param swing_miss_status: The swing_miss_status of this PitchCodeRestObject.  # noqa: E501
        :type: bool
        """

        self._swing_miss_status = swing_miss_status

    @property
    def swing_contact_status(self):
        """Gets the swing_contact_status of this PitchCodeRestObject.  # noqa: E501


        :return: The swing_contact_status of this PitchCodeRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._swing_contact_status

    @swing_contact_status.setter
    def swing_contact_status(self, swing_contact_status):
        """Sets the swing_contact_status of this PitchCodeRestObject.


        :param swing_contact_status: The swing_contact_status of this PitchCodeRestObject.  # noqa: E501
        :type: bool
        """

        self._swing_contact_status = swing_contact_status

    @property
    def sort_order(self):
        """Gets the sort_order of this PitchCodeRestObject.  # noqa: E501


        :return: The sort_order of this PitchCodeRestObject.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this PitchCodeRestObject.


        :param sort_order: The sort_order of this PitchCodeRestObject.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def strike_status(self):
        """Gets the strike_status of this PitchCodeRestObject.  # noqa: E501


        :return: The strike_status of this PitchCodeRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._strike_status

    @strike_status.setter
    def strike_status(self, strike_status):
        """Sets the strike_status of this PitchCodeRestObject.


        :param strike_status: The strike_status of this PitchCodeRestObject.  # noqa: E501
        :type: bool
        """

        self._strike_status = strike_status

    @property
    def ball_status(self):
        """Gets the ball_status of this PitchCodeRestObject.  # noqa: E501


        :return: The ball_status of this PitchCodeRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._ball_status

    @ball_status.setter
    def ball_status(self, ball_status):
        """Sets the ball_status of this PitchCodeRestObject.


        :param ball_status: The ball_status of this PitchCodeRestObject.  # noqa: E501
        :type: bool
        """

        self._ball_status = ball_status

    @property
    def pitch_status(self):
        """Gets the pitch_status of this PitchCodeRestObject.  # noqa: E501


        :return: The pitch_status of this PitchCodeRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._pitch_status

    @pitch_status.setter
    def pitch_status(self, pitch_status):
        """Sets the pitch_status of this PitchCodeRestObject.


        :param pitch_status: The pitch_status of this PitchCodeRestObject.  # noqa: E501
        :type: bool
        """

        self._pitch_status = pitch_status

    @property
    def pitch_result_text(self):
        """Gets the pitch_result_text of this PitchCodeRestObject.  # noqa: E501


        :return: The pitch_result_text of this PitchCodeRestObject.  # noqa: E501
        :rtype: str
        """
        return self._pitch_result_text

    @pitch_result_text.setter
    def pitch_result_text(self, pitch_result_text):
        """Sets the pitch_result_text of this PitchCodeRestObject.


        :param pitch_result_text: The pitch_result_text of this PitchCodeRestObject.  # noqa: E501
        :type: str
        """

        self._pitch_result_text = pitch_result_text

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
        if issubclass(PitchCodeRestObject, dict):
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
        if not isinstance(other, PitchCodeRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
