# TravelLandMotorbikeDistance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'motorbike']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 6)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'kilometers']

## Example

```python
from klimapi_python.models.travel_land_motorbike_distance import TravelLandMotorbikeDistance

# TODO update the JSON string below
json = "{}"
# create an instance of TravelLandMotorbikeDistance from a JSON string
travel_land_motorbike_distance_instance = TravelLandMotorbikeDistance.from_json(json)
# print the JSON string representation of the object
print(TravelLandMotorbikeDistance.to_json())

# convert the object into a dict
travel_land_motorbike_distance_dict = travel_land_motorbike_distance_instance.to_dict()
# create an instance of TravelLandMotorbikeDistance from a dict
travel_land_motorbike_distance_from_dict = TravelLandMotorbikeDistance.from_dict(travel_land_motorbike_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


