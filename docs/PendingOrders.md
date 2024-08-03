# PendingOrders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending_orders** | [**List[PendingOrder]**](PendingOrder.md) |  | [optional] 

## Example

```python
from klimapi_python.models.pending_orders import PendingOrders

# TODO update the JSON string below
json = "{}"
# create an instance of PendingOrders from a JSON string
pending_orders_instance = PendingOrders.from_json(json)
# print the JSON string representation of the object
print(PendingOrders.to_json())

# convert the object into a dict
pending_orders_dict = pending_orders_instance.to_dict()
# create an instance of PendingOrders from a dict
pending_orders_from_dict = PendingOrders.from_dict(pending_orders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


