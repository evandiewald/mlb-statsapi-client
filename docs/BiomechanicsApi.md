# swagger_client.BiomechanicsApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**biomechanical**](BiomechanicsApi.md#biomechanical) | **GET** /api/v1/game/{gamePk}/{playId}/analytics/biomechanics/{positionId} | View Biomechanical data by playId and gameId filtered by player positionId

# **biomechanical**
> SkeletalDataWrapperRestObject biomechanical(game_pk, play_id, position_id, fields=fields)

View Biomechanical data by playId and gameId filtered by player positionId

This endpoint allows you to pull biomechanical tracking data by gameId and playId filtered by player positionId

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
api_instance = swagger_client.BiomechanicsApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game
play_id = 'play_id_example' # str | Unique play identifier
position_id = 56 # int | Position number. Format: 1, 2, 3, etc
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View Biomechanical data by playId and gameId filtered by player positionId
    api_response = api_instance.biomechanical(game_pk, play_id, position_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiomechanicsApi->biomechanical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **play_id** | **str**| Unique play identifier | 
 **position_id** | **int**| Position number. Format: 1, 2, 3, etc | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**SkeletalDataWrapperRestObject**](SkeletalDataWrapperRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

