# swagger_client.TeamsApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**affiliates**](TeamsApi.md#affiliates) | **GET** /api/v1/teams/{teamId}/affiliates | View team and affiliate teams
[**affiliates1**](TeamsApi.md#affiliates1) | **GET** /api/v1/teams/affiliates | View team and affiliate teams
[**all_teams**](TeamsApi.md#all_teams) | **GET** /api/v1/teams/{teamId}/history | View historical records for a list of teams
[**all_teams1**](TeamsApi.md#all_teams1) | **GET** /api/v1/teams/history | View historical records for a list of teams
[**alumni**](TeamsApi.md#alumni) | **GET** /api/v1/teams/{teamId}/alumni | View all team alumni
[**coaches**](TeamsApi.md#coaches) | **GET** /api/v1/teams/{teamId}/coaches | View all coaches for a team
[**leaders**](TeamsApi.md#leaders) | **GET** /api/v1/teams/{teamId}/leaders | View team stat leaders
[**leaders1**](TeamsApi.md#leaders1) | **GET** /api/v1/teams/stats/leaders | View leaders for team stats
[**personnel**](TeamsApi.md#personnel) | **GET** /api/v1/teams/{teamId}/personnel | View all coaches for a team
[**roster**](TeamsApi.md#roster) | **GET** /api/v1/teams/{teamId}/roster | View a teams roster
[**roster1**](TeamsApi.md#roster1) | **GET** /api/v1/teams/{teamId}/roster/{rosterType} | View a teams roster
[**stats**](TeamsApi.md#stats) | **GET** /api/v1/teams/{teamId}/stats | View a teams stats
[**stats1**](TeamsApi.md#stats1) | **GET** /api/v1/teams/stats | View a teams stats
[**teams**](TeamsApi.md#teams) | **GET** /api/v1/teams | View info for all teams
[**teams1**](TeamsApi.md#teams1) | **GET** /api/v1/teams/{teamId} | View info for all teams
[**update_alumni**](TeamsApi.md#update_alumni) | **POST** /api/v1/teams/{teamId}/alumni | 

# **affiliates**
> TeamsRestObject affiliates(team_id, team_ids=team_ids, sport_id=sport_id, season=season, game_type=game_type, fields=fields)

View team and affiliate teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
team_ids = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
season = 'season_example' # str | Season of play (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View team and affiliate teams
    api_response = api_instance.affiliates(team_id, team_ids=team_ids, sport_id=sport_id, season=season, game_type=game_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->affiliates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **team_ids** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **season** | **str**| Season of play | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**TeamsRestObject**](TeamsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliates1**
> TeamsRestObject affiliates1(team_id, team_ids=team_ids, sport_id=sport_id, season=season, game_type=game_type, fields=fields)

View team and affiliate teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
team_ids = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
season = 'season_example' # str | Season of play (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View team and affiliate teams
    api_response = api_instance.affiliates1(team_id, team_ids=team_ids, sport_id=sport_id, season=season, game_type=game_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->affiliates1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **team_ids** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **season** | **str**| Season of play | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**TeamsRestObject**](TeamsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_teams**
> TeamsRestObject all_teams(team_id, team_ids=team_ids, start_season=start_season, end_season=end_season, fields=fields)

View historical records for a list of teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
team_ids = [56] # list[int] | Comma delimited list of Unique Team identifiers (optional)
start_season = 'start_season_example' # str | Start date for range of data (used with end date optionally). Example: '2018' or '2018.2' (optional)
end_season = 'end_season_example' # str | End date for range of data (used with start date optionally). Format: '2018' or '2018.2' (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    # View historical records for a list of teams
    api_response = api_instance.all_teams(team_id, team_ids=team_ids, start_season=start_season, end_season=end_season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->all_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **team_ids** | [**list[int]**](int.md)| Comma delimited list of Unique Team identifiers | [optional] 
 **start_season** | **str**| Start date for range of data (used with end date optionally). Example: &#x27;2018&#x27; or &#x27;2018.2&#x27; | [optional] 
 **end_season** | **str**| End date for range of data (used with start date optionally). Format: &#x27;2018&#x27; or &#x27;2018.2&#x27; | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**TeamsRestObject**](TeamsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_teams1**
> TeamsRestObject all_teams1(team_id, team_ids=team_ids, start_season=start_season, end_season=end_season, fields=fields)

View historical records for a list of teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
team_ids = [56] # list[int] | Comma delimited list of Unique Team identifiers (optional)
start_season = 'start_season_example' # str | Start date for range of data (used with end date optionally). Example: '2018' or '2018.2' (optional)
end_season = 'end_season_example' # str | End date for range of data (used with start date optionally). Format: '2018' or '2018.2' (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    # View historical records for a list of teams
    api_response = api_instance.all_teams1(team_id, team_ids=team_ids, start_season=start_season, end_season=end_season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->all_teams1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **team_ids** | [**list[int]**](int.md)| Comma delimited list of Unique Team identifiers | [optional] 
 **start_season** | **str**| Start date for range of data (used with end date optionally). Example: &#x27;2018&#x27; or &#x27;2018.2&#x27; | [optional] 
 **end_season** | **str**| End date for range of data (used with start date optionally). Format: &#x27;2018&#x27; or &#x27;2018.2&#x27; | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**TeamsRestObject**](TeamsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alumni**
> PeopleRestObject alumni(team_id, season, group=group, fields=fields)

View all team alumni

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
season = 'season_example' # str | Season of play
group = swagger_client.StatGroup() # StatGroup | Category of statistic to return. Available types in /api/v1/statGroups (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    # View all team alumni
    api_response = api_instance.alumni(team_id, season, group=group, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->alumni: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **season** | **str**| Season of play | 
 **group** | [**StatGroup**](.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**PeopleRestObject**](PeopleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaches**
> RosterRestObject coaches(team_id, season=season, _date=_date, fields=fields)

View all coaches for a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
season = 'season_example' # str | Season of play (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    # View all coaches for a team
    api_response = api_instance.coaches(team_id, season=season, _date=_date, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->coaches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **season** | **str**| Season of play | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**RosterRestObject**](RosterRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaders**
> TeamLeaderContainerRestObject leaders(team_id, leader_categories=leader_categories, season=season, leader_game_types=leader_game_types, expand=expand, limit=limit, offset=offset, player_pool=player_pool, fields=fields)

View team stat leaders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | 
leader_categories = [swagger_client.PersonLeadersEnum()] # list[PersonLeadersEnum] |  (optional)
season = 'season_example' # str |  (optional)
leader_game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] |  (optional)
expand = [swagger_client.ExpandEnum()] # list[ExpandEnum] |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
player_pool = swagger_client.PlayerPoolEnum() # PlayerPoolEnum |  (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    # View team stat leaders
    api_response = api_instance.leaders(team_id, leader_categories=leader_categories, season=season, leader_game_types=leader_game_types, expand=expand, limit=limit, offset=offset, player_pool=player_pool, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->leaders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | 
 **leader_categories** | [**list[PersonLeadersEnum]**](PersonLeadersEnum.md)|  | [optional] 
 **season** | **str**|  | [optional] 
 **leader_game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)|  | [optional] 
 **expand** | [**list[ExpandEnum]**](ExpandEnum.md)|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **player_pool** | [**PlayerPoolEnum**](.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**TeamLeaderContainerRestObject**](TeamLeaderContainerRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaders1**
> LeagueLeaderContainerRestObject leaders1(leader_categories=leader_categories, game_types=game_types, stats=stats, stat_type=stat_type, sport_id=sport_id, sport_ids=sport_ids, league_id=league_id, league_ids=league_ids, season=season, stat_group=stat_group, group=group, start_date=start_date, end_date=end_date, days_back=days_back, sit_codes=sit_codes, opposing_team_id=opposing_team_id, limit=limit, offset=offset, fields=fields)

View leaders for team stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
leader_categories = [swagger_client.PersonLeadersEnum()] # list[PersonLeadersEnum] | TBD (optional)
game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Type of Game. Available types in /api/v1/gameTypes (optional)
stats = [swagger_client.StatType()] # list[StatType] | Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes (optional)
stat_type = swagger_client.StatType() # StatType |  (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
league_id = 56 # int | Unique League Identifier (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
season = 'season_example' # str | Season of play (optional)
stat_group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups (optional)
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
days_back = 56 # int | Returns results from the last 'X' days (Starting from yesterday). (optional)
sit_codes = 'sit_codes_example' # str | Situation code for a given stat split. (optional)
opposing_team_id = 56 # int | A unique identifier for the opposing team. Must be used with Team ID (optional)
limit = 56 # int | Number of results to return (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    # View leaders for team stats
    api_response = api_instance.leaders1(leader_categories=leader_categories, game_types=game_types, stats=stats, stat_type=stat_type, sport_id=sport_id, sport_ids=sport_ids, league_id=league_id, league_ids=league_ids, season=season, stat_group=stat_group, group=group, start_date=start_date, end_date=end_date, days_back=days_back, sit_codes=sit_codes, opposing_team_id=opposing_team_id, limit=limit, offset=offset, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->leaders1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leader_categories** | [**list[PersonLeadersEnum]**](PersonLeadersEnum.md)| TBD | [optional] 
 **game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **stats** | [**list[StatType]**](StatType.md)| Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes | [optional] 
 **stat_type** | [**StatType**](.md)|  | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **league_id** | **int**| Unique League Identifier | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **season** | **str**| Season of play | [optional] 
 **stat_group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **days_back** | **int**| Returns results from the last &#x27;X&#x27; days (Starting from yesterday). | [optional] 
 **sit_codes** | **str**| Situation code for a given stat split. | [optional] 
 **opposing_team_id** | **int**| A unique identifier for the opposing team. Must be used with Team ID | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**LeagueLeaderContainerRestObject**](LeagueLeaderContainerRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **personnel**
> RosterRestObject personnel(team_id, season=season, _date=_date, fields=fields)

View all coaches for a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
season = 'season_example' # str | Season of play (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    # View all coaches for a team
    api_response = api_instance.personnel(team_id, season=season, _date=_date, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->personnel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **season** | **str**| Season of play | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**RosterRestObject**](RosterRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roster**
> RosterRestObject roster(team_id, roster_type, season=season, _date=_date, game_type=game_type, fields=fields)

View a teams roster

This endpoint allows you to pull teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
roster_type = 'roster_type_example' # str | Type of roster. Available types in /api/v1/rosterTypes
season = 'season_example' # str | Season of play (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a teams roster
    api_response = api_instance.roster(team_id, roster_type, season=season, _date=_date, game_type=game_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->roster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **roster_type** | **str**| Type of roster. Available types in /api/v1/rosterTypes | 
 **season** | **str**| Season of play | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**RosterRestObject**](RosterRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roster1**
> RosterRestObject roster1(team_id, roster_type, season=season, _date=_date, game_type=game_type, fields=fields)

View a teams roster

This endpoint allows you to pull teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
roster_type = 'roster_type_example' # str | Type of roster. Available types in /api/v1/rosterTypes
season = 'season_example' # str | Season of play (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a teams roster
    api_response = api_instance.roster1(team_id, roster_type, season=season, _date=_date, game_type=game_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->roster1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **roster_type** | **str**| Type of roster. Available types in /api/v1/rosterTypes | 
 **season** | **str**| Season of play | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**RosterRestObject**](RosterRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats**
> StatsRestObject stats(team_id, group, sport_id=sport_id, season=season, game_type=game_type, stats=stats, sort_stat=sort_stat, order=order, group_by=group_by, opposing_team_id=opposing_team_id, opposing_player_id=opposing_player_id, sit_codes=sit_codes, start_date=start_date, end_date=end_date, fields=fields)

View a teams stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups
sport_id = 56 # int | Top level organization of a sport (optional)
season = 'season_example' # str | Season of play (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
stats = [swagger_client.StatType()] # list[StatType] | Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes (optional)
sort_stat = swagger_client.BaseballStatsEnum() # BaseballStatsEnum | Baseball stat to sort splits by. (optional)
order = swagger_client.SortOrderEnum() # SortOrderEnum | The order of sorting, ascending or descending (optional)
group_by = [swagger_client.GroupByEnum()] # list[GroupByEnum] | Group stats by PLAYER, TEAM, SEASON, VENUE, SPORT or STAT_GROUP (optional)
opposing_team_id = 56 # int | A unique identifier for the opposing team. Must be used with Team ID (optional)
opposing_player_id = 56 # int | A unique identifier for the opposing team (optional)
sit_codes = 'sit_codes_example' # str | Situation code for a given stat split. (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a teams stats
    api_response = api_instance.stats(team_id, group, sport_id=sport_id, season=season, game_type=game_type, stats=stats, sort_stat=sort_stat, order=order, group_by=group_by, opposing_team_id=opposing_team_id, opposing_player_id=opposing_player_id, sit_codes=sit_codes, start_date=start_date, end_date=end_date, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **season** | **str**| Season of play | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **stats** | [**list[StatType]**](StatType.md)| Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes | [optional] 
 **sort_stat** | [**BaseballStatsEnum**](.md)| Baseball stat to sort splits by. | [optional] 
 **order** | [**SortOrderEnum**](.md)| The order of sorting, ascending or descending | [optional] 
 **group_by** | [**list[GroupByEnum]**](GroupByEnum.md)| Group stats by PLAYER, TEAM, SEASON, VENUE, SPORT or STAT_GROUP | [optional] 
 **opposing_team_id** | **int**| A unique identifier for the opposing team. Must be used with Team ID | [optional] 
 **opposing_player_id** | **int**| A unique identifier for the opposing team | [optional] 
 **sit_codes** | **str**| Situation code for a given stat split. | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**StatsRestObject**](StatsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats1**
> StatsRestObject stats1(group, game_type=game_type, stats=stats, sport_id=sport_id, sport_ids=sport_ids, league_ids=league_ids, season=season, sort_stat=sort_stat, order=order, start_date=start_date, end_date=end_date, days_back=days_back, sit_codes=sit_codes, combine_sits=combine_sits, opposing_team_id=opposing_team_id, offset=offset, limit=limit, fields=fields)

View a teams stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
stats = [swagger_client.StatType()] # list[StatType] | Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
season = 'season_example' # str | Season of play (optional)
sort_stat = swagger_client.BaseballStatsEnum() # BaseballStatsEnum | Baseball stat to sort splits by. (optional)
order = swagger_client.SortOrderEnum() # SortOrderEnum | The order of sorting, ascending or descending (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
days_back = 56 # int | Returns results from the last 'X' days (Starting from yesterday). (optional)
sit_codes = 'sit_codes_example' # str | Situation code for a given stat split. (optional)
combine_sits = true # bool | If true, gathers stats where all of the situational criteria are met. If false, returns stats where any of the situational criteria are met. Default: false (optional)
opposing_team_id = 56 # int | A unique identifier for the opposing team. Must be used with Team ID (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
limit = 56 # int | Number of results to return (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    # View a teams stats
    api_response = api_instance.stats1(group, game_type=game_type, stats=stats, sport_id=sport_id, sport_ids=sport_ids, league_ids=league_ids, season=season, sort_stat=sort_stat, order=order, start_date=start_date, end_date=end_date, days_back=days_back, sit_codes=sit_codes, combine_sits=combine_sits, opposing_team_id=opposing_team_id, offset=offset, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->stats1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **stats** | [**list[StatType]**](StatType.md)| Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **season** | **str**| Season of play | [optional] 
 **sort_stat** | [**BaseballStatsEnum**](.md)| Baseball stat to sort splits by. | [optional] 
 **order** | [**SortOrderEnum**](.md)| The order of sorting, ascending or descending | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **days_back** | **int**| Returns results from the last &#x27;X&#x27; days (Starting from yesterday). | [optional] 
 **sit_codes** | **str**| Situation code for a given stat split. | [optional] 
 **combine_sits** | **bool**| If true, gathers stats where all of the situational criteria are met. If false, returns stats where any of the situational criteria are met. Default: false | [optional] 
 **opposing_team_id** | **int**| A unique identifier for the opposing team. Must be used with Team ID | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**StatsRestObject**](StatsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams**
> TeamsRestObject teams(team_id, season=season, sport_id=sport_id, division_id=division_id, game_type=game_type, league_ids=league_ids, sport_ids=sport_ids, active_status=active_status, league_list_id=league_list_id, all_star_statuses=all_star_statuses, fields=fields)

View info for all teams

This endpoint allows you to pull teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
season = 'season_example' # str | Season of play (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
division_id = 56 # int | Unique Division Identifier (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
active_status = swagger_client.TeamActiveStatusEnum() # TeamActiveStatusEnum | Flag for fetching teams that are currently active (Y), inactive (N), pending (P), or all teams (B) (optional)
league_list_id = swagger_client.LeagueListsEnum() # LeagueListsEnum | Unique League List Identifier (optional)
all_star_statuses = [swagger_client.AllStarEnum()] # list[AllStarEnum] |  (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View info for all teams
    api_response = api_instance.teams(team_id, season=season, sport_id=sport_id, division_id=division_id, game_type=game_type, league_ids=league_ids, sport_ids=sport_ids, active_status=active_status, league_list_id=league_list_id, all_star_statuses=all_star_statuses, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **season** | **str**| Season of play | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **division_id** | **int**| Unique Division Identifier | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **active_status** | [**TeamActiveStatusEnum**](.md)| Flag for fetching teams that are currently active (Y), inactive (N), pending (P), or all teams (B) | [optional] 
 **league_list_id** | [**LeagueListsEnum**](.md)| Unique League List Identifier | [optional] 
 **all_star_statuses** | [**list[AllStarEnum]**](AllStarEnum.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**TeamsRestObject**](TeamsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams1**
> TeamsRestObject teams1(team_id, season=season, sport_id=sport_id, division_id=division_id, game_type=game_type, league_ids=league_ids, sport_ids=sport_ids, active_status=active_status, league_list_id=league_list_id, all_star_statuses=all_star_statuses, fields=fields)

View info for all teams

This endpoint allows you to pull teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
season = 'season_example' # str | Season of play (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
division_id = 56 # int | Unique Division Identifier (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
active_status = swagger_client.TeamActiveStatusEnum() # TeamActiveStatusEnum | Flag for fetching teams that are currently active (Y), inactive (N), pending (P), or all teams (B) (optional)
league_list_id = swagger_client.LeagueListsEnum() # LeagueListsEnum | Unique League List Identifier (optional)
all_star_statuses = [swagger_client.AllStarEnum()] # list[AllStarEnum] |  (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View info for all teams
    api_response = api_instance.teams1(team_id, season=season, sport_id=sport_id, division_id=division_id, game_type=game_type, league_ids=league_ids, sport_ids=sport_ids, active_status=active_status, league_list_id=league_list_id, all_star_statuses=all_star_statuses, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **season** | **str**| Season of play | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **division_id** | **int**| Unique Division Identifier | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **active_status** | [**TeamActiveStatusEnum**](.md)| Flag for fetching teams that are currently active (Y), inactive (N), pending (P), or all teams (B) | [optional] 
 **league_list_id** | [**LeagueListsEnum**](.md)| Unique League List Identifier | [optional] 
 **all_star_statuses** | [**list[AllStarEnum]**](AllStarEnum.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**TeamsRestObject**](TeamsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alumni**
> str update_alumni(team_id, season, group=group, fields=fields)



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
api_instance = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc
season = 'season_example' # str | Season of play
group = swagger_client.StatGroup() # StatGroup | Category of statistic to return. Available types in /api/v1/statGroups (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    api_response = api_instance.update_alumni(team_id, season, group=group, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_alumni: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | 
 **season** | **str**| Season of play | 
 **group** | [**StatGroup**](.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

