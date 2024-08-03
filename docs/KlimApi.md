# Methods

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_webhook**](KlimApi.md#add_webhook) | **POST** /webhooks/add | Add Webhook
[**calculate**](KlimApi.md#calculate) | **POST** /calculate | Calculate
[**calculate_cart**](KlimApi.md#calculate_cart) | **POST** /stores/{store_ident}/cart | Calculate
[**get_categories**](KlimApi.md#get_categories) | **GET** /categories | Get all Categories
[**get_certification_authorities**](KlimApi.md#get_certification_authorities) | **GET** /certification_authorities | Get all Certification Authorities
[**get_metrics**](KlimApi.md#get_metrics) | **POST** /metrics | Order Metrics
[**get_order**](KlimApi.md#get_order) | **GET** /orders/{order_id} | Get Order
[**get_orders**](KlimApi.md#get_orders) | **POST** /orders | Get Orders
[**get_payment_link**](KlimApi.md#get_payment_link) | **GET** /orders/link/{payment_link_id} | Get Checkout Link
[**get_project**](KlimApi.md#get_project) | **GET** /projects/{project_id} | Get Project
[**get_projects**](KlimApi.md#get_projects) | **GET** /projects | Get all supported Projects
[**link_by_calculation**](KlimApi.md#link_by_calculation) | **POST** /orders/link/calculate | By calculation
[**link_by_carbon**](KlimApi.md#link_by_carbon) | **POST** /orders/link/carbon | By carbon
[**link_by_price**](KlimApi.md#link_by_price) | **POST** /orders/link/price | By price
[**me**](KlimApi.md#me) | **GET** /me | Get Authenticated User
[**order_by_calculation**](KlimApi.md#order_by_calculation) | **POST** /orders/process/calculate | By calculation
[**order_by_carbon**](KlimApi.md#order_by_carbon) | **POST** /orders/process/carbon | By carbon
[**order_by_price**](KlimApi.md#order_by_price) | **POST** /orders/process/price | By price
[**pending_by_calculation**](KlimApi.md#pending_by_calculation) | **POST** /orders/pending/calculate | By calculation
[**pending_by_carbon**](KlimApi.md#pending_by_carbon) | **POST** /orders/pending/carbon | By carbon
[**pending_by_price**](KlimApi.md#pending_by_price) | **POST** /orders/pending/price | By price
[**process**](KlimApi.md#process) | **POST** /orders/{order_id}/process | Process pending Order
[**process_cart**](KlimApi.md#process_cart) | **POST** /stores/{store_ident}/cart/{order_id}/process | Process cart
[**refund**](KlimApi.md#refund) | **DELETE** /orders/{order_id}/refund | Refund Order
[**remove_webhook**](KlimApi.md#remove_webhook) | **DELETE** /webhooks/remove | Remove Webhook
[**sync_bulk_store**](KlimApi.md#sync_bulk_store) | **POST** /stores/{store_ident}/sync/bulk | Sync multiple Products
[**sync_store**](KlimApi.md#sync_store) | **POST** /stores/{store_ident}/sync | Sync a single Product


# **add_webhook**
> add_webhook(add_webhook_request)

Add Webhook

Add a new Webhook to an integration. The webhook will be triggered by the given trigger.

### Example


```python
import klimapi_python
from klimapi_python.models.add_webhook_request import AddWebhookRequest
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

add_webhook_request = klimapi_python.AddWebhookRequest() # AddWebhookRequest | 

try:
    # Add Webhook
    klimapi.add_webhook(add_webhook_request)
except Exception as e:
    print("Exception when calling KlimApi->add_webhook: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **add_webhook_request** | [**AddWebhookRequest**](AddWebhookRequest.md)|  |  |

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **201** | Successfully added the Webhook |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **500** | System unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate**
> CalculationResults calculate(calculate_request)

Calculate

**IMPORTANT:** Calling this route using API keys created in the **sandbox mode** is returning **random numbers** instead of **real calculations**.

### Example


```python
import klimapi_python
from klimapi_python.models.calculate_request import CalculateRequest
from klimapi_python.models.calculation_results import CalculationResults
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

calculate_request = klimapi_python.CalculateRequest() # CalculateRequest | Choose up to 100 Elements from the **[Calculation Options](/resources/factors)**. In this example it is just **Travel by Car**.

try:
    # Calculate
    api_response = klimapi.calculate(calculate_request)
    print("The response of KlimApi->calculate:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->calculate: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **calculate_request** | [**CalculateRequest**](CalculateRequest.md)| Choose up to 100 Elements from the **[Calculation Options](/resources/factors)**. In this example it is just **Travel by Car**. |  |

### Return type

[**CalculationResults**](CalculationResults.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully calculated |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **422** | Unknown calculation parameter |  -  |
| **500** | System unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_cart**
> CartResult calculate_cart(store_ident, cart_item, locale=locale, currency=currency)

Calculate

**IMPORTANT:** Calling this route using API keys created in the **sandbox mode** is returning **random numbers** instead of **real calculations**.

### Example


```python
import klimapi_python
from klimapi_python.models.cart_item import CartItem
from klimapi_python.models.cart_result import CartResult
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

store_ident = 'store_ident_example' # str | Setup a new store **[here](/dashboard/ecommerce)** to get a store ident
cart_item = [klimapi_python.CartItem()] # List[CartItem] | 
locale = DE # str |  (optional) (default to DE)
currency = EUR # str |  (optional) (default to EUR)

try:
    # Calculate
    api_response = klimapi.calculate_cart(store_ident, cart_item, locale=locale, currency=currency)
    print("The response of KlimApi->calculate_cart:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->calculate_cart: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **store_ident** | **str**| Setup a new store **[here](/dashboard/ecommerce)** to get a store ident |  |
| **cart_item** | [**List[CartItem]**](CartItem.md)|  |  |
| **locale** | **str**|  | [optional] [default to DE] |
| **currency** | **str**|  | [optional] [default to EUR] |

### Return type

[**CartResult**](CartResult.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully calculated the cart |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> List[Category] get_categories(locale=locale)

Get all Categories

Use the method to get all activated categories for the given API key.

### Example


```python
import klimapi_python
from klimapi_python.models.category import Category
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

locale = DE # str |  (optional) (default to DE)

try:
    # Get all Categories
    api_response = klimapi.get_categories(locale=locale)
    print("The response of KlimApi->get_categories:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->get_categories: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **locale** | **str**|  | [optional] [default to DE] |

### Return type

[**List[Category]**](Category.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got all categories |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certification_authorities**
> List[CertificationAuthority] get_certification_authorities()

Get all Certification Authorities

Use this endpoint to get all external certification authorities we are using for our compensation projects. Learn more about our [Portfolio](/portfolio).

### Example


```python
import klimapi_python
from klimapi_python.models.certification_authority import CertificationAuthority
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')


try:
    # Get all Certification Authorities
    api_response = klimapi.get_certification_authorities()
    print("The response of KlimApi->get_certification_authorities:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->get_certification_authorities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CertificationAuthority]**](CertificationAuthority.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got all Certification Authorities |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics**
> OrderMetrics get_metrics(get_metrics_request)

Order Metrics

Get metrics to all orders

### Example


```python
import klimapi_python
from klimapi_python.models.get_metrics_request import GetMetricsRequest
from klimapi_python.models.order_metrics import OrderMetrics
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

get_metrics_request = klimapi_python.GetMetricsRequest() # GetMetricsRequest | 

try:
    # Order Metrics
    api_response = klimapi.get_metrics(get_metrics_request)
    print("The response of KlimApi->get_metrics:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->get_metrics: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **get_metrics_request** | [**GetMetricsRequest**](GetMetricsRequest.md)|  |  |

### Return type

[**OrderMetrics**](OrderMetrics.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got metrics for the orders |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> Order get_order(order_id, locale=locale)

Get Order

Here you can request information about a specific Order.

### Example


```python
import klimapi_python
from klimapi_python.models.order import Order
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

order_id = 'order_id_example' # str | You can get the order_id from several endpoints, for example when creating an Order.
locale = DE # str |  (optional) (default to DE)

try:
    # Get Order
    api_response = klimapi.get_order(order_id, locale=locale)
    print("The response of KlimApi->get_order:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->get_order: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **order_id** | **str**| You can get the order_id from several endpoints, for example when creating an Order. |  |
| **locale** | **str**|  | [optional] [default to DE] |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got the requested order |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **404** | Order not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> MetadataOrders get_orders(get_orders_request, locale=locale)

Get Orders

Query all orders

### Example


```python
import klimapi_python
from klimapi_python.models.get_orders_request import GetOrdersRequest
from klimapi_python.models.metadata_orders import MetadataOrders
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

get_orders_request = klimapi_python.GetOrdersRequest() # GetOrdersRequest | 
locale = DE # str |  (optional) (default to DE)

try:
    # Get Orders
    api_response = klimapi.get_orders(get_orders_request, locale=locale)
    print("The response of KlimApi->get_orders:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->get_orders: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **get_orders_request** | [**GetOrdersRequest**](GetOrdersRequest.md)|  |  |
| **locale** | **str**|  | [optional] [default to DE] |

### Return type

[**MetadataOrders**](MetadataOrders.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got the requested orders |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_link**
> CheckoutLink get_payment_link(payment_link_id, locale=locale)

Get Checkout Link

Here you can request information about a specific Checkout Link.

### Example


```python
import klimapi_python
from klimapi_python.models.checkout_link import CheckoutLink
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

payment_link_id = 'payment_link_id_example' # str | 
locale = DE # str |  (optional) (default to DE)

try:
    # Get Checkout Link
    api_response = klimapi.get_payment_link(payment_link_id, locale=locale)
    print("The response of KlimApi->get_payment_link:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->get_payment_link: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **payment_link_id** | **str**|  |  |
| **locale** | **str**|  | [optional] [default to DE] |

### Return type

[**CheckoutLink**](CheckoutLink.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got the requested Checkout Link |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **404** | Checkout Link not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_id, locale=locale)

Get Project

Here you can request information to every project in our database.

### Example


```python
import klimapi_python
from klimapi_python.models.project import Project
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

project_id = 'project_id_example' # str | You can get the project_id from several endpoints, for example when creating an Order.
locale = DE # str |  (optional) (default to DE)

try:
    # Get Project
    api_response = klimapi.get_project(project_id, locale=locale)
    print("The response of KlimApi->get_project:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->get_project: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **str**| You can get the project_id from several endpoints, for example when creating an Order. |  |
| **locale** | **str**|  | [optional] [default to DE] |

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got the requested project |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> List[Project] get_projects(locale=locale)

Get all supported Projects

Get all projects you supported with the given API key.

### Example


```python
import klimapi_python
from klimapi_python.models.project import Project
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

locale = DE # str |  (optional) (default to DE)

try:
    # Get all supported Projects
    api_response = klimapi.get_projects(locale=locale)
    print("The response of KlimApi->get_projects:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->get_projects: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **locale** | **str**|  | [optional] [default to DE] |

### Return type

[**List[Project]**](Project.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got the requested projects |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **404** | No Projects found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_by_calculation**
> CheckoutLinksCalculated link_by_calculation(link_by_calculation_request, locale=locale, currency=currency)

By calculation

**IMPORTANT:** Calling this route using API keys created in the **sandbox mode** is returning **random numbers** instead of **real calculations**.

### Example


```python
import klimapi_python
from klimapi_python.models.checkout_links_calculated import CheckoutLinksCalculated
from klimapi_python.models.link_by_calculation_request import LinkByCalculationRequest
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

link_by_calculation_request = klimapi_python.LinkByCalculationRequest() # LinkByCalculationRequest | Choose up to 100 Elements from the **[Calculation Options](/resources/factors)**. In this example it is just **Travel by Car**.
locale = DE # str |  (optional) (default to DE)
currency = EUR # str |  (optional) (default to EUR)

try:
    # By calculation
    api_response = klimapi.link_by_calculation(link_by_calculation_request, locale=locale, currency=currency)
    print("The response of KlimApi->link_by_calculation:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->link_by_calculation: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **link_by_calculation_request** | [**LinkByCalculationRequest**](LinkByCalculationRequest.md)| Choose up to 100 Elements from the **[Calculation Options](/resources/factors)**. In this example it is just **Travel by Car**. |  |
| **locale** | **str**|  | [optional] [default to DE] |
| **currency** | **str**|  | [optional] [default to EUR] |

### Return type

[**CheckoutLinksCalculated**](CheckoutLinksCalculated.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got a Checkout Link |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **422** | Unknown calculation parameter |  -  |
| **503** | Order exceeds default stock limit. Contact us for larger orders and to increase the inventory limit for your API requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_by_carbon**
> CheckoutLinks link_by_carbon(locale=locale, currency=currency, link_by_carbon_request=link_by_carbon_request)

By carbon

Get the compensation instantly by kilogram CO2e.

### Example


```python
import klimapi_python
from klimapi_python.models.checkout_links import CheckoutLinks
from klimapi_python.models.link_by_carbon_request import LinkByCarbonRequest
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

locale = DE # str |  (optional) (default to DE)
currency = EUR # str |  (optional) (default to EUR)
link_by_carbon_request = klimapi_python.LinkByCarbonRequest() # LinkByCarbonRequest |  (optional)

try:
    # By carbon
    api_response = klimapi.link_by_carbon(locale=locale, currency=currency, link_by_carbon_request=link_by_carbon_request)
    print("The response of KlimApi->link_by_carbon:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->link_by_carbon: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **locale** | **str**|  | [optional] [default to DE] |
| **currency** | **str**|  | [optional] [default to EUR] |
| **link_by_carbon_request** | [**LinkByCarbonRequest**](LinkByCarbonRequest.md)|  | [optional]  |

### Return type

[**CheckoutLinks**](CheckoutLinks.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got a Checkout Link |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **503** | Order exceeds default stock limit. Contact us for larger orders and to increase the inventory limit for your API requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_by_price**
> CheckoutLinks link_by_price(locale=locale, currency=currency, link_by_price_request=link_by_price_request)

By price

Get the compensation instantly by price.

### Example


```python
import klimapi_python
from klimapi_python.models.checkout_links import CheckoutLinks
from klimapi_python.models.link_by_price_request import LinkByPriceRequest
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

locale = DE # str |  (optional) (default to DE)
currency = EUR # str |  (optional) (default to EUR)
link_by_price_request = klimapi_python.LinkByPriceRequest() # LinkByPriceRequest |  (optional)

try:
    # By price
    api_response = klimapi.link_by_price(locale=locale, currency=currency, link_by_price_request=link_by_price_request)
    print("The response of KlimApi->link_by_price:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->link_by_price: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **locale** | **str**|  | [optional] [default to DE] |
| **currency** | **str**|  | [optional] [default to EUR] |
| **link_by_price_request** | [**LinkByPriceRequest**](LinkByPriceRequest.md)|  | [optional]  |

### Return type

[**CheckoutLinks**](CheckoutLinks.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got a Checkout Link |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **503** | Order exceeds default stock limit. Contact us for larger orders and to increase the inventory limit for your API requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me**
> object me()

Get Authenticated User

Get Information about the Authenticated User, the Integration and the given API Key.

### Example


```python
import klimapi_python
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')


try:
    # Get Authenticated User
    api_response = klimapi.me()
    print("The response of KlimApi->me:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got the user |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_by_calculation**
> OrderCalculated order_by_calculation(order_by_calculation_request, locale=locale, currency=currency)

By calculation

**IMPORTANT:** Calling this route using API keys created in the **sandbox mode** is returning **random numbers** instead of **real calculations**.

### Example


```python
import klimapi_python
from klimapi_python.models.order_by_calculation_request import OrderByCalculationRequest
from klimapi_python.models.order_calculated import OrderCalculated
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

order_by_calculation_request = klimapi_python.OrderByCalculationRequest() # OrderByCalculationRequest | Choose up to 100 Elements from the **[Calculation Options](/resources/factors)**. In this example it is just **Travel by Car**.
locale = DE # str |  (optional) (default to DE)
currency = EUR # str |  (optional) (default to EUR)

try:
    # By calculation
    api_response = klimapi.order_by_calculation(order_by_calculation_request, locale=locale, currency=currency)
    print("The response of KlimApi->order_by_calculation:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->order_by_calculation: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **order_by_calculation_request** | [**OrderByCalculationRequest**](OrderByCalculationRequest.md)| Choose up to 100 Elements from the **[Calculation Options](/resources/factors)**. In this example it is just **Travel by Car**. |  |
| **locale** | **str**|  | [optional] [default to DE] |
| **currency** | **str**|  | [optional] [default to EUR] |

### Return type

[**OrderCalculated**](OrderCalculated.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got an Order |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **406** | The Request exceeds the given &lt;code&gt;price_limit&lt;/code&gt; |  -  |
| **422** | Unknown calculation parameter |  -  |
| **503** | Order exceeds default stock limit. Contact us for larger orders and to increase the inventory limit for your API requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_by_carbon**
> Order order_by_carbon(locale=locale, currency=currency, buy_amount=buy_amount)

By carbon

Get the compensation instantly by kilogram CO2e. For this route the API key has no limits.

### Example


```python
import klimapi_python
from klimapi_python.models.buy_amount import BuyAmount
from klimapi_python.models.order import Order
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

locale = DE # str |  (optional) (default to DE)
currency = EUR # str |  (optional) (default to EUR)
buy_amount = klimapi_python.BuyAmount() # BuyAmount |  (optional)

try:
    # By carbon
    api_response = klimapi.order_by_carbon(locale=locale, currency=currency, buy_amount=buy_amount)
    print("The response of KlimApi->order_by_carbon:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->order_by_carbon: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **locale** | **str**|  | [optional] [default to DE] |
| **currency** | **str**|  | [optional] [default to EUR] |
| **buy_amount** | [**BuyAmount**](BuyAmount.md)|  | [optional]  |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got an Order |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **406** | The Request exceeds the given &lt;code&gt;price_limit&lt;/code&gt; |  -  |
| **503** | Order exceeds default stock limit. Contact us for larger orders and to increase the inventory limit for your API requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_by_price**
> Order order_by_price(locale=locale, currency=currency, buy_price=buy_price)

By price

Get the compensation instantly by price. For this route the API key has no limits.

### Example


```python
import klimapi_python
from klimapi_python.models.buy_price import BuyPrice
from klimapi_python.models.order import Order
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

locale = DE # str |  (optional) (default to DE)
currency = EUR # str |  (optional) (default to EUR)
buy_price = klimapi_python.BuyPrice() # BuyPrice |  (optional)

try:
    # By price
    api_response = klimapi.order_by_price(locale=locale, currency=currency, buy_price=buy_price)
    print("The response of KlimApi->order_by_price:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->order_by_price: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **locale** | **str**|  | [optional] [default to DE] |
| **currency** | **str**|  | [optional] [default to EUR] |
| **buy_price** | [**BuyPrice**](BuyPrice.md)|  | [optional]  |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got an Order |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **503** | Order exceeds default stock limit. Contact us for larger orders and to increase the inventory limit for your API requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pending_by_calculation**
> PendingOrdersCalculated pending_by_calculation(pending_by_calculation_request, locale=locale, currency=currency)

By calculation

**IMPORTANT:** Calling this route using API keys created in the **sandbox mode** is returning **random numbers** instead of **real calculations**.

### Example


```python
import klimapi_python
from klimapi_python.models.pending_by_calculation_request import PendingByCalculationRequest
from klimapi_python.models.pending_orders_calculated import PendingOrdersCalculated
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

pending_by_calculation_request = klimapi_python.PendingByCalculationRequest() # PendingByCalculationRequest | Choose up to 100 Elements from the **[Calculation Options](/resources/factors)**. In this example it is just **Travel by Car**.
locale = DE # str |  (optional) (default to DE)
currency = EUR # str |  (optional) (default to EUR)

try:
    # By calculation
    api_response = klimapi.pending_by_calculation(pending_by_calculation_request, locale=locale, currency=currency)
    print("The response of KlimApi->pending_by_calculation:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->pending_by_calculation: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pending_by_calculation_request** | [**PendingByCalculationRequest**](PendingByCalculationRequest.md)| Choose up to 100 Elements from the **[Calculation Options](/resources/factors)**. In this example it is just **Travel by Car**. |  |
| **locale** | **str**|  | [optional] [default to DE] |
| **currency** | **str**|  | [optional] [default to EUR] |

### Return type

[**PendingOrdersCalculated**](PendingOrdersCalculated.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got an Order |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **422** | Unknown calculation parameter |  -  |
| **503** | Order exceeds default stock limit. Contact us for larger orders and to increase the inventory limit for your API requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pending_by_carbon**
> PendingOrders pending_by_carbon(pending_by_carbon_request, locale=locale, currency=currency)

By carbon

Here you can create an Order by kilogram CO2e. Please note the request limits of your API key, normally it is 15000kg per request. We are happy to increase the limits on request, please write us a message.

### Example


```python
import klimapi_python
from klimapi_python.models.pending_by_carbon_request import PendingByCarbonRequest
from klimapi_python.models.pending_orders import PendingOrders
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

pending_by_carbon_request = klimapi_python.PendingByCarbonRequest() # PendingByCarbonRequest | 
locale = DE # str |  (optional) (default to DE)
currency = EUR # str |  (optional) (default to EUR)

try:
    # By carbon
    api_response = klimapi.pending_by_carbon(pending_by_carbon_request, locale=locale, currency=currency)
    print("The response of KlimApi->pending_by_carbon:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->pending_by_carbon: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pending_by_carbon_request** | [**PendingByCarbonRequest**](PendingByCarbonRequest.md)|  |  |
| **locale** | **str**|  | [optional] [default to DE] |
| **currency** | **str**|  | [optional] [default to EUR] |

### Return type

[**PendingOrders**](PendingOrders.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got an Order |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **426** | You reached a limit of your API key, contact us to upgrade the default limits |  -  |
| **503** | Order exceeds default stock limit. Contact us for larger orders and to increase the inventory limit for your API requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pending_by_price**
> PendingOrders pending_by_price(pending_by_price_request, locale=locale, currency=currency)

By price

Here you can create an Order by price. Please note the request limits of your API key, normally it is 250€ per request. We are happy to increase the limits on request, please write us a message.

### Example


```python
import klimapi_python
from klimapi_python.models.pending_by_price_request import PendingByPriceRequest
from klimapi_python.models.pending_orders import PendingOrders
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

pending_by_price_request = klimapi_python.PendingByPriceRequest() # PendingByPriceRequest | 
locale = DE # str |  (optional) (default to DE)
currency = EUR # str |  (optional) (default to EUR)

try:
    # By price
    api_response = klimapi.pending_by_price(pending_by_price_request, locale=locale, currency=currency)
    print("The response of KlimApi->pending_by_price:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->pending_by_price: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pending_by_price_request** | [**PendingByPriceRequest**](PendingByPriceRequest.md)|  |  |
| **locale** | **str**|  | [optional] [default to DE] |
| **currency** | **str**|  | [optional] [default to EUR] |

### Return type

[**PendingOrders**](PendingOrders.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | Successfully got an Order |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **426** | You reached a limit of your API key, contact us to upgrade the default limits |  -  |
| **503** | Order exceeds default stock limit. Contact us for larger orders and to increase the inventory limit for your API requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process**
> Order process(order_id, process_order, locale=locale)

Process pending Order

You accepted the given order. You may now show a confirmation or provide the link to the certificate.

### Example


```python
import klimapi_python
from klimapi_python.models.order import Order
from klimapi_python.models.process_order import ProcessOrder
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

order_id = 'order_id_example' # str | The order id specified in the Order
process_order = klimapi_python.ProcessOrder() # ProcessOrder | 
locale = DE # str |  (optional) (default to DE)

try:
    # Process pending Order
    api_response = klimapi.process(order_id, process_order, locale=locale)
    print("The response of KlimApi->process:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->process: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **order_id** | **str**| The order id specified in the Order |  |
| **process_order** | [**ProcessOrder**](ProcessOrder.md)|  |  |
| **locale** | **str**|  | [optional] [default to DE] |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | The processed Order |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **410** | The order is no longer available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_cart**
> Order process_cart(store_ident, order_id, process_order, locale=locale)

Process cart



### Example


```python
import klimapi_python
from klimapi_python.models.order import Order
from klimapi_python.models.process_order import ProcessOrder
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

store_ident = 'store_ident_example' # str | Setup a new store **[here](/dashboard/ecommerce)** to get a store ident
order_id = 'order_id_example' # str | The order id specified in the Order
process_order = klimapi_python.ProcessOrder() # ProcessOrder | 
locale = DE # str |  (optional) (default to DE)

try:
    # Process cart
    api_response = klimapi.process_cart(store_ident, order_id, process_order, locale=locale)
    print("The response of KlimApi->process_cart:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling KlimApi->process_cart: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **store_ident** | **str**| Setup a new store **[here](/dashboard/ecommerce)** to get a store ident |  |
| **order_id** | **str**| The order id specified in the Order |  |
| **process_order** | [**ProcessOrder**](ProcessOrder.md)|  |  |
| **locale** | **str**|  | [optional] [default to DE] |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200** | The processed Order |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **410** | The order is no longer available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund**
> refund(order_id)

Refund Order

**Refunding an Order is only available for 30 days after the initial create/process call. Refunding is not available for Checkout Link Orders**

### Example


```python
import klimapi_python
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

order_id = 'order_id_example' # str | The order id specified in the Order

try:
    # Refund Order
    klimapi.refund(order_id)
except Exception as e:
    print("Exception when calling KlimApi->refund: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **order_id** | **str**| The order id specified in the Order |  |

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **204** | Order successfully refunded |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **410** | Order not found or the period of 30 days was exceeded and a refund is no longer available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_webhook**
> remove_webhook(add_webhook_request)

Remove Webhook

Remove a Webhook from an integration.

### Example


```python
import klimapi_python
from klimapi_python.models.add_webhook_request import AddWebhookRequest
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

add_webhook_request = klimapi_python.AddWebhookRequest() # AddWebhookRequest | 

try:
    # Remove Webhook
    klimapi.remove_webhook(add_webhook_request)
except Exception as e:
    print("Exception when calling KlimApi->remove_webhook: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **add_webhook_request** | [**AddWebhookRequest**](AddWebhookRequest.md)|  |  |

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **201** | Successfully removed the Webhook |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **500** | System unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_bulk_store**
> sync_bulk_store(store_ident, product)

Sync multiple Products

Use the method to sync multiple products from the given store to our database.

### Example


```python
import klimapi_python
from klimapi_python.models.product import Product
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

store_ident = 'store_ident_example' # str | Setup a new store **[here](/dashboard/ecommerce)** to get a store ident
product = [klimapi_python.Product()] # List[Product] | 

try:
    # Sync multiple Products
    klimapi.sync_bulk_store(store_ident, product)
except Exception as e:
    print("Exception when calling KlimApi->sync_bulk_store: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **store_ident** | **str**| Setup a new store **[here](/dashboard/ecommerce)** to get a store ident |  |
| **product** | [**List[Product]**](Product.md)|  |  |

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **204** | Products successfully synced |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **413** | You exceeded the maximum number of products (100) per request |  -  |
| **422** | Unknown or missing product parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_store**
> sync_store(store_ident, product)

Sync a single Product

Use the method to sync a single product from the given store to our database.

### Example


```python
import klimapi_python
from klimapi_python.models.product import Product
from klimapi_python.rest import ApiException
from pprint import pprint

klimapi = klimapi_python.KlimApi('your-private-api-key')

store_ident = 'store_ident_example' # str | Setup a new store **[here](/dashboard/ecommerce)** to get a store ident
product = klimapi_python.Product() # Product | 

try:
    # Sync a single Product
    klimapi.sync_store(store_ident, product)
except Exception as e:
    print("Exception when calling KlimApi->sync_store: %s\n" % e)
```



### Parameters


| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **store_ident** | **str**| Setup a new store **[here](/dashboard/ecommerce)** to get a store ident |  |
| **product** | [**Product**](Product.md)|  |  |

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md)

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **204** | Product successfully synced |  -  |
| **400** | Your request is invalid, please check the given parameters |  -  |
| **401** | Your API Key is invalid, deactivated or your account has been suspended |  -  |
| **422** | Unknown or missing product parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

