# BioenergyAverageWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**. | [optional] [default to 'metric tons']

## Example

```python
from klimapi_python.models.bioenergy_average_weight import BioenergyAverageWeight

# TODO update the JSON string below
json = "{}"
# create an instance of BioenergyAverageWeight from a JSON string
bioenergy_average_weight_instance = BioenergyAverageWeight.from_json(json)
# print the JSON string representation of the object
print(BioenergyAverageWeight.to_json())

# convert the object into a dict
bioenergy_average_weight_dict = bioenergy_average_weight_instance.to_dict()
# create an instance of BioenergyAverageWeight from a dict
bioenergy_average_weight_from_dict = BioenergyAverageWeight.from_dict(bioenergy_average_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


