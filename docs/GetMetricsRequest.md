# GetMetricsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | The operator to combine the filters with | [optional] [default to 'AND']
**filters** | [**GetOrdersRequestFilters**](GetOrdersRequestFilters.md) |  | [optional] 

## Example

```python
from klimapi_python.models.get_metrics_request import GetMetricsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsRequest from a JSON string
get_metrics_request_instance = GetMetricsRequest.from_json(json)
# print the JSON string representation of the object
print(GetMetricsRequest.to_json())

# convert the object into a dict
get_metrics_request_dict = get_metrics_request_instance.to_dict()
# create an instance of GetMetricsRequest from a dict
get_metrics_request_from_dict = GetMetricsRequest.from_dict(get_metrics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


