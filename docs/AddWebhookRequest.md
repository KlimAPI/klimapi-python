# AddWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hook_url** | **str** | The endpoint the POST request will be sent to | 
**trigger** | **str** | The trigger which will cause the webhook to be sent | 

## Example

```python
from klimapi_python.models.add_webhook_request import AddWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddWebhookRequest from a JSON string
add_webhook_request_instance = AddWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(AddWebhookRequest.to_json())

# convert the object into a dict
add_webhook_request_dict = add_webhook_request_instance.to_dict()
# create an instance of AddWebhookRequest from a dict
add_webhook_request_from_dict = AddWebhookRequest.from_dict(add_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


