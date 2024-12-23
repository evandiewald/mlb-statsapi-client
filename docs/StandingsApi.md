# swagger_client.StandingsApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**standings**](StandingsApi.md#standings) | **GET** /api/v1/standings/{standingsType} | View standings for a league
[**standings1**](StandingsApi.md#standings1) | **GET** /api/v1/standings | View standings for a league

# **standings**
> StandingsRestObject standings(standings_type, league_id=league_id, season=season, standings_types=standings_types, _date=_date, team_id=team_id, include_mlb=include_mlb, fields=fields)

View standings for a league

This endpoint allows you to pull standings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StandingsApi()
standings_type = 'standings_type_example' # str | Type of season. Available types in /api/v1/standingsTypes
league_id = [56] # list[int] | Unique League Identifier (optional)
season = 'season_example' # str | Season of play (optional)
standings_types = [swagger_client.StandingsType()] # list[StandingsType] | Type of season. Available types in /api/v1/standingsTypes (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
include_mlb = true # bool | Determines whether to include major league teams when using the 'BY_ORGANIZATION' standings type (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View standings for a league
    api_response = api_instance.standings(standings_type, league_id=league_id, season=season, standings_types=standings_types, _date=_date, team_id=team_id, include_mlb=include_mlb, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandingsApi->standings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standings_type** | **str**| Type of season. Available types in /api/v1/standingsTypes | 
 **league_id** | [**list[int]**](int.md)| Unique League Identifier | [optional] 
 **season** | **str**| Season of play | [optional] 
 **standings_types** | [**list[StandingsType]**](StandingsType.md)| Type of season. Available types in /api/v1/standingsTypes | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **include_mlb** | **bool**| Determines whether to include major league teams when using the &#x27;BY_ORGANIZATION&#x27; standings type | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**StandingsRestObject**](StandingsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **standings1**
> StandingsRestObject standings1(standings_type, league_id=league_id, season=season, standings_types=standings_types, _date=_date, team_id=team_id, include_mlb=include_mlb, fields=fields)

View standings for a league

This endpoint allows you to pull standings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StandingsApi()
standings_type = 'standings_type_example' # str | Type of season. Available types in /api/v1/standingsTypes
league_id = [56] # list[int] | Unique League Identifier (optional)
season = 'season_example' # str | Season of play (optional)
standings_types = [swagger_client.StandingsType()] # list[StandingsType] | Type of season. Available types in /api/v1/standingsTypes (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
include_mlb = true # bool | Determines whether to include major league teams when using the 'BY_ORGANIZATION' standings type (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View standings for a league
    api_response = api_instance.standings1(standings_type, league_id=league_id, season=season, standings_types=standings_types, _date=_date, team_id=team_id, include_mlb=include_mlb, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandingsApi->standings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standings_type** | **str**| Type of season. Available types in /api/v1/standingsTypes | 
 **league_id** | [**list[int]**](int.md)| Unique League Identifier | [optional] 
 **season** | **str**| Season of play | [optional] 
 **standings_types** | [**list[StandingsType]**](StandingsType.md)| Type of season. Available types in /api/v1/standingsTypes | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **include_mlb** | **bool**| Determines whether to include major league teams when using the &#x27;BY_ORGANIZATION&#x27; standings type | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**StandingsRestObject**](StandingsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

