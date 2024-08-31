# CartResultCalculationResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | A unique identifier for the product | [optional] 
**source** | **str** | The source of the calculation | [optional] 
**kg_co2e** | **float** | The amount of kg CO<sub>2</sub>e calculated for the given product. | [optional] 

## Example

```python
from klimapi_python.models.cart_result_calculation_results_inner import CartResultCalculationResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CartResultCalculationResultsInner from a JSON string
cart_result_calculation_results_inner_instance = CartResultCalculationResultsInner.from_json(json)
# print the JSON string representation of the object
print(CartResultCalculationResultsInner.to_json())

# convert the object into a dict
cart_result_calculation_results_inner_dict = cart_result_calculation_results_inner_instance.to_dict()
# create an instance of CartResultCalculationResultsInner from a dict
cart_result_calculation_results_inner_from_dict = CartResultCalculationResultsInner.from_dict(cart_result_calculation_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


