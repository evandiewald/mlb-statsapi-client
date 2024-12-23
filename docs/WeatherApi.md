# swagger_client.WeatherApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**weather_basic**](WeatherApi.md#weather_basic) | **GET** /api/v1/weather/venues/{venueId}/basic | Get basic weather for a venue.
[**weather_data_based_on_play**](WeatherApi.md#weather_data_based_on_play) | **GET** /api/v1/weather/game/{gamePk}/{playId} | Get the raw field weather data.
[**weather_forecast**](WeatherApi.md#weather_forecast) | **GET** /api/v1/weather/game/{gamePk}/forecast/{roofType} | Get the weather forecast for a game.
[**weather_full**](WeatherApi.md#weather_full) | **GET** /api/v1/weather/venues/{venueId}/full | Get full weather for a venue.

# **weather_basic**
> BasicWeatherWrapperRestObject weather_basic(venue_id, fields=fields)

Get basic weather for a venue.

Returns a json file containing basic weather for a specific venue.

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
api_instance = swagger_client.WeatherApi(swagger_client.ApiClient(configuration))
venue_id = 56 # int | Unique Venue Identifier
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get basic weather for a venue.
    api_response = api_instance.weather_basic(venue_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeatherApi->weather_basic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **venue_id** | **int**| Unique Venue Identifier | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**BasicWeatherWrapperRestObject**](BasicWeatherWrapperRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weather_data_based_on_play**
> PlayWeatherWrapperRestObject weather_data_based_on_play(game_pk, play_id, fields=fields)

Get the raw field weather data.

Returns a json file containing weather for the current play.

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
api_instance = swagger_client.WeatherApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game
play_id = 'play_id_example' # str | Unique identifier for a play within a game
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get the raw field weather data.
    api_response = api_instance.weather_data_based_on_play(game_pk, play_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeatherApi->weather_data_based_on_play: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **play_id** | **str**| Unique identifier for a play within a game | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**PlayWeatherWrapperRestObject**](PlayWeatherWrapperRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weather_forecast**
> ForecastWeatherWrapperRestObject weather_forecast(game_pk, roof_type, fields=fields)

Get the weather forecast for a game.

Returns a json file containing the weather forecast for a specific game.

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
api_instance = swagger_client.WeatherApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | Unique Primary Key Representing a Game
roof_type = swagger_client.RoofType() # RoofType | Venue roof type
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get the weather forecast for a game.
    api_response = api_instance.weather_forecast(game_pk, roof_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeatherApi->weather_forecast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**| Unique Primary Key Representing a Game | 
 **roof_type** | [**RoofType**](.md)| Venue roof type | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**ForecastWeatherWrapperRestObject**](ForecastWeatherWrapperRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weather_full**
> FullWeatherWrapperRestObject weather_full(venue_id, fields=fields)

Get full weather for a venue.

Returns a json file containing full weather for a specific venue.

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
api_instance = swagger_client.WeatherApi(swagger_client.ApiClient(configuration))
venue_id = 56 # int | Unique Venue Identifier
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get full weather for a venue.
    api_response = api_instance.weather_full(venue_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeatherApi->weather_full: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **venue_id** | **int**| Unique Venue Identifier | 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**FullWeatherWrapperRestObject**](FullWeatherWrapperRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

