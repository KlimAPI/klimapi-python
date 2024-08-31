# BioenergyAverageVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 11)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'cubic meters']

## Example

```python
from klimapi_python.models.bioenergy_average_volume import BioenergyAverageVolume

# TODO update the JSON string below
json = "{}"
# create an instance of BioenergyAverageVolume from a JSON string
bioenergy_average_volume_instance = BioenergyAverageVolume.from_json(json)
# print the JSON string representation of the object
print(BioenergyAverageVolume.to_json())

# convert the object into a dict
bioenergy_average_volume_dict = bioenergy_average_volume_instance.to_dict()
# create an instance of BioenergyAverageVolume from a dict
bioenergy_average_volume_from_dict = BioenergyAverageVolume.from_dict(bioenergy_average_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


