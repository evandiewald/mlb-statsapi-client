# ScheduleEventRestObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**non_game_guid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**event_type** | [**ScheduleEventTypeRestObject**](ScheduleEventTypeRestObject.md) |  | [optional] 
**event_date** | **datetime** |  | [optional] 
**end_date_time** | **datetime** |  | [optional] 
**images** | [**list[ImageRestObject]**](ImageRestObject.md) |  | [optional] 
**venue** | [**VenueRestObject**](VenueRestObject.md) |  | [optional] 
**sports** | [**list[SportRestObject]**](SportRestObject.md) |  | [optional] 
**leagues** | [**list[LeagueRestObject]**](LeagueRestObject.md) |  | [optional] 
**divisions** | [**list[DivisionRestObject]**](DivisionRestObject.md) |  | [optional] 
**game** | [**BaseballScheduleItemRestObject**](BaseballScheduleItemRestObject.md) |  | [optional] 
**content** | [**ScheduleEventCms**](ScheduleEventCms.md) |  | [optional] 
**time_zone** | [**TimeZoneRestObject**](TimeZoneRestObject.md) |  | [optional] 
**designations** | [**list[DesignationRestObject]**](DesignationRestObject.md) |  | [optional] 
**tickets** | [**list[BaseballTicketRestObject]**](BaseballTicketRestObject.md) |  | [optional] 
**promotions** | [**list[BaseballTicketRestObject]**](BaseballTicketRestObject.md) |  | [optional] 
**event_status** | [**GameStatusRestObject**](GameStatusRestObject.md) |  | [optional] 
**is_multi_day** | **bool** |  | [optional] 
**is_primary_calendar** | **bool** |  | [optional] 
**file_code** | **str** |  | [optional] 
**event_number** | **int** |  | [optional] 
**public_facing** | **bool** |  | [optional] 
**teams** | [**list[BaseballTeamRestObject]**](BaseballTeamRestObject.md) |  | [optional] 
**tracking_version** | [**TrackingVersionRestObject**](TrackingVersionRestObject.md) |  | [optional] 
**coaching_video** | [**list[MediaSourceType]**](MediaSourceType.md) |  | [optional] 
**rule_settings** | [**list[RuleSettingsRestObject]**](RuleSettingsRestObject.md) |  | [optional] 
**broadcasts** | [**list[NonGameBroadcastRestObject]**](NonGameBroadcastRestObject.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

