# IndividualFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** | Describe the individual factor | 
**specification** | **str** | Specify the individual factor | 
**unit** | **str** | Describe the unit used by the multiplier | 
**amount** | **int** | The amount of kg CO*2*e you want to add to the calculation. | 
**multiplier** | **int** | Multiplier for the given amount | [optional] [default to 1]

## Example

```python
from klimapi_python.models.individual_factor import IndividualFactor

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualFactor from a JSON string
individual_factor_instance = IndividualFactor.from_json(json)
# print the JSON string representation of the object
print(IndividualFactor.to_json())

# convert the object into a dict
individual_factor_dict = individual_factor_instance.to_dict()
# create an instance of IndividualFactor from a dict
individual_factor_from_dict = IndividualFactor.from_dict(individual_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


