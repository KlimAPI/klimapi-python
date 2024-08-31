# OrderByCalculationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_options** | [**List[PendingByCalculationRequestCalculationOptionsInner]**](PendingByCalculationRequestCalculationOptionsInner.md) | An Array of [Calculation Options](https://klimapi.com/resources/factors). See the full list of supported options [here](https://klimapi.com/resources/factors). | 
**recipient_name** | **str** | The name which should be associated with the compensation | [optional] 
**recipient_email** | **str** | If a valid e-mail address is provided, we will send the certificate to this address | [optional] 
**send_at** | **datetime** | Timestamp of when the certificate should be send to the customer in ISO 8601 format (UTC). Defaults to the current timestamp. | [optional] 
**price_limit** | **float** | Set an optional price limit. if the order would exceed the limit a error will be thrown. Set the limit in the given currency. | [optional] 
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 
**fractional_digits** | **int** | Normally, the calculation results are rounded to the nearest whole number. Specify here how many decimal places you would like to receive in addition. This only applies to calculation results, compensations are always made in whole kilograms | [optional] [default to 2]

## Example

```python
from klimapi_python.models.order_by_calculation_request import OrderByCalculationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderByCalculationRequest from a JSON string
order_by_calculation_request_instance = OrderByCalculationRequest.from_json(json)
# print the JSON string representation of the object
print(OrderByCalculationRequest.to_json())

# convert the object into a dict
order_by_calculation_request_dict = order_by_calculation_request_instance.to_dict()
# create an instance of OrderByCalculationRequest from a dict
order_by_calculation_request_from_dict = OrderByCalculationRequest.from_dict(order_by_calculation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


