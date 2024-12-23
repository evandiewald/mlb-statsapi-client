# swagger_client.PersonApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**award**](PersonApi.md#award) | **GET** /api/v1/people/{personId}/awards | View a player&#x27;s awards
[**current_game_stats**](PersonApi.md#current_game_stats) | **GET** /api/v1/people/changes | View a player&#x27;s change log
[**free_agents**](PersonApi.md#free_agents) | **GET** /api/v1/people/freeAgents | Get free agents
[**person**](PersonApi.md#person) | **GET** /api/v1/people/{personId} | View a player
[**person1**](PersonApi.md#person1) | **GET** /api/v1/people | View a player
[**player_game_stats**](PersonApi.md#player_game_stats) | **GET** /api/v1/people/{personId}/stats/game/{gamePk} | View a player&#x27;s game stats
[**search**](PersonApi.md#search) | **GET** /api/v1/people/search | Search for a player by name
[**stats3**](PersonApi.md#stats3) | **GET** /api/v1/people/{personId}/stats | View a players stats
[**stats_metrics**](PersonApi.md#stats_metrics) | **GET** /api/v1/people/{personId}/stats/metrics | View a player&#x27;s stat metrics

# **award**
> AwardsRestObject award(person_id, fields=fields)

View a player's awards

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PersonApi()
person_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a player's awards
    api_response = api_instance.award(person_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->award: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**AwardsRestObject**](AwardsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **current_game_stats**
> PeopleRestObject current_game_stats(updated_since, limit=limit, offset=offset, accent=accent, fields=fields)

View a player's change log

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PersonApi()
updated_since = '2013-10-20T19:20:30+01:00' # datetime | Format: YYYY-MM-DDTHH:MM:SSZ
limit = 56 # int | Number of results to return (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a player's change log
    api_response = api_instance.current_game_stats(updated_since, limit=limit, offset=offset, accent=accent, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->current_game_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_since** | **datetime**| Format: YYYY-MM-DDTHH:MM:SSZ | 
 **limit** | **int**| Number of results to return | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**PeopleRestObject**](PeopleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **free_agents**
> FreeAgentListRestObject free_agents(season, order=order, accent=accent, fields=fields)

Get free agents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PersonApi()
season = 'season_example' # str | Season of play
order = swagger_client.SortOrderEnum() # SortOrderEnum | The order of sorting, ascending or descending (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    # Get free agents
    api_response = api_instance.free_agents(season, order=order, accent=accent, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->free_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **str**| Season of play | 
 **order** | [**SortOrderEnum**](.md)| The order of sorting, ascending or descending | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**FreeAgentListRestObject**](FreeAgentListRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person**
> PeopleRestObject person(person_id, person_ids=person_ids, accent=accent, season=season, group=group, fields=fields)

View a player

This endpoint allows you to pull the information of players

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PersonApi()
person_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc
person_ids = [56] # list[int] | Comma delimited list of person ID. Format: 1234, 2345 (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)
season = 'season_example' # str | Season of play (optional)
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a player
    api_response = api_instance.person(person_id, person_ids=person_ids, accent=accent, season=season, group=group, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | 
 **person_ids** | [**list[int]**](int.md)| Comma delimited list of person ID. Format: 1234, 2345 | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 
 **season** | **str**| Season of play | [optional] 
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**PeopleRestObject**](PeopleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person1**
> PeopleRestObject person1(person_id, person_ids=person_ids, accent=accent, season=season, group=group, fields=fields)

View a player

This endpoint allows you to pull the information of players

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PersonApi()
person_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc
person_ids = [56] # list[int] | Comma delimited list of person ID. Format: 1234, 2345 (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)
season = 'season_example' # str | Season of play (optional)
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a player
    api_response = api_instance.person1(person_id, person_ids=person_ids, accent=accent, season=season, group=group, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->person1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | 
 **person_ids** | [**list[int]**](int.md)| Comma delimited list of person ID. Format: 1234, 2345 | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 
 **season** | **str**| Season of play | [optional] 
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**PeopleRestObject**](PeopleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_game_stats**
> StatsRestObject player_game_stats(person_id, game_pk, group=group, fields=fields)

View a player's game stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PersonApi()
person_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc
game_pk = 56 # int | Unique Primary Key Representing a Game
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a player's game stats
    api_response = api_instance.player_game_stats(person_id, game_pk, group=group, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->player_game_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | 
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**StatsRestObject**](StatsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> PeopleRestObject search(names=names, person_ids=person_ids, sport_ids=sport_ids, league_ids=league_ids, team_ids=team_ids, league_list_id=league_list_id, active=active, verified=verified, rookie=rookie, seasons=seasons, fields=fields, accent=accent, limit=limit)

Search for a player by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PersonApi()
names = ['names_example'] # list[str] | Name a player uses (optional)
person_ids = [56] # list[int] | Comma delimited list of person ID. Format: 1234, 2345 (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
team_ids = [56] # list[int] | Comma delimited list of Unique Team identifiers (optional)
league_list_id = swagger_client.LeagueListsEnum() # LeagueListsEnum | Unique League List Identifier (optional)
active = true # bool | Whether or not a player is active (optional)
verified = true # bool | Complete and confirmed all biographical data (optional)
rookie = true # bool | Whether or not a player is a rookie (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)
limit = 56 # int | Number of results to return (optional)

try:
    # Search for a player by name
    api_response = api_instance.search(names=names, person_ids=person_ids, sport_ids=sport_ids, league_ids=league_ids, team_ids=team_ids, league_list_id=league_list_id, active=active, verified=verified, rookie=rookie, seasons=seasons, fields=fields, accent=accent, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| Name a player uses | [optional] 
 **person_ids** | [**list[int]**](int.md)| Comma delimited list of person ID. Format: 1234, 2345 | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **team_ids** | [**list[int]**](int.md)| Comma delimited list of Unique Team identifiers | [optional] 
 **league_list_id** | [**LeagueListsEnum**](.md)| Unique League List Identifier | [optional] 
 **active** | **bool**| Whether or not a player is active | [optional] 
 **verified** | **bool**| Complete and confirmed all biographical data | [optional] 
 **rookie** | **bool**| Whether or not a player is a rookie | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 
 **limit** | **int**| Number of results to return | [optional] 

### Return type

[**PeopleRestObject**](PeopleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats3**
> StatsRestObject stats3(person_id, stats, group=group, season=season, seasons=seasons, sport_id=sport_id, opposing_team_id=opposing_team_id, opposing_player_id=opposing_player_id, metrics=metrics, league_id=league_id, league_list_id=league_list_id, sit_codes=sit_codes, combine_sits=combine_sits, start_date=start_date, end_date=end_date, days_back=days_back, games_back=games_back, limit=limit, event_type=event_type, pitch_type=pitch_type, hit_trajectory=hit_trajectory, bat_side=bat_side, game_type=game_type, group_by=group_by, accent=accent, fields=fields)

View a players stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PersonApi()
person_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc
stats = [swagger_client.StatType()] # list[StatType] | Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
opposing_team_id = 56 # int | A unique identifier for the opposing team. Must be used with Team ID (optional)
opposing_player_id = 56 # int | A unique identifier for the opposing team (optional)
metrics = [swagger_client.MetricType()] # list[MetricType] | Name of metric(s) for metric log stats.  Available metrics in /api/v1/metrics (optional)
league_id = 56 # int | Unique League Identifier (optional)
league_list_id = swagger_client.LeagueListsEnum() # LeagueListsEnum | Unique League List Identifier (optional)
sit_codes = ['sit_codes_example'] # list[str] | Situation code for a given stat split. (optional)
combine_sits = true # bool | If true, gathers stats where all of the situational criteria are met. If false, returns stats where any of the situational criteria are met. Default: false (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
days_back = 56 # int | Returns results from the last 'X' days (Starting from yesterday). (optional)
games_back = 56 # int | Returns results from the last 'X' games played. (optional)
limit = 56 # int | Number of results to return (optional)
event_type = [swagger_client.EventType()] # list[EventType] | Type of event (optional)
pitch_type = ['pitch_type_example'] # list[str] | Classification of pitch (fastball, curveball, etc...) (optional)
hit_trajectory = [swagger_client.HitTrajectory()] # list[HitTrajectory] | Trajectory of hit (line drive, fly ball, etc...) (optional)
bat_side = 'bat_side_example' # str | Bat side of hitter (optional)
game_type = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Type of Game. Available types in /api/v1/gameTypes (optional)
group_by = [swagger_client.GroupByEnum()] # list[GroupByEnum] | Group stats by PLAYER, TEAM, SEASON, VENUE, SPORT or STAT_GROUP (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a players stats
    api_response = api_instance.stats3(person_id, stats, group=group, season=season, seasons=seasons, sport_id=sport_id, opposing_team_id=opposing_team_id, opposing_player_id=opposing_player_id, metrics=metrics, league_id=league_id, league_list_id=league_list_id, sit_codes=sit_codes, combine_sits=combine_sits, start_date=start_date, end_date=end_date, days_back=days_back, games_back=games_back, limit=limit, event_type=event_type, pitch_type=pitch_type, hit_trajectory=hit_trajectory, bat_side=bat_side, game_type=game_type, group_by=group_by, accent=accent, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->stats3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | 
 **stats** | [**list[StatType]**](StatType.md)| Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes | 
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **opposing_team_id** | **int**| A unique identifier for the opposing team. Must be used with Team ID | [optional] 
 **opposing_player_id** | **int**| A unique identifier for the opposing team | [optional] 
 **metrics** | [**list[MetricType]**](MetricType.md)| Name of metric(s) for metric log stats.  Available metrics in /api/v1/metrics | [optional] 
 **league_id** | **int**| Unique League Identifier | [optional] 
 **league_list_id** | [**LeagueListsEnum**](.md)| Unique League List Identifier | [optional] 
 **sit_codes** | [**list[str]**](str.md)| Situation code for a given stat split. | [optional] 
 **combine_sits** | **bool**| If true, gathers stats where all of the situational criteria are met. If false, returns stats where any of the situational criteria are met. Default: false | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **days_back** | **int**| Returns results from the last &#x27;X&#x27; days (Starting from yesterday). | [optional] 
 **games_back** | **int**| Returns results from the last &#x27;X&#x27; games played. | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **event_type** | [**list[EventType]**](EventType.md)| Type of event | [optional] 
 **pitch_type** | [**list[str]**](str.md)| Classification of pitch (fastball, curveball, etc...) | [optional] 
 **hit_trajectory** | [**list[HitTrajectory]**](HitTrajectory.md)| Trajectory of hit (line drive, fly ball, etc...) | [optional] 
 **bat_side** | **str**| Bat side of hitter | [optional] 
 **game_type** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **group_by** | [**list[GroupByEnum]**](GroupByEnum.md)| Group stats by PLAYER, TEAM, SEASON, VENUE, SPORT or STAT_GROUP | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**StatsRestObject**](StatsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_metrics**
> StatsRestObject stats_metrics(person_id, stats, group=group, season=season, seasons=seasons, sport_id=sport_id, opposing_team_id=opposing_team_id, opposing_player_id=opposing_player_id, metrics=metrics, league_id=league_id, league_list_id=league_list_id, sit_codes=sit_codes, combine_sits=combine_sits, start_date=start_date, end_date=end_date, days_back=days_back, games_back=games_back, limit=limit, event_type=event_type, pitch_type=pitch_type, hit_trajectory=hit_trajectory, bat_side=bat_side, game_type=game_type, group_by=group_by, accent=accent, fields=fields)

View a player's stat metrics

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
api_instance = swagger_client.PersonApi(swagger_client.ApiClient(configuration))
person_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc
stats = [swagger_client.StatType()] # list[StatType] | Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
opposing_team_id = 56 # int | A unique identifier for the opposing team. Must be used with Team ID (optional)
opposing_player_id = 56 # int | A unique identifier for the opposing team (optional)
metrics = [swagger_client.MetricType()] # list[MetricType] | Name of metric(s) for metric log stats.  Available metrics in /api/v1/metrics (optional)
league_id = 56 # int | Unique League Identifier (optional)
league_list_id = swagger_client.LeagueListsEnum() # LeagueListsEnum | Unique League List Identifier (optional)
sit_codes = ['sit_codes_example'] # list[str] | Situation code for a given stat split. (optional)
combine_sits = true # bool | If true, gathers stats where all of the situational criteria are met. If false, returns stats where any of the situational criteria are met. Default: false (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
days_back = 56 # int | Returns results from the last 'X' days (Starting from yesterday). (optional)
games_back = 56 # int | Returns results from the last 'X' games played. (optional)
limit = 56 # int | Number of results to return (optional)
event_type = [swagger_client.EventType()] # list[EventType] | Type of event (optional)
pitch_type = ['pitch_type_example'] # list[str] | Classification of pitch (fastball, curveball, etc...) (optional)
hit_trajectory = [swagger_client.HitTrajectory()] # list[HitTrajectory] | Trajectory of hit (line drive, fly ball, etc...) (optional)
bat_side = 'bat_side_example' # str | Bat side of hitter (optional)
game_type = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Type of Game. Available types in /api/v1/gameTypes (optional)
group_by = [swagger_client.GroupByEnum()] # list[GroupByEnum] | Group stats by PLAYER, TEAM, SEASON, VENUE, SPORT or STAT_GROUP (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a player's stat metrics
    api_response = api_instance.stats_metrics(person_id, stats, group=group, season=season, seasons=seasons, sport_id=sport_id, opposing_team_id=opposing_team_id, opposing_player_id=opposing_player_id, metrics=metrics, league_id=league_id, league_list_id=league_list_id, sit_codes=sit_codes, combine_sits=combine_sits, start_date=start_date, end_date=end_date, days_back=days_back, games_back=games_back, limit=limit, event_type=event_type, pitch_type=pitch_type, hit_trajectory=hit_trajectory, bat_side=bat_side, game_type=game_type, group_by=group_by, accent=accent, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->stats_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | 
 **stats** | [**list[StatType]**](StatType.md)| Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes | 
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **opposing_team_id** | **int**| A unique identifier for the opposing team. Must be used with Team ID | [optional] 
 **opposing_player_id** | **int**| A unique identifier for the opposing team | [optional] 
 **metrics** | [**list[MetricType]**](MetricType.md)| Name of metric(s) for metric log stats.  Available metrics in /api/v1/metrics | [optional] 
 **league_id** | **int**| Unique League Identifier | [optional] 
 **league_list_id** | [**LeagueListsEnum**](.md)| Unique League List Identifier | [optional] 
 **sit_codes** | [**list[str]**](str.md)| Situation code for a given stat split. | [optional] 
 **combine_sits** | **bool**| If true, gathers stats where all of the situational criteria are met. If false, returns stats where any of the situational criteria are met. Default: false | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **days_back** | **int**| Returns results from the last &#x27;X&#x27; days (Starting from yesterday). | [optional] 
 **games_back** | **int**| Returns results from the last &#x27;X&#x27; games played. | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **event_type** | [**list[EventType]**](EventType.md)| Type of event | [optional] 
 **pitch_type** | [**list[str]**](str.md)| Classification of pitch (fastball, curveball, etc...) | [optional] 
 **hit_trajectory** | [**list[HitTrajectory]**](HitTrajectory.md)| Trajectory of hit (line drive, fly ball, etc...) | [optional] 
 **bat_side** | **str**| Bat side of hitter | [optional] 
 **game_type** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **group_by** | [**list[GroupByEnum]**](GroupByEnum.md)| Group stats by PLAYER, TEAM, SEASON, VENUE, SPORT or STAT_GROUP | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**StatsRestObject**](StatsRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

