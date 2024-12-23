# swagger_client.HomerunDerbyApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**home_run_derby_bracket**](HomerunDerbyApi.md#home_run_derby_bracket) | **GET** /api/v1/homeRunDerby/{gamePk} | View a home run derby object
[**home_run_derby_bracket1**](HomerunDerbyApi.md#home_run_derby_bracket1) | **GET** /api/v1/homeRunDerby | View a home run derby object
[**home_run_derby_bracket2**](HomerunDerbyApi.md#home_run_derby_bracket2) | **GET** /api/v1/homeRunDerby/{gamePk}/bracket | View a home run derby object
[**home_run_derby_bracket3**](HomerunDerbyApi.md#home_run_derby_bracket3) | **GET** /api/v1/homeRunDerby/bracket | View a home run derby object
[**home_run_derby_mixed_mode**](HomerunDerbyApi.md#home_run_derby_mixed_mode) | **GET** /api/v1/homeRunDerby/{gamePk}/mixed | View home run derby mixed mode (Bracket/Pool combo)
[**home_run_derby_mixed_mode1**](HomerunDerbyApi.md#home_run_derby_mixed_mode1) | **GET** /api/v1/homeRunDerby/mixed | View home run derby mixed mode (Bracket/Pool combo)
[**home_run_derby_pool**](HomerunDerbyApi.md#home_run_derby_pool) | **GET** /api/v1/homeRunDerby/{gamePk}/pool | View home run derby pool
[**home_run_derby_pool1**](HomerunDerbyApi.md#home_run_derby_pool1) | **GET** /api/v1/homeRunDerby/pool | View home run derby pool

# **home_run_derby_bracket**
> HomeRunDerbyRestObject home_run_derby_bracket(game_pk, fields=fields)

View a home run derby object

This endpoint allows you to pull home run derby information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomerunDerbyApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a home run derby object
    api_response = api_instance.home_run_derby_bracket(game_pk, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomerunDerbyApi->home_run_derby_bracket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**HomeRunDerbyRestObject**](HomeRunDerbyRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **home_run_derby_bracket1**
> HomeRunDerbyRestObject home_run_derby_bracket1(game_pk, fields=fields)

View a home run derby object

This endpoint allows you to pull home run derby information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomerunDerbyApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a home run derby object
    api_response = api_instance.home_run_derby_bracket1(game_pk, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomerunDerbyApi->home_run_derby_bracket1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**HomeRunDerbyRestObject**](HomeRunDerbyRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **home_run_derby_bracket2**
> HomeRunDerbyRestObject home_run_derby_bracket2(game_pk, fields=fields)

View a home run derby object

This endpoint allows you to pull home run derby information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomerunDerbyApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a home run derby object
    api_response = api_instance.home_run_derby_bracket2(game_pk, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomerunDerbyApi->home_run_derby_bracket2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**HomeRunDerbyRestObject**](HomeRunDerbyRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **home_run_derby_bracket3**
> HomeRunDerbyRestObject home_run_derby_bracket3(game_pk, fields=fields)

View a home run derby object

This endpoint allows you to pull home run derby information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomerunDerbyApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a home run derby object
    api_response = api_instance.home_run_derby_bracket3(game_pk, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomerunDerbyApi->home_run_derby_bracket3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**HomeRunDerbyRestObject**](HomeRunDerbyRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **home_run_derby_mixed_mode**
> HomeRunDerbyRestObject home_run_derby_mixed_mode(game_pk, fields=fields)

View home run derby mixed mode (Bracket/Pool combo)

This endpoint allows you to pull home run derby information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomerunDerbyApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View home run derby mixed mode (Bracket/Pool combo)
    api_response = api_instance.home_run_derby_mixed_mode(game_pk, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomerunDerbyApi->home_run_derby_mixed_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**HomeRunDerbyRestObject**](HomeRunDerbyRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **home_run_derby_mixed_mode1**
> HomeRunDerbyRestObject home_run_derby_mixed_mode1(game_pk, fields=fields)

View home run derby mixed mode (Bracket/Pool combo)

This endpoint allows you to pull home run derby information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomerunDerbyApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View home run derby mixed mode (Bracket/Pool combo)
    api_response = api_instance.home_run_derby_mixed_mode1(game_pk, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomerunDerbyApi->home_run_derby_mixed_mode1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**HomeRunDerbyRestObject**](HomeRunDerbyRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **home_run_derby_pool**
> HomeRunDerbyRestObject home_run_derby_pool(game_pk, fields=fields)

View home run derby pool

This endpoint allows you to pull home run derby information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomerunDerbyApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View home run derby pool
    api_response = api_instance.home_run_derby_pool(game_pk, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomerunDerbyApi->home_run_derby_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**HomeRunDerbyRestObject**](HomeRunDerbyRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **home_run_derby_pool1**
> HomeRunDerbyRestObject home_run_derby_pool1(game_pk, fields=fields)

View home run derby pool

This endpoint allows you to pull home run derby information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomerunDerbyApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View home run derby pool
    api_response = api_instance.home_run_derby_pool1(game_pk, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomerunDerbyApi->home_run_derby_pool1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**HomeRunDerbyRestObject**](HomeRunDerbyRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

