# EnergyConsumptionByTypeEnergy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'by_type']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 3)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'kWh']

## Example

```python
from klimapi_python.models.energy_consumption_by_type_energy import EnergyConsumptionByTypeEnergy

# TODO update the JSON string below
json = "{}"
# create an instance of EnergyConsumptionByTypeEnergy from a JSON string
energy_consumption_by_type_energy_instance = EnergyConsumptionByTypeEnergy.from_json(json)
# print the JSON string representation of the object
print(EnergyConsumptionByTypeEnergy.to_json())

# convert the object into a dict
energy_consumption_by_type_energy_dict = energy_consumption_by_type_energy_instance.to_dict()
# create an instance of EnergyConsumptionByTypeEnergy from a dict
energy_consumption_by_type_energy_from_dict = EnergyConsumptionByTypeEnergy.from_dict(energy_consumption_by_type_energy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


