# PendingByCarbonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kg_co2e** | **int** | The amount of kg CO&lt;sub&gt;2&lt;/sub&gt;e the compensation should provide | 
**order_count** | **int** | The amount of pending Orders you want to receive. This is especially useful if you want to offer your customers several different projects for their compensation. | [optional] [default to 1]
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 

## Example

```python
from klimapi_python.models.pending_by_carbon_request import PendingByCarbonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PendingByCarbonRequest from a JSON string
pending_by_carbon_request_instance = PendingByCarbonRequest.from_json(json)
# print the JSON string representation of the object
print(PendingByCarbonRequest.to_json())

# convert the object into a dict
pending_by_carbon_request_dict = pending_by_carbon_request_instance.to_dict()
# create an instance of PendingByCarbonRequest from a dict
pending_by_carbon_request_from_dict = PendingByCarbonRequest.from_dict(pending_by_carbon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


