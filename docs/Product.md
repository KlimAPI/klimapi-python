# Product

A specific product element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | A unique identifier for the product | 
**name** | **str** | The name of the product | [optional] 
**description** | **str** | A description of the product | [optional] 
**price** | **float** | The price of the product | 
**categories** | **List[str]** | The categories of the product | [optional] 
**tags** | **List[str]** | The tags of the product | [optional] 
**weight** | **float** | The weight of the product | [optional] 
**weight_unit** | **str** | The weight unit of the product | [optional] [default to 'kg']
**made_in** | **str** | The country of origin of the product | [optional] 
**emission_factor** | **str** | Already know the emissions of the given product? Then you can provide the emission factor here. Unit: **kg CO<sub>2</sub>e** | [optional] 
**emission_multiplicator** | **str** | Include the multiplicator of the given factor. | [optional] 

## Example

```python
from klimapi_python.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print(Product.to_json())

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_from_dict = Product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


