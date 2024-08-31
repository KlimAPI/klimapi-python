# WaterSupplyVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 11)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'cubic meters']

## Example

```python
from klimapi_python.models.water_supply_volume import WaterSupplyVolume

# TODO update the JSON string below
json = "{}"
# create an instance of WaterSupplyVolume from a JSON string
water_supply_volume_instance = WaterSupplyVolume.from_json(json)
# print the JSON string representation of the object
print(WaterSupplyVolume.to_json())

# convert the object into a dict
water_supply_volume_dict = water_supply_volume_instance.to_dict()
# create an instance of WaterSupplyVolume from a dict
water_supply_volume_from_dict = WaterSupplyVolume.from_dict(water_supply_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


