# swagger_client.ConferenceApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conferences**](ConferenceApi.md#conferences) | **GET** /api/v1/conferences | View conference info
[**conferences1**](ConferenceApi.md#conferences1) | **GET** /api/v1/conferences/{conferenceId} | View conference info

# **conferences**
> ConferencesRestObject conferences(conference_id, season=season, include_inactive=include_inactive, fields=fields)

View conference info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConferenceApi()
conference_id = 56 # int | 
season = 'season_example' # str | Season of play (optional)
include_inactive = true # bool |  (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View conference info
    api_response = api_instance.conferences(conference_id, season=season, include_inactive=include_inactive, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConferenceApi->conferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conference_id** | **int**|  | 
 **season** | **str**| Season of play | [optional] 
 **include_inactive** | **bool**|  | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**ConferencesRestObject**](ConferencesRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conferences1**
> ConferencesRestObject conferences1(conference_id, season=season, include_inactive=include_inactive, fields=fields)

View conference info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConferenceApi()
conference_id = 56 # int | 
season = 'season_example' # str | Season of play (optional)
include_inactive = true # bool |  (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View conference info
    api_response = api_instance.conferences1(conference_id, season=season, include_inactive=include_inactive, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConferenceApi->conferences1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conference_id** | **int**|  | 
 **season** | **str**| Season of play | [optional] 
 **include_inactive** | **bool**|  | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**ConferencesRestObject**](ConferencesRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

