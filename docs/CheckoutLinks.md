# CheckoutLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_links** | [**List[CheckoutLink]**](CheckoutLink.md) |  | [optional] 

## Example

```python
from klimapi_python.models.checkout_links import CheckoutLinks

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutLinks from a JSON string
checkout_links_instance = CheckoutLinks.from_json(json)
# print the JSON string representation of the object
print(CheckoutLinks.to_json())

# convert the object into a dict
checkout_links_dict = checkout_links_instance.to_dict()
# create an instance of CheckoutLinks from a dict
checkout_links_from_dict = CheckoutLinks.from_dict(checkout_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


