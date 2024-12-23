# swagger_client.PredictionsApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_props**](PredictionsApi.md#get_props) | **GET** /api/v1/props/play/predictions | Get play-level predictions based on input scenarios
[**get_props_adjust**](PredictionsApi.md#get_props_adjust) | **GET** /api/v1/props/play/predictions/adjust | Get play-level predictions based on input scenarios

# **get_props**
> object get_props(batter_id=batter_id, pitcher_id=pitcher_id, venue_id=venue_id, bat_side=bat_side, pitch_hand=pitch_hand, batter_position=batter_position, pitcher_position=pitcher_position)

Get play-level predictions based on input scenarios

This endpoint allows you to get play-level predictions based on input scenarios

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
api_instance = swagger_client.PredictionsApi(swagger_client.ApiClient(configuration))
batter_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc (optional)
pitcher_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc (optional)
venue_id = 56 # int | Unique Venue Identifier (optional)
bat_side = 'bat_side_example' # str | Bat side of hitter (optional)
pitch_hand = 'pitch_hand_example' # str | Handedness of pitcher (optional)
batter_position = 'batter_position_example' # str | Position abbreviation. Format: SS, P, 1B, etc (optional)
pitcher_position = 'pitcher_position_example' # str | Position abbreviation. Format: SS, P, 1B, etc (optional)

try:
    # Get play-level predictions based on input scenarios
    api_response = api_instance.get_props(batter_id=batter_id, pitcher_id=pitcher_id, venue_id=venue_id, bat_side=bat_side, pitch_hand=pitch_hand, batter_position=batter_position, pitcher_position=pitcher_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictionsApi->get_props: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batter_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **pitcher_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **venue_id** | **int**| Unique Venue Identifier | [optional] 
 **bat_side** | **str**| Bat side of hitter | [optional] 
 **pitch_hand** | **str**| Handedness of pitcher | [optional] 
 **batter_position** | **str**| Position abbreviation. Format: SS, P, 1B, etc | [optional] 
 **pitcher_position** | **str**| Position abbreviation. Format: SS, P, 1B, etc | [optional] 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_props_adjust**
> object get_props_adjust(game_pk)

Get play-level predictions based on input scenarios

This endpoint allows you to get play-level predictions based on input scenarios

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
api_instance = swagger_client.PredictionsApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game

try:
    # Get play-level predictions based on input scenarios
    api_response = api_instance.get_props_adjust(game_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictionsApi->get_props_adjust: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

