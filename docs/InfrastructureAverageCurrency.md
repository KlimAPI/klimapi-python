# InfrastructureAverageCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.infrastructure_average_currency import InfrastructureAverageCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureAverageCurrency from a JSON string
infrastructure_average_currency_instance = InfrastructureAverageCurrency.from_json(json)
# print the JSON string representation of the object
print(InfrastructureAverageCurrency.to_json())

# convert the object into a dict
infrastructure_average_currency_dict = infrastructure_average_currency_instance.to_dict()
# create an instance of InfrastructureAverageCurrency from a dict
infrastructure_average_currency_from_dict = InfrastructureAverageCurrency.from_dict(infrastructure_average_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


