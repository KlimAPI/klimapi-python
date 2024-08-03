# CalculationResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kg_co2e** | **float** | The calculated Amount of CO&lt;sub&gt;2&lt;/sub&gt; in Kilogram. | [optional] 
**calculation_id** | **str** | The unique identifier of the calculation | [optional] 
**results** | [**List[CalculationResult]**](CalculationResult.md) |  | [optional] 

## Example

```python
from klimapi_python.models.calculation_results import CalculationResults

# TODO update the JSON string below
json = "{}"
# create an instance of CalculationResults from a JSON string
calculation_results_instance = CalculationResults.from_json(json)
# print the JSON string representation of the object
print(CalculationResults.to_json())

# convert the object into a dict
calculation_results_dict = calculation_results_instance.to_dict()
# create an instance of CalculationResults from a dict
calculation_results_from_dict = CalculationResults.from_dict(calculation_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


