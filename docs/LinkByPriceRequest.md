# LinkByPriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_amount** | **float** | The total of the compensation in your given currency **incl. VAT**. Minimum order is 0.5 in your given currency. | 
**change_allowed** | **bool** | Choose if the customer should be allowed to change the amount. | [optional] [default to False]
**success_url** | **str** | The URL the customer is redirected to after the successful compensation. | 
**cancel_url** | **str** | The URL the customer is redirected to after a failed or aborted compensation. | 
**order_count** | **int** | The amount of pending Orders you want to receive. This is especially useful if you want to offer your customers several different projects for their compensation. | [optional] [default to 1]
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 

## Example

```python
from klimapi_python.models.link_by_price_request import LinkByPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkByPriceRequest from a JSON string
link_by_price_request_instance = LinkByPriceRequest.from_json(json)
# print the JSON string representation of the object
print(LinkByPriceRequest.to_json())

# convert the object into a dict
link_by_price_request_dict = link_by_price_request_instance.to_dict()
# create an instance of LinkByPriceRequest from a dict
link_by_price_request_from_dict = LinkByPriceRequest.from_dict(link_by_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


