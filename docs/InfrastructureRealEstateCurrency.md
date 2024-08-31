# InfrastructureRealEstateCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'real_estate']
**specification** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from klimapi_python.models.infrastructure_real_estate_currency import InfrastructureRealEstateCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureRealEstateCurrency from a JSON string
infrastructure_real_estate_currency_instance = InfrastructureRealEstateCurrency.from_json(json)
# print the JSON string representation of the object
print(InfrastructureRealEstateCurrency.to_json())

# convert the object into a dict
infrastructure_real_estate_currency_dict = infrastructure_real_estate_currency_instance.to_dict()
# create an instance of InfrastructureRealEstateCurrency from a dict
infrastructure_real_estate_currency_from_dict = InfrastructureRealEstateCurrency.from_dict(infrastructure_real_estate_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


