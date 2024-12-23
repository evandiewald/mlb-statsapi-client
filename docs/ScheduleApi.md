# swagger_client.ScheduleApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postseason_schedule**](ScheduleApi.md#postseason_schedule) | **GET** /api/v1/schedule/postseason | Get postseason schedule
[**postseason_schedule_series**](ScheduleApi.md#postseason_schedule_series) | **GET** /api/v1/schedule/postseason/series | Get postseason series schedules
[**schedule**](ScheduleApi.md#schedule) | **GET** /api/v1/schedule | View schedule info based on scheduleType.
[**schedule1**](ScheduleApi.md#schedule1) | **GET** /api/v1/schedule/{scheduleType} | View schedule info based on scheduleType.
[**tie_games**](ScheduleApi.md#tie_games) | **GET** /api/v1/schedule/games/tied | Get tied game schedules
[**tracking_events_schedule**](ScheduleApi.md#tracking_events_schedule) | **GET** /api/v1/schedule/trackingEvents | Get tracking event schedules
[**tune_in**](ScheduleApi.md#tune_in) | **GET** /api/v1/schedule/postseason/tuneIn | Get postseason TuneIn schedules

# **postseason_schedule**
> ScheduleRestObject postseason_schedule(game_types=game_types, series_number=series_number, team_id=team_id, sport_id=sport_id, use_latest_games=use_latest_games, use_featured_game=use_featured_game, season=season, public_facing=public_facing, fields=fields)

Get postseason schedule

This endpoint allows you to pull postseason schedules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduleApi()
game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Comma delimited list of type of Game. Available types in /api/v1/gameTypes (optional)
series_number = 56 # int |  (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
sport_id = 56 # int | Unique League Identifier (optional)
use_latest_games = true # bool |  (optional)
use_featured_game = true # bool |  (optional)
season = 'season_example' # str |  (optional)
public_facing = swagger_client.PublicFacingEnum() # PublicFacingEnum | Return public, non-public or all games. Format: Public Facing = 'Y', Non-Public Facing = 'N', All = 'A' (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get postseason schedule
    api_response = api_instance.postseason_schedule(game_types=game_types, series_number=series_number, team_id=team_id, sport_id=sport_id, use_latest_games=use_latest_games, use_featured_game=use_featured_game, season=season, public_facing=public_facing, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->postseason_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Comma delimited list of type of Game. Available types in /api/v1/gameTypes | [optional] 
 **series_number** | **int**|  | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **sport_id** | **int**| Unique League Identifier | [optional] 
 **use_latest_games** | **bool**|  | [optional] 
 **use_featured_game** | **bool**|  | [optional] 
 **season** | **str**|  | [optional] 
 **public_facing** | [**PublicFacingEnum**](.md)| Return public, non-public or all games. Format: Public Facing &#x3D; &#x27;Y&#x27;, Non-Public Facing &#x3D; &#x27;N&#x27;, All &#x3D; &#x27;A&#x27; | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**ScheduleRestObject**](ScheduleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postseason_schedule_series**
> PostseasonScheduleRestObject postseason_schedule_series(game_types=game_types, series_number=series_number, team_id=team_id, sport_id=sport_id, _date=_date, start_date=start_date, end_date=end_date, use_latest_games=use_latest_games, use_featured_game=use_featured_game, season=season, fields=fields)

Get postseason series schedules

This endpoint allows you to pull postseason schedules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduleApi()
game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Comma delimited list of type of Game. Available types in /api/v1/gameTypes (optional)
series_number = 56 # int |  (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
sport_id = 56 # int | Unique League Identifier (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
use_latest_games = true # bool |  (optional)
use_featured_game = true # bool |  (optional)
season = 'season_example' # str |  (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get postseason series schedules
    api_response = api_instance.postseason_schedule_series(game_types=game_types, series_number=series_number, team_id=team_id, sport_id=sport_id, _date=_date, start_date=start_date, end_date=end_date, use_latest_games=use_latest_games, use_featured_game=use_featured_game, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->postseason_schedule_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Comma delimited list of type of Game. Available types in /api/v1/gameTypes | [optional] 
 **series_number** | **int**|  | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **sport_id** | **int**| Unique League Identifier | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **use_latest_games** | **bool**|  | [optional] 
 **use_featured_game** | **bool**|  | [optional] 
 **season** | **str**|  | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**PostseasonScheduleRestObject**](PostseasonScheduleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule**
> ScheduleRestObject schedule(using_private_endpoint, calendar_types=calendar_types, event_types=event_types, schedule_event_types=schedule_event_types, team_id=team_id, league_id=league_id, sport_id=sport_id, game_pk=game_pk, game_pks=game_pks, event_ids=event_ids, venue_ids=venue_ids, performer_ids=performer_ids, game_types=game_types, game_type=game_type, season=season, seasons=seasons, _date=_date, start_date=start_date, end_date=end_date, timecode=timecode, use_latest_games=use_latest_games, opponent_id=opponent_id, public_facing=public_facing, fields=fields)

View schedule info based on scheduleType.

View schedule info. This endpoint allows you to pull schedules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduleApi()
using_private_endpoint = true # bool | 
calendar_types = [swagger_client.CalendarTypes()] # list[CalendarTypes] | Comma delimited list of type of calendar types (optional)
event_types = [swagger_client.CalendarTypes()] # list[CalendarTypes] | Comma delimited list of type of events. <b>Note: Don't Use. This will be deprecated in favor of calendarTypes</b> (optional)
schedule_event_types = [swagger_client.ScheduleEventTypes()] # list[ScheduleEventTypes] | Comma delimited list of type of event types (optional)
team_id = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
league_id = [56] # list[int] | Unique League Identifier (optional)
sport_id = [56] # list[int] | Top level organization of a sport (optional)
game_pk = 56 # int | Unique Primary Key Representing a Game (optional)
game_pks = [56] # list[int] | Comma delimited list of unique primary keys (optional)
event_ids = [56] # list[int] | A unique identifier for non-game event (optional)
venue_ids = [56] # list[int] | Unique Venue Identifier (optional)
performer_ids = [56] # list[int] | A unique identifier for non-team event performers (optional)
game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Comma delimited list of type of Game. Available types in /api/v1/gameTypes (optional)
game_type = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Type of Game. Available types in /api/v1/gameTypes (optional)
season = ['season_example'] # list[str] | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
timecode = 'timecode_example' # str | Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS (optional)
use_latest_games = true # bool |  (optional)
opponent_id = [56] # list[int] | A unique identifier for the opposing team. Must be used with Team ID (optional)
public_facing = swagger_client.PublicFacingEnum() # PublicFacingEnum | Return public, non-public or all games. Format: Public Facing = 'Y', Non-Public Facing = 'N', All = 'A' (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View schedule info based on scheduleType.
    api_response = api_instance.schedule(using_private_endpoint, calendar_types=calendar_types, event_types=event_types, schedule_event_types=schedule_event_types, team_id=team_id, league_id=league_id, sport_id=sport_id, game_pk=game_pk, game_pks=game_pks, event_ids=event_ids, venue_ids=venue_ids, performer_ids=performer_ids, game_types=game_types, game_type=game_type, season=season, seasons=seasons, _date=_date, start_date=start_date, end_date=end_date, timecode=timecode, use_latest_games=use_latest_games, opponent_id=opponent_id, public_facing=public_facing, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **using_private_endpoint** | **bool**|  | 
 **calendar_types** | [**list[CalendarTypes]**](CalendarTypes.md)| Comma delimited list of type of calendar types | [optional] 
 **event_types** | [**list[CalendarTypes]**](CalendarTypes.md)| Comma delimited list of type of events. &lt;b&gt;Note: Don&#x27;t Use. This will be deprecated in favor of calendarTypes&lt;/b&gt; | [optional] 
 **schedule_event_types** | [**list[ScheduleEventTypes]**](ScheduleEventTypes.md)| Comma delimited list of type of event types | [optional] 
 **team_id** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **league_id** | [**list[int]**](int.md)| Unique League Identifier | [optional] 
 **sport_id** | [**list[int]**](int.md)| Top level organization of a sport | [optional] 
 **game_pk** | **int**| Unique Primary Key Representing a Game | [optional] 
 **game_pks** | [**list[int]**](int.md)| Comma delimited list of unique primary keys | [optional] 
 **event_ids** | [**list[int]**](int.md)| A unique identifier for non-game event | [optional] 
 **venue_ids** | [**list[int]**](int.md)| Unique Venue Identifier | [optional] 
 **performer_ids** | [**list[int]**](int.md)| A unique identifier for non-team event performers | [optional] 
 **game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Comma delimited list of type of Game. Available types in /api/v1/gameTypes | [optional] 
 **game_type** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **season** | [**list[str]**](str.md)| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **timecode** | **str**| Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS | [optional] 
 **use_latest_games** | **bool**|  | [optional] 
 **opponent_id** | [**list[int]**](int.md)| A unique identifier for the opposing team. Must be used with Team ID | [optional] 
 **public_facing** | [**PublicFacingEnum**](.md)| Return public, non-public or all games. Format: Public Facing &#x3D; &#x27;Y&#x27;, Non-Public Facing &#x3D; &#x27;N&#x27;, All &#x3D; &#x27;A&#x27; | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**ScheduleRestObject**](ScheduleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule1**
> ScheduleRestObject schedule1(using_private_endpoint, calendar_types=calendar_types, event_types=event_types, schedule_event_types=schedule_event_types, team_id=team_id, league_id=league_id, sport_id=sport_id, game_pk=game_pk, game_pks=game_pks, event_ids=event_ids, venue_ids=venue_ids, performer_ids=performer_ids, game_types=game_types, game_type=game_type, season=season, seasons=seasons, _date=_date, start_date=start_date, end_date=end_date, timecode=timecode, use_latest_games=use_latest_games, opponent_id=opponent_id, public_facing=public_facing, fields=fields)

View schedule info based on scheduleType.

View schedule info. This endpoint allows you to pull schedules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduleApi()
using_private_endpoint = true # bool | 
calendar_types = [swagger_client.CalendarTypes()] # list[CalendarTypes] | Comma delimited list of type of calendar types (optional)
event_types = [swagger_client.CalendarTypes()] # list[CalendarTypes] | Comma delimited list of type of events. <b>Note: Don't Use. This will be deprecated in favor of calendarTypes</b> (optional)
schedule_event_types = [swagger_client.ScheduleEventTypes()] # list[ScheduleEventTypes] | Comma delimited list of type of event types (optional)
team_id = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
league_id = [56] # list[int] | Unique League Identifier (optional)
sport_id = [56] # list[int] | Top level organization of a sport (optional)
game_pk = 56 # int | Unique Primary Key Representing a Game (optional)
game_pks = [56] # list[int] | Comma delimited list of unique primary keys (optional)
event_ids = [56] # list[int] | A unique identifier for non-game event (optional)
venue_ids = [56] # list[int] | Unique Venue Identifier (optional)
performer_ids = [56] # list[int] | A unique identifier for non-team event performers (optional)
game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Comma delimited list of type of Game. Available types in /api/v1/gameTypes (optional)
game_type = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Type of Game. Available types in /api/v1/gameTypes (optional)
season = ['season_example'] # list[str] | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
timecode = 'timecode_example' # str | Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS (optional)
use_latest_games = true # bool |  (optional)
opponent_id = [56] # list[int] | A unique identifier for the opposing team. Must be used with Team ID (optional)
public_facing = swagger_client.PublicFacingEnum() # PublicFacingEnum | Return public, non-public or all games. Format: Public Facing = 'Y', Non-Public Facing = 'N', All = 'A' (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View schedule info based on scheduleType.
    api_response = api_instance.schedule1(using_private_endpoint, calendar_types=calendar_types, event_types=event_types, schedule_event_types=schedule_event_types, team_id=team_id, league_id=league_id, sport_id=sport_id, game_pk=game_pk, game_pks=game_pks, event_ids=event_ids, venue_ids=venue_ids, performer_ids=performer_ids, game_types=game_types, game_type=game_type, season=season, seasons=seasons, _date=_date, start_date=start_date, end_date=end_date, timecode=timecode, use_latest_games=use_latest_games, opponent_id=opponent_id, public_facing=public_facing, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->schedule1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **using_private_endpoint** | **bool**|  | 
 **calendar_types** | [**list[CalendarTypes]**](CalendarTypes.md)| Comma delimited list of type of calendar types | [optional] 
 **event_types** | [**list[CalendarTypes]**](CalendarTypes.md)| Comma delimited list of type of events. &lt;b&gt;Note: Don&#x27;t Use. This will be deprecated in favor of calendarTypes&lt;/b&gt; | [optional] 
 **schedule_event_types** | [**list[ScheduleEventTypes]**](ScheduleEventTypes.md)| Comma delimited list of type of event types | [optional] 
 **team_id** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **league_id** | [**list[int]**](int.md)| Unique League Identifier | [optional] 
 **sport_id** | [**list[int]**](int.md)| Top level organization of a sport | [optional] 
 **game_pk** | **int**| Unique Primary Key Representing a Game | [optional] 
 **game_pks** | [**list[int]**](int.md)| Comma delimited list of unique primary keys | [optional] 
 **event_ids** | [**list[int]**](int.md)| A unique identifier for non-game event | [optional] 
 **venue_ids** | [**list[int]**](int.md)| Unique Venue Identifier | [optional] 
 **performer_ids** | [**list[int]**](int.md)| A unique identifier for non-team event performers | [optional] 
 **game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Comma delimited list of type of Game. Available types in /api/v1/gameTypes | [optional] 
 **game_type** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **season** | [**list[str]**](str.md)| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **timecode** | **str**| Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS | [optional] 
 **use_latest_games** | **bool**|  | [optional] 
 **opponent_id** | [**list[int]**](int.md)| A unique identifier for the opposing team. Must be used with Team ID | [optional] 
 **public_facing** | [**PublicFacingEnum**](.md)| Return public, non-public or all games. Format: Public Facing &#x3D; &#x27;Y&#x27;, Non-Public Facing &#x3D; &#x27;N&#x27;, All &#x3D; &#x27;A&#x27; | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**ScheduleRestObject**](ScheduleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tie_games**
> ScheduleRestObject tie_games(season, sport_id=sport_id, game_types=game_types, fields=fields)

Get tied game schedules

This endpoint allows you to pull tie game schedules for the given season

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduleApi()
season = 'season_example' # str | Season of play
sport_id = [56] # list[int] | Top level organization of a sport (optional)
game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Comma delimited list of type of Game. Available types in /api/v1/gameTypes (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get tied game schedules
    api_response = api_instance.tie_games(season, sport_id=sport_id, game_types=game_types, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->tie_games: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **str**| Season of play | 
 **sport_id** | [**list[int]**](int.md)| Top level organization of a sport | [optional] 
 **game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Comma delimited list of type of Game. Available types in /api/v1/gameTypes | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**ScheduleRestObject**](ScheduleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracking_events_schedule**
> ScheduleRestObject tracking_events_schedule(calendar_types=calendar_types, event_types=event_types, team_id=team_id, league_id=league_id, sport_id=sport_id, game_pk=game_pk, game_pks=game_pks, event_ids=event_ids, venue_ids=venue_ids, performer_ids=performer_ids, game_types=game_types, game_type=game_type, season=season, seasons=seasons, _date=_date, start_date=start_date, end_date=end_date, timecode=timecode, use_latest_games=use_latest_games, opponent_id=opponent_id, public_facing=public_facing, fields=fields)

Get tracking event schedules

This endpoint allows you to pull schedules for tracking events

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
api_instance = swagger_client.ScheduleApi(swagger_client.ApiClient(configuration))
calendar_types = [swagger_client.CalendarTypes()] # list[CalendarTypes] | Comma delimited list of type of calendar types (optional)
event_types = [swagger_client.CalendarTypes()] # list[CalendarTypes] | Comma delimited list of type of events. <b>Note: Don't Use. This will be deprecated in favor of calendarTypes</b> (optional)
team_id = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
league_id = [56] # list[int] | Unique League Identifier (optional)
sport_id = [56] # list[int] | Top level organization of a sport (optional)
game_pk = 56 # int | Unique Primary Key Representing a Game (optional)
game_pks = [56] # list[int] | Comma delimited list of unique primary keys (optional)
event_ids = [56] # list[int] | A unique identifier for non-game event (optional)
venue_ids = [56] # list[int] | Unique Venue Identifier (optional)
performer_ids = [56] # list[int] | A unique identifier for non-team event performers (optional)
game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Comma delimited list of type of Game. Available types in /api/v1/gameTypes (optional)
game_type = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Type of Game. Available types in /api/v1/gameTypes (optional)
season = ['season_example'] # list[str] | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
timecode = 'timecode_example' # str | Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS (optional)
use_latest_games = true # bool |  (optional)
opponent_id = [56] # list[int] | A unique identifier for the opposing team. Must be used with Team ID (optional)
public_facing = swagger_client.PublicFacingEnum() # PublicFacingEnum | Return public, non-public or all games. Format: Public Facing = 'Y', Non-Public Facing = 'N', All = 'A' (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get tracking event schedules
    api_response = api_instance.tracking_events_schedule(calendar_types=calendar_types, event_types=event_types, team_id=team_id, league_id=league_id, sport_id=sport_id, game_pk=game_pk, game_pks=game_pks, event_ids=event_ids, venue_ids=venue_ids, performer_ids=performer_ids, game_types=game_types, game_type=game_type, season=season, seasons=seasons, _date=_date, start_date=start_date, end_date=end_date, timecode=timecode, use_latest_games=use_latest_games, opponent_id=opponent_id, public_facing=public_facing, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->tracking_events_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_types** | [**list[CalendarTypes]**](CalendarTypes.md)| Comma delimited list of type of calendar types | [optional] 
 **event_types** | [**list[CalendarTypes]**](CalendarTypes.md)| Comma delimited list of type of events. &lt;b&gt;Note: Don&#x27;t Use. This will be deprecated in favor of calendarTypes&lt;/b&gt; | [optional] 
 **team_id** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **league_id** | [**list[int]**](int.md)| Unique League Identifier | [optional] 
 **sport_id** | [**list[int]**](int.md)| Top level organization of a sport | [optional] 
 **game_pk** | **int**| Unique Primary Key Representing a Game | [optional] 
 **game_pks** | [**list[int]**](int.md)| Comma delimited list of unique primary keys | [optional] 
 **event_ids** | [**list[int]**](int.md)| A unique identifier for non-game event | [optional] 
 **venue_ids** | [**list[int]**](int.md)| Unique Venue Identifier | [optional] 
 **performer_ids** | [**list[int]**](int.md)| A unique identifier for non-team event performers | [optional] 
 **game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Comma delimited list of type of Game. Available types in /api/v1/gameTypes | [optional] 
 **game_type** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **season** | [**list[str]**](str.md)| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **timecode** | **str**| Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS | [optional] 
 **use_latest_games** | **bool**|  | [optional] 
 **opponent_id** | [**list[int]**](int.md)| A unique identifier for the opposing team. Must be used with Team ID | [optional] 
 **public_facing** | [**PublicFacingEnum**](.md)| Return public, non-public or all games. Format: Public Facing &#x3D; &#x27;Y&#x27;, Non-Public Facing &#x3D; &#x27;N&#x27;, All &#x3D; &#x27;A&#x27; | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**ScheduleRestObject**](ScheduleRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tune_in**
> ScheduleRestObject tune_in(team_id=team_id, sport_id=sport_id, season=season, fields=fields)

Get postseason TuneIn schedules

This endpoint allows you to pull postseason schedules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduleApi()
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
sport_id = 56 # int | Unique League Identifier (optional)
season = 'season_example' # str | Unique Primary Key Representing a Game (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get postseason TuneIn schedules
    api_response = api_instance.tune_in(team_id=team_id, sport_id=sport_id, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->tune_in: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **sport_id** | **int**| Unique League Identifier | [optional] 
 **season** | **str**| Unique Primary Key Representing a Game | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**ScheduleRestObject**](ScheduleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

