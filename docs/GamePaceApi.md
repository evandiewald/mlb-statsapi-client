# swagger_client.GamePaceApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**game_pace**](GamePaceApi.md#game_pace) | **GET** /api/v1/gamePace | View time of game info

# **game_pace**
> GamePaceWrapperRestObject game_pace(season=season, team_id=team_id, team_ids=team_ids, league_id=league_id, league_ids=league_ids, league_list_id=league_list_id, sport_id=sport_id, sport_ids=sport_ids, game_type=game_type, start_date=start_date, end_date=end_date, venue_ids=venue_ids, exclude_venue_ids=exclude_venue_ids, exclude_game_pks=exclude_game_pks, org_type=org_type, include_children=include_children, fields=fields)

View time of game info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GamePaceApi()
season = 'season_example' # str | Season of play (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
team_ids = [56] # list[int] | Comma delimited list of Unique Team identifiers (optional)
league_id = 56 # int | Unique League Identifier (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
league_list_id = swagger_client.LeagueListsEnum() # LeagueListsEnum | Unique League List Identifier (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
venue_ids = [56] # list[int] | Comma delimited list of Unique venue identifiers (optional)
exclude_venue_ids = [56] # list[int] | Comma delimited list of Unique venue identifiers (optional)
exclude_game_pks = [56] # list[int] | Comma delimited list of unique primary keys (optional)
org_type = swagger_client.OrganizationType() # OrganizationType | Organization level. Format: T(Team), L(League), S(Sport) (optional)
include_children = false # bool | Determines weather to include results from an organization's children (ex. a sport would also include results for the teams and leagues) (optional) (default to false)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View time of game info
    api_response = api_instance.game_pace(season=season, team_id=team_id, team_ids=team_ids, league_id=league_id, league_ids=league_ids, league_list_id=league_list_id, sport_id=sport_id, sport_ids=sport_ids, game_type=game_type, start_date=start_date, end_date=end_date, venue_ids=venue_ids, exclude_venue_ids=exclude_venue_ids, exclude_game_pks=exclude_game_pks, org_type=org_type, include_children=include_children, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamePaceApi->game_pace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **str**| Season of play | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **team_ids** | [**list[int]**](int.md)| Comma delimited list of Unique Team identifiers | [optional] 
 **league_id** | **int**| Unique League Identifier | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **league_list_id** | [**LeagueListsEnum**](.md)| Unique League List Identifier | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **venue_ids** | [**list[int]**](int.md)| Comma delimited list of Unique venue identifiers | [optional] 
 **exclude_venue_ids** | [**list[int]**](int.md)| Comma delimited list of Unique venue identifiers | [optional] 
 **exclude_game_pks** | [**list[int]**](int.md)| Comma delimited list of unique primary keys | [optional] 
 **org_type** | [**OrganizationType**](.md)| Organization level. Format: T(Team), L(League), S(Sport) | [optional] 
 **include_children** | **bool**| Determines weather to include results from an organization&#x27;s children (ex. a sport would also include results for the teams and leagues) | [optional] [default to false]
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**GamePaceWrapperRestObject**](GamePaceWrapperRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

