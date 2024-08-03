# MetadataOrders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[Order]**](Order.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from klimapi_python.models.metadata_orders import MetadataOrders

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataOrders from a JSON string
metadata_orders_instance = MetadataOrders.from_json(json)
# print the JSON string representation of the object
print(MetadataOrders.to_json())

# convert the object into a dict
metadata_orders_dict = metadata_orders_instance.to_dict()
# create an instance of MetadataOrders from a dict
metadata_orders_from_dict = MetadataOrders.from_dict(metadata_orders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


