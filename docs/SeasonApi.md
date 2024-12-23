# swagger_client.SeasonApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_seasons**](SeasonApi.md#all_seasons) | **GET** /api/v1/seasons/all | View all seasons
[**seasons**](SeasonApi.md#seasons) | **GET** /api/v1/seasons | View season info
[**seasons1**](SeasonApi.md#seasons1) | **GET** /api/v1/seasons/{seasonId} | View season info

# **all_seasons**
> SeasonsRestObject all_seasons(division_id=division_id, league_id=league_id, sport_id=sport_id, with_game_type_dates=with_game_type_dates, fields=fields)

View all seasons

This endpoint allows you to view all seasons for a given Division, League or Sport

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeasonApi()
division_id = 56 # int | Unique Division Identifier (optional)
league_id = 56 # int | Unique League Identifier (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
with_game_type_dates = true # bool | Retrieve dates for each game type (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View all seasons
    api_response = api_instance.all_seasons(division_id=division_id, league_id=league_id, sport_id=sport_id, with_game_type_dates=with_game_type_dates, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeasonApi->all_seasons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division_id** | **int**| Unique Division Identifier | [optional] 
 **league_id** | **int**| Unique League Identifier | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **with_game_type_dates** | **bool**| Retrieve dates for each game type | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**SeasonsRestObject**](SeasonsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seasons**
> SeasonsRestObject seasons(season_id, season=season, sport_id=sport_id, with_game_type_dates=with_game_type_dates, fields=fields)

View season info

This endpoint allows you to pull seasons

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeasonApi()
season_id = 'season_id_example' # str | Season of play
season = ['season_example'] # list[str] | Season of play (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
with_game_type_dates = true # bool | Retrieve dates for each game type (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View season info
    api_response = api_instance.seasons(season_id, season=season, sport_id=sport_id, with_game_type_dates=with_game_type_dates, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeasonApi->seasons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season_id** | **str**| Season of play | 
 **season** | [**list[str]**](str.md)| Season of play | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **with_game_type_dates** | **bool**| Retrieve dates for each game type | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**SeasonsRestObject**](SeasonsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seasons1**
> SeasonsRestObject seasons1(season_id, season=season, sport_id=sport_id, with_game_type_dates=with_game_type_dates, fields=fields)

View season info

This endpoint allows you to pull seasons

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeasonApi()
season_id = 'season_id_example' # str | Season of play
season = ['season_example'] # list[str] | Season of play (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
with_game_type_dates = true # bool | Retrieve dates for each game type (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View season info
    api_response = api_instance.seasons1(season_id, season=season, sport_id=sport_id, with_game_type_dates=with_game_type_dates, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeasonApi->seasons1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season_id** | **str**| Season of play | 
 **season** | [**list[str]**](str.md)| Season of play | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **with_game_type_dates** | **bool**| Retrieve dates for each game type | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**SeasonsRestObject**](SeasonsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

