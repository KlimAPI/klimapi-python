# InvoiceDetailsTaxId

The customer’s tax ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the tax ID | 
**value** | **str** | Value of the tax ID | 

## Example

```python
from klimapi_python.models.invoice_details_tax_id import InvoiceDetailsTaxId

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsTaxId from a JSON string
invoice_details_tax_id_instance = InvoiceDetailsTaxId.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetailsTaxId.to_json())

# convert the object into a dict
invoice_details_tax_id_dict = invoice_details_tax_id_instance.to_dict()
# create an instance of InvoiceDetailsTaxId from a dict
invoice_details_tax_id_from_dict = InvoiceDetailsTaxId.from_dict(invoice_details_tax_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


