# WasteDisposalPlasticWeight


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
from klimapi_python.models.waste_disposal_plastic_weight import WasteDisposalPlasticWeight

# TODO update the JSON string below
json = "{}"
# create an instance of WasteDisposalPlasticWeight from a JSON string
waste_disposal_plastic_weight_instance = WasteDisposalPlasticWeight.from_json(json)
# print the JSON string representation of the object
print(WasteDisposalPlasticWeight.to_json())

# convert the object into a dict
waste_disposal_plastic_weight_dict = waste_disposal_plastic_weight_instance.to_dict()
# create an instance of WasteDisposalPlasticWeight from a dict
waste_disposal_plastic_weight_from_dict = WasteDisposalPlasticWeight.from_dict(waste_disposal_plastic_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


