# BioenergyBiogasWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'biogas']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.bioenergy_biogas_weight import BioenergyBiogasWeight

# TODO update the JSON string below
json = "{}"
# create an instance of BioenergyBiogasWeight from a JSON string
bioenergy_biogas_weight_instance = BioenergyBiogasWeight.from_json(json)
# print the JSON string representation of the object
print(BioenergyBiogasWeight.to_json())

# convert the object into a dict
bioenergy_biogas_weight_dict = bioenergy_biogas_weight_instance.to_dict()
# create an instance of BioenergyBiogasWeight from a dict
bioenergy_biogas_weight_from_dict = BioenergyBiogasWeight.from_dict(bioenergy_biogas_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


