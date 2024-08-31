# FreightingGoodsSeaTankerWeightAndDistance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'sea_tanker']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  **Hint:** Some specifications only support certain details. | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Distance a specific weight traveled in the given unit.    **Example:** 10 metric tons travel 50 kilometers. So the right `value` would be **500** and the `unit` would be **metric tons.kilometers**.    Need a more specific unit? See the **[full list of supported units (Sections 5 and 6)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons.kilometers']

## Example

```python
from klimapi_python.models.freighting_goods_sea_tanker_weight_and_distance import FreightingGoodsSeaTankerWeightAndDistance

# TODO update the JSON string below
json = "{}"
# create an instance of FreightingGoodsSeaTankerWeightAndDistance from a JSON string
freighting_goods_sea_tanker_weight_and_distance_instance = FreightingGoodsSeaTankerWeightAndDistance.from_json(json)
# print the JSON string representation of the object
print(FreightingGoodsSeaTankerWeightAndDistance.to_json())

# convert the object into a dict
freighting_goods_sea_tanker_weight_and_distance_dict = freighting_goods_sea_tanker_weight_and_distance_instance.to_dict()
# create an instance of FreightingGoodsSeaTankerWeightAndDistance from a dict
freighting_goods_sea_tanker_weight_and_distance_from_dict = FreightingGoodsSeaTankerWeightAndDistance.from_dict(freighting_goods_sea_tanker_weight_and_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

