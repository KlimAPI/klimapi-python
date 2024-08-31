# CheckoutLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_link** | **str** | The checkout link you can transfer to the customer. | [optional] 
**payment_link_id** | **str** | The checkout link id, used to make further calls to the API. | [optional] 
**certificate_issued_at** | **datetime** | When payment_received is true, timestamp of when the certificate was issued in ISO 8601 format (UTC) | [optional] 
**certificate_url** | **str** | When payment_received is true, the url to the certificate will be given. | [optional] 
**certificate_pdf** | **str** | When payment_received is true, the url to the certificate pdf will be given. | [optional] 
**order_id** | **str** | The id of the order created for the checkout link. | [optional] 
**kg_co2e** | **int** | The amount of kg CO<sub>2</sub>e. | [optional] 
**price** | **float** | The total of the compensation in your given currency **incl. VAT**. | [optional] 
**currency** | **str** |  | [optional] 
**payment_received** | **str** | This indicates if the order via the checkout link is already fulfilled or not. | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 

## Example

```python
from klimapi_python.models.checkout_link import CheckoutLink

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutLink from a JSON string
checkout_link_instance = CheckoutLink.from_json(json)
# print the JSON string representation of the object
print(CheckoutLink.to_json())

# convert the object into a dict
checkout_link_dict = checkout_link_instance.to_dict()
# create an instance of CheckoutLink from a dict
checkout_link_from_dict = CheckoutLink.from_dict(checkout_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


