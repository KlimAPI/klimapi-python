# FoodProcessedRiceCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'processed_rice']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.food_processed_rice_currency import FoodProcessedRiceCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of FoodProcessedRiceCurrency from a JSON string
food_processed_rice_currency_instance = FoodProcessedRiceCurrency.from_json(json)
# print the JSON string representation of the object
print(FoodProcessedRiceCurrency.to_json())

# convert the object into a dict
food_processed_rice_currency_dict = food_processed_rice_currency_instance.to_dict()
# create an instance of FoodProcessedRiceCurrency from a dict
food_processed_rice_currency_from_dict = FoodProcessedRiceCurrency.from_dict(food_processed_rice_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


