# swagger_client.DraftApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**draft_picks**](DraftApi.md#draft_picks) | **GET** /api/v1/draft | View MLB Drafted Players
[**draft_picks1**](DraftApi.md#draft_picks1) | **GET** /api/v1/draft/{year} | View MLB Drafted Players
[**draft_prospects**](DraftApi.md#draft_prospects) | **GET** /api/v1/draft/prospects | View MLB Draft Prospects
[**draft_prospects1**](DraftApi.md#draft_prospects1) | **GET** /api/v1/draft/prospects/{year} | View MLB Draft Prospects
[**latest_draft_picks**](DraftApi.md#latest_draft_picks) | **GET** /api/v1/draft/{year}/latest | Get the last drafted player and the next 5 teams up to pick

# **draft_picks**
> BaseballDraftListRestObject draft_picks(year, limit=limit, offset=offset, fields=fields, order=order, sort_by=sort_by, drafted=drafted, round=round, name=name, school=school, position=position, team=team, team_id=team_id, state=state, country=country, player_id=player_id, bis_player_id=bis_player_id)

View MLB Drafted Players

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DraftApi()
year = 56 # int | Year the player was drafted. Format: 2000
limit = 56 # int | Number of results to return (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
order = swagger_client.SortOrderEnum() # SortOrderEnum | The order of sorting, ascending or descending (optional)
sort_by = 'sort_by_example' # str | Sort the set of data by the specified field (optional)
drafted = true # bool | Whether or not the players been drafted (optional)
round = 'round_example' # str | Round in which a player was drafted (optional)
name = 'name_example' # str | Filter players by the first letter of their name using using the specific character (optional)
school = 'school_example' # str | Filter players by the first letter of their school using using the specific character (optional)
position = swagger_client.BaseballPosition() # BaseballPosition | Position number. Format: 1, 2, 3, etc (optional)
team = 'team_example' # str | Unique Team Code. Format: tor, nya, etc (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
state = 'state_example' # str | State where the venue is located. Format: Ohio (optional)
country = 'country_example' # str | Filter players by their home country (optional)
player_id = 56 # int | A unique identifier for a player (optional)
bis_player_id = 56 # int | A unique identifier for a player in the EBIS system (optional)

try:
    # View MLB Drafted Players
    api_response = api_instance.draft_picks(year, limit=limit, offset=offset, fields=fields, order=order, sort_by=sort_by, drafted=drafted, round=round, name=name, school=school, position=position, team=team, team_id=team_id, state=state, country=country, player_id=player_id, bis_player_id=bis_player_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->draft_picks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year the player was drafted. Format: 2000 | 
 **limit** | **int**| Number of results to return | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **order** | [**SortOrderEnum**](.md)| The order of sorting, ascending or descending | [optional] 
 **sort_by** | **str**| Sort the set of data by the specified field | [optional] 
 **drafted** | **bool**| Whether or not the players been drafted | [optional] 
 **round** | **str**| Round in which a player was drafted | [optional] 
 **name** | **str**| Filter players by the first letter of their name using using the specific character | [optional] 
 **school** | **str**| Filter players by the first letter of their school using using the specific character | [optional] 
 **position** | [**BaseballPosition**](.md)| Position number. Format: 1, 2, 3, etc | [optional] 
 **team** | **str**| Unique Team Code. Format: tor, nya, etc | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **state** | **str**| State where the venue is located. Format: Ohio | [optional] 
 **country** | **str**| Filter players by their home country | [optional] 
 **player_id** | **int**| A unique identifier for a player | [optional] 
 **bis_player_id** | **int**| A unique identifier for a player in the EBIS system | [optional] 

### Return type

[**BaseballDraftListRestObject**](BaseballDraftListRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **draft_picks1**
> BaseballDraftListRestObject draft_picks1(year, limit=limit, offset=offset, fields=fields, order=order, sort_by=sort_by, drafted=drafted, round=round, name=name, school=school, position=position, team=team, team_id=team_id, state=state, country=country, player_id=player_id, bis_player_id=bis_player_id)

View MLB Drafted Players

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DraftApi()
year = 56 # int | Year the player was drafted. Format: 2000
limit = 56 # int | Number of results to return (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
order = swagger_client.SortOrderEnum() # SortOrderEnum | The order of sorting, ascending or descending (optional)
sort_by = 'sort_by_example' # str | Sort the set of data by the specified field (optional)
drafted = true # bool | Whether or not the players been drafted (optional)
round = 'round_example' # str | Round in which a player was drafted (optional)
name = 'name_example' # str | Filter players by the first letter of their name using using the specific character (optional)
school = 'school_example' # str | Filter players by the first letter of their school using using the specific character (optional)
position = swagger_client.BaseballPosition() # BaseballPosition | Position number. Format: 1, 2, 3, etc (optional)
team = 'team_example' # str | Unique Team Code. Format: tor, nya, etc (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
state = 'state_example' # str | State where the venue is located. Format: Ohio (optional)
country = 'country_example' # str | Filter players by their home country (optional)
player_id = 56 # int | A unique identifier for a player (optional)
bis_player_id = 56 # int | A unique identifier for a player in the EBIS system (optional)

try:
    # View MLB Drafted Players
    api_response = api_instance.draft_picks1(year, limit=limit, offset=offset, fields=fields, order=order, sort_by=sort_by, drafted=drafted, round=round, name=name, school=school, position=position, team=team, team_id=team_id, state=state, country=country, player_id=player_id, bis_player_id=bis_player_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->draft_picks1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year the player was drafted. Format: 2000 | 
 **limit** | **int**| Number of results to return | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **order** | [**SortOrderEnum**](.md)| The order of sorting, ascending or descending | [optional] 
 **sort_by** | **str**| Sort the set of data by the specified field | [optional] 
 **drafted** | **bool**| Whether or not the players been drafted | [optional] 
 **round** | **str**| Round in which a player was drafted | [optional] 
 **name** | **str**| Filter players by the first letter of their name using using the specific character | [optional] 
 **school** | **str**| Filter players by the first letter of their school using using the specific character | [optional] 
 **position** | [**BaseballPosition**](.md)| Position number. Format: 1, 2, 3, etc | [optional] 
 **team** | **str**| Unique Team Code. Format: tor, nya, etc | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **state** | **str**| State where the venue is located. Format: Ohio | [optional] 
 **country** | **str**| Filter players by their home country | [optional] 
 **player_id** | **int**| A unique identifier for a player | [optional] 
 **bis_player_id** | **int**| A unique identifier for a player in the EBIS system | [optional] 

### Return type

[**BaseballDraftListRestObject**](BaseballDraftListRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **draft_prospects**
> ProspectListRestObject draft_prospects(year, limit=limit, offset=offset, fields=fields, order=order, sort_by=sort_by, drafted=drafted, round=round, name=name, school=school, position=position, team=team, team_id=team_id, state=state, country=country, player_id=player_id, bis_player_id=bis_player_id)

View MLB Draft Prospects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DraftApi()
year = 56 # int | Year the player was drafted. Format: 2000
limit = 56 # int | Number of results to return (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
order = swagger_client.SortOrderEnum() # SortOrderEnum | The order of sorting, ascending or descending (optional)
sort_by = 'sort_by_example' # str | Sort the set of data by the specified field (optional)
drafted = true # bool | Whether or not the players been drafted (optional)
round = 'round_example' # str | Round in which a player was drafted (optional)
name = 'name_example' # str | Filter players by the first letter of their name using using the specific character (optional)
school = 'school_example' # str | Filter players by the first letter of their school using using the specific character (optional)
position = swagger_client.BaseballPosition() # BaseballPosition | Position number. Format: 1, 2, 3, etc (optional)
team = 'team_example' # str | Unique Team Code. Format: tor, nya, etc (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
state = 'state_example' # str | State where the venue is located. Format: Ohio (optional)
country = 'country_example' # str | Filter players by their home country (optional)
player_id = 56 # int | A unique identifier for a player (optional)
bis_player_id = 56 # int | A unique identifier for a player in the EBIS system (optional)

try:
    # View MLB Draft Prospects
    api_response = api_instance.draft_prospects(year, limit=limit, offset=offset, fields=fields, order=order, sort_by=sort_by, drafted=drafted, round=round, name=name, school=school, position=position, team=team, team_id=team_id, state=state, country=country, player_id=player_id, bis_player_id=bis_player_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->draft_prospects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year the player was drafted. Format: 2000 | 
 **limit** | **int**| Number of results to return | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **order** | [**SortOrderEnum**](.md)| The order of sorting, ascending or descending | [optional] 
 **sort_by** | **str**| Sort the set of data by the specified field | [optional] 
 **drafted** | **bool**| Whether or not the players been drafted | [optional] 
 **round** | **str**| Round in which a player was drafted | [optional] 
 **name** | **str**| Filter players by the first letter of their name using using the specific character | [optional] 
 **school** | **str**| Filter players by the first letter of their school using using the specific character | [optional] 
 **position** | [**BaseballPosition**](.md)| Position number. Format: 1, 2, 3, etc | [optional] 
 **team** | **str**| Unique Team Code. Format: tor, nya, etc | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **state** | **str**| State where the venue is located. Format: Ohio | [optional] 
 **country** | **str**| Filter players by their home country | [optional] 
 **player_id** | **int**| A unique identifier for a player | [optional] 
 **bis_player_id** | **int**| A unique identifier for a player in the EBIS system | [optional] 

### Return type

[**ProspectListRestObject**](ProspectListRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **draft_prospects1**
> ProspectListRestObject draft_prospects1(year, limit=limit, offset=offset, fields=fields, order=order, sort_by=sort_by, drafted=drafted, round=round, name=name, school=school, position=position, team=team, team_id=team_id, state=state, country=country, player_id=player_id, bis_player_id=bis_player_id)

View MLB Draft Prospects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DraftApi()
year = 56 # int | Year the player was drafted. Format: 2000
limit = 56 # int | Number of results to return (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
order = swagger_client.SortOrderEnum() # SortOrderEnum | The order of sorting, ascending or descending (optional)
sort_by = 'sort_by_example' # str | Sort the set of data by the specified field (optional)
drafted = true # bool | Whether or not the players been drafted (optional)
round = 'round_example' # str | Round in which a player was drafted (optional)
name = 'name_example' # str | Filter players by the first letter of their name using using the specific character (optional)
school = 'school_example' # str | Filter players by the first letter of their school using using the specific character (optional)
position = swagger_client.BaseballPosition() # BaseballPosition | Position number. Format: 1, 2, 3, etc (optional)
team = 'team_example' # str | Unique Team Code. Format: tor, nya, etc (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
state = 'state_example' # str | State where the venue is located. Format: Ohio (optional)
country = 'country_example' # str | Filter players by their home country (optional)
player_id = 56 # int | A unique identifier for a player (optional)
bis_player_id = 56 # int | A unique identifier for a player in the EBIS system (optional)

try:
    # View MLB Draft Prospects
    api_response = api_instance.draft_prospects1(year, limit=limit, offset=offset, fields=fields, order=order, sort_by=sort_by, drafted=drafted, round=round, name=name, school=school, position=position, team=team, team_id=team_id, state=state, country=country, player_id=player_id, bis_player_id=bis_player_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->draft_prospects1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year the player was drafted. Format: 2000 | 
 **limit** | **int**| Number of results to return | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **order** | [**SortOrderEnum**](.md)| The order of sorting, ascending or descending | [optional] 
 **sort_by** | **str**| Sort the set of data by the specified field | [optional] 
 **drafted** | **bool**| Whether or not the players been drafted | [optional] 
 **round** | **str**| Round in which a player was drafted | [optional] 
 **name** | **str**| Filter players by the first letter of their name using using the specific character | [optional] 
 **school** | **str**| Filter players by the first letter of their school using using the specific character | [optional] 
 **position** | [**BaseballPosition**](.md)| Position number. Format: 1, 2, 3, etc | [optional] 
 **team** | **str**| Unique Team Code. Format: tor, nya, etc | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **state** | **str**| State where the venue is located. Format: Ohio | [optional] 
 **country** | **str**| Filter players by their home country | [optional] 
 **player_id** | **int**| A unique identifier for a player | [optional] 
 **bis_player_id** | **int**| A unique identifier for a player in the EBIS system | [optional] 

### Return type

[**ProspectListRestObject**](ProspectListRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **latest_draft_picks**
> BaseballDraftLatestRestObject latest_draft_picks(year, fields=fields)

Get the last drafted player and the next 5 teams up to pick

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DraftApi()
year = 56 # int | Year the player was drafted. Format: 2000
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get the last drafted player and the next 5 teams up to pick
    api_response = api_instance.latest_draft_picks(year, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->latest_draft_picks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year the player was drafted. Format: 2000 | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**BaseballDraftLatestRestObject**](BaseballDraftLatestRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

