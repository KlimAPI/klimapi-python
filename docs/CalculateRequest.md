# CalculateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_options** | [**List[PendingByCalculationRequestCalculationOptionsInner]**](PendingByCalculationRequestCalculationOptionsInner.md) | An Array of [Calculation Options](https://klimapi.com/resources/factors). See the full list of supported options [here](https://klimapi.com/resources/factors). | 
**fractional_digits** | **int** | Normally, the calculation results are rounded to the nearest whole number. Specify here how many decimal places you would like to receive in addition. This only applies to calculation results, compensations are always made in whole kilograms | [optional] [default to 2]

## Example

```python
from klimapi_python.models.calculate_request import CalculateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateRequest from a JSON string
calculate_request_instance = CalculateRequest.from_json(json)
# print the JSON string representation of the object
print(CalculateRequest.to_json())

# convert the object into a dict
calculate_request_dict = calculate_request_instance.to_dict()
# create an instance of CalculateRequest from a dict
calculate_request_from_dict = CalculateRequest.from_dict(calculate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


