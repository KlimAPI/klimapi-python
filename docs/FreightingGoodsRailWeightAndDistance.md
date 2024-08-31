# FreightingGoodsRailWeightAndDistance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'rail']
**specification** | **str** |  | [optional] [default to 'freight_train']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Distance a specific weight traveled in the given unit.    **Example:** 10 metric tons travel 50 kilometers. So the right `value` would be **500** and the `unit` would be **metric tons.kilometers**.    Need a more specific unit? See the **[full list of supported units (Sections 5 and 6)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons.kilometers']

## Example

```python
from klimapi_python.models.freighting_goods_rail_weight_and_distance import FreightingGoodsRailWeightAndDistance

# TODO update the JSON string below
json = "{}"
# create an instance of FreightingGoodsRailWeightAndDistance from a JSON string
freighting_goods_rail_weight_and_distance_instance = FreightingGoodsRailWeightAndDistance.from_json(json)
# print the JSON string representation of the object
print(FreightingGoodsRailWeightAndDistance.to_json())

# convert the object into a dict
freighting_goods_rail_weight_and_distance_dict = freighting_goods_rail_weight_and_distance_instance.to_dict()
# create an instance of FreightingGoodsRailWeightAndDistance from a dict
freighting_goods_rail_weight_and_distance_from_dict = FreightingGoodsRailWeightAndDistance.from_dict(freighting_goods_rail_weight_and_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


