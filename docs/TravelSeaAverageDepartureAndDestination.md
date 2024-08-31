# TravelSeaAverageDepartureAndDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**departure** | **str** | City, Postal Address, Train Station or IATA Code of the departure address | 
**destination** | **str** | City, Postal Address, Train Station or IATA Code of the destination address | 
**return_trip** | **bool** | Decide if the trip is one way or return | [optional] [default to True]
**passengers** | **int** | The total of passengers travelling this route | [optional] [default to 1]

## Example

```python
from klimapi_python.models.travel_sea_average_departure_and_destination import TravelSeaAverageDepartureAndDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TravelSeaAverageDepartureAndDestination from a JSON string
travel_sea_average_departure_and_destination_instance = TravelSeaAverageDepartureAndDestination.from_json(json)
# print the JSON string representation of the object
print(TravelSeaAverageDepartureAndDestination.to_json())

# convert the object into a dict
travel_sea_average_departure_and_destination_dict = travel_sea_average_departure_and_destination_instance.to_dict()
# create an instance of TravelSeaAverageDepartureAndDestination from a dict
travel_sea_average_departure_and_destination_from_dict = TravelSeaAverageDepartureAndDestination.from_dict(travel_sea_average_departure_and_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


