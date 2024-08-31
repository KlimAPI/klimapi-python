# MaterialUsePaperProductsCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'paper_products']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.material_use_paper_products_currency import MaterialUsePaperProductsCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialUsePaperProductsCurrency from a JSON string
material_use_paper_products_currency_instance = MaterialUsePaperProductsCurrency.from_json(json)
# print the JSON string representation of the object
print(MaterialUsePaperProductsCurrency.to_json())

# convert the object into a dict
material_use_paper_products_currency_dict = material_use_paper_products_currency_instance.to_dict()
# create an instance of MaterialUsePaperProductsCurrency from a dict
material_use_paper_products_currency_from_dict = MaterialUsePaperProductsCurrency.from_dict(material_use_paper_products_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


