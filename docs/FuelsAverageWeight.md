# FuelsAverageWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.fuels_average_weight import FuelsAverageWeight

# TODO update the JSON string below
json = "{}"
# create an instance of FuelsAverageWeight from a JSON string
fuels_average_weight_instance = FuelsAverageWeight.from_json(json)
# print the JSON string representation of the object
print(FuelsAverageWeight.to_json())

# convert the object into a dict
fuels_average_weight_dict = fuels_average_weight_instance.to_dict()
# create an instance of FuelsAverageWeight from a dict
fuels_average_weight_from_dict = FuelsAverageWeight.from_dict(fuels_average_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


