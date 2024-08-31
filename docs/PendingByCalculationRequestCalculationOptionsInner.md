# PendingByCalculationRequestCalculationOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** | Describe the individual factor | 
**specification** | **str** | Specify the individual factor | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Describe the unit used by the multiplier | 
**detail** | **str** |  **Hint:** Some specifications only support certain details. | [optional] [default to 'average']
**departure** | **str** | City, Postal Address, Train Station or IATA Code of the departure address | 
**destination** | **str** | City, Postal Address, Train Station or IATA Code of the destination address | 
**return_trip** | **bool** | Decide if the trip is one way or return | [optional] [default to True]
**passengers** | **int** | The total of passengers travelling this route | [optional] [default to 1]
**weight** | **float** | The total weight travelling this route | [optional] [default to 1]
**weight_unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']
**amount** | **int** | The amount of kg CO*2*e you want to add to the calculation. | 
**multiplier** | **int** | Multiplier for the given amount | [optional] [default to 1]

## Example

```python
from klimapi_python.models.pending_by_calculation_request_calculation_options_inner import PendingByCalculationRequestCalculationOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PendingByCalculationRequestCalculationOptionsInner from a JSON string
pending_by_calculation_request_calculation_options_inner_instance = PendingByCalculationRequestCalculationOptionsInner.from_json(json)
# print the JSON string representation of the object
print(PendingByCalculationRequestCalculationOptionsInner.to_json())

# convert the object into a dict
pending_by_calculation_request_calculation_options_inner_dict = pending_by_calculation_request_calculation_options_inner_instance.to_dict()
# create an instance of PendingByCalculationRequestCalculationOptionsInner from a dict
pending_by_calculation_request_calculation_options_inner_from_dict = PendingByCalculationRequestCalculationOptionsInner.from_dict(pending_by_calculation_request_calculation_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


