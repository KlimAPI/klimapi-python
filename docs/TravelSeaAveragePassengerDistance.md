# TravelSeaAveragePassengerDistance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Distance a passenger traveled in the given unit.    **Example:** 2 passengers travel 300 kilometers. So the right `value` would be **600** and the `unit` would be **passenger.kilometers**.    Need a more specific unit? See the **[full list of supported units (Section 6)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'kilometers']

## Example

```python
from klimapi_python.models.travel_sea_average_passenger_distance import TravelSeaAveragePassengerDistance

# TODO update the JSON string below
json = "{}"
# create an instance of TravelSeaAveragePassengerDistance from a JSON string
travel_sea_average_passenger_distance_instance = TravelSeaAveragePassengerDistance.from_json(json)
# print the JSON string representation of the object
print(TravelSeaAveragePassengerDistance.to_json())

# convert the object into a dict
travel_sea_average_passenger_distance_dict = travel_sea_average_passenger_distance_instance.to_dict()
# create an instance of TravelSeaAveragePassengerDistance from a dict
travel_sea_average_passenger_distance_from_dict = TravelSeaAveragePassengerDistance.from_dict(travel_sea_average_passenger_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


