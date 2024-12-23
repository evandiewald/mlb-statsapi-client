# swagger_client.AwardsApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**award_recipients**](AwardsApi.md#award_recipients) | **GET** /api/v1/awards/{awardId}/recipients | View recipients of an award
[**awards**](AwardsApi.md#awards) | **GET** /api/v1/awards | View awards info
[**awards1**](AwardsApi.md#awards1) | **GET** /api/v1/awards/{awardId} | View awards info

# **award_recipients**
> AwardsRestObject award_recipients(award_id, season=season, sport_id=sport_id, league_id=league_id, fields=fields)

View recipients of an award

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwardsApi()
award_id = 'award_id_example' # str | Unique Award Identifier. Available awards in /api/v1/awards
season = 'season_example' # str | Season of play (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
league_id = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    # View recipients of an award
    api_response = api_instance.award_recipients(award_id, season=season, sport_id=sport_id, league_id=league_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwardsApi->award_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **award_id** | **str**| Unique Award Identifier. Available awards in /api/v1/awards | 
 **season** | **str**| Season of play | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **league_id** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**AwardsRestObject**](AwardsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **awards**
> AwardsRestObject awards(award_id, org_id=org_id, fields=fields)

View awards info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwardsApi()
award_id = 'award_id_example' # str | Unique Award Identifier. Available awards in /api/v1/awards
org_id = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View awards info
    api_response = api_instance.awards(award_id, org_id=org_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwardsApi->awards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **award_id** | **str**| Unique Award Identifier. Available awards in /api/v1/awards | 
 **org_id** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**AwardsRestObject**](AwardsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **awards1**
> AwardsRestObject awards1(award_id, org_id=org_id, fields=fields)

View awards info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwardsApi()
award_id = 'award_id_example' # str | Unique Award Identifier. Available awards in /api/v1/awards
org_id = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View awards info
    api_response = api_instance.awards1(award_id, org_id=org_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwardsApi->awards1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **award_id** | **str**| Unique Award Identifier. Available awards in /api/v1/awards | 
 **org_id** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**AwardsRestObject**](AwardsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

