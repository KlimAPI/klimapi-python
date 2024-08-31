# FreightingGoodsHgvRefrigeratedAllDieselDistance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'hgv_refrigerated_all_diesel']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 6)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'kilometers']

## Example

```python
from klimapi_python.models.freighting_goods_hgv_refrigerated_all_diesel_distance import FreightingGoodsHgvRefrigeratedAllDieselDistance

# TODO update the JSON string below
json = "{}"
# create an instance of FreightingGoodsHgvRefrigeratedAllDieselDistance from a JSON string
freighting_goods_hgv_refrigerated_all_diesel_distance_instance = FreightingGoodsHgvRefrigeratedAllDieselDistance.from_json(json)
# print the JSON string representation of the object
print(FreightingGoodsHgvRefrigeratedAllDieselDistance.to_json())

# convert the object into a dict
freighting_goods_hgv_refrigerated_all_diesel_distance_dict = freighting_goods_hgv_refrigerated_all_diesel_distance_instance.to_dict()
# create an instance of FreightingGoodsHgvRefrigeratedAllDieselDistance from a dict
freighting_goods_hgv_refrigerated_all_diesel_distance_from_dict = FreightingGoodsHgvRefrigeratedAllDieselDistance.from_dict(freighting_goods_hgv_refrigerated_all_diesel_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


