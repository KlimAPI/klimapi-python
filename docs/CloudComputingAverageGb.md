# CloudComputingAverageGb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need another unit? Contact us! | [optional] [default to 'gb']

## Example

```python
from klimapi_python.models.cloud_computing_average_gb import CloudComputingAverageGb

# TODO update the JSON string below
json = "{}"
# create an instance of CloudComputingAverageGb from a JSON string
cloud_computing_average_gb_instance = CloudComputingAverageGb.from_json(json)
# print the JSON string representation of the object
print(CloudComputingAverageGb.to_json())

# convert the object into a dict
cloud_computing_average_gb_dict = cloud_computing_average_gb_instance.to_dict()
# create an instance of CloudComputingAverageGb from a dict
cloud_computing_average_gb_from_dict = CloudComputingAverageGb.from_dict(cloud_computing_average_gb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


