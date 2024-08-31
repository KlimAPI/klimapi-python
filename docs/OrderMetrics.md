# OrderMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The sum of all orders | [optional] 
**total** | **float** | Returns the total sum of money spend in your invoice currency | [optional] 
**kg_co2e** | **int** | The total amount of kg CO<sub>2</sub>e compensated. | [optional] 

## Example

```python
from klimapi_python.models.order_metrics import OrderMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMetrics from a JSON string
order_metrics_instance = OrderMetrics.from_json(json)
# print the JSON string representation of the object
print(OrderMetrics.to_json())

# convert the object into a dict
order_metrics_dict = order_metrics_instance.to_dict()
# create an instance of OrderMetrics from a dict
order_metrics_from_dict = OrderMetrics.from_dict(order_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


