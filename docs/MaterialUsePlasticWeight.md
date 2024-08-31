# MaterialUsePlasticWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'plastic']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.material_use_plastic_weight import MaterialUsePlasticWeight

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialUsePlasticWeight from a JSON string
material_use_plastic_weight_instance = MaterialUsePlasticWeight.from_json(json)
# print the JSON string representation of the object
print(MaterialUsePlasticWeight.to_json())

# convert the object into a dict
material_use_plastic_weight_dict = material_use_plastic_weight_instance.to_dict()
# create an instance of MaterialUsePlasticWeight from a dict
material_use_plastic_weight_from_dict = MaterialUsePlasticWeight.from_dict(material_use_plastic_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


