# CalculationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kg_co2e** | **float** | The calculated Amount of CO<sub>2</sub> in Kilogram. | [optional] 
**type** | **str** | The type of the calculation | [optional] 
**activity** | **str** | The activity of the calculation | [optional] 
**specification** | **str** | The specification of the calculation | [optional] 
**detail** | **str** | The detail of the calculation | [optional] 
**value** | **float** | The value of the calculation | [optional] 
**unit** | **str** | The unit of the calculation | [optional] 
**emission_factor_id** | **str** | The unique identifier of the emission factor the calculation is based on | [optional] 
**emission_factor_last_updated** | **str** | ISO 8601 formatted timestamp of the latest update for the given emission factor | [optional] 

## Example

```python
from klimapi_python.models.calculation_result import CalculationResult

# TODO update the JSON string below
json = "{}"
# create an instance of CalculationResult from a JSON string
calculation_result_instance = CalculationResult.from_json(json)
# print the JSON string representation of the object
print(CalculationResult.to_json())

# convert the object into a dict
calculation_result_dict = calculation_result_instance.to_dict()
# create an instance of CalculationResult from a dict
calculation_result_from_dict = CalculationResult.from_dict(calculation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


