# swagger_client.SportsApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_sport_ballot**](SportsApi.md#all_sport_ballot) | **GET** /api/v1/sports/{sportId}/allSportBallot | Get ALL MLB ballot for sport
[**sport_players**](SportsApi.md#sport_players) | **GET** /api/v1/sports/{sportId}/players | Get all players for a sport level
[**sports**](SportsApi.md#sports) | **GET** /api/v1/sports | Get sports information
[**sports1**](SportsApi.md#sports1) | **GET** /api/v1/sports/{sportId} | Get sports information

# **all_sport_ballot**
> PeopleRestObject all_sport_ballot(sport_id, season, fields=fields)

Get ALL MLB ballot for sport

This endpoint allows you to get all players for MLB ballot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SportsApi()
sport_id = 56 # int | Top level organization of a sport
season = 'season_example' # str | season
fields = ['fields_example'] # list[str] |  (optional)

try:
    # Get ALL MLB ballot for sport
    api_response = api_instance.all_sport_ballot(sport_id, season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SportsApi->all_sport_ballot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**| Top level organization of a sport | 
 **season** | **str**| season | 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**PeopleRestObject**](PeopleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sport_players**
> PeopleRestObject sport_players(sport_id, season=season, game_type=game_type, has_stats=has_stats, accent=accent, fields=fields)

Get all players for a sport level

This endpoint allows you to pull all players for a given sport

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SportsApi()
sport_id = 56 # int | Top level organization of a sport
season = 'season_example' # str | Season of play (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
has_stats = true # bool | Returns sports that have individual player stats (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get all players for a sport level
    api_response = api_instance.sport_players(sport_id, season=season, game_type=game_type, has_stats=has_stats, accent=accent, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SportsApi->sport_players: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**| Top level organization of a sport | 
 **season** | **str**| Season of play | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **has_stats** | **bool**| Returns sports that have individual player stats | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**PeopleRestObject**](PeopleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sports**
> SportsRestObject sports(sport_id, season=season, fields=fields, has_stats=has_stats, active_status=active_status)

Get sports information

This endpoint allows you to pull sports

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SportsApi()
sport_id = 56 # int | Top level organization of a sport
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
has_stats = true # bool | Returns sports that have individual player stats (optional)
active_status = swagger_client.SportActiveStatusEnum() # SportActiveStatusEnum | Flag for fetching sports that are currently active (Y), inactive (N), pending (P), or all teams (B) (optional)

try:
    # Get sports information
    api_response = api_instance.sports(sport_id, season=season, fields=fields, has_stats=has_stats, active_status=active_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SportsApi->sports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**| Top level organization of a sport | 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **has_stats** | **bool**| Returns sports that have individual player stats | [optional] 
 **active_status** | [**SportActiveStatusEnum**](.md)| Flag for fetching sports that are currently active (Y), inactive (N), pending (P), or all teams (B) | [optional] 

### Return type

[**SportsRestObject**](SportsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sports1**
> SportsRestObject sports1(sport_id, season=season, fields=fields, has_stats=has_stats, active_status=active_status)

Get sports information

This endpoint allows you to pull sports

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SportsApi()
sport_id = 56 # int | Top level organization of a sport
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
has_stats = true # bool | Returns sports that have individual player stats (optional)
active_status = swagger_client.SportActiveStatusEnum() # SportActiveStatusEnum | Flag for fetching sports that are currently active (Y), inactive (N), pending (P), or all teams (B) (optional)

try:
    # Get sports information
    api_response = api_instance.sports1(sport_id, season=season, fields=fields, has_stats=has_stats, active_status=active_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SportsApi->sports1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**| Top level organization of a sport | 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **has_stats** | **bool**| Returns sports that have individual player stats | [optional] 
 **active_status** | [**SportActiveStatusEnum**](.md)| Flag for fetching sports that are currently active (Y), inactive (N), pending (P), or all teams (B) | [optional] 

### Return type

[**SportsRestObject**](SportsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

