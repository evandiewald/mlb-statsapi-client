# swagger_client.AnalyticsApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**context_metrics**](AnalyticsApi.md#context_metrics) | **GET** /api/v1/game/{gamePk}/{guid}/contextMetrics | Get context metrics for a specific gamePk.
[**context_metrics_with_averages**](AnalyticsApi.md#context_metrics_with_averages) | **GET** /api/v1/game/{gamePk}/{guid}/contextMetricsAverages | Get a json file containing raw coordinate data and refined calculated metrics.
[**context_metrics_with_averages_post**](AnalyticsApi.md#context_metrics_with_averages_post) | **POST** /api/v1/game/{gamePk}/{guid}/contextMetricsAverages | Get a json file containing raw coordinate data and refined calculated metrics.
[**game_guids**](AnalyticsApi.md#game_guids) | **GET** /api/v1/game/{gamePk}/guids | Get the GUIDs (plays) for a specific game. 
[**game_guids_from_postgres_range**](AnalyticsApi.md#game_guids_from_postgres_range) | **GET** /api/v1/analytics/guids | Get the GUIDs (plays) for a specific game. 
[**game_guids_from_postgres_range_by_game**](AnalyticsApi.md#game_guids_from_postgres_range_by_game) | **GET** /api/v1/analytics/game | Get all games by updated date.
[**game_last_pitch**](AnalyticsApi.md#game_last_pitch) | **GET** /api/v1/game/lastPitch | Get the last pitch for a list of games
[**home_run_ballparks**](AnalyticsApi.md#home_run_ballparks) | **GET** /api/v1/game/{gamePk}/{guid}/homeRunBallparks | Get if the play is a home run is each park for a specific play.
[**parsed_json_formatted_analytics**](AnalyticsApi.md#parsed_json_formatted_analytics) | **GET** /api/v1/game/{gamePk}/{guid}/analytics | Get Statcast data for a specific play.

# **context_metrics**
> list[CalculatedMetricRestObject] context_metrics(game_pk, guid, fields=fields)

Get context metrics for a specific gamePk.

Returns a json file containing raw coordinate data and refined calculated metrics.<br/><br/>This responses can be very large, so it is strongly recommended that you pass \"Accept-Encoding: gzip\" as a header to have the responses compressed.

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
api_instance = swagger_client.AnalyticsApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game
guid = 'guid_example' # str | Unique identifier for a play within a game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get context metrics for a specific gamePk.
    api_response = api_instance.context_metrics(game_pk, guid, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->context_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **guid** | **str**| Unique identifier for a play within a game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**list[CalculatedMetricRestObject]**](CalculatedMetricRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_metrics_with_averages**
> list[CalculatedMetricRestObject] context_metrics_with_averages(game_pk, guid, fields=fields)

Get a json file containing raw coordinate data and refined calculated metrics.

Returns a json file containing raw coordinate data and refined calculated metrics.<br/><br/>This responses can be very large, so it is strongly recommended that you pass \"Accept-Encoding: gzip\" as a header to have the responses compressed.

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
api_instance = swagger_client.AnalyticsApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game
guid = 'guid_example' # str | Unique identifier for a play within a game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get a json file containing raw coordinate data and refined calculated metrics.
    api_response = api_instance.context_metrics_with_averages(game_pk, guid, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->context_metrics_with_averages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **guid** | **str**| Unique identifier for a play within a game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**list[CalculatedMetricRestObject]**](CalculatedMetricRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_metrics_with_averages_post**
> list[CalculatedMetricRestObject] context_metrics_with_averages_post(game_pk, guid, fields=fields)

Get a json file containing raw coordinate data and refined calculated metrics.

Returns a json file containing raw coordinate data and refined calculated metrics.<br/><br/>This responses can be very large, so it is strongly recommended that you pass \"Accept-Encoding: gzip\" as a header to have the responses compressed.

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
api_instance = swagger_client.AnalyticsApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game
guid = 'guid_example' # str | Unique identifier for a play within a game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get a json file containing raw coordinate data and refined calculated metrics.
    api_response = api_instance.context_metrics_with_averages_post(game_pk, guid, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->context_metrics_with_averages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **guid** | **str**| Unique identifier for a play within a game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**list[CalculatedMetricRestObject]**](CalculatedMetricRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_guids**
> list[AnalyticsPlayMetadataRestObject] game_guids(game_pk, fields=fields, game_mode_id=game_mode_id, is_pitch=is_pitch, is_hit=is_hit, is_pickoff=is_pickoff, has_updates=has_updates, since=since, updated_since=updated_since, last_play_time=last_play_time, last_updated_time=last_updated_time, last_metrics_updated_time=last_metrics_updated_time, last_audit_updated_time=last_audit_updated_time, last_video_updated_time=last_video_updated_time)

Get the GUIDs (plays) for a specific game. 

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
api_instance = swagger_client.AnalyticsApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
game_mode_id = 56 # int | Statcast game mode. Format: 0 = Batting Practive, 1 = Warmup 2 = Live (optional)
is_pitch = true # bool | If there was a pitch (optional)
is_hit = true # bool | If there was a hit ball tracked (optional)
is_pickoff = true # bool | If there was a pickoff (optional)
has_updates = true # bool | True if updated by an auditor (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Returns all data that was created after the specified timestamp. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
updated_since = '2013-10-20T19:20:30+01:00' # datetime | Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_play_time = '2013-10-20T19:20:30+01:00' # datetime | Returns all data that was created after the specified timestamp. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_updated_time = '2013-10-20T19:20:30+01:00' # datetime | Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_metrics_updated_time = '2013-10-20T19:20:30+01:00' # datetime | Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_audit_updated_time = '2013-10-20T19:20:30+01:00' # datetime | Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_video_updated_time = '2013-10-20T19:20:30+01:00' # datetime | The last time SportyBot video was updated (optional)

try:
    # Get the GUIDs (plays) for a specific game. 
    api_response = api_instance.game_guids(game_pk, fields=fields, game_mode_id=game_mode_id, is_pitch=is_pitch, is_hit=is_hit, is_pickoff=is_pickoff, has_updates=has_updates, since=since, updated_since=updated_since, last_play_time=last_play_time, last_updated_time=last_updated_time, last_metrics_updated_time=last_metrics_updated_time, last_audit_updated_time=last_audit_updated_time, last_video_updated_time=last_video_updated_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->game_guids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **game_mode_id** | **int**| Statcast game mode. Format: 0 &#x3D; Batting Practive, 1 &#x3D; Warmup 2 &#x3D; Live | [optional] 
 **is_pitch** | **bool**| If there was a pitch | [optional] 
 **is_hit** | **bool**| If there was a hit ball tracked | [optional] 
 **is_pickoff** | **bool**| If there was a pickoff | [optional] 
 **has_updates** | **bool**| True if updated by an auditor | [optional] 
 **since** | **datetime**| Returns all data that was created after the specified timestamp. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **updated_since** | **datetime**| Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_play_time** | **datetime**| Returns all data that was created after the specified timestamp. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_updated_time** | **datetime**| Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_metrics_updated_time** | **datetime**| Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_audit_updated_time** | **datetime**| Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_video_updated_time** | **datetime**| The last time SportyBot video was updated | [optional] 

### Return type

[**list[AnalyticsPlayMetadataRestObject]**](AnalyticsPlayMetadataRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_guids_from_postgres_range**
> AnalyticsPlayMetadataWrapperRestObject game_guids_from_postgres_range(fields=fields, game_mode_id=game_mode_id, is_pitch=is_pitch, is_hit=is_hit, is_pickoff=is_pickoff, is_non_statcast=is_non_statcast, gameday_type=gameday_type, has_updates=has_updates, last_play_time=last_play_time, last_updated_time=last_updated_time, last_metrics_updated_time=last_metrics_updated_time, last_audit_updated_time=last_audit_updated_time, last_video_updated_time=last_video_updated_time, game_date=game_date, sport_id=sport_id, game_type=game_type, tracking_system_owner=tracking_system_owner, season=season, sort_by=sort_by, limit=limit, offset=offset)

Get the GUIDs (plays) for a specific game. 

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
api_instance = swagger_client.AnalyticsApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
game_mode_id = 56 # int | Statcast game mode. Format: 0 = Batting Practive, 1 = Warmup 2 = Live (optional)
is_pitch = true # bool | If there was a pitch (optional)
is_hit = true # bool | If there was a hit ball tracked (optional)
is_pickoff = true # bool | If there was a pickoff (optional)
is_non_statcast = true # bool | If non statcast games need to be included (optional)
gameday_type = 'gameday_type_example' # str | Indicates the level of Gameday (tracking, play-by-play, linescore, etc...) (optional)
has_updates = true # bool | True if updated by an auditor (optional)
last_play_time = '2013-10-20T19:20:30+01:00' # datetime | Returns all data that was created after the specified timestamp. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_updated_time = '2013-10-20T19:20:30+01:00' # datetime | Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_metrics_updated_time = '2013-10-20T19:20:30+01:00' # datetime | Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_audit_updated_time = '2013-10-20T19:20:30+01:00' # datetime | Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_video_updated_time = '2013-10-20T19:20:30+01:00' # datetime | The last time SportyBot video was updated (optional)
game_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
tracking_system_owner = swagger_client.TrackingSystemOwner() # TrackingSystemOwner | Owner of the tracking system (optional)
season = 'season_example' # str | Season of play (optional)
sort_by = 'sort_by_example' # str | Sort the set of data by the specified field (optional)
limit = 56 # int | Number of results to return (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)

try:
    # Get the GUIDs (plays) for a specific game. 
    api_response = api_instance.game_guids_from_postgres_range(fields=fields, game_mode_id=game_mode_id, is_pitch=is_pitch, is_hit=is_hit, is_pickoff=is_pickoff, is_non_statcast=is_non_statcast, gameday_type=gameday_type, has_updates=has_updates, last_play_time=last_play_time, last_updated_time=last_updated_time, last_metrics_updated_time=last_metrics_updated_time, last_audit_updated_time=last_audit_updated_time, last_video_updated_time=last_video_updated_time, game_date=game_date, sport_id=sport_id, game_type=game_type, tracking_system_owner=tracking_system_owner, season=season, sort_by=sort_by, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->game_guids_from_postgres_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **game_mode_id** | **int**| Statcast game mode. Format: 0 &#x3D; Batting Practive, 1 &#x3D; Warmup 2 &#x3D; Live | [optional] 
 **is_pitch** | **bool**| If there was a pitch | [optional] 
 **is_hit** | **bool**| If there was a hit ball tracked | [optional] 
 **is_pickoff** | **bool**| If there was a pickoff | [optional] 
 **is_non_statcast** | **bool**| If non statcast games need to be included | [optional] 
 **gameday_type** | **str**| Indicates the level of Gameday (tracking, play-by-play, linescore, etc...) | [optional] 
 **has_updates** | **bool**| True if updated by an auditor | [optional] 
 **last_play_time** | **datetime**| Returns all data that was created after the specified timestamp. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_updated_time** | **datetime**| Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_metrics_updated_time** | **datetime**| Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_audit_updated_time** | **datetime**| Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_video_updated_time** | **datetime**| The last time SportyBot video was updated | [optional] 
 **game_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **tracking_system_owner** | [**TrackingSystemOwner**](.md)| Owner of the tracking system | [optional] 
 **season** | **str**| Season of play | [optional] 
 **sort_by** | **str**| Sort the set of data by the specified field | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 

### Return type

[**AnalyticsPlayMetadataWrapperRestObject**](AnalyticsPlayMetadataWrapperRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_guids_from_postgres_range_by_game**
> AnalyticsGameMetadataWrapperRestObject game_guids_from_postgres_range_by_game(fields=fields, game_mode_id=game_mode_id, is_pitch=is_pitch, is_hit=is_hit, is_pickoff=is_pickoff, is_non_statcast=is_non_statcast, gameday_type=gameday_type, has_updates=has_updates, last_play_time=last_play_time, last_video_updated_time=last_video_updated_time, last_updated_time=last_updated_time, last_metrics_updated_time=last_metrics_updated_time, last_audit_updated_time=last_audit_updated_time, game_date=game_date, sport_id=sport_id, game_type=game_type, season=season, tracking_system_owner=tracking_system_owner, sort_by=sort_by, limit=limit, offset=offset, schedule_event_types=schedule_event_types)

Get all games by updated date.

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
api_instance = swagger_client.AnalyticsApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
game_mode_id = 56 # int | Statcast game mode. Format: 0 = Batting Practive, 1 = Warmup 2 = Live (optional)
is_pitch = true # bool | If there was a pitch (optional)
is_hit = true # bool | If there was a hit ball tracked (optional)
is_pickoff = true # bool | If there was a pickoff (optional)
is_non_statcast = true # bool | If non statcast games need to be included (optional)
gameday_type = 'gameday_type_example' # str | Indicates the level of Gameday (tracking, play-by-play, linescore, etc...) (optional)
has_updates = true # bool | True if updated by an auditor (optional)
last_play_time = '2013-10-20T19:20:30+01:00' # datetime | Returns all data that was created after the specified timestamp. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_video_updated_time = '2013-10-20T19:20:30+01:00' # datetime | The last time SportyBot video was updated (optional)
last_updated_time = '2013-10-20T19:20:30+01:00' # datetime | Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_metrics_updated_time = '2013-10-20T19:20:30+01:00' # datetime | Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
last_audit_updated_time = '2013-10-20T19:20:30+01:00' # datetime | Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ (optional)
game_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
season = 'season_example' # str | Season of play (optional)
tracking_system_owner = swagger_client.TrackingSystemOwner() # TrackingSystemOwner | Owner of the tracking system (optional)
sort_by = 'sort_by_example' # str | Sort the set of data by the specified field (optional)
limit = 56 # int | Number of results to return (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
schedule_event_types = [swagger_client.ScheduleEventTypes()] # list[ScheduleEventTypes] | Comma delimited list of type of event types (optional)

try:
    # Get all games by updated date.
    api_response = api_instance.game_guids_from_postgres_range_by_game(fields=fields, game_mode_id=game_mode_id, is_pitch=is_pitch, is_hit=is_hit, is_pickoff=is_pickoff, is_non_statcast=is_non_statcast, gameday_type=gameday_type, has_updates=has_updates, last_play_time=last_play_time, last_video_updated_time=last_video_updated_time, last_updated_time=last_updated_time, last_metrics_updated_time=last_metrics_updated_time, last_audit_updated_time=last_audit_updated_time, game_date=game_date, sport_id=sport_id, game_type=game_type, season=season, tracking_system_owner=tracking_system_owner, sort_by=sort_by, limit=limit, offset=offset, schedule_event_types=schedule_event_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->game_guids_from_postgres_range_by_game: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **game_mode_id** | **int**| Statcast game mode. Format: 0 &#x3D; Batting Practive, 1 &#x3D; Warmup 2 &#x3D; Live | [optional] 
 **is_pitch** | **bool**| If there was a pitch | [optional] 
 **is_hit** | **bool**| If there was a hit ball tracked | [optional] 
 **is_pickoff** | **bool**| If there was a pickoff | [optional] 
 **is_non_statcast** | **bool**| If non statcast games need to be included | [optional] 
 **gameday_type** | **str**| Indicates the level of Gameday (tracking, play-by-play, linescore, etc...) | [optional] 
 **has_updates** | **bool**| True if updated by an auditor | [optional] 
 **last_play_time** | **datetime**| Returns all data that was created after the specified timestamp. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_video_updated_time** | **datetime**| The last time SportyBot video was updated | [optional] 
 **last_updated_time** | **datetime**| Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_metrics_updated_time** | **datetime**| Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **last_audit_updated_time** | **datetime**| Return data updated since a specified date. Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **game_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **season** | **str**| Season of play | [optional] 
 **tracking_system_owner** | [**TrackingSystemOwner**](.md)| Owner of the tracking system | [optional] 
 **sort_by** | **str**| Sort the set of data by the specified field | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **schedule_event_types** | [**list[ScheduleEventTypes]**](ScheduleEventTypes.md)| Comma delimited list of type of event types | [optional] 

### Return type

[**AnalyticsGameMetadataWrapperRestObject**](AnalyticsGameMetadataWrapperRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_last_pitch**
> list[AnalyticsPlayMetadataRestObject] game_last_pitch(game_pks, fields=fields)

Get the last pitch for a list of games

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
api_instance = swagger_client.AnalyticsApi(swagger_client.ApiClient(configuration))
game_pks = [56] # list[int] | Unique Primary Key Representing a Game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get the last pitch for a list of games
    api_response = api_instance.game_last_pitch(game_pks, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->game_last_pitch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pks** | [**list[int]**](int.md)| Unique Primary Key Representing a Game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**list[AnalyticsPlayMetadataRestObject]**](AnalyticsPlayMetadataRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **home_run_ballparks**
> VenuesRestObject home_run_ballparks(game_pk, guid, is_home_run_parks, fields=fields)

Get if the play is a home run is each park for a specific play.

Returns a json file containing raw coordinate data and refined calculated metrics.<br/><br/>This responses can be very large, so it is strongly recommended that you pass \"Accept-Encoding: gzip\" as a header to have the responses compressed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
guid = 'guid_example' # str | Unique identifier for a play within a game
is_home_run_parks = true # bool | 
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get if the play is a home run is each park for a specific play.
    api_response = api_instance.home_run_ballparks(game_pk, guid, is_home_run_parks, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->home_run_ballparks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **guid** | **str**| Unique identifier for a play within a game | 
 **is_home_run_parks** | **bool**|  | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**VenuesRestObject**](VenuesRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parsed_json_formatted_analytics**
> AnalyticsRestObject parsed_json_formatted_analytics(game_pk, guid, fields=fields)

Get Statcast data for a specific play.

Returns a json file containing raw coordinate data and refined calculated metrics.<br/><br/>This responses can be very large, so it is strongly recommended that you pass \"Accept-Encoding: gzip\" as a header to have the responses compressed.

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
api_instance = swagger_client.AnalyticsApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game
guid = 'guid_example' # str | Unique identifier for a play within a game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get Statcast data for a specific play.
    api_response = api_instance.parsed_json_formatted_analytics(game_pk, guid, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->parsed_json_formatted_analytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **guid** | **str**| Unique identifier for a play within a game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**AnalyticsRestObject**](AnalyticsRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

