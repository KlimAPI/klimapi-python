# PendingByPriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_amount** | **float** | The total of the compensation in your given currency **excl. VAT**. Minimum order is 0.5 in your given currency. | 
**order_count** | **int** | The amount of pending Orders you want to receive. This is especially useful if you want to offer your customers several different projects for their compensation. | [optional] [default to 1]
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 

## Example

```python
from klimapi_python.models.pending_by_price_request import PendingByPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PendingByPriceRequest from a JSON string
pending_by_price_request_instance = PendingByPriceRequest.from_json(json)
# print the JSON string representation of the object
print(PendingByPriceRequest.to_json())

# convert the object into a dict
pending_by_price_request_dict = pending_by_price_request_instance.to_dict()
# create an instance of PendingByPriceRequest from a dict
pending_by_price_request_from_dict = PendingByPriceRequest.from_dict(pending_by_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


