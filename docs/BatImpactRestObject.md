# BatImpactRestObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**attack_angle** | **float** | The angle of the bat&#x27;s path, at impact, relative to horizontal. A negative value represents swinging downward, a positive value upward. | [optional] 
**speed** | [**BatImpactSpeedRestObject**](BatImpactSpeedRestObject.md) |  | [optional] 
**contact_point** | [**ContactPointPositionRestObject**](ContactPointPositionRestObject.md) |  | [optional] 
**head_position** | [**HeadPositionRestObject**](HeadPositionRestObject.md) |  | [optional] 
**handle_position** | [**HandlePositionRestObject**](HandlePositionRestObject.md) |  | [optional] 
**velocity** | [**BatImpactVelocityRestObject**](BatImpactVelocityRestObject.md) |  | [optional] 
**time_stamp** | **str** | TimeStamp when bat and ball either intersect in case of contact, or in cases where they don’t collide, timeStamp where ball is closest to any point along the bat. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

