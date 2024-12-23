# swagger_client.BroadcastApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_broadcasters**](BroadcastApi.md#get_all_broadcasters) | **GET** /api/v1/broadcasters | Get All Active Broadcasters
[**get_broadcasts**](BroadcastApi.md#get_broadcasts) | **GET** /api/v1/broadcast | Get Broadcasters

# **get_all_broadcasters**
> list[BroadcasterRestObject] get_all_broadcasters(active_status=active_status, fields=fields)

Get All Active Broadcasters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BroadcastApi()
active_status = swagger_client.BroadcasterActiveStatusEnum() # BroadcasterActiveStatusEnum | Current status of the broadcaster. Format: Active = y, inactive = n, both = b (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get All Active Broadcasters
    api_response = api_instance.get_all_broadcasters(active_status=active_status, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->get_all_broadcasters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active_status** | [**BroadcasterActiveStatusEnum**](.md)| Current status of the broadcaster. Format: Active &#x3D; y, inactive &#x3D; n, both &#x3D; b | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**list[BroadcasterRestObject]**](BroadcasterRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_broadcasts**
> list[BroadcasterRestObject] get_broadcasts(broadcaster_ids, fields=fields)

Get Broadcasters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BroadcastApi()
broadcaster_ids = [56] # list[int] | All of the broadcast details
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get Broadcasters
    api_response = api_instance.get_broadcasts(broadcaster_ids, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->get_broadcasts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broadcaster_ids** | [**list[int]**](int.md)| All of the broadcast details | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**list[BroadcasterRestObject]**](BroadcasterRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

