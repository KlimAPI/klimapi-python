# PendingOrdersCalculated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending_orders** | [**List[PendingOrderCalculated]**](PendingOrderCalculated.md) |  | [optional] 

## Example

```python
from klimapi_python.models.pending_orders_calculated import PendingOrdersCalculated

# TODO update the JSON string below
json = "{}"
# create an instance of PendingOrdersCalculated from a JSON string
pending_orders_calculated_instance = PendingOrdersCalculated.from_json(json)
# print the JSON string representation of the object
print(PendingOrdersCalculated.to_json())

# convert the object into a dict
pending_orders_calculated_dict = pending_orders_calculated_instance.to_dict()
# create an instance of PendingOrdersCalculated from a dict
pending_orders_calculated_from_dict = PendingOrdersCalculated.from_dict(pending_orders_calculated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


