# PendingOrderCalculated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**status** | **str** | The status of the order | [optional] 
**price** | **float** | The total of the compensation in your given currency **excl. VAT**. | [optional] 
**currency** | **str** |  | [optional] 
**kg_co2e** | **int** | The amount of kg CO<sub>2</sub>e. | [optional] 
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**results** | [**List[CalculationResult]**](CalculationResult.md) | An array of the calculation results | [optional] 

## Example

```python
from klimapi_python.models.pending_order_calculated import PendingOrderCalculated

# TODO update the JSON string below
json = "{}"
# create an instance of PendingOrderCalculated from a JSON string
pending_order_calculated_instance = PendingOrderCalculated.from_json(json)
# print the JSON string representation of the object
print(PendingOrderCalculated.to_json())

# convert the object into a dict
pending_order_calculated_dict = pending_order_calculated_instance.to_dict()
# create an instance of PendingOrderCalculated from a dict
pending_order_calculated_from_dict = PendingOrderCalculated.from_dict(pending_order_calculated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


