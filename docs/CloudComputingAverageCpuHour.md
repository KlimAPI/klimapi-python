# CloudComputingAverageCpuHour


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need another unit? Contact us! | [optional] [default to 'cpu-hour']

## Example

```python
from klimapi_python.models.cloud_computing_average_cpu_hour import CloudComputingAverageCpuHour

# TODO update the JSON string below
json = "{}"
# create an instance of CloudComputingAverageCpuHour from a JSON string
cloud_computing_average_cpu_hour_instance = CloudComputingAverageCpuHour.from_json(json)
# print the JSON string representation of the object
print(CloudComputingAverageCpuHour.to_json())

# convert the object into a dict
cloud_computing_average_cpu_hour_dict = cloud_computing_average_cpu_hour_instance.to_dict()
# create an instance of CloudComputingAverageCpuHour from a dict
cloud_computing_average_cpu_hour_from_dict = CloudComputingAverageCpuHour.from_dict(cloud_computing_average_cpu_hour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

