# MaterialUseAverageWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.material_use_average_weight import MaterialUseAverageWeight

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialUseAverageWeight from a JSON string
material_use_average_weight_instance = MaterialUseAverageWeight.from_json(json)
# print the JSON string representation of the object
print(MaterialUseAverageWeight.to_json())

# convert the object into a dict
material_use_average_weight_dict = material_use_average_weight_instance.to_dict()
# create an instance of MaterialUseAverageWeight from a dict
material_use_average_weight_from_dict = MaterialUseAverageWeight.from_dict(material_use_average_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


