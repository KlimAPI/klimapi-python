# OrderRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from klimapi_python.models.order_recipient import OrderRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRecipient from a JSON string
order_recipient_instance = OrderRecipient.from_json(json)
# print the JSON string representation of the object
print(OrderRecipient.to_json())

# convert the object into a dict
order_recipient_dict = order_recipient_instance.to_dict()
# create an instance of OrderRecipient from a dict
order_recipient_from_dict = OrderRecipient.from_dict(order_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


