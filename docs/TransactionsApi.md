# swagger_client.TransactionsApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions**](TransactionsApi.md#transactions) | **GET** /api/v1/transactions | View transaction info

# **transactions**
> TransactionsRestObject transactions(league_id=league_id, sport_id=sport_id, team_id=team_id, player_id=player_id, _date=_date, start_date=start_date, end_date=end_date, transaction_ids=transaction_ids, transaction_types=transaction_types, division_ids=division_ids, order=order, limit=limit, fields=fields)

View transaction info

This endpoint allows you to pull transactions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
league_id = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
sport_id = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
team_id = [56] # list[int] | Comma delimited list of Unique Team identifiers (optional)
player_id = [56] # list[int] | A unique identifier for a player (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
transaction_ids = [56] # list[int] |  (optional)
transaction_types = ['transaction_types_example'] # list[str] |  (optional)
division_ids = [56] # list[int] |  (optional)
order = swagger_client.SortOrderEnum() # SortOrderEnum |  (optional)
limit = 56 # int |  (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # View transaction info
    api_response = api_instance.transactions(league_id=league_id, sport_id=sport_id, team_id=team_id, player_id=player_id, _date=_date, start_date=start_date, end_date=end_date, transaction_ids=transaction_ids, transaction_types=transaction_types, division_ids=division_ids, order=order, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **sport_id** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **team_id** | [**list[int]**](int.md)| Comma delimited list of Unique Team identifiers | [optional] 
 **player_id** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **transaction_ids** | [**list[int]**](int.md)|  | [optional] 
 **transaction_types** | [**list[str]**](str.md)|  | [optional] 
 **division_ids** | [**list[int]**](int.md)|  | [optional] 
 **order** | [**SortOrderEnum**](.md)|  | [optional] 
 **limit** | **int**|  | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**TransactionsRestObject**](TransactionsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

