# MaterialUseOtherWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'other']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  **Hint:** Some specifications only support certain details. | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.material_use_other_weight import MaterialUseOtherWeight

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialUseOtherWeight from a JSON string
material_use_other_weight_instance = MaterialUseOtherWeight.from_json(json)
# print the JSON string representation of the object
print(MaterialUseOtherWeight.to_json())

# convert the object into a dict
material_use_other_weight_dict = material_use_other_weight_instance.to_dict()
# create an instance of MaterialUseOtherWeight from a dict
material_use_other_weight_from_dict = MaterialUseOtherWeight.from_dict(material_use_other_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


