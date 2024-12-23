# swagger_client.ReviewsApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_review_info**](ReviewsApi.md#get_review_info) | **GET** /api/v1/review | Get review info

# **get_review_info**
> StatContainerRestObject get_review_info(sport_id, season, game_type=game_type, fields=fields)

Get review info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReviewsApi()
sport_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
season = 'season_example' # str | Comma delimited list of Seasons of play
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get review info
    api_response = api_instance.get_review_info(sport_id, season, game_type=game_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReviewsApi->get_review_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **season** | **str**| Comma delimited list of Seasons of play | 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**StatContainerRestObject**](StatContainerRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

