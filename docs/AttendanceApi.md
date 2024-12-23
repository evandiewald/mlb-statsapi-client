# swagger_client.AttendanceApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_team_attendance**](AttendanceApi.md#get_team_attendance) | **GET** /api/v1/attendance | Get team attendance

# **get_team_attendance**
> AttendanceRestObject get_team_attendance(team_id=team_id, league_id=league_id, season=season, league_list_id=league_list_id, game_type=game_type, _date=_date, start_date=start_date, end_date=end_date, fields=fields)

Get team attendance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttendanceApi()
team_id = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
league_id = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
season = ['season_example'] # list[str] | Comma delimited list of Seasons of play (optional)
league_list_id = swagger_client.LeagueListsEnum() # LeagueListsEnum | Unique League List Identifier (optional)
game_type = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Type of Game. Available types in /api/v1/gameTypes (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get team attendance
    api_response = api_instance.get_team_attendance(team_id=team_id, league_id=league_id, season=season, league_list_id=league_list_id, game_type=game_type, _date=_date, start_date=start_date, end_date=end_date, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttendanceApi->get_team_attendance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **league_id** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **season** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **league_list_id** | [**LeagueListsEnum**](.md)| Unique League List Identifier | [optional] 
 **game_type** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**AttendanceRestObject**](AttendanceRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

