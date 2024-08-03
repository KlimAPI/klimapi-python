# CheckoutLinksCalculated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_links** | [**List[CheckoutLinkCalculated]**](CheckoutLinkCalculated.md) |  | [optional] 

## Example

```python
from klimapi_python.models.checkout_links_calculated import CheckoutLinksCalculated

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutLinksCalculated from a JSON string
checkout_links_calculated_instance = CheckoutLinksCalculated.from_json(json)
# print the JSON string representation of the object
print(CheckoutLinksCalculated.to_json())

# convert the object into a dict
checkout_links_calculated_dict = checkout_links_calculated_instance.to_dict()
# create an instance of CheckoutLinksCalculated from a dict
checkout_links_calculated_from_dict = CheckoutLinksCalculated.from_dict(checkout_links_calculated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


