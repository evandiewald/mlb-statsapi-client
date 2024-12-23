# swagger_client.BatTrackingApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bat_tracking**](BatTrackingApi.md#bat_tracking) | **GET** /api/v1/batTracking/game/{gamePk}/{playId} | View Bat Tracking Data by playId and gameId

# **bat_tracking**
> BatTrackingRestObject bat_tracking(game_pk, play_id, fields=fields)

View Bat Tracking Data by playId and gameId

This endpoint allows you to pull bat tracking data by gameId and playId

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
api_instance = swagger_client.BatTrackingApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game
play_id = 'play_id_example' # str | Unique play identifier
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View Bat Tracking Data by playId and gameId
    api_response = api_instance.bat_tracking(game_pk, play_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatTrackingApi->bat_tracking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **play_id** | **str**| Unique play identifier | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**BatTrackingRestObject**](BatTrackingRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

