# InvoiceDetails

Required with **billing_type** = `invoice`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The customer’s full name or business name | 
**email** | **str** | The customer’s email address | 
**address** | [**InvoiceDetailsAddress**](InvoiceDetailsAddress.md) |  | 
**tax_id** | [**InvoiceDetailsTaxId**](InvoiceDetailsTaxId.md) |  | [optional] 

## Example

```python
from klimapi_python.models.invoice_details import InvoiceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetails from a JSON string
invoice_details_instance = InvoiceDetails.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetails.to_json())

# convert the object into a dict
invoice_details_dict = invoice_details_instance.to_dict()
# create an instance of InvoiceDetails from a dict
invoice_details_from_dict = InvoiceDetails.from_dict(invoice_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


