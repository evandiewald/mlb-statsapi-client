# swagger_client.StreaksApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_streaks**](StreaksApi.md#get_streaks) | **GET** /api/v1/streaks | View streaks
[**streak_types**](StreaksApi.md#streak_types) | **GET** /api/v1/streaks/types | View streaks parameter options

# **get_streaks**
> StreaksWrapperRestObject get_streaks(streak_org=streak_org, streak_stat=streak_stat, streak_span=streak_span, streak_level=streak_level, streak_threshold=streak_threshold, inverse=inverse, starters_only=starters_only, stat_group=stat_group, game_type=game_type, season=season, team_id=team_id, league_id=league_id, sport_id=sport_id, active_streak=active_streak, limit=limit, fields=fields, player_id=player_id)

View streaks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StreaksApi(swagger_client.ApiClient(configuration))
streak_org = swagger_client.OrganizationType() # OrganizationType |  (optional)
streak_stat = [swagger_client.StreakStatEnum()] # list[StreakStatEnum] |  (optional)
streak_span = swagger_client.StreakSpanEnum() # StreakSpanEnum |  (optional)
streak_level = swagger_client.StreakLevelEnum() # StreakLevelEnum |  (optional)
streak_threshold = 56 # int |  (optional)
inverse = true # bool |  (optional)
starters_only = true # bool |  (optional)
stat_group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups (optional)
game_type = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Type of Game. Available types in /api/v1/gameTypes (optional)
season = ['season_example'] # list[str] | Season of play (optional)
team_id = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
league_id = [56] # list[int] | Unique League Identifier (optional)
sport_id = [56] # list[int] | Top level organization of a sport (optional)
active_streak = true # bool | Whether or not a player is active (optional)
limit = 56 # int | Number of results to return (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
player_id = [56] # list[int] | A unique identifier for a player (optional)

try:
    # View streaks
    api_response = api_instance.get_streaks(streak_org=streak_org, streak_stat=streak_stat, streak_span=streak_span, streak_level=streak_level, streak_threshold=streak_threshold, inverse=inverse, starters_only=starters_only, stat_group=stat_group, game_type=game_type, season=season, team_id=team_id, league_id=league_id, sport_id=sport_id, active_streak=active_streak, limit=limit, fields=fields, player_id=player_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreaksApi->get_streaks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **streak_org** | [**OrganizationType**](.md)|  | [optional] 
 **streak_stat** | [**list[StreakStatEnum]**](StreakStatEnum.md)|  | [optional] 
 **streak_span** | [**StreakSpanEnum**](.md)|  | [optional] 
 **streak_level** | [**StreakLevelEnum**](.md)|  | [optional] 
 **streak_threshold** | **int**|  | [optional] 
 **inverse** | **bool**|  | [optional] 
 **starters_only** | **bool**|  | [optional] 
 **stat_group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **game_type** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **season** | [**list[str]**](str.md)| Season of play | [optional] 
 **team_id** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **league_id** | [**list[int]**](int.md)| Unique League Identifier | [optional] 
 **sport_id** | [**list[int]**](int.md)| Top level organization of a sport | [optional] 
 **active_streak** | **bool**| Whether or not a player is active | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **player_id** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 

### Return type

[**StreaksWrapperRestObject**](StreaksWrapperRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **streak_types**
> dict(str, list[object]) streak_types()

View streaks parameter options

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreaksApi()

try:
    # View streaks parameter options
    api_response = api_instance.streak_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreaksApi->streak_types: %s\n" % e)
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

