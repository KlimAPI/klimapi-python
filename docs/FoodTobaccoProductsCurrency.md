# FoodTobaccoProductsCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'tobacco_products']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.food_tobacco_products_currency import FoodTobaccoProductsCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of FoodTobaccoProductsCurrency from a JSON string
food_tobacco_products_currency_instance = FoodTobaccoProductsCurrency.from_json(json)
# print the JSON string representation of the object
print(FoodTobaccoProductsCurrency.to_json())

# convert the object into a dict
food_tobacco_products_currency_dict = food_tobacco_products_currency_instance.to_dict()
# create an instance of FoodTobaccoProductsCurrency from a dict
food_tobacco_products_currency_from_dict = FoodTobaccoProductsCurrency.from_dict(food_tobacco_products_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


