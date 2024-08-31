# HotelStayRoomPerNight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need another unit? Contact us! | [optional] [default to 'room_per_night']

## Example

```python
from klimapi_python.models.hotel_stay_room_per_night import HotelStayRoomPerNight

# TODO update the JSON string below
json = "{}"
# create an instance of HotelStayRoomPerNight from a JSON string
hotel_stay_room_per_night_instance = HotelStayRoomPerNight.from_json(json)
# print the JSON string representation of the object
print(HotelStayRoomPerNight.to_json())

# convert the object into a dict
hotel_stay_room_per_night_dict = hotel_stay_room_per_night_instance.to_dict()
# create an instance of HotelStayRoomPerNight from a dict
hotel_stay_room_per_night_from_dict = HotelStayRoomPerNight.from_dict(hotel_stay_room_per_night_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


