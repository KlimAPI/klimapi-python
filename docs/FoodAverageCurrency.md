# FoodAverageCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.food_average_currency import FoodAverageCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of FoodAverageCurrency from a JSON string
food_average_currency_instance = FoodAverageCurrency.from_json(json)
# print the JSON string representation of the object
print(FoodAverageCurrency.to_json())

# convert the object into a dict
food_average_currency_dict = food_average_currency_instance.to_dict()
# create an instance of FoodAverageCurrency from a dict
food_average_currency_from_dict = FoodAverageCurrency.from_dict(food_average_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


