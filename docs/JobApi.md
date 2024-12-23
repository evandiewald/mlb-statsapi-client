# swagger_client.JobApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datacasters**](JobApi.md#datacasters) | **GET** /api/v1/jobs/datacasters | Get datacaster jobs
[**get_jobs_by_type**](JobApi.md#get_jobs_by_type) | **GET** /api/v1/jobs | Get jobs by type
[**official_scorers**](JobApi.md#official_scorers) | **GET** /api/v1/jobs/officialScorers | Get official scorers
[**umpire_schedule**](JobApi.md#umpire_schedule) | **GET** /api/v1/jobs/umpires/games/{umpireId} | Get umpires and associated game for umpireId
[**umpires**](JobApi.md#umpires) | **GET** /api/v1/jobs/umpires | Get umpires

# **datacasters**
> RosterRestObject datacasters(sport_id=sport_id, _date=_date, fields=fields)

Get datacaster jobs

Get datacaster jobs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobApi()
sport_id = 56 # int | Top level organization of a sport (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get datacaster jobs
    api_response = api_instance.datacasters(sport_id=sport_id, _date=_date, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->datacasters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**RosterRestObject**](RosterRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_by_type**
> RosterRestObject get_jobs_by_type(job_type, sport_id=sport_id, _date=_date, fields=fields)

Get jobs by type

This endpoint allows you to pull teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobApi()
job_type = 'job_type_example' # str | Job Type Identifier (ie. UMPR, etc..)
sport_id = 56 # int | Top level organization of a sport (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get jobs by type
    api_response = api_instance.get_jobs_by_type(job_type, sport_id=sport_id, _date=_date, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_jobs_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type** | **str**| Job Type Identifier (ie. UMPR, etc..) | 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**RosterRestObject**](RosterRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **official_scorers**
> RosterRestObject official_scorers(sport_id=sport_id, _date=_date, fields=fields)

Get official scorers

This endpoint allows you to pull teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobApi()
sport_id = 56 # int | Top level organization of a sport (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get official scorers
    api_response = api_instance.official_scorers(sport_id=sport_id, _date=_date, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->official_scorers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**RosterRestObject**](RosterRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umpire_schedule**
> ScheduleRestObject umpire_schedule(umpire_id, season, fields=fields)

Get umpires and associated game for umpireId

This endpoint allows you to pull teams

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
api_instance = swagger_client.JobApi(swagger_client.ApiClient(configuration))
umpire_id = 56 # int | A unique identifier for an umpire
season = 'season_example' # str | Season of play
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get umpires and associated game for umpireId
    api_response = api_instance.umpire_schedule(umpire_id, season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->umpire_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **umpire_id** | **int**| A unique identifier for an umpire | 
 **season** | **str**| Season of play | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**ScheduleRestObject**](ScheduleRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umpires**
> RosterRestObject umpires(sport_id=sport_id, _date=_date, fields=fields, season=season)

Get umpires

This endpoint allows you to pull teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobApi()
sport_id = 56 # int | Top level organization of a sport (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
season = 'season_example' # str | Season of play (optional)

try:
    # Get umpires
    api_response = api_instance.umpires(sport_id=sport_id, _date=_date, fields=fields, season=season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->umpires: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **season** | **str**| Season of play | [optional] 

### Return type

[**RosterRestObject**](RosterRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

