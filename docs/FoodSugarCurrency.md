# FoodSugarCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'sugar']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.food_sugar_currency import FoodSugarCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of FoodSugarCurrency from a JSON string
food_sugar_currency_instance = FoodSugarCurrency.from_json(json)
# print the JSON string representation of the object
print(FoodSugarCurrency.to_json())

# convert the object into a dict
food_sugar_currency_dict = food_sugar_currency_instance.to_dict()
# create an instance of FoodSugarCurrency from a dict
food_sugar_currency_from_dict = FoodSugarCurrency.from_dict(food_sugar_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


