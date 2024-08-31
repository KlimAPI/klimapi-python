# FuelsLiquidFuelsWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'liquid_fuels']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.fuels_liquid_fuels_weight import FuelsLiquidFuelsWeight

# TODO update the JSON string below
json = "{}"
# create an instance of FuelsLiquidFuelsWeight from a JSON string
fuels_liquid_fuels_weight_instance = FuelsLiquidFuelsWeight.from_json(json)
# print the JSON string representation of the object
print(FuelsLiquidFuelsWeight.to_json())

# convert the object into a dict
fuels_liquid_fuels_weight_dict = fuels_liquid_fuels_weight_instance.to_dict()
# create an instance of FuelsLiquidFuelsWeight from a dict
fuels_liquid_fuels_weight_from_dict = FuelsLiquidFuelsWeight.from_dict(fuels_liquid_fuels_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


