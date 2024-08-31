# BioenergyBiomassWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'biomass']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.bioenergy_biomass_weight import BioenergyBiomassWeight

# TODO update the JSON string below
json = "{}"
# create an instance of BioenergyBiomassWeight from a JSON string
bioenergy_biomass_weight_instance = BioenergyBiomassWeight.from_json(json)
# print the JSON string representation of the object
print(BioenergyBiomassWeight.to_json())

# convert the object into a dict
bioenergy_biomass_weight_dict = bioenergy_biomass_weight_instance.to_dict()
# create an instance of BioenergyBiomassWeight from a dict
bioenergy_biomass_weight_from_dict = BioenergyBiomassWeight.from_dict(bioenergy_biomass_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


