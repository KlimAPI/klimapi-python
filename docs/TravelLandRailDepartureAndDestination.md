# TravelLandRailDepartureAndDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'rail']
**specification** | **str** |  | [optional] [default to 'average']
**departure** | **str** | City, Postal Address, Train Station or IATA Code of the departure address | 
**destination** | **str** | City, Postal Address, Train Station or IATA Code of the destination address | 
**return_trip** | **bool** | Decide if the trip is one way or return | [optional] [default to True]
**passengers** | **int** | The total of passengers travelling this route | [optional] [default to 1]

## Example

```python
from klimapi_python.models.travel_land_rail_departure_and_destination import TravelLandRailDepartureAndDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TravelLandRailDepartureAndDestination from a JSON string
travel_land_rail_departure_and_destination_instance = TravelLandRailDepartureAndDestination.from_json(json)
# print the JSON string representation of the object
print(TravelLandRailDepartureAndDestination.to_json())

# convert the object into a dict
travel_land_rail_departure_and_destination_dict = travel_land_rail_departure_and_destination_instance.to_dict()
# create an instance of TravelLandRailDepartureAndDestination from a dict
travel_land_rail_departure_and_destination_from_dict = TravelLandRailDepartureAndDestination.from_dict(travel_land_rail_departure_and_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


