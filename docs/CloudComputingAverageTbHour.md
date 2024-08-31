# CloudComputingAverageTbHour


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need another unit? Contact us! | [optional] [default to 'tb-hour']

## Example

```python
from klimapi_python.models.cloud_computing_average_tb_hour import CloudComputingAverageTbHour

# TODO update the JSON string below
json = "{}"
# create an instance of CloudComputingAverageTbHour from a JSON string
cloud_computing_average_tb_hour_instance = CloudComputingAverageTbHour.from_json(json)
# print the JSON string representation of the object
print(CloudComputingAverageTbHour.to_json())

# convert the object into a dict
cloud_computing_average_tb_hour_dict = cloud_computing_average_tb_hour_instance.to_dict()
# create an instance of CloudComputingAverageTbHour from a dict
cloud_computing_average_tb_hour_from_dict = CloudComputingAverageTbHour.from_dict(cloud_computing_average_tb_hour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


