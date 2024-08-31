# CloudComputingNetworkGb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'network']
**specification** | **str** |  | [optional] [default to 'average']
**detail** | **str** |  **Hint:** Some specifications only support certain details. | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need another unit? Contact us! | [optional] [default to 'gb']

## Example

```python
from klimapi_python.models.cloud_computing_network_gb import CloudComputingNetworkGb

# TODO update the JSON string below
json = "{}"
# create an instance of CloudComputingNetworkGb from a JSON string
cloud_computing_network_gb_instance = CloudComputingNetworkGb.from_json(json)
# print the JSON string representation of the object
print(CloudComputingNetworkGb.to_json())

# convert the object into a dict
cloud_computing_network_gb_dict = cloud_computing_network_gb_instance.to_dict()
# create an instance of CloudComputingNetworkGb from a dict
cloud_computing_network_gb_from_dict = CloudComputingNetworkGb.from_dict(cloud_computing_network_gb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


