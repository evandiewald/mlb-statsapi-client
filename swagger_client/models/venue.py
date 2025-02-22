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

class Venue(object):
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
        'name': 'str',
        'city': 'str',
        'location': 'Location',
        'time_zone': 'TimeZone',
        'field_info': 'FieldInfo',
        'sport_type': 'SportTypeEnum',
        'related_venues': 'list[Venue]',
        'parent_venues': 'list[Venue]',
        'resident_venues': 'list[Venue]',
        'related_applications': 'list[RelatedApplication]',
        'related_images': 'list[Image]',
        'social_media_info': 'SocialMediaInfo',
        'menu': 'VenueCms',
        'metadata': 'VenueMetadata',
        'schedule': 'BaseballSchedule',
        'next_schedule': 'BaseballSchedule',
        'previous_schedule': 'BaseballSchedule',
        'xref_ids': 'list[XrefId]',
        'season': 'str',
        'tracking_version': 'TrackingVersion',
        'tracking_system_owner': 'TrackingSystemOwner',
        'coaching_video': 'list[MediaSourceType]',
        'app_enabled': 'bool',
        'active': 'bool',
        'time_zone_id': 'str',
        'user_privileges': 'list[Privilege]'
    }

    attribute_map = {
        'requesting_user_role': 'requestingUserRole',
        'id': 'id',
        'name': 'name',
        'city': 'city',
        'location': 'location',
        'time_zone': 'timeZone',
        'field_info': 'fieldInfo',
        'sport_type': 'sportType',
        'related_venues': 'relatedVenues',
        'parent_venues': 'parentVenues',
        'resident_venues': 'residentVenues',
        'related_applications': 'relatedApplications',
        'related_images': 'relatedImages',
        'social_media_info': 'socialMediaInfo',
        'menu': 'menu',
        'metadata': 'metadata',
        'schedule': 'schedule',
        'next_schedule': 'nextSchedule',
        'previous_schedule': 'previousSchedule',
        'xref_ids': 'xrefIds',
        'season': 'season',
        'tracking_version': 'trackingVersion',
        'tracking_system_owner': 'trackingSystemOwner',
        'coaching_video': 'coachingVideo',
        'app_enabled': 'appEnabled',
        'active': 'active',
        'time_zone_id': 'timeZoneId',
        'user_privileges': 'userPrivileges'
    }

    def __init__(self, requesting_user_role=None, id=None, name=None, city=None, location=None, time_zone=None, field_info=None, sport_type=None, related_venues=None, parent_venues=None, resident_venues=None, related_applications=None, related_images=None, social_media_info=None, menu=None, metadata=None, schedule=None, next_schedule=None, previous_schedule=None, xref_ids=None, season=None, tracking_version=None, tracking_system_owner=None, coaching_video=None, app_enabled=None, active=None, time_zone_id=None, user_privileges=None):  # noqa: E501
        """Venue - a model defined in Swagger"""  # noqa: E501
        self._requesting_user_role = None
        self._id = None
        self._name = None
        self._city = None
        self._location = None
        self._time_zone = None
        self._field_info = None
        self._sport_type = None
        self._related_venues = None
        self._parent_venues = None
        self._resident_venues = None
        self._related_applications = None
        self._related_images = None
        self._social_media_info = None
        self._menu = None
        self._metadata = None
        self._schedule = None
        self._next_schedule = None
        self._previous_schedule = None
        self._xref_ids = None
        self._season = None
        self._tracking_version = None
        self._tracking_system_owner = None
        self._coaching_video = None
        self._app_enabled = None
        self._active = None
        self._time_zone_id = None
        self._user_privileges = None
        self.discriminator = None
        if requesting_user_role is not None:
            self.requesting_user_role = requesting_user_role
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if city is not None:
            self.city = city
        if location is not None:
            self.location = location
        if time_zone is not None:
            self.time_zone = time_zone
        if field_info is not None:
            self.field_info = field_info
        if sport_type is not None:
            self.sport_type = sport_type
        if related_venues is not None:
            self.related_venues = related_venues
        if parent_venues is not None:
            self.parent_venues = parent_venues
        if resident_venues is not None:
            self.resident_venues = resident_venues
        if related_applications is not None:
            self.related_applications = related_applications
        if related_images is not None:
            self.related_images = related_images
        if social_media_info is not None:
            self.social_media_info = social_media_info
        if menu is not None:
            self.menu = menu
        if metadata is not None:
            self.metadata = metadata
        if schedule is not None:
            self.schedule = schedule
        if next_schedule is not None:
            self.next_schedule = next_schedule
        if previous_schedule is not None:
            self.previous_schedule = previous_schedule
        if xref_ids is not None:
            self.xref_ids = xref_ids
        if season is not None:
            self.season = season
        if tracking_version is not None:
            self.tracking_version = tracking_version
        if tracking_system_owner is not None:
            self.tracking_system_owner = tracking_system_owner
        if coaching_video is not None:
            self.coaching_video = coaching_video
        if app_enabled is not None:
            self.app_enabled = app_enabled
        if active is not None:
            self.active = active
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if user_privileges is not None:
            self.user_privileges = user_privileges

    @property
    def requesting_user_role(self):
        """Gets the requesting_user_role of this Venue.  # noqa: E501


        :return: The requesting_user_role of this Venue.  # noqa: E501
        :rtype: Role
        """
        return self._requesting_user_role

    @requesting_user_role.setter
    def requesting_user_role(self, requesting_user_role):
        """Sets the requesting_user_role of this Venue.


        :param requesting_user_role: The requesting_user_role of this Venue.  # noqa: E501
        :type: Role
        """

        self._requesting_user_role = requesting_user_role

    @property
    def id(self):
        """Gets the id of this Venue.  # noqa: E501


        :return: The id of this Venue.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Venue.


        :param id: The id of this Venue.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Venue.  # noqa: E501


        :return: The name of this Venue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Venue.


        :param name: The name of this Venue.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def city(self):
        """Gets the city of this Venue.  # noqa: E501


        :return: The city of this Venue.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Venue.


        :param city: The city of this Venue.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def location(self):
        """Gets the location of this Venue.  # noqa: E501


        :return: The location of this Venue.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Venue.


        :param location: The location of this Venue.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def time_zone(self):
        """Gets the time_zone of this Venue.  # noqa: E501


        :return: The time_zone of this Venue.  # noqa: E501
        :rtype: TimeZone
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Venue.


        :param time_zone: The time_zone of this Venue.  # noqa: E501
        :type: TimeZone
        """

        self._time_zone = time_zone

    @property
    def field_info(self):
        """Gets the field_info of this Venue.  # noqa: E501


        :return: The field_info of this Venue.  # noqa: E501
        :rtype: FieldInfo
        """
        return self._field_info

    @field_info.setter
    def field_info(self, field_info):
        """Sets the field_info of this Venue.


        :param field_info: The field_info of this Venue.  # noqa: E501
        :type: FieldInfo
        """

        self._field_info = field_info

    @property
    def sport_type(self):
        """Gets the sport_type of this Venue.  # noqa: E501


        :return: The sport_type of this Venue.  # noqa: E501
        :rtype: SportTypeEnum
        """
        return self._sport_type

    @sport_type.setter
    def sport_type(self, sport_type):
        """Sets the sport_type of this Venue.


        :param sport_type: The sport_type of this Venue.  # noqa: E501
        :type: SportTypeEnum
        """

        self._sport_type = sport_type

    @property
    def related_venues(self):
        """Gets the related_venues of this Venue.  # noqa: E501


        :return: The related_venues of this Venue.  # noqa: E501
        :rtype: list[Venue]
        """
        return self._related_venues

    @related_venues.setter
    def related_venues(self, related_venues):
        """Sets the related_venues of this Venue.


        :param related_venues: The related_venues of this Venue.  # noqa: E501
        :type: list[Venue]
        """

        self._related_venues = related_venues

    @property
    def parent_venues(self):
        """Gets the parent_venues of this Venue.  # noqa: E501


        :return: The parent_venues of this Venue.  # noqa: E501
        :rtype: list[Venue]
        """
        return self._parent_venues

    @parent_venues.setter
    def parent_venues(self, parent_venues):
        """Sets the parent_venues of this Venue.


        :param parent_venues: The parent_venues of this Venue.  # noqa: E501
        :type: list[Venue]
        """

        self._parent_venues = parent_venues

    @property
    def resident_venues(self):
        """Gets the resident_venues of this Venue.  # noqa: E501


        :return: The resident_venues of this Venue.  # noqa: E501
        :rtype: list[Venue]
        """
        return self._resident_venues

    @resident_venues.setter
    def resident_venues(self, resident_venues):
        """Sets the resident_venues of this Venue.


        :param resident_venues: The resident_venues of this Venue.  # noqa: E501
        :type: list[Venue]
        """

        self._resident_venues = resident_venues

    @property
    def related_applications(self):
        """Gets the related_applications of this Venue.  # noqa: E501


        :return: The related_applications of this Venue.  # noqa: E501
        :rtype: list[RelatedApplication]
        """
        return self._related_applications

    @related_applications.setter
    def related_applications(self, related_applications):
        """Sets the related_applications of this Venue.


        :param related_applications: The related_applications of this Venue.  # noqa: E501
        :type: list[RelatedApplication]
        """

        self._related_applications = related_applications

    @property
    def related_images(self):
        """Gets the related_images of this Venue.  # noqa: E501


        :return: The related_images of this Venue.  # noqa: E501
        :rtype: list[Image]
        """
        return self._related_images

    @related_images.setter
    def related_images(self, related_images):
        """Sets the related_images of this Venue.


        :param related_images: The related_images of this Venue.  # noqa: E501
        :type: list[Image]
        """

        self._related_images = related_images

    @property
    def social_media_info(self):
        """Gets the social_media_info of this Venue.  # noqa: E501


        :return: The social_media_info of this Venue.  # noqa: E501
        :rtype: SocialMediaInfo
        """
        return self._social_media_info

    @social_media_info.setter
    def social_media_info(self, social_media_info):
        """Sets the social_media_info of this Venue.


        :param social_media_info: The social_media_info of this Venue.  # noqa: E501
        :type: SocialMediaInfo
        """

        self._social_media_info = social_media_info

    @property
    def menu(self):
        """Gets the menu of this Venue.  # noqa: E501


        :return: The menu of this Venue.  # noqa: E501
        :rtype: VenueCms
        """
        return self._menu

    @menu.setter
    def menu(self, menu):
        """Sets the menu of this Venue.


        :param menu: The menu of this Venue.  # noqa: E501
        :type: VenueCms
        """

        self._menu = menu

    @property
    def metadata(self):
        """Gets the metadata of this Venue.  # noqa: E501


        :return: The metadata of this Venue.  # noqa: E501
        :rtype: VenueMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Venue.


        :param metadata: The metadata of this Venue.  # noqa: E501
        :type: VenueMetadata
        """

        self._metadata = metadata

    @property
    def schedule(self):
        """Gets the schedule of this Venue.  # noqa: E501


        :return: The schedule of this Venue.  # noqa: E501
        :rtype: BaseballSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this Venue.


        :param schedule: The schedule of this Venue.  # noqa: E501
        :type: BaseballSchedule
        """

        self._schedule = schedule

    @property
    def next_schedule(self):
        """Gets the next_schedule of this Venue.  # noqa: E501


        :return: The next_schedule of this Venue.  # noqa: E501
        :rtype: BaseballSchedule
        """
        return self._next_schedule

    @next_schedule.setter
    def next_schedule(self, next_schedule):
        """Sets the next_schedule of this Venue.


        :param next_schedule: The next_schedule of this Venue.  # noqa: E501
        :type: BaseballSchedule
        """

        self._next_schedule = next_schedule

    @property
    def previous_schedule(self):
        """Gets the previous_schedule of this Venue.  # noqa: E501


        :return: The previous_schedule of this Venue.  # noqa: E501
        :rtype: BaseballSchedule
        """
        return self._previous_schedule

    @previous_schedule.setter
    def previous_schedule(self, previous_schedule):
        """Sets the previous_schedule of this Venue.


        :param previous_schedule: The previous_schedule of this Venue.  # noqa: E501
        :type: BaseballSchedule
        """

        self._previous_schedule = previous_schedule

    @property
    def xref_ids(self):
        """Gets the xref_ids of this Venue.  # noqa: E501


        :return: The xref_ids of this Venue.  # noqa: E501
        :rtype: list[XrefId]
        """
        return self._xref_ids

    @xref_ids.setter
    def xref_ids(self, xref_ids):
        """Sets the xref_ids of this Venue.


        :param xref_ids: The xref_ids of this Venue.  # noqa: E501
        :type: list[XrefId]
        """

        self._xref_ids = xref_ids

    @property
    def season(self):
        """Gets the season of this Venue.  # noqa: E501


        :return: The season of this Venue.  # noqa: E501
        :rtype: str
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Venue.


        :param season: The season of this Venue.  # noqa: E501
        :type: str
        """

        self._season = season

    @property
    def tracking_version(self):
        """Gets the tracking_version of this Venue.  # noqa: E501


        :return: The tracking_version of this Venue.  # noqa: E501
        :rtype: TrackingVersion
        """
        return self._tracking_version

    @tracking_version.setter
    def tracking_version(self, tracking_version):
        """Sets the tracking_version of this Venue.


        :param tracking_version: The tracking_version of this Venue.  # noqa: E501
        :type: TrackingVersion
        """

        self._tracking_version = tracking_version

    @property
    def tracking_system_owner(self):
        """Gets the tracking_system_owner of this Venue.  # noqa: E501


        :return: The tracking_system_owner of this Venue.  # noqa: E501
        :rtype: TrackingSystemOwner
        """
        return self._tracking_system_owner

    @tracking_system_owner.setter
    def tracking_system_owner(self, tracking_system_owner):
        """Sets the tracking_system_owner of this Venue.


        :param tracking_system_owner: The tracking_system_owner of this Venue.  # noqa: E501
        :type: TrackingSystemOwner
        """

        self._tracking_system_owner = tracking_system_owner

    @property
    def coaching_video(self):
        """Gets the coaching_video of this Venue.  # noqa: E501


        :return: The coaching_video of this Venue.  # noqa: E501
        :rtype: list[MediaSourceType]
        """
        return self._coaching_video

    @coaching_video.setter
    def coaching_video(self, coaching_video):
        """Sets the coaching_video of this Venue.


        :param coaching_video: The coaching_video of this Venue.  # noqa: E501
        :type: list[MediaSourceType]
        """

        self._coaching_video = coaching_video

    @property
    def app_enabled(self):
        """Gets the app_enabled of this Venue.  # noqa: E501


        :return: The app_enabled of this Venue.  # noqa: E501
        :rtype: bool
        """
        return self._app_enabled

    @app_enabled.setter
    def app_enabled(self, app_enabled):
        """Sets the app_enabled of this Venue.


        :param app_enabled: The app_enabled of this Venue.  # noqa: E501
        :type: bool
        """

        self._app_enabled = app_enabled

    @property
    def active(self):
        """Gets the active of this Venue.  # noqa: E501


        :return: The active of this Venue.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Venue.


        :param active: The active of this Venue.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this Venue.  # noqa: E501


        :return: The time_zone_id of this Venue.  # noqa: E501
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this Venue.


        :param time_zone_id: The time_zone_id of this Venue.  # noqa: E501
        :type: str
        """

        self._time_zone_id = time_zone_id

    @property
    def user_privileges(self):
        """Gets the user_privileges of this Venue.  # noqa: E501


        :return: The user_privileges of this Venue.  # noqa: E501
        :rtype: list[Privilege]
        """
        return self._user_privileges

    @user_privileges.setter
    def user_privileges(self, user_privileges):
        """Sets the user_privileges of this Venue.


        :param user_privileges: The user_privileges of this Venue.  # noqa: E501
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
        if issubclass(Venue, dict):
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
        if not isinstance(other, Venue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
