# swagger_client.DivisionApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**divisions**](DivisionApi.md#divisions) | **GET** /api/v1/divisions | Get division information
[**divisions1**](DivisionApi.md#divisions1) | **GET** /api/v1/divisions/{divisionId} | Get division information

# **divisions**
> DivisionsRestObject divisions(division_id, include_inactive=include_inactive, league_id=league_id, sport_id=sport_id, season=season, fields=fields)

Get division information

This endpoint allows you to pull divisions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DivisionApi()
division_id = 56 # int | Unique Division Identifier
include_inactive = false # bool | Whether or not to include inactive (optional) (default to false)
league_id = 56 # int | Unique League Identifier (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get division information
    api_response = api_instance.divisions(division_id, include_inactive=include_inactive, league_id=league_id, sport_id=sport_id, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DivisionApi->divisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division_id** | **int**| Unique Division Identifier | 
 **include_inactive** | **bool**| Whether or not to include inactive | [optional] [default to false]
 **league_id** | **int**| Unique League Identifier | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**DivisionsRestObject**](DivisionsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **divisions1**
> DivisionsRestObject divisions1(division_id, include_inactive=include_inactive, league_id=league_id, sport_id=sport_id, season=season, fields=fields)

Get division information

This endpoint allows you to pull divisions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DivisionApi()
division_id = 56 # int | Unique Division Identifier
include_inactive = false # bool | Whether or not to include inactive (optional) (default to false)
league_id = 56 # int | Unique League Identifier (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get division information
    api_response = api_instance.divisions1(division_id, include_inactive=include_inactive, league_id=league_id, sport_id=sport_id, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DivisionApi->divisions1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division_id** | **int**| Unique Division Identifier | 
 **include_inactive** | **bool**| Whether or not to include inactive | [optional] [default to false]
 **league_id** | **int**| Unique League Identifier | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**DivisionsRestObject**](DivisionsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

