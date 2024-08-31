# FoodFoodProductsNotElsewhereSpecifiedCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'food_products_not_elsewhere_specified']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.food_food_products_not_elsewhere_specified_currency import FoodFoodProductsNotElsewhereSpecifiedCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of FoodFoodProductsNotElsewhereSpecifiedCurrency from a JSON string
food_food_products_not_elsewhere_specified_currency_instance = FoodFoodProductsNotElsewhereSpecifiedCurrency.from_json(json)
# print the JSON string representation of the object
print(FoodFoodProductsNotElsewhereSpecifiedCurrency.to_json())

# convert the object into a dict
food_food_products_not_elsewhere_specified_currency_dict = food_food_products_not_elsewhere_specified_currency_instance.to_dict()
# create an instance of FoodFoodProductsNotElsewhereSpecifiedCurrency from a dict
food_food_products_not_elsewhere_specified_currency_from_dict = FoodFoodProductsNotElsewhereSpecifiedCurrency.from_dict(food_food_products_not_elsewhere_specified_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


