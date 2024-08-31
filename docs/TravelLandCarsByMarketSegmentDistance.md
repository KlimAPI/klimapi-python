# TravelLandCarsByMarketSegmentDistance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'cars_by_market_segment']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  **Hint:** Some specifications only support certain details. | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 6)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'kilometers']

## Example

```python
from klimapi_python.models.travel_land_cars_by_market_segment_distance import TravelLandCarsByMarketSegmentDistance

# TODO update the JSON string below
json = "{}"
# create an instance of TravelLandCarsByMarketSegmentDistance from a JSON string
travel_land_cars_by_market_segment_distance_instance = TravelLandCarsByMarketSegmentDistance.from_json(json)
# print the JSON string representation of the object
print(TravelLandCarsByMarketSegmentDistance.to_json())

# convert the object into a dict
travel_land_cars_by_market_segment_distance_dict = travel_land_cars_by_market_segment_distance_instance.to_dict()
# create an instance of TravelLandCarsByMarketSegmentDistance from a dict
travel_land_cars_by_market_segment_distance_from_dict = TravelLandCarsByMarketSegmentDistance.from_dict(travel_land_cars_by_market_segment_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


