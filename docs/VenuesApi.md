# swagger_client.VenuesApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**venues**](VenuesApi.md#venues) | **GET** /api/v1/venues | View venue info
[**venues1**](VenuesApi.md#venues1) | **GET** /api/v1/venues/{venueId} | View venue info

# **venues**
> VenuesRestObject venues(venue_id, venue_ids=venue_ids, league_id=league_id, league_ids=league_ids, game_type=game_type, game_types=game_types, season=season, seasons=seasons, fields=fields, active=active, include_events=include_events, sport_id=sport_id, sport_ids=sport_ids)

View venue info

This endpoint allows you to pull venues

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VenuesApi()
venue_id = 56 # int | Unique Venue Identifier
venue_ids = [56] # list[int] | Comma delimited list of Unique venue identifiers (optional)
league_id = 56 # int | Unique League Identifier (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Comma delimited list of type of Game. Available types in /api/v1/gameTypes (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
active = true # bool | Whether or not a player is active (optional)
include_events = true # bool |  (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)

try:
    # View venue info
    api_response = api_instance.venues(venue_id, venue_ids=venue_ids, league_id=league_id, league_ids=league_ids, game_type=game_type, game_types=game_types, season=season, seasons=seasons, fields=fields, active=active, include_events=include_events, sport_id=sport_id, sport_ids=sport_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VenuesApi->venues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **venue_id** | **int**| Unique Venue Identifier | 
 **venue_ids** | [**list[int]**](int.md)| Comma delimited list of Unique venue identifiers | [optional] 
 **league_id** | **int**| Unique League Identifier | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Comma delimited list of type of Game. Available types in /api/v1/gameTypes | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **active** | **bool**| Whether or not a player is active | [optional] 
 **include_events** | **bool**|  | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 

### Return type

[**VenuesRestObject**](VenuesRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **venues1**
> VenuesRestObject venues1(venue_id, venue_ids=venue_ids, league_id=league_id, league_ids=league_ids, game_type=game_type, game_types=game_types, season=season, seasons=seasons, fields=fields, active=active, include_events=include_events, sport_id=sport_id, sport_ids=sport_ids)

View venue info

This endpoint allows you to pull venues

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VenuesApi()
venue_id = 56 # int | Unique Venue Identifier
venue_ids = [56] # list[int] | Comma delimited list of Unique venue identifiers (optional)
league_id = 56 # int | Unique League Identifier (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Comma delimited list of type of Game. Available types in /api/v1/gameTypes (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
active = true # bool | Whether or not a player is active (optional)
include_events = true # bool |  (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)

try:
    # View venue info
    api_response = api_instance.venues1(venue_id, venue_ids=venue_ids, league_id=league_id, league_ids=league_ids, game_type=game_type, game_types=game_types, season=season, seasons=seasons, fields=fields, active=active, include_events=include_events, sport_id=sport_id, sport_ids=sport_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VenuesApi->venues1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **venue_id** | **int**| Unique Venue Identifier | 
 **venue_ids** | [**list[int]**](int.md)| Comma delimited list of Unique venue identifiers | [optional] 
 **league_id** | **int**| Unique League Identifier | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Comma delimited list of type of Game. Available types in /api/v1/gameTypes | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **active** | **bool**| Whether or not a player is active | [optional] 
 **include_events** | **bool**|  | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 

### Return type

[**VenuesRestObject**](VenuesRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

