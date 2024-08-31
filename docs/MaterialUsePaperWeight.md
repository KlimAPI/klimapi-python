# MaterialUsePaperWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'paper']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.material_use_paper_weight import MaterialUsePaperWeight

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialUsePaperWeight from a JSON string
material_use_paper_weight_instance = MaterialUsePaperWeight.from_json(json)
# print the JSON string representation of the object
print(MaterialUsePaperWeight.to_json())

# convert the object into a dict
material_use_paper_weight_dict = material_use_paper_weight_instance.to_dict()
# create an instance of MaterialUsePaperWeight from a dict
material_use_paper_weight_from_dict = MaterialUsePaperWeight.from_dict(material_use_paper_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

