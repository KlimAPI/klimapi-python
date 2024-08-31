# FreightingGoodsAverageDepartureAndDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**departure** | **str** | City, Postal Address, Train Station or IATA Code of the departure address | 
**destination** | **str** | City, Postal Address, Train Station or IATA Code of the destination address | 
**return_trip** | **bool** | Decide if the trip is one way or return | [optional] [default to True]

## Example

```python
from klimapi_python.models.freighting_goods_average_departure_and_destination import FreightingGoodsAverageDepartureAndDestination

# TODO update the JSON string below
json = "{}"
# create an instance of FreightingGoodsAverageDepartureAndDestination from a JSON string
freighting_goods_average_departure_and_destination_instance = FreightingGoodsAverageDepartureAndDestination.from_json(json)
# print the JSON string representation of the object
print(FreightingGoodsAverageDepartureAndDestination.to_json())

# convert the object into a dict
freighting_goods_average_departure_and_destination_dict = freighting_goods_average_departure_and_destination_instance.to_dict()
# create an instance of FreightingGoodsAverageDepartureAndDestination from a dict
freighting_goods_average_departure_and_destination_from_dict = FreightingGoodsAverageDepartureAndDestination.from_dict(freighting_goods_average_departure_and_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


