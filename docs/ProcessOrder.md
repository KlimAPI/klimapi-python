# ProcessOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_name** | **str** | The name which should be associated with the compensation | 
**recipient_email** | **str** | If a valid e-mail address is provided, we will send the certificate to this address | [optional] 
**send_at** | **datetime** | Timestamp of when the certificate should be send to the customer in ISO 8601 format (UTC). Defaults to the current timestamp. | [optional] 
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 

## Example

```python
from klimapi_python.models.process_order import ProcessOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessOrder from a JSON string
process_order_instance = ProcessOrder.from_json(json)
# print the JSON string representation of the object
print(ProcessOrder.to_json())

# convert the object into a dict
process_order_dict = process_order_instance.to_dict()
# create an instance of ProcessOrder from a dict
process_order_from_dict = ProcessOrder.from_dict(process_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


