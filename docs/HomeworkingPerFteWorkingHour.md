# HomeworkingPerFteWorkingHour


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**activity** | **str** |  | [optional] [default to 'average']
**value** | **float** | The value in the given unit | 
**unit** | **str** | Need another unit? Contact us! | [optional] [default to 'per_fte_working_hour']

## Example

```python
from klimapi_python.models.homeworking_per_fte_working_hour import HomeworkingPerFteWorkingHour

# TODO update the JSON string below
json = "{}"
# create an instance of HomeworkingPerFteWorkingHour from a JSON string
homeworking_per_fte_working_hour_instance = HomeworkingPerFteWorkingHour.from_json(json)
# print the JSON string representation of the object
print(HomeworkingPerFteWorkingHour.to_json())

# convert the object into a dict
homeworking_per_fte_working_hour_dict = homeworking_per_fte_working_hour_instance.to_dict()
# create an instance of HomeworkingPerFteWorkingHour from a dict
homeworking_per_fte_working_hour_from_dict = HomeworkingPerFteWorkingHour.from_dict(homeworking_per_fte_working_hour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


