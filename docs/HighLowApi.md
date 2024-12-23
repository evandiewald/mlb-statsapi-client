# swagger_client.HighLowApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**high_low**](HighLowApi.md#high_low) | **GET** /api/v1/highLow/{highLowType} | View high/low stats by player or team
[**high_low_stats**](HighLowApi.md#high_low_stats) | **GET** /api/v1/highLow/types | View high/low stat types

# **high_low**
> HighLowWrapperRestObject high_low(high_low_type, stat_group=stat_group, sort_stat=sort_stat, season=season, game_type=game_type, team_id=team_id, league_id=league_id, sport_id=sport_id, offset=offset, limit=limit, fields=fields)

View high/low stats by player or team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HighLowApi()
high_low_type = swagger_client.HighLowTypeEnum() # HighLowTypeEnum | Type of high/low stats ('player', 'team', 'game')
stat_group = [swagger_client.StatGroup()] # list[StatGroup] | Comma delimited list of  categories of statistic to return. Available types in /api/v1/statGroups (optional)
sort_stat = [swagger_client.HighLowStatEnum()] # list[HighLowStatEnum] | Comma delimited list of baseball stats to sort splits by. (optional)
season = ['season_example'] # list[str] | Comma delimited list of Seasons of play (optional)
game_type = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Comma delimited list of type of Game. Available types in /api/v1/gameTypes (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
league_id = 56 # int | Unique League Identifier (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
limit = 56 # int | Number of results to return (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View high/low stats by player or team
    api_response = api_instance.high_low(high_low_type, stat_group=stat_group, sort_stat=sort_stat, season=season, game_type=game_type, team_id=team_id, league_id=league_id, sport_id=sport_id, offset=offset, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighLowApi->high_low: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **high_low_type** | [**HighLowTypeEnum**](.md)| Type of high/low stats (&#x27;player&#x27;, &#x27;team&#x27;, &#x27;game&#x27;) | 
 **stat_group** | [**list[StatGroup]**](StatGroup.md)| Comma delimited list of  categories of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **sort_stat** | [**list[HighLowStatEnum]**](HighLowStatEnum.md)| Comma delimited list of baseball stats to sort splits by. | [optional] 
 **season** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **game_type** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Comma delimited list of type of Game. Available types in /api/v1/gameTypes | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **league_id** | **int**| Unique League Identifier | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**HighLowWrapperRestObject**](HighLowWrapperRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **high_low_stats**
> list[BaseballStatsTypeRestObject] high_low_stats()

View high/low stat types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HighLowApi()

try:
    # View high/low stat types
    api_response = api_instance.high_low_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighLowApi->high_low_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BaseballStatsTypeRestObject]**](BaseballStatsTypeRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

