# TravelSeaCruiseDays


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'cruise']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need another unit? Contact us! | [optional] [default to 'days']

## Example

```python
from klimapi_python.models.travel_sea_cruise_days import TravelSeaCruiseDays

# TODO update the JSON string below
json = "{}"
# create an instance of TravelSeaCruiseDays from a JSON string
travel_sea_cruise_days_instance = TravelSeaCruiseDays.from_json(json)
# print the JSON string representation of the object
print(TravelSeaCruiseDays.to_json())

# convert the object into a dict
travel_sea_cruise_days_dict = travel_sea_cruise_days_instance.to_dict()
# create an instance of TravelSeaCruiseDays from a dict
travel_sea_cruise_days_from_dict = TravelSeaCruiseDays.from_dict(travel_sea_cruise_days_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


