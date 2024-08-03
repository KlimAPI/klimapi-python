# klimapi-python
This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

- API version: v2
- Package version: 1.1.25

For more information, please visit [https://klimapi.com/resources/docs](https://klimapi.com/resources/docs)

## Requirements

Python 3.7+

## Installation

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/KlimAPI/klimapi-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/KlimAPI/klimapi-python.git`)

Then import the package:
```python
import klimapi_python
```

## Setup new API Instance

```python
import klimapi_python

klimapi = klimapi_python.KlimApi('your-private-api-key')
```

## Methods

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_webhook**](docs/KlimApi.md#add_webhook) | **POST** /webhooks/add | Add Webhook
[**calculate**](docs/KlimApi.md#calculate) | **POST** /calculate | Calculate
[**calculate_cart**](docs/KlimApi.md#calculate_cart) | **POST** /stores/{store_ident}/cart | Calculate
[**get_categories**](docs/KlimApi.md#get_categories) | **GET** /categories | Get all Categories
[**get_certification_authorities**](docs/KlimApi.md#get_certification_authorities) | **GET** /certification_authorities | Get all Certification Authorities
[**get_metrics**](docs/KlimApi.md#get_metrics) | **POST** /metrics | Order Metrics
[**get_order**](docs/KlimApi.md#get_order) | **GET** /orders/{order_id} | Get Order
[**get_orders**](docs/KlimApi.md#get_orders) | **POST** /orders | Get Orders
[**get_payment_link**](docs/KlimApi.md#get_payment_link) | **GET** /orders/link/{payment_link_id} | Get Checkout Link
[**get_project**](docs/KlimApi.md#get_project) | **GET** /projects/{project_id} | Get Project
[**get_projects**](docs/KlimApi.md#get_projects) | **GET** /projects | Get all supported Projects
[**link_by_calculation**](docs/KlimApi.md#link_by_calculation) | **POST** /orders/link/calculate | By calculation
[**link_by_carbon**](docs/KlimApi.md#link_by_carbon) | **POST** /orders/link/carbon | By carbon
[**link_by_price**](docs/KlimApi.md#link_by_price) | **POST** /orders/link/price | By price
[**me**](docs/KlimApi.md#me) | **GET** /me | Get Authenticated User
[**order_by_calculation**](docs/KlimApi.md#order_by_calculation) | **POST** /orders/process/calculate | By calculation
[**order_by_carbon**](docs/KlimApi.md#order_by_carbon) | **POST** /orders/process/carbon | By carbon
[**order_by_price**](docs/KlimApi.md#order_by_price) | **POST** /orders/process/price | By price
[**pending_by_calculation**](docs/KlimApi.md#pending_by_calculation) | **POST** /orders/pending/calculate | By calculation
[**pending_by_carbon**](docs/KlimApi.md#pending_by_carbon) | **POST** /orders/pending/carbon | By carbon
[**pending_by_price**](docs/KlimApi.md#pending_by_price) | **POST** /orders/pending/price | By price
[**process**](docs/KlimApi.md#process) | **POST** /orders/{order_id}/process | Process pending Order
[**process_cart**](docs/KlimApi.md#process_cart) | **POST** /stores/{store_ident}/cart/{order_id}/process | Process cart
[**refund**](docs/KlimApi.md#refund) | **DELETE** /orders/{order_id}/refund | Refund Order
[**remove_webhook**](docs/KlimApi.md#remove_webhook) | **DELETE** /webhooks/remove | Remove Webhook
[**sync_bulk_store**](docs/KlimApi.md#sync_bulk_store) | **POST** /stores/{store_ident}/sync/bulk | Sync multiple Products
[**sync_store**](docs/KlimApi.md#sync_store) | **POST** /stores/{store_ident}/sync | Sync a single Product


## Models

 - [AddWebhookRequest](docs/AddWebhookRequest.md)
 - [BuyAmount](docs/BuyAmount.md)
 - [BuyPrice](docs/BuyPrice.md)
 - [CalculateRequest](docs/CalculateRequest.md)
 - [CalculationResult](docs/CalculationResult.md)
 - [CalculationResults](docs/CalculationResults.md)
 - [CartItem](docs/CartItem.md)
 - [CartResult](docs/CartResult.md)
 - [CartResultCalculationResultsInner](docs/CartResultCalculationResultsInner.md)
 - [CartResultSettings](docs/CartResultSettings.md)
 - [Category](docs/Category.md)
 - [CertificationAuthority](docs/CertificationAuthority.md)
 - [CheckoutLink](docs/CheckoutLink.md)
 - [CheckoutLinkCalculated](docs/CheckoutLinkCalculated.md)
 - [CheckoutLinks](docs/CheckoutLinks.md)
 - [CheckoutLinksCalculated](docs/CheckoutLinksCalculated.md)
 - [GetMetricsRequest](docs/GetMetricsRequest.md)
 - [GetOrdersRequest](docs/GetOrdersRequest.md)
 - [GetOrdersRequestFilters](docs/GetOrdersRequestFilters.md)
 - [LinkByCalculationRequest](docs/LinkByCalculationRequest.md)
 - [LinkByCarbonRequest](docs/LinkByCarbonRequest.md)
 - [LinkByPriceRequest](docs/LinkByPriceRequest.md)
 - [MetadataOrders](docs/MetadataOrders.md)
 - [Order](docs/Order.md)
 - [OrderByCalculationRequest](docs/OrderByCalculationRequest.md)
 - [OrderCalculated](docs/OrderCalculated.md)
 - [OrderMetrics](docs/OrderMetrics.md)
 - [OrderRecipient](docs/OrderRecipient.md)
 - [PendingByCalculationRequest](docs/PendingByCalculationRequest.md)
 - [PendingByCarbonRequest](docs/PendingByCarbonRequest.md)
 - [PendingByPriceRequest](docs/PendingByPriceRequest.md)
 - [PendingOrder](docs/PendingOrder.md)
 - [PendingOrderCalculated](docs/PendingOrderCalculated.md)
 - [PendingOrders](docs/PendingOrders.md)
 - [PendingOrdersCalculated](docs/PendingOrdersCalculated.md)
 - [ProcessOrder](docs/ProcessOrder.md)
 - [Product](docs/Product.md)
 - [Project](docs/Project.md)


