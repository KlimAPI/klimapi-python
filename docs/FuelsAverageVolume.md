# FuelsAverageVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 11)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'cubic meters']

## Example

```python
from klimapi_python.models.fuels_average_volume import FuelsAverageVolume

# TODO update the JSON string below
json = "{}"
# create an instance of FuelsAverageVolume from a JSON string
fuels_average_volume_instance = FuelsAverageVolume.from_json(json)
# print the JSON string representation of the object
print(FuelsAverageVolume.to_json())

# convert the object into a dict
fuels_average_volume_dict = fuels_average_volume_instance.to_dict()
# create an instance of FuelsAverageVolume from a dict
fuels_average_volume_from_dict = FuelsAverageVolume.from_dict(fuels_average_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


