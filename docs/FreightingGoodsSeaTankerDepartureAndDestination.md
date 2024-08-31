# FreightingGoodsSeaTankerDepartureAndDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'sea_tanker']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  **Hint:** Some specifications only support certain details. | [optional] [default to 'average']
**departure** | **str** | City, Postal Address, Train Station or IATA Code of the departure address | 
**destination** | **str** | City, Postal Address, Train Station or IATA Code of the destination address | 
**return_trip** | **bool** | Decide if the trip is one way or return | [optional] [default to True]
**weight** | **float** | The total weight travelling this route | [optional] [default to 1]
**weight_unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.freighting_goods_sea_tanker_departure_and_destination import FreightingGoodsSeaTankerDepartureAndDestination

# TODO update the JSON string below
json = "{}"
# create an instance of FreightingGoodsSeaTankerDepartureAndDestination from a JSON string
freighting_goods_sea_tanker_departure_and_destination_instance = FreightingGoodsSeaTankerDepartureAndDestination.from_json(json)
# print the JSON string representation of the object
print(FreightingGoodsSeaTankerDepartureAndDestination.to_json())

# convert the object into a dict
freighting_goods_sea_tanker_departure_and_destination_dict = freighting_goods_sea_tanker_departure_and_destination_instance.to_dict()
# create an instance of FreightingGoodsSeaTankerDepartureAndDestination from a dict
freighting_goods_sea_tanker_departure_and_destination_from_dict = FreightingGoodsSeaTankerDepartureAndDestination.from_dict(freighting_goods_sea_tanker_departure_and_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


