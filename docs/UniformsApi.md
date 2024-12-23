# swagger_client.UniformsApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uniforms_by_game**](UniformsApi.md#uniforms_by_game) | **GET** /api/v1/uniforms/game | View Game Uniform info
[**uniforms_by_team**](UniformsApi.md#uniforms_by_team) | **GET** /api/v1/uniforms/team | View Team Uniform info

# **uniforms_by_game**
> UniformsGamesRestObject uniforms_by_game(game_pks, fields=fields)

View Game Uniform info

This endpoint allows you to pull team uniform data for a game

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UniformsApi()
game_pks = [56] # list[int] | Comma delimited list of unique primary keys
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View Game Uniform info
    api_response = api_instance.uniforms_by_game(game_pks, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniformsApi->uniforms_by_game: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pks** | [**list[int]**](int.md)| Comma delimited list of unique primary keys | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**UniformsGamesRestObject**](UniformsGamesRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uniforms_by_team**
> UniformsTeamsRestObject uniforms_by_team(team_ids, season=season, fields=fields)

View Team Uniform info

This endpoint allows you to pull team uniform data for a season

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UniformsApi()
team_ids = [56] # list[int] | 
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View Team Uniform info
    api_response = api_instance.uniforms_by_team(team_ids, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniformsApi->uniforms_by_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_ids** | [**list[int]**](int.md)|  | 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**UniformsTeamsRestObject**](UniformsTeamsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

