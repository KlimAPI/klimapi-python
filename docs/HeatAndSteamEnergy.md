# HeatAndSteamEnergy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 3)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'kWh']

## Example

```python
from klimapi_python.models.heat_and_steam_energy import HeatAndSteamEnergy

# TODO update the JSON string below
json = "{}"
# create an instance of HeatAndSteamEnergy from a JSON string
heat_and_steam_energy_instance = HeatAndSteamEnergy.from_json(json)
# print the JSON string representation of the object
print(HeatAndSteamEnergy.to_json())

# convert the object into a dict
heat_and_steam_energy_dict = heat_and_steam_energy_instance.to_dict()
# create an instance of HeatAndSteamEnergy from a dict
heat_and_steam_energy_from_dict = HeatAndSteamEnergy.from_dict(heat_and_steam_energy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


