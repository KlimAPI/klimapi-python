# BioenergyBiofuelWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'biofuel']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.bioenergy_biofuel_weight import BioenergyBiofuelWeight

# TODO update the JSON string below
json = "{}"
# create an instance of BioenergyBiofuelWeight from a JSON string
bioenergy_biofuel_weight_instance = BioenergyBiofuelWeight.from_json(json)
# print the JSON string representation of the object
print(BioenergyBiofuelWeight.to_json())

# convert the object into a dict
bioenergy_biofuel_weight_dict = bioenergy_biofuel_weight_instance.to_dict()
# create an instance of BioenergyBiofuelWeight from a dict
bioenergy_biofuel_weight_from_dict = BioenergyBiofuelWeight.from_dict(bioenergy_biofuel_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


