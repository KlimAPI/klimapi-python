# FoodBeveragesCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'beverages']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.food_beverages_currency import FoodBeveragesCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of FoodBeveragesCurrency from a JSON string
food_beverages_currency_instance = FoodBeveragesCurrency.from_json(json)
# print the JSON string representation of the object
print(FoodBeveragesCurrency.to_json())

# convert the object into a dict
food_beverages_currency_dict = food_beverages_currency_instance.to_dict()
# create an instance of FoodBeveragesCurrency from a dict
food_beverages_currency_from_dict = FoodBeveragesCurrency.from_dict(food_beverages_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


