# CartResultSettings

The settings used for the calculation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**split** | **int** | The default split of the compensation between the customer and the store in percent | [optional] 
**default** | **bool** | Specifies whether compensation should be selected by default | [optional] 

## Example

```python
from klimapi_python.models.cart_result_settings import CartResultSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CartResultSettings from a JSON string
cart_result_settings_instance = CartResultSettings.from_json(json)
# print the JSON string representation of the object
print(CartResultSettings.to_json())

# convert the object into a dict
cart_result_settings_dict = cart_result_settings_instance.to_dict()
# create an instance of CartResultSettings from a dict
cart_result_settings_from_dict = CartResultSettings.from_dict(cart_result_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


