# CartResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kg_co2e** | **float** | The total amount of kg CO<sub>2</sub>e calculated. | [optional] 
**settings** | [**CartResultSettings**](CartResultSettings.md) |  | [optional] 
**calculation_results** | [**List[CartResultCalculationResultsInner]**](CartResultCalculationResultsInner.md) | The calculation results | [optional] 
**orders** | [**List[PendingOrder]**](PendingOrder.md) |  | [optional] 

## Example

```python
from klimapi_python.models.cart_result import CartResult

# TODO update the JSON string below
json = "{}"
# create an instance of CartResult from a JSON string
cart_result_instance = CartResult.from_json(json)
# print the JSON string representation of the object
print(CartResult.to_json())

# convert the object into a dict
cart_result_dict = cart_result_instance.to_dict()
# create an instance of CartResult from a dict
cart_result_from_dict = CartResult.from_dict(cart_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


