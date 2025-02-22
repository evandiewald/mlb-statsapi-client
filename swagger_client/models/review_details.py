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

class ReviewDetails(object):
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
        'is_overturned': 'bool',
        'in_progress': 'bool',
        'review_type': 'str',
        'challenge_team_id': 'int',
        'additional_reviews': 'list[ReviewDetails]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'is_overturned': 'isOverturned',
        'in_progress': 'inProgress',
        'review_type': 'reviewType',
        'challenge_team_id': 'challengeTeamId',
        'additional_reviews': 'additionalReviews'
    }

    def __init__(self, copyright=None, is_overturned=None, in_progress=None, review_type=None, challenge_team_id=None, additional_reviews=None):  # noqa: E501
        """ReviewDetails - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._is_overturned = None
        self._in_progress = None
        self._review_type = None
        self._challenge_team_id = None
        self._additional_reviews = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if is_overturned is not None:
            self.is_overturned = is_overturned
        if in_progress is not None:
            self.in_progress = in_progress
        if review_type is not None:
            self.review_type = review_type
        if challenge_team_id is not None:
            self.challenge_team_id = challenge_team_id
        if additional_reviews is not None:
            self.additional_reviews = additional_reviews

    @property
    def copyright(self):
        """Gets the copyright of this ReviewDetails.  # noqa: E501


        :return: The copyright of this ReviewDetails.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this ReviewDetails.


        :param copyright: The copyright of this ReviewDetails.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def is_overturned(self):
        """Gets the is_overturned of this ReviewDetails.  # noqa: E501


        :return: The is_overturned of this ReviewDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_overturned

    @is_overturned.setter
    def is_overturned(self, is_overturned):
        """Sets the is_overturned of this ReviewDetails.


        :param is_overturned: The is_overturned of this ReviewDetails.  # noqa: E501
        :type: bool
        """

        self._is_overturned = is_overturned

    @property
    def in_progress(self):
        """Gets the in_progress of this ReviewDetails.  # noqa: E501


        :return: The in_progress of this ReviewDetails.  # noqa: E501
        :rtype: bool
        """
        return self._in_progress

    @in_progress.setter
    def in_progress(self, in_progress):
        """Sets the in_progress of this ReviewDetails.


        :param in_progress: The in_progress of this ReviewDetails.  # noqa: E501
        :type: bool
        """

        self._in_progress = in_progress

    @property
    def review_type(self):
        """Gets the review_type of this ReviewDetails.  # noqa: E501


        :return: The review_type of this ReviewDetails.  # noqa: E501
        :rtype: str
        """
        return self._review_type

    @review_type.setter
    def review_type(self, review_type):
        """Sets the review_type of this ReviewDetails.


        :param review_type: The review_type of this ReviewDetails.  # noqa: E501
        :type: str
        """

        self._review_type = review_type

    @property
    def challenge_team_id(self):
        """Gets the challenge_team_id of this ReviewDetails.  # noqa: E501


        :return: The challenge_team_id of this ReviewDetails.  # noqa: E501
        :rtype: int
        """
        return self._challenge_team_id

    @challenge_team_id.setter
    def challenge_team_id(self, challenge_team_id):
        """Sets the challenge_team_id of this ReviewDetails.


        :param challenge_team_id: The challenge_team_id of this ReviewDetails.  # noqa: E501
        :type: int
        """

        self._challenge_team_id = challenge_team_id

    @property
    def additional_reviews(self):
        """Gets the additional_reviews of this ReviewDetails.  # noqa: E501


        :return: The additional_reviews of this ReviewDetails.  # noqa: E501
        :rtype: list[ReviewDetails]
        """
        return self._additional_reviews

    @additional_reviews.setter
    def additional_reviews(self, additional_reviews):
        """Sets the additional_reviews of this ReviewDetails.


        :param additional_reviews: The additional_reviews of this ReviewDetails.  # noqa: E501
        :type: list[ReviewDetails]
        """

        self._additional_reviews = additional_reviews

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
        if issubclass(ReviewDetails, dict):
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
        if not isinstance(other, ReviewDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
