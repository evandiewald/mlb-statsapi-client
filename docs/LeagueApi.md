# swagger_client.LeagueApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_star_ballot**](LeagueApi.md#all_star_ballot) | **GET** /api/v1/league/allStarBallot | View al star ballot info
[**all_star_ballot1**](LeagueApi.md#all_star_ballot1) | **GET** /api/v1/league/{leagueId}/allStarBallot | View al star ballot info
[**all_star_ballot2**](LeagueApi.md#all_star_ballot2) | **GET** /api/v1/leagues/allStarBallot | View al star ballot info
[**all_star_ballot3**](LeagueApi.md#all_star_ballot3) | **GET** /api/v1/leagues/{leagueId}/allStarBallot | View al star ballot info
[**all_star_final_vote**](LeagueApi.md#all_star_final_vote) | **GET** /api/v1/league/{leagueId}/allStarFinalVote | View all star final vote info
[**all_star_final_vote1**](LeagueApi.md#all_star_final_vote1) | **GET** /api/v1/leagues/{leagueId}/allStarFinalVote | View all star final vote info
[**all_star_write_ins**](LeagueApi.md#all_star_write_ins) | **GET** /api/v1/league/{leagueId}/allStarWriteIns | View all star write ins info
[**all_star_write_ins1**](LeagueApi.md#all_star_write_ins1) | **GET** /api/v1/leagues/{leagueId}/allStarWriteIns | View all star write ins info
[**league**](LeagueApi.md#league) | **GET** /api/v1/league | View league info
[**league1**](LeagueApi.md#league1) | **GET** /api/v1/league/{leagueId} | View league info
[**league2**](LeagueApi.md#league2) | **GET** /api/v1/leagues | View league info
[**league3**](LeagueApi.md#league3) | **GET** /api/v1/leagues/{leagueId} | View league info

# **all_star_ballot**
> str all_star_ballot(league_id, league_ids=league_ids, season=season, fields=fields)

View al star ballot info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View al star ballot info
    api_response = api_instance.all_star_ballot(league_id, league_ids=league_ids, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->all_star_ballot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_star_ballot1**
> str all_star_ballot1(league_id, league_ids=league_ids, season=season, fields=fields)

View al star ballot info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View al star ballot info
    api_response = api_instance.all_star_ballot1(league_id, league_ids=league_ids, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->all_star_ballot1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_star_ballot2**
> str all_star_ballot2(league_id, league_ids=league_ids, season=season, fields=fields)

View al star ballot info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View al star ballot info
    api_response = api_instance.all_star_ballot2(league_id, league_ids=league_ids, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->all_star_ballot2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_star_ballot3**
> str all_star_ballot3(league_id, league_ids=league_ids, season=season, fields=fields)

View al star ballot info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View al star ballot info
    api_response = api_instance.all_star_ballot3(league_id, league_ids=league_ids, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->all_star_ballot3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_star_final_vote**
> str all_star_final_vote(league_id, season=season, fields=fields)

View all star final vote info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View all star final vote info
    api_response = api_instance.all_star_final_vote(league_id, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->all_star_final_vote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_star_final_vote1**
> str all_star_final_vote1(league_id, season=season, fields=fields)

View all star final vote info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View all star final vote info
    api_response = api_instance.all_star_final_vote1(league_id, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->all_star_final_vote1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_star_write_ins**
> str all_star_write_ins(league_id, season=season, fields=fields)

View all star write ins info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View all star write ins info
    api_response = api_instance.all_star_write_ins(league_id, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->all_star_write_ins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_star_write_ins1**
> str all_star_write_ins1(league_id, season=season, fields=fields)

View all star write ins info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
season = 'season_example' # str | Season of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View all star write ins info
    api_response = api_instance.all_star_write_ins1(league_id, season=season, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->all_star_write_ins1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **season** | **str**| Season of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league**
> str league(league_id, league_ids=league_ids, season=season, seasons=seasons, fields=fields, sport_id=sport_id, active_status=active_status)

View league info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
active_status = swagger_client.LeagueActiveStatusEnum() # LeagueActiveStatusEnum | Flag for fetching leagues that are currently active (Y), inactive (N), pending (P), or all teams (B) (optional)

try:
    # View league info
    api_response = api_instance.league(league_id, league_ids=league_ids, season=season, seasons=seasons, fields=fields, sport_id=sport_id, active_status=active_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->league: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **active_status** | [**LeagueActiveStatusEnum**](.md)| Flag for fetching leagues that are currently active (Y), inactive (N), pending (P), or all teams (B) | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league1**
> str league1(league_id, league_ids=league_ids, season=season, seasons=seasons, fields=fields, sport_id=sport_id, active_status=active_status)

View league info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
active_status = swagger_client.LeagueActiveStatusEnum() # LeagueActiveStatusEnum | Flag for fetching leagues that are currently active (Y), inactive (N), pending (P), or all teams (B) (optional)

try:
    # View league info
    api_response = api_instance.league1(league_id, league_ids=league_ids, season=season, seasons=seasons, fields=fields, sport_id=sport_id, active_status=active_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->league1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **active_status** | [**LeagueActiveStatusEnum**](.md)| Flag for fetching leagues that are currently active (Y), inactive (N), pending (P), or all teams (B) | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league2**
> str league2(league_id, league_ids=league_ids, season=season, seasons=seasons, fields=fields, sport_id=sport_id, active_status=active_status)

View league info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
active_status = swagger_client.LeagueActiveStatusEnum() # LeagueActiveStatusEnum | Flag for fetching leagues that are currently active (Y), inactive (N), pending (P), or all teams (B) (optional)

try:
    # View league info
    api_response = api_instance.league2(league_id, league_ids=league_ids, season=season, seasons=seasons, fields=fields, sport_id=sport_id, active_status=active_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->league2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **active_status** | [**LeagueActiveStatusEnum**](.md)| Flag for fetching leagues that are currently active (Y), inactive (N), pending (P), or all teams (B) | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league3**
> str league3(league_id, league_ids=league_ids, season=season, seasons=seasons, fields=fields, sport_id=sport_id, active_status=active_status)

View league info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeagueApi()
league_id = 56 # int | Unique League Identifier
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
active_status = swagger_client.LeagueActiveStatusEnum() # LeagueActiveStatusEnum | Flag for fetching leagues that are currently active (Y), inactive (N), pending (P), or all teams (B) (optional)

try:
    # View league info
    api_response = api_instance.league3(league_id, league_ids=league_ids, season=season, seasons=seasons, fields=fields, sport_id=sport_id, active_status=active_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeagueApi->league3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| Unique League Identifier | 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **active_status** | [**LeagueActiveStatusEnum**](.md)| Flag for fetching leagues that are currently active (Y), inactive (N), pending (P), or all teams (B) | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

