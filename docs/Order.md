# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**certificate_issued_at** | **datetime** | Timestamp of when the certificate was issued in ISO 8601 format (UTC) | [optional] 
**certificate_url** | **str** |  | [optional] 
**certificate_pdf** | **str** |  | [optional] 
**price** | **float** | The total of the compensation in your given currency **excl. VAT**. | [optional] 
**currency** | **str** |  | [optional] 
**kg_co2e** | **int** | The amount of kg CO&lt;sub&gt;2&lt;/sub&gt;e. | [optional] 
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**recipient** | [**OrderRecipient**](OrderRecipient.md) |  | [optional] 

## Example

```python
from klimapi_python.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


