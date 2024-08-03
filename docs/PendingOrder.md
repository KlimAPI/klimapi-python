# PendingOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**price** | **float** | The total of the compensation in your given currency **excl. VAT**. | [optional] 
**currency** | **str** |  | [optional] 
**kg_co2e** | **int** | The amount of kg CO&lt;sub&gt;2&lt;/sub&gt;e. | [optional] 
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 

## Example

```python
from klimapi_python.models.pending_order import PendingOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PendingOrder from a JSON string
pending_order_instance = PendingOrder.from_json(json)
# print the JSON string representation of the object
print(PendingOrder.to_json())

# convert the object into a dict
pending_order_dict = pending_order_instance.to_dict()
# create an instance of PendingOrder from a dict
pending_order_from_dict = PendingOrder.from_dict(pending_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


