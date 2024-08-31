# PendingByCalculationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_options** | [**List[PendingByCalculationRequestCalculationOptionsInner]**](PendingByCalculationRequestCalculationOptionsInner.md) | An Array of [Calculation Options](https://klimapi.com/resources/factors). See the full list of supported options [here](https://klimapi.com/resources/factors). | 
**order_count** | **int** | The amount of pending Orders you want to receive. This is especially useful if you want to offer your customers several different projects for their compensation. | [optional] [default to 1]
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 
**fractional_digits** | **int** | Normally, the calculation results are rounded to the nearest whole number. Specify here how many decimal places you would like to receive in addition. This only applies to calculation results, compensations are always made in whole kilograms | [optional] [default to 2]

## Example

```python
from klimapi_python.models.pending_by_calculation_request import PendingByCalculationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PendingByCalculationRequest from a JSON string
pending_by_calculation_request_instance = PendingByCalculationRequest.from_json(json)
# print the JSON string representation of the object
print(PendingByCalculationRequest.to_json())

# convert the object into a dict
pending_by_calculation_request_dict = pending_by_calculation_request_instance.to_dict()
# create an instance of PendingByCalculationRequest from a dict
pending_by_calculation_request_from_dict = PendingByCalculationRequest.from_dict(pending_by_calculation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


