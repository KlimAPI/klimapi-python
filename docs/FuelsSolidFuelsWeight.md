# FuelsSolidFuelsWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'solid_fuels']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.fuels_solid_fuels_weight import FuelsSolidFuelsWeight

# TODO update the JSON string below
json = "{}"
# create an instance of FuelsSolidFuelsWeight from a JSON string
fuels_solid_fuels_weight_instance = FuelsSolidFuelsWeight.from_json(json)
# print the JSON string representation of the object
print(FuelsSolidFuelsWeight.to_json())

# convert the object into a dict
fuels_solid_fuels_weight_dict = fuels_solid_fuels_weight_instance.to_dict()
# create an instance of FuelsSolidFuelsWeight from a dict
fuels_solid_fuels_weight_from_dict = FuelsSolidFuelsWeight.from_dict(fuels_solid_fuels_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


