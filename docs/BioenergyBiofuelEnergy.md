# BioenergyBiofuelEnergy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'biofuel']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 3)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'kWh']

## Example

```python
from klimapi_python.models.bioenergy_biofuel_energy import BioenergyBiofuelEnergy

# TODO update the JSON string below
json = "{}"
# create an instance of BioenergyBiofuelEnergy from a JSON string
bioenergy_biofuel_energy_instance = BioenergyBiofuelEnergy.from_json(json)
# print the JSON string representation of the object
print(BioenergyBiofuelEnergy.to_json())

# convert the object into a dict
bioenergy_biofuel_energy_dict = bioenergy_biofuel_energy_instance.to_dict()
# create an instance of BioenergyBiofuelEnergy from a dict
bioenergy_biofuel_energy_from_dict = BioenergyBiofuelEnergy.from_dict(bioenergy_biofuel_energy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


