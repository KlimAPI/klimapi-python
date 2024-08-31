# MaterialUseAverageCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.material_use_average_currency import MaterialUseAverageCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialUseAverageCurrency from a JSON string
material_use_average_currency_instance = MaterialUseAverageCurrency.from_json(json)
# print the JSON string representation of the object
print(MaterialUseAverageCurrency.to_json())

# convert the object into a dict
material_use_average_currency_dict = material_use_average_currency_instance.to_dict()
# create an instance of MaterialUseAverageCurrency from a dict
material_use_average_currency_from_dict = MaterialUseAverageCurrency.from_dict(material_use_average_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


