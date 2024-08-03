# LinkByCalculationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_options** | **List[object]** | An Array of [Calculation Options](/resources/factors). | 
**change_allowed** | **bool** | Choose if the customer should be allowed to change the amount. | [optional] [default to False]
**success_url** | **str** | The URL the customer is redirected to after the successful compensation. | 
**cancel_url** | **str** | The URL the customer is redirected to after a failed or aborted compensation. | 
**order_count** | **int** | The amount of pending Orders you want to receive. This is especially useful if you want to offer your customers several different projects for their compensation. | [optional] [default to 1]
**metadata** | **Dict[str, str]** | Add additional queryable information to the order as key-value pairs | [optional] 
**fractional_digits** | **int** | Normally, the calculation results are rounded to the nearest whole number. Specify here how many decimal places you would like to receive in addition. This only applies to calculation results, compensations are always made in whole kilograms | [optional] [default to 2]

## Example

```python
from klimapi_python.models.link_by_calculation_request import LinkByCalculationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkByCalculationRequest from a JSON string
link_by_calculation_request_instance = LinkByCalculationRequest.from_json(json)
# print the JSON string representation of the object
print(LinkByCalculationRequest.to_json())

# convert the object into a dict
link_by_calculation_request_dict = link_by_calculation_request_instance.to_dict()
# create an instance of LinkByCalculationRequest from a dict
link_by_calculation_request_from_dict = LinkByCalculationRequest.from_dict(link_by_calculation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


