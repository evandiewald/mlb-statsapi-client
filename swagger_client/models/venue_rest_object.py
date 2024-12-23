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

class VenueRestObject(object):
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
        'id': 'int',
        'name': 'str',
        'link': 'str',
        'location': 'LocationRestObject',
        'time_zone': 'TimeZoneRestObject',
        'field_info': 'FieldInfoRestObject',
        'related_applications': 'list[ApplicationRestObject]',
        'images': 'dict(str, ImageRestObject)',
        'social': 'SocialMediaRestObject',
        'menu': 'JsonNode',
        'schedule': 'ScheduleRestObject',
        'next_schedule': 'ScheduleRestObject',
        'previous_schedule': 'ScheduleRestObject',
        'metadata': 'VenueMetadataRestObject',
        'app_enabled': 'bool',
        'xref_ids': 'list[XrefIdRestObject]',
        'tracking_version': 'TrackingVersionRestObject',
        'coaching_video': 'list[MediaSourceType]',
        'rule_settings': 'list[RuleSettingsRestObject]',
        'active': 'bool',
        'season': 'str'
    }

    attribute_map = {
        'copyright': 'copyright',
        'hydrations': 'hydrations',
        'id': 'id',
        'name': 'name',
        'link': 'link',
        'location': 'location',
        'time_zone': 'timeZone',
        'field_info': 'fieldInfo',
        'related_applications': 'relatedApplications',
        'images': 'images',
        'social': 'social',
        'menu': 'menu',
        'schedule': 'schedule',
        'next_schedule': 'nextSchedule',
        'previous_schedule': 'previousSchedule',
        'metadata': 'metadata',
        'app_enabled': 'appEnabled',
        'xref_ids': 'xrefIds',
        'tracking_version': 'trackingVersion',
        'coaching_video': 'coachingVideo',
        'rule_settings': 'ruleSettings',
        'active': 'active',
        'season': 'season'
    }

    def __init__(self, copyright=None, hydrations=None, id=None, name=None, link=None, location=None, time_zone=None, field_info=None, related_applications=None, images=None, social=None, menu=None, schedule=None, next_schedule=None, previous_schedule=None, metadata=None, app_enabled=None, xref_ids=None, tracking_version=None, coaching_video=None, rule_settings=None, active=None, season=None):  # noqa: E501
        """VenueRestObject - a model defined in Swagger"""  # noqa: E501
        self._copyright = None
        self._hydrations = None
        self._id = None
        self._name = None
        self._link = None
        self._location = None
        self._time_zone = None
        self._field_info = None
        self._related_applications = None
        self._images = None
        self._social = None
        self._menu = None
        self._schedule = None
        self._next_schedule = None
        self._previous_schedule = None
        self._metadata = None
        self._app_enabled = None
        self._xref_ids = None
        self._tracking_version = None
        self._coaching_video = None
        self._rule_settings = None
        self._active = None
        self._season = None
        self.discriminator = None
        if copyright is not None:
            self.copyright = copyright
        if hydrations is not None:
            self.hydrations = hydrations
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if link is not None:
            self.link = link
        if location is not None:
            self.location = location
        if time_zone is not None:
            self.time_zone = time_zone
        if field_info is not None:
            self.field_info = field_info
        if related_applications is not None:
            self.related_applications = related_applications
        if images is not None:
            self.images = images
        if social is not None:
            self.social = social
        if menu is not None:
            self.menu = menu
        if schedule is not None:
            self.schedule = schedule
        if next_schedule is not None:
            self.next_schedule = next_schedule
        if previous_schedule is not None:
            self.previous_schedule = previous_schedule
        if metadata is not None:
            self.metadata = metadata
        if app_enabled is not None:
            self.app_enabled = app_enabled
        if xref_ids is not None:
            self.xref_ids = xref_ids
        if tracking_version is not None:
            self.tracking_version = tracking_version
        if coaching_video is not None:
            self.coaching_video = coaching_video
        if rule_settings is not None:
            self.rule_settings = rule_settings
        if active is not None:
            self.active = active
        if season is not None:
            self.season = season

    @property
    def copyright(self):
        """Gets the copyright of this VenueRestObject.  # noqa: E501


        :return: The copyright of this VenueRestObject.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this VenueRestObject.


        :param copyright: The copyright of this VenueRestObject.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def hydrations(self):
        """Gets the hydrations of this VenueRestObject.  # noqa: E501


        :return: The hydrations of this VenueRestObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._hydrations

    @hydrations.setter
    def hydrations(self, hydrations):
        """Sets the hydrations of this VenueRestObject.


        :param hydrations: The hydrations of this VenueRestObject.  # noqa: E501
        :type: list[str]
        """

        self._hydrations = hydrations

    @property
    def id(self):
        """Gets the id of this VenueRestObject.  # noqa: E501


        :return: The id of this VenueRestObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VenueRestObject.


        :param id: The id of this VenueRestObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VenueRestObject.  # noqa: E501


        :return: The name of this VenueRestObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VenueRestObject.


        :param name: The name of this VenueRestObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def link(self):
        """Gets the link of this VenueRestObject.  # noqa: E501


        :return: The link of this VenueRestObject.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this VenueRestObject.


        :param link: The link of this VenueRestObject.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def location(self):
        """Gets the location of this VenueRestObject.  # noqa: E501


        :return: The location of this VenueRestObject.  # noqa: E501
        :rtype: LocationRestObject
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this VenueRestObject.


        :param location: The location of this VenueRestObject.  # noqa: E501
        :type: LocationRestObject
        """

        self._location = location

    @property
    def time_zone(self):
        """Gets the time_zone of this VenueRestObject.  # noqa: E501


        :return: The time_zone of this VenueRestObject.  # noqa: E501
        :rtype: TimeZoneRestObject
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this VenueRestObject.


        :param time_zone: The time_zone of this VenueRestObject.  # noqa: E501
        :type: TimeZoneRestObject
        """

        self._time_zone = time_zone

    @property
    def field_info(self):
        """Gets the field_info of this VenueRestObject.  # noqa: E501


        :return: The field_info of this VenueRestObject.  # noqa: E501
        :rtype: FieldInfoRestObject
        """
        return self._field_info

    @field_info.setter
    def field_info(self, field_info):
        """Sets the field_info of this VenueRestObject.


        :param field_info: The field_info of this VenueRestObject.  # noqa: E501
        :type: FieldInfoRestObject
        """

        self._field_info = field_info

    @property
    def related_applications(self):
        """Gets the related_applications of this VenueRestObject.  # noqa: E501


        :return: The related_applications of this VenueRestObject.  # noqa: E501
        :rtype: list[ApplicationRestObject]
        """
        return self._related_applications

    @related_applications.setter
    def related_applications(self, related_applications):
        """Sets the related_applications of this VenueRestObject.


        :param related_applications: The related_applications of this VenueRestObject.  # noqa: E501
        :type: list[ApplicationRestObject]
        """

        self._related_applications = related_applications

    @property
    def images(self):
        """Gets the images of this VenueRestObject.  # noqa: E501


        :return: The images of this VenueRestObject.  # noqa: E501
        :rtype: dict(str, ImageRestObject)
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this VenueRestObject.


        :param images: The images of this VenueRestObject.  # noqa: E501
        :type: dict(str, ImageRestObject)
        """

        self._images = images

    @property
    def social(self):
        """Gets the social of this VenueRestObject.  # noqa: E501


        :return: The social of this VenueRestObject.  # noqa: E501
        :rtype: SocialMediaRestObject
        """
        return self._social

    @social.setter
    def social(self, social):
        """Sets the social of this VenueRestObject.


        :param social: The social of this VenueRestObject.  # noqa: E501
        :type: SocialMediaRestObject
        """

        self._social = social

    @property
    def menu(self):
        """Gets the menu of this VenueRestObject.  # noqa: E501


        :return: The menu of this VenueRestObject.  # noqa: E501
        :rtype: JsonNode
        """
        return self._menu

    @menu.setter
    def menu(self, menu):
        """Sets the menu of this VenueRestObject.


        :param menu: The menu of this VenueRestObject.  # noqa: E501
        :type: JsonNode
        """

        self._menu = menu

    @property
    def schedule(self):
        """Gets the schedule of this VenueRestObject.  # noqa: E501


        :return: The schedule of this VenueRestObject.  # noqa: E501
        :rtype: ScheduleRestObject
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this VenueRestObject.


        :param schedule: The schedule of this VenueRestObject.  # noqa: E501
        :type: ScheduleRestObject
        """

        self._schedule = schedule

    @property
    def next_schedule(self):
        """Gets the next_schedule of this VenueRestObject.  # noqa: E501


        :return: The next_schedule of this VenueRestObject.  # noqa: E501
        :rtype: ScheduleRestObject
        """
        return self._next_schedule

    @next_schedule.setter
    def next_schedule(self, next_schedule):
        """Sets the next_schedule of this VenueRestObject.


        :param next_schedule: The next_schedule of this VenueRestObject.  # noqa: E501
        :type: ScheduleRestObject
        """

        self._next_schedule = next_schedule

    @property
    def previous_schedule(self):
        """Gets the previous_schedule of this VenueRestObject.  # noqa: E501


        :return: The previous_schedule of this VenueRestObject.  # noqa: E501
        :rtype: ScheduleRestObject
        """
        return self._previous_schedule

    @previous_schedule.setter
    def previous_schedule(self, previous_schedule):
        """Sets the previous_schedule of this VenueRestObject.


        :param previous_schedule: The previous_schedule of this VenueRestObject.  # noqa: E501
        :type: ScheduleRestObject
        """

        self._previous_schedule = previous_schedule

    @property
    def metadata(self):
        """Gets the metadata of this VenueRestObject.  # noqa: E501


        :return: The metadata of this VenueRestObject.  # noqa: E501
        :rtype: VenueMetadataRestObject
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this VenueRestObject.


        :param metadata: The metadata of this VenueRestObject.  # noqa: E501
        :type: VenueMetadataRestObject
        """

        self._metadata = metadata

    @property
    def app_enabled(self):
        """Gets the app_enabled of this VenueRestObject.  # noqa: E501


        :return: The app_enabled of this VenueRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._app_enabled

    @app_enabled.setter
    def app_enabled(self, app_enabled):
        """Sets the app_enabled of this VenueRestObject.


        :param app_enabled: The app_enabled of this VenueRestObject.  # noqa: E501
        :type: bool
        """

        self._app_enabled = app_enabled

    @property
    def xref_ids(self):
        """Gets the xref_ids of this VenueRestObject.  # noqa: E501


        :return: The xref_ids of this VenueRestObject.  # noqa: E501
        :rtype: list[XrefIdRestObject]
        """
        return self._xref_ids

    @xref_ids.setter
    def xref_ids(self, xref_ids):
        """Sets the xref_ids of this VenueRestObject.


        :param xref_ids: The xref_ids of this VenueRestObject.  # noqa: E501
        :type: list[XrefIdRestObject]
        """

        self._xref_ids = xref_ids

    @property
    def tracking_version(self):
        """Gets the tracking_version of this VenueRestObject.  # noqa: E501


        :return: The tracking_version of this VenueRestObject.  # noqa: E501
        :rtype: TrackingVersionRestObject
        """
        return self._tracking_version

    @tracking_version.setter
    def tracking_version(self, tracking_version):
        """Sets the tracking_version of this VenueRestObject.


        :param tracking_version: The tracking_version of this VenueRestObject.  # noqa: E501
        :type: TrackingVersionRestObject
        """

        self._tracking_version = tracking_version

    @property
    def coaching_video(self):
        """Gets the coaching_video of this VenueRestObject.  # noqa: E501


        :return: The coaching_video of this VenueRestObject.  # noqa: E501
        :rtype: list[MediaSourceType]
        """
        return self._coaching_video

    @coaching_video.setter
    def coaching_video(self, coaching_video):
        """Sets the coaching_video of this VenueRestObject.


        :param coaching_video: The coaching_video of this VenueRestObject.  # noqa: E501
        :type: list[MediaSourceType]
        """

        self._coaching_video = coaching_video

    @property
    def rule_settings(self):
        """Gets the rule_settings of this VenueRestObject.  # noqa: E501


        :return: The rule_settings of this VenueRestObject.  # noqa: E501
        :rtype: list[RuleSettingsRestObject]
        """
        return self._rule_settings

    @rule_settings.setter
    def rule_settings(self, rule_settings):
        """Sets the rule_settings of this VenueRestObject.


        :param rule_settings: The rule_settings of this VenueRestObject.  # noqa: E501
        :type: list[RuleSettingsRestObject]
        """

        self._rule_settings = rule_settings

    @property
    def active(self):
        """Gets the active of this VenueRestObject.  # noqa: E501


        :return: The active of this VenueRestObject.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this VenueRestObject.


        :param active: The active of this VenueRestObject.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def season(self):
        """Gets the season of this VenueRestObject.  # noqa: E501


        :return: The season of this VenueRestObject.  # noqa: E501
        :rtype: str
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this VenueRestObject.


        :param season: The season of this VenueRestObject.  # noqa: E501
        :type: str
        """

        self._season = season

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
        if issubclass(VenueRestObject, dict):
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
        if not isinstance(other, VenueRestObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other