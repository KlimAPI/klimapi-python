# OrderCalculated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**certificate_issued_at** | **datetime** | Timestamp of when the certificate was issued in ISO 8601 format (UTC) | [optional] 
**certificate_url** | **str** |  | [optional] 
**certificate_pdf** | **str** |  | [optional] 
**price** | **float** | The total of the compensation in your given currency **excl. VAT**. | [optional] 
**currency** | **str** |  | [optional] 
**kg_co2e** | **int** | The amount of kg CO&lt;sub&gt;2&lt;/sub&gt;e. | [optional] 
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**results** | [**List[CalculationResult]**](CalculationResult.md) | An array of the calculation results | [optional] 
**recipient** | [**OrderRecipient**](OrderRecipient.md) |  | [optional] 

## Example

```python
from klimapi_python.models.order_calculated import OrderCalculated

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCalculated from a JSON string
order_calculated_instance = OrderCalculated.from_json(json)
# print the JSON string representation of the object
print(OrderCalculated.to_json())

# convert the object into a dict
order_calculated_dict = order_calculated_instance.to_dict()
# create an instance of OrderCalculated from a dict
order_calculated_from_dict = OrderCalculated.from_dict(order_calculated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


