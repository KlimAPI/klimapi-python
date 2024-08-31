# BioenergyAverageEnergy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 3)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'kWh']

## Example

```python
from klimapi_python.models.bioenergy_average_energy import BioenergyAverageEnergy

# TODO update the JSON string below
json = "{}"
# create an instance of BioenergyAverageEnergy from a JSON string
bioenergy_average_energy_instance = BioenergyAverageEnergy.from_json(json)
# print the JSON string representation of the object
print(BioenergyAverageEnergy.to_json())

# convert the object into a dict
bioenergy_average_energy_dict = bioenergy_average_energy_instance.to_dict()
# create an instance of BioenergyAverageEnergy from a dict
bioenergy_average_energy_from_dict = BioenergyAverageEnergy.from_dict(bioenergy_average_energy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


