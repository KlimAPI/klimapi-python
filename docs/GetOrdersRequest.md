# GetOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | The operator to combine the filters with | [optional] [default to 'AND']
**filters** | [**GetOrdersRequestFilters**](GetOrdersRequestFilters.md) |  | [optional] 
**limit** | **int** | The maximum amount of orders you want to receive | [optional] [default to 10]
**skip** | **int** | The amount of orders you want to skip | [optional] [default to 0]

## Example

```python
from klimapi_python.models.get_orders_request import GetOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrdersRequest from a JSON string
get_orders_request_instance = GetOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrdersRequest.to_json())

# convert the object into a dict
get_orders_request_dict = get_orders_request_instance.to_dict()
# create an instance of GetOrdersRequest from a dict
get_orders_request_from_dict = GetOrdersRequest.from_dict(get_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


