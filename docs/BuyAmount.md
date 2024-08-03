# BuyAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kg_co2e** | **int** | The amount of kg CO&lt;sub&gt;2&lt;/sub&gt;e the compensation should provide | 
**recipient_name** | **str** | The name which should be associated with the compensation | 
**recipient_email** | **str** | If a valid e-mail address is provided, we will send the certificate to this address | [optional] 
**send_at** | **datetime** | Timestamp of when the certificate should be send to the customer in ISO 8601 format (UTC). Defaults to the current timestamp. | [optional] 
**price_limit** | **float** | Set an optional price limit. if the order would exceed the limit a error will be thrown. Set the limit in the given currency. | [optional] 
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 

## Example

```python
from klimapi_python.models.buy_amount import BuyAmount

# TODO update the JSON string below
json = "{}"
# create an instance of BuyAmount from a JSON string
buy_amount_instance = BuyAmount.from_json(json)
# print the JSON string representation of the object
print(BuyAmount.to_json())

# convert the object into a dict
buy_amount_dict = buy_amount_instance.to_dict()
# create an instance of BuyAmount from a dict
buy_amount_from_dict = BuyAmount.from_dict(buy_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


