# GetOrdersRequestFilters

Add filters to your query. All filters are optional

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 
**status** | **str** | The status of the orders you want to receive | [optional] [default to 'processed']
**recipient_name** | **str** | The recipient name of the orders you want to receive | [optional] 
**recipient_email** | **str** | The recipient email of the orders you want to receive | [optional] 
**price** | **float** | The price of the orders you want to receive | [optional] 
**currency** | **str** | The currency of the orders you want to receive | [optional] 
**kg_co2e** | **int** | The amount of kg CO<sub>2</sub>e of the orders you want to receive | [optional] 
**var_from** | **datetime** | Specify a timeframe for your response in ISO 8601 format (UTC) | [optional] 
**to** | **datetime** | Specify a timeframe for your response in ISO 8601 format (UTC) | [optional] 

## Example

```python
from klimapi_python.models.get_orders_request_filters import GetOrdersRequestFilters

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrdersRequestFilters from a JSON string
get_orders_request_filters_instance = GetOrdersRequestFilters.from_json(json)
# print the JSON string representation of the object
print(GetOrdersRequestFilters.to_json())

# convert the object into a dict
get_orders_request_filters_dict = get_orders_request_filters_instance.to_dict()
# create an instance of GetOrdersRequestFilters from a dict
get_orders_request_filters_from_dict = GetOrdersRequestFilters.from_dict(get_orders_request_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


