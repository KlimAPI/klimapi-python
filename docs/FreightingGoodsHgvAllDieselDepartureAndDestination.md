# FreightingGoodsHgvAllDieselDepartureAndDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'hgv_all_diesel']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  | [optional] [default to 'average']
**departure** | **str** | City, Postal Address, Train Station or IATA Code of the departure address | 
**destination** | **str** | City, Postal Address, Train Station or IATA Code of the destination address | 
**return_trip** | **bool** | Decide if the trip is one way or return | [optional] [default to True]

## Example

```python
from klimapi_python.models.freighting_goods_hgv_all_diesel_departure_and_destination import FreightingGoodsHgvAllDieselDepartureAndDestination

# TODO update the JSON string below
json = "{}"
# create an instance of FreightingGoodsHgvAllDieselDepartureAndDestination from a JSON string
freighting_goods_hgv_all_diesel_departure_and_destination_instance = FreightingGoodsHgvAllDieselDepartureAndDestination.from_json(json)
# print the JSON string representation of the object
print(FreightingGoodsHgvAllDieselDepartureAndDestination.to_json())

# convert the object into a dict
freighting_goods_hgv_all_diesel_departure_and_destination_dict = freighting_goods_hgv_all_diesel_departure_and_destination_instance.to_dict()
# create an instance of FreightingGoodsHgvAllDieselDepartureAndDestination from a dict
freighting_goods_hgv_all_diesel_departure_and_destination_from_dict = FreightingGoodsHgvAllDieselDepartureAndDestination.from_dict(freighting_goods_hgv_all_diesel_departure_and_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


