# FreightingGoodsVansDistance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'vans']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  **Hint:** Some specifications only support certain details. | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 6)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'kilometers']

## Example

```python
from klimapi_python.models.freighting_goods_vans_distance import FreightingGoodsVansDistance

# TODO update the JSON string below
json = "{}"
# create an instance of FreightingGoodsVansDistance from a JSON string
freighting_goods_vans_distance_instance = FreightingGoodsVansDistance.from_json(json)
# print the JSON string representation of the object
print(FreightingGoodsVansDistance.to_json())

# convert the object into a dict
freighting_goods_vans_distance_dict = freighting_goods_vans_distance_instance.to_dict()
# create an instance of FreightingGoodsVansDistance from a dict
freighting_goods_vans_distance_from_dict = FreightingGoodsVansDistance.from_dict(freighting_goods_vans_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


