# swagger_client.MilestonesApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**achievement_statuses**](MilestonesApi.md#achievement_statuses) | **GET** /api/v1/achievementStatuses | View available achievementStatus options
[**milestone_durations**](MilestonesApi.md#milestone_durations) | **GET** /api/v1/milestoneDurations | View available milestoneDurations options
[**milestone_lookups**](MilestonesApi.md#milestone_lookups) | **GET** /api/v1/milestoneLookups | View available milestoneLookup options
[**milestone_statistics**](MilestonesApi.md#milestone_statistics) | **GET** /api/v1/milestoneStatistics | View available milestone statistics options
[**milestone_types**](MilestonesApi.md#milestone_types) | **GET** /api/v1/milestoneTypes | View available milestoneType options
[**milestones**](MilestonesApi.md#milestones) | **GET** /api/v1/milestones | View pending and achieved milestones.

# **achievement_statuses**
> list[MilestoneAchievementType] achievement_statuses()

View available achievementStatus options

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MilestonesApi()

try:
    # View available achievementStatus options
    api_response = api_instance.achievement_statuses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MilestonesApi->achievement_statuses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MilestoneAchievementType]**](MilestoneAchievementType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **milestone_durations**
> list[MilestoneDuration] milestone_durations()

View available milestoneDurations options

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MilestonesApi()

try:
    # View available milestoneDurations options
    api_response = api_instance.milestone_durations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MilestonesApi->milestone_durations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MilestoneDuration]**](MilestoneDuration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **milestone_lookups**
> dict(str, list[object]) milestone_lookups()

View available milestoneLookup options

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MilestonesApi()

try:
    # View available milestoneLookup options
    api_response = api_instance.milestone_lookups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MilestonesApi->milestone_lookups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, list[object])**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **milestone_statistics**
> list[MilestoneStatisticRestObject] milestone_statistics()

View available milestone statistics options

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MilestonesApi()

try:
    # View available milestone statistics options
    api_response = api_instance.milestone_statistics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MilestonesApi->milestone_statistics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MilestoneStatisticRestObject]**](MilestoneStatisticRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **milestone_types**
> list[MilestoneType] milestone_types()

View available milestoneType options

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MilestonesApi()

try:
    # View available milestoneType options
    api_response = api_instance.milestone_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MilestonesApi->milestone_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MilestoneType]**](MilestoneType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **milestones**
> MilestoneContainerRestObject milestones(org_type=org_type, achievement_statuses=achievement_statuses, milestone_types=milestone_types, is_last_achievement=is_last_achievement, milestone_statistics=milestone_statistics, milestone_values=milestone_values, player_ids=player_ids, team_ids=team_ids, league_ids=league_ids, stat_group=stat_group, season=season, seasons=seasons, venue_ids=venue_ids, game_pks=game_pks, limit=limit, fields=fields, show_firsts=show_firsts)

View pending and achieved milestones.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MilestonesApi()
org_type = swagger_client.OrganizationType() # OrganizationType | Organization level. Format: T(Team), L(League), S(Sport) (optional)
achievement_statuses = [swagger_client.MilestoneAchievementType()] # list[MilestoneAchievementType] | Comma delimited list of milestone achievement types (optional)
milestone_types = [swagger_client.MilestoneType()] # list[MilestoneType] | Comma delimited list of milestone types (optional)
is_last_achievement = true # bool | Filters out milestones that have already been surpassed. (optional)
milestone_statistics = [swagger_client.Statistic()] # list[Statistic] | Comma delimited list of milestone statistics (optional)
milestone_values = [56] # list[int] | Comma delimited list of milestone values (optional)
player_ids = [56] # list[int] | A unique identifier for players (optional)
team_ids = [56] # list[int] | Comma delimited list of Unique Team identifiers (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
stat_group = swagger_client.StatGroup() # StatGroup | Category of statistic to return. Available types in /api/v1/statGroups (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
venue_ids = [56] # list[int] | Comma delimited list of Unique venue identifiers (optional)
game_pks = [56] # list[int] | Comma delimited list of unique primary keys (optional)
limit = 56 # int | Number of results to return (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
show_firsts = true # bool | True to show play first milestones, like first HR, first Save, etc (optional)

try:
    # View pending and achieved milestones.
    api_response = api_instance.milestones(org_type=org_type, achievement_statuses=achievement_statuses, milestone_types=milestone_types, is_last_achievement=is_last_achievement, milestone_statistics=milestone_statistics, milestone_values=milestone_values, player_ids=player_ids, team_ids=team_ids, league_ids=league_ids, stat_group=stat_group, season=season, seasons=seasons, venue_ids=venue_ids, game_pks=game_pks, limit=limit, fields=fields, show_firsts=show_firsts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MilestonesApi->milestones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_type** | [**OrganizationType**](.md)| Organization level. Format: T(Team), L(League), S(Sport) | [optional] 
 **achievement_statuses** | [**list[MilestoneAchievementType]**](MilestoneAchievementType.md)| Comma delimited list of milestone achievement types | [optional] 
 **milestone_types** | [**list[MilestoneType]**](MilestoneType.md)| Comma delimited list of milestone types | [optional] 
 **is_last_achievement** | **bool**| Filters out milestones that have already been surpassed. | [optional] 
 **milestone_statistics** | [**list[Statistic]**](Statistic.md)| Comma delimited list of milestone statistics | [optional] 
 **milestone_values** | [**list[int]**](int.md)| Comma delimited list of milestone values | [optional] 
 **player_ids** | [**list[int]**](int.md)| A unique identifier for players | [optional] 
 **team_ids** | [**list[int]**](int.md)| Comma delimited list of Unique Team identifiers | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **stat_group** | [**StatGroup**](.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **venue_ids** | [**list[int]**](int.md)| Comma delimited list of Unique venue identifiers | [optional] 
 **game_pks** | [**list[int]**](int.md)| Comma delimited list of unique primary keys | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **show_firsts** | **bool**| True to show play first milestones, like first HR, first Save, etc | [optional] 

### Return type

[**MilestoneContainerRestObject**](MilestoneContainerRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

