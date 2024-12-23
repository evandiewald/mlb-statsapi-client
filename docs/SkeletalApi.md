# swagger_client.SkeletalApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**skeletal_chunked**](SkeletalApi.md#skeletal_chunked) | **GET** /api/v1/game/{gamePk}/{playId}/analytics/skeletalData/chunked | View Skeletal Data by playId and gameId chunked
[**skeletal_data_file_names**](SkeletalApi.md#skeletal_data_file_names) | **GET** /api/v1/game/{gamePk}/{playId}/analytics/skeletalData/files | View Skeletal Data by playId and gameId files

# **skeletal_chunked**
> str skeletal_chunked(game_pk, play_id, file_name, fields=fields)

View Skeletal Data by playId and gameId chunked

This endpoint allows you to pull chunked skeletal tracking data by gameId and playId

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
api_instance = swagger_client.SkeletalApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game
play_id = 'play_id_example' # str | Unique play identifier
file_name = 'file_name_example' # str | Skeletal chunked file name
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View Skeletal Data by playId and gameId chunked
    api_response = api_instance.skeletal_chunked(game_pk, play_id, file_name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkeletalApi->skeletal_chunked: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **play_id** | **str**| Unique play identifier | 
 **file_name** | **str**| Skeletal chunked file name | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skeletal_data_file_names**
> SkeletalFileData skeletal_data_file_names(game_pk, play_id, fields=fields)

View Skeletal Data by playId and gameId files

This endpoint allows you to pull chunked skeletal tracking data by gameId and playId

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
api_instance = swagger_client.SkeletalApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game
play_id = 'play_id_example' # str | Unique play identifier
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View Skeletal Data by playId and gameId files
    api_response = api_instance.skeletal_data_file_names(game_pk, play_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkeletalApi->skeletal_data_file_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **play_id** | **str**| Unique play identifier | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**SkeletalFileData**](SkeletalFileData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

