# swagger_client.GameApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boxscore**](GameApi.md#boxscore) | **GET** /api/v1/game/{game_pk}/boxscore | Get game boxscore.
[**color_feed**](GameApi.md#color_feed) | **GET** /api/v1/game/{game_pk}/feed/color | Get game color feed.
[**color_timestamps**](GameApi.md#color_timestamps) | **GET** /api/v1/game/{game_pk}/feed/color/timestamps | Retrieve all of the color timestamps for a game.
[**content**](GameApi.md#content) | **GET** /api/v1/game/{game_pk}/content | Retrieve all content for a game.
[**current_game_stats1**](GameApi.md#current_game_stats1) | **GET** /api/v1/game/changes | View a game change log
[**get_game_context_metrics**](GameApi.md#get_game_context_metrics) | **GET** /api/v1/game/{gamePk}/contextMetrics | Get the context metrics for this game based on its current state
[**get_game_with_metrics**](GameApi.md#get_game_with_metrics) | **GET** /api/v1/game/{gamePk}/withMetrics | Get game info with metrics
[**get_win_probability**](GameApi.md#get_win_probability) | **GET** /api/v1/game/{gamePk}/winProbability | Get the win probability for this game
[**linescore**](GameApi.md#linescore) | **GET** /api/v1/game/{game_pk}/linescore | Get game linescore
[**live_game_diff_patch_v1**](GameApi.md#live_game_diff_patch_v1) | **GET** /api/v1.1/game/{game_pk}/feed/live/diffPatch | Get live game status diffPatch.
[**live_game_v1**](GameApi.md#live_game_v1) | **GET** /api/v1.1/game/{game_pk}/feed/live | Get live game status.
[**live_timestampv11**](GameApi.md#live_timestampv11) | **GET** /api/v1.1/game/{game_pk}/feed/live/timestamps | Retrieve all of the play timestamps for a game.
[**play_by_play**](GameApi.md#play_by_play) | **GET** /api/v1/game/{game_pk}/playByPlay | Get game play By Play

# **boxscore**
> BaseballBoxscoreRestObject boxscore(game_pk, timecode=timecode, fields=fields, inclusive_timecode=inclusive_timecode, num_players=num_players, no_ties=no_ties, accent=accent)

Get game boxscore.

This endpoint allows you to pull a boxscore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
timecode = 'timecode_example' # str | Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
inclusive_timecode = true # bool | True to include plays that happen before or at the specified timecode (optional)
num_players = 3 # int | Number of top player game scores to show. Default is 3. (optional) (default to 3)
no_ties = true # bool | If set to false, will show all players tied for the last spot in the game scores list. (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)

try:
    # Get game boxscore.
    api_response = api_instance.boxscore(game_pk, timecode=timecode, fields=fields, inclusive_timecode=inclusive_timecode, num_players=num_players, no_ties=no_ties, accent=accent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->boxscore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **timecode** | **str**| Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **inclusive_timecode** | **bool**| True to include plays that happen before or at the specified timecode | [optional] 
 **num_players** | **int**| Number of top player game scores to show. Default is 3. | [optional] [default to 3]
 **no_ties** | **bool**| If set to false, will show all players tied for the last spot in the game scores list. | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 

### Return type

[**BaseballBoxscoreRestObject**](BaseballBoxscoreRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **color_feed**
> str color_feed(game_pk, timecode=timecode, fields=fields)

Get game color feed.

This API can return very large payloads.  It is STRONGLY recommended that clients ask for diffs and use \"Accept-Encoding: gzip\" header.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
timecode = 'timecode_example' # str | Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get game color feed.
    api_response = api_instance.color_feed(game_pk, timecode=timecode, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->color_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **timecode** | **str**| Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **color_timestamps**
> list[str] color_timestamps(game_pk)

Retrieve all of the color timestamps for a game.

This can be used for replaying games.  Endpoint returns all of the timecodes that can be used with diffs for /v1/game/{game_pk}/feed/color

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | Unique Primary Key Representing a Game

try:
    # Retrieve all of the color timestamps for a game.
    api_response = api_instance.color_timestamps(game_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->color_timestamps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content**
> GameContentRestObject content(game_pk, highlight_limit=highlight_limit)

Retrieve all content for a game.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | 
highlight_limit = 56 # int | Number of results to return (optional)

try:
    # Retrieve all content for a game.
    api_response = api_instance.content(game_pk, highlight_limit=highlight_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**|  | 
 **highlight_limit** | **int**| Number of results to return | [optional] 

### Return type

[**GameContentRestObject**](GameContentRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **current_game_stats1**
> ScheduleRestObject current_game_stats1(updated_since=updated_since, sport_id=sport_id, sport_ids=sport_ids, game_type=game_type, game_types=game_types, season=season, game_pks=game_pks, limit=limit, offset=offset, fields=fields)

View a game change log

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
updated_since = '2013-10-20T19:20:30+01:00' # datetime | Format: YYYY-MM-DDTHH:MM:SSZ (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Comma delimited list of type of Game. Available types in /api/v1/gameTypes (optional)
season = 'season_example' # str | Season of play (optional)
game_pks = [56] # list[int] | Comma delimited list of unique primary keys (optional)
limit = 56 # int | Number of results to return (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View a game change log
    api_response = api_instance.current_game_stats1(updated_since=updated_since, sport_id=sport_id, sport_ids=sport_ids, game_type=game_type, game_types=game_types, season=season, game_pks=game_pks, limit=limit, offset=offset, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->current_game_stats1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_since** | **datetime**| Format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Comma delimited list of type of Game. Available types in /api/v1/gameTypes | [optional] 
 **season** | **str**| Season of play | [optional] 
 **game_pks** | [**list[int]**](int.md)| Comma delimited list of unique primary keys | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**ScheduleRestObject**](ScheduleRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game_context_metrics**
> BaseballGameContextRestObject get_game_context_metrics(game_pk, timecode=timecode, fields=fields)

Get the context metrics for this game based on its current state

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
timecode = 'timecode_example' # str | Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get the context metrics for this game based on its current state
    api_response = api_instance.get_game_context_metrics(game_pk, timecode=timecode, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->get_game_context_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **timecode** | **str**| Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**BaseballGameContextRestObject**](BaseballGameContextRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game_with_metrics**
> BaseballGameRestObject get_game_with_metrics(game_pk, timecode=timecode, inclusive_timecode=inclusive_timecode, fields=fields, accent=accent)

Get game info with metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
timecode = 'timecode_example' # str | Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS (optional)
inclusive_timecode = true # bool | True to include plays that happen before or at the specified timecode (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)

try:
    # Get game info with metrics
    api_response = api_instance.get_game_with_metrics(game_pk, timecode=timecode, inclusive_timecode=inclusive_timecode, fields=fields, accent=accent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->get_game_with_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **timecode** | **str**| Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS | [optional] 
 **inclusive_timecode** | **bool**| True to include plays that happen before or at the specified timecode | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 

### Return type

[**BaseballGameRestObject**](BaseballGameRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_win_probability**
> list[BaseballPlayRestObject] get_win_probability(game_pk, timecode=timecode, fields=fields, inclusive_timecode=inclusive_timecode, accent=accent)

Get the win probability for this game

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
timecode = 'timecode_example' # str | Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
inclusive_timecode = true # bool | True to include plays that happen before or at the specified timecode (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)

try:
    # Get the win probability for this game
    api_response = api_instance.get_win_probability(game_pk, timecode=timecode, fields=fields, inclusive_timecode=inclusive_timecode, accent=accent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->get_win_probability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **timecode** | **str**| Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **inclusive_timecode** | **bool**| True to include plays that happen before or at the specified timecode | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 

### Return type

[**list[BaseballPlayRestObject]**](BaseballPlayRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **linescore**
> BaseballLinescoreRestObject linescore(game_pk, timecode=timecode, fields=fields, inclusive_timecode=inclusive_timecode)

Get game linescore

This endpoint allows you to pull the linescore for a game

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
timecode = 'timecode_example' # str | Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
inclusive_timecode = true # bool | True to include plays that happen before or at the specified timecode (optional)

try:
    # Get game linescore
    api_response = api_instance.linescore(game_pk, timecode=timecode, fields=fields, inclusive_timecode=inclusive_timecode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->linescore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **timecode** | **str**| Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **inclusive_timecode** | **bool**| True to include plays that happen before or at the specified timecode | [optional] 

### Return type

[**BaseballLinescoreRestObject**](BaseballLinescoreRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **live_game_diff_patch_v1**
> str live_game_diff_patch_v1(game_pk, start_timecode=start_timecode, end_timecode=end_timecode, accent=accent)

Get live game status diffPatch.

This endpoint allows comparison of game files and shows any differences/discrepancies between the two<br/><br/><b>Diff/Patch System:</b> startTimecode and endTimecode can be used for getting diffs.<br/>Expected usage:  <br/> 1) Request full payload by not passing startTimecode or endTimecode.  This will return the most recent game state.<br/> 2) Find the latest timecode in this response.  <br/> 3) Wait X seconds<br/> 4) Use the timecode from 2 as the startTimecode.  This will give you a diff of everything that has happened since startTimecode.  <br/> 5) If no data is returned, wait X seconds and do the same request.  <br/> 6) If data is returned, get a new timeStamp from the response, and use that for the next call as startTimecode.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
start_timecode = 'start_timecode_example' # str | Start time code will give you everything since that time. Format: MMDDYYYY_HHMMSS (optional)
end_timecode = 'end_timecode_example' # str | End time code will give you a snapshot at that specific time. Format: MMDDYYYY_HHMMSS (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)

try:
    # Get live game status diffPatch.
    api_response = api_instance.live_game_diff_patch_v1(game_pk, start_timecode=start_timecode, end_timecode=end_timecode, accent=accent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->live_game_diff_patch_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **start_timecode** | **str**| Start time code will give you everything since that time. Format: MMDDYYYY_HHMMSS | [optional] 
 **end_timecode** | **str**| End time code will give you a snapshot at that specific time. Format: MMDDYYYY_HHMMSS | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **live_game_v1**
> BaseballGameRestObject live_game_v1(game_pk, timecode=timecode, fields=fields, inclusive_timecode=inclusive_timecode, accent=accent)

Get live game status.

This API can return very large payloads.  It is STRONGLY recommended that clients ask for diffs and use \"Accept-Encoding: gzip\" header.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
timecode = 'timecode_example' # str | Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
inclusive_timecode = true # bool | True to include plays that happen before or at the specified timecode (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)

try:
    # Get live game status.
    api_response = api_instance.live_game_v1(game_pk, timecode=timecode, fields=fields, inclusive_timecode=inclusive_timecode, accent=accent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->live_game_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **timecode** | **str**| Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **inclusive_timecode** | **bool**| True to include plays that happen before or at the specified timecode | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 

### Return type

[**BaseballGameRestObject**](BaseballGameRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **live_timestampv11**
> str live_timestampv11(game_pk)

Retrieve all of the play timestamps for a game.

This can be used for replaying games.  Endpoint returns all of the timecodes that can be used with diffs for /v1/game/{game_pk}/feed/live

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | Unique Primary Key Representing a Game

try:
    # Retrieve all of the play timestamps for a game.
    api_response = api_instance.live_timestampv11(game_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->live_timestampv11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_by_play**
> BaseballPlayByPlayRestObject play_by_play(game_pk, timecode=timecode, fields=fields, inclusive_timecode=inclusive_timecode, accent=accent)

Get game play By Play

This endpoint allows you to pull the play by play of a game

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GameApi()
game_pk = 56 # int | Unique Primary Key Representing a Game
timecode = 'timecode_example' # str | Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
inclusive_timecode = true # bool | True to include plays that happen before or at the specified timecode (optional)
accent = true # bool | Boolean value to specify wanting a person's name with accents or without (optional)

try:
    # Get game play By Play
    api_response = api_instance.play_by_play(game_pk, timecode=timecode, fields=fields, inclusive_timecode=inclusive_timecode, accent=accent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->play_by_play: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **timecode** | **str**| Use this parameter to return a snapshot of the data at the specified time. Format: YYYYMMDD_HHMMSS | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **inclusive_timecode** | **bool**| True to include plays that happen before or at the specified timecode | [optional] 
 **accent** | **bool**| Boolean value to specify wanting a person&#x27;s name with accents or without | [optional] 

### Return type

[**BaseballPlayByPlayRestObject**](BaseballPlayByPlayRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

