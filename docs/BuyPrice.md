# BuyPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_amount** | **float** | The total of the compensation in your given currency **excl. VAT**. Minimum order is 0.5 in your given currency. | 
**recipient_name** | **str** | The name which should be associated with the compensation | 
**recipient_email** | **str** | If a valid e-mail address is provided, we will send the certificate to this address | [optional] 
**send_at** | **datetime** | Timestamp of when the certificate should be send to the customer in ISO 8601 format (UTC). Defaults to the current timestamp. | [optional] 
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 

## Example

```python
from klimapi_python.models.buy_price import BuyPrice

# TODO update the JSON string below
json = "{}"
# create an instance of BuyPrice from a JSON string
buy_price_instance = BuyPrice.from_json(json)
# print the JSON string representation of the object
print(BuyPrice.to_json())

# convert the object into a dict
buy_price_dict = buy_price_instance.to_dict()
# create an instance of BuyPrice from a dict
buy_price_from_dict = BuyPrice.from_dict(buy_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


