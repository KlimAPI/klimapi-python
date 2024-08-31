# FoodVegetableOilsAndFatsCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'vegetable_oils_and_fats']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.food_vegetable_oils_and_fats_currency import FoodVegetableOilsAndFatsCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of FoodVegetableOilsAndFatsCurrency from a JSON string
food_vegetable_oils_and_fats_currency_instance = FoodVegetableOilsAndFatsCurrency.from_json(json)
# print the JSON string representation of the object
print(FoodVegetableOilsAndFatsCurrency.to_json())

# convert the object into a dict
food_vegetable_oils_and_fats_currency_dict = food_vegetable_oils_and_fats_currency_instance.to_dict()
# create an instance of FoodVegetableOilsAndFatsCurrency from a dict
food_vegetable_oils_and_fats_currency_from_dict = FoodVegetableOilsAndFatsCurrency.from_dict(food_vegetable_oils_and_fats_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


