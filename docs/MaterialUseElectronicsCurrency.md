# MaterialUseElectronicsCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'electronics']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.material_use_electronics_currency import MaterialUseElectronicsCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialUseElectronicsCurrency from a JSON string
material_use_electronics_currency_instance = MaterialUseElectronicsCurrency.from_json(json)
# print the JSON string representation of the object
print(MaterialUseElectronicsCurrency.to_json())

# convert the object into a dict
material_use_electronics_currency_dict = material_use_electronics_currency_instance.to_dict()
# create an instance of MaterialUseElectronicsCurrency from a dict
material_use_electronics_currency_from_dict = MaterialUseElectronicsCurrency.from_dict(material_use_electronics_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


