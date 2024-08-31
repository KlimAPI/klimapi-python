# CloudComputingMemoryGbHour


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'memory']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  **Hint:** Some specifications only support certain details. | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need another unit? Contact us! | [optional] [default to 'gb-hour']

## Example

```python
from klimapi_python.models.cloud_computing_memory_gb_hour import CloudComputingMemoryGbHour

# TODO update the JSON string below
json = "{}"
# create an instance of CloudComputingMemoryGbHour from a JSON string
cloud_computing_memory_gb_hour_instance = CloudComputingMemoryGbHour.from_json(json)
# print the JSON string representation of the object
print(CloudComputingMemoryGbHour.to_json())

# convert the object into a dict
cloud_computing_memory_gb_hour_dict = cloud_computing_memory_gb_hour_instance.to_dict()
# create an instance of CloudComputingMemoryGbHour from a dict
cloud_computing_memory_gb_hour_from_dict = CloudComputingMemoryGbHour.from_dict(cloud_computing_memory_gb_hour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


