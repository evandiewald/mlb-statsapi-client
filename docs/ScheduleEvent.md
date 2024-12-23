# ScheduleEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**event_type** | [**ScheduleEventTypes**](ScheduleEventTypes.md) |  | [optional] 
**event_date** | **datetime** |  | [optional] 
**calendar_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**end_date_time** | **datetime** |  | [optional] 
**images** | [**list[Image]**](Image.md) |  | [optional] 
**venue** | [**Venue**](Venue.md) |  | [optional] 
**sports** | [**list[Sport]**](Sport.md) |  | [optional] 
**leagues** | [**list[League]**](League.md) |  | [optional] 
**divisions** | [**list[Division]**](Division.md) |  | [optional] 
**organization_ids** | **list[int]** |  | [optional] 
**game** | [**BaseballScheduleItem**](BaseballScheduleItem.md) |  | [optional] 
**content** | [**ScheduleEventCms**](ScheduleEventCms.md) |  | [optional] 
**event_designations** | [**list[Designation]**](Designation.md) |  | [optional] 
**tickets** | [**list[BaseballTicket]**](BaseballTicket.md) |  | [optional] 
**promotion_tickets** | [**list[BaseballTicket]**](BaseballTicket.md) |  | [optional] 
**time_zone** | [**TimeZone**](TimeZone.md) |  | [optional] 
**event_status** | [**EventStatus**](EventStatus.md) |  | [optional] 
**team_id** | **int** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**organization_type** | **str** |  | [optional] 
**calendar_type** | [**CalendarTypes**](CalendarTypes.md) |  | [optional] 
**file_code** | **str** |  | [optional] 
**event_number** | **int** |  | [optional] 
**public_facing** | [**PublicFacingEnum**](PublicFacingEnum.md) |  | [optional] 
**teams** | [**list[BaseballTeam]**](BaseballTeam.md) |  | [optional] 
**tracking_version** | [**TrackingVersion**](TrackingVersion.md) |  | [optional] 
**tracking_system_owner** | [**TrackingSystemOwner**](TrackingSystemOwner.md) |  | [optional] 
**coaching_video** | [**list[MediaSourceType]**](MediaSourceType.md) |  | [optional] 
**broadcasts** | [**list[NonGameDateBroadcast]**](NonGameDateBroadcast.md) |  | [optional] 
**non_game_guid** | **str** |  | [optional] 
**multi_day** | **bool** |  | [optional] 
**primary_calendar** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

