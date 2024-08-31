# TravelLandCarsByMarketSegmentDepartureAndDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'cars_by_market_segment']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  **Hint:** Some specifications only support certain details. | [optional] [default to 'average']
**departure** | **str** | City, Postal Address, Train Station or IATA Code of the departure address | 
**destination** | **str** | City, Postal Address, Train Station or IATA Code of the destination address | 
**return_trip** | **bool** | Decide if the trip is one way or return | [optional] [default to True]

## Example

```python
from klimapi_python.models.travel_land_cars_by_market_segment_departure_and_destination import TravelLandCarsByMarketSegmentDepartureAndDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TravelLandCarsByMarketSegmentDepartureAndDestination from a JSON string
travel_land_cars_by_market_segment_departure_and_destination_instance = TravelLandCarsByMarketSegmentDepartureAndDestination.from_json(json)
# print the JSON string representation of the object
print(TravelLandCarsByMarketSegmentDepartureAndDestination.to_json())

# convert the object into a dict
travel_land_cars_by_market_segment_departure_and_destination_dict = travel_land_cars_by_market_segment_departure_and_destination_instance.to_dict()
# create an instance of TravelLandCarsByMarketSegmentDepartureAndDestination from a dict
travel_land_cars_by_market_segment_departure_and_destination_from_dict = TravelLandCarsByMarketSegmentDepartureAndDestination.from_dict(travel_land_cars_by_market_segment_departure_and_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


