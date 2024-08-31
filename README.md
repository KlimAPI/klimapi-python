# klimapi-python
This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

- API version: v2
- Package version: 1.1.29

For more information, please visit [https://klimapi.com/resources/docs](https://klimapi.com/resources/docs)

## Requirements

Python 3.7+

## Installation

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install klimapi-python
```
(you may need to run `pip` with root permission: `sudo pip install klimapi-python`)

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
[**link_by_calculation**](docs/KlimApi.md#link_by_calculation) | **POST** /orders/link/calculate | By Calculation
[**link_by_carbon**](docs/KlimApi.md#link_by_carbon) | **POST** /orders/link/carbon | By Carbon
[**link_by_price**](docs/KlimApi.md#link_by_price) | **POST** /orders/link/price | By Price
[**me**](docs/KlimApi.md#me) | **GET** /me | Get Authenticated User
[**order_by_calculation**](docs/KlimApi.md#order_by_calculation) | **POST** /orders/process/calculate | By Calculation
[**order_by_carbon**](docs/KlimApi.md#order_by_carbon) | **POST** /orders/process/carbon | By Carbon
[**order_by_price**](docs/KlimApi.md#order_by_price) | **POST** /orders/process/price | By Price
[**pending_by_calculation**](docs/KlimApi.md#pending_by_calculation) | **POST** /orders/pending/calculate | By Calculation
[**pending_by_carbon**](docs/KlimApi.md#pending_by_carbon) | **POST** /orders/pending/carbon | By Carbon
[**pending_by_price**](docs/KlimApi.md#pending_by_price) | **POST** /orders/pending/price | By Price
[**process**](docs/KlimApi.md#process) | **POST** /orders/{order_id}/process | Process Pending Order
[**process_cart**](docs/KlimApi.md#process_cart) | **POST** /stores/{store_ident}/cart/{order_id}/process | Process Cart
[**refund**](docs/KlimApi.md#refund) | **DELETE** /orders/{order_id}/refund | Refund Order
[**remove_webhook**](docs/KlimApi.md#remove_webhook) | **DELETE** /webhooks/remove | Remove Webhook
[**sync_bulk_store**](docs/KlimApi.md#sync_bulk_store) | **POST** /stores/{store_ident}/sync/bulk | Sync multiple Products
[**sync_store**](docs/KlimApi.md#sync_store) | **POST** /stores/{store_ident}/sync | Sync a single Product


## Models

 - [AddWebhookRequest](docs/AddWebhookRequest.md)
 - [BioenergyAverageEnergy](docs/BioenergyAverageEnergy.md)
 - [BioenergyAverageVolume](docs/BioenergyAverageVolume.md)
 - [BioenergyAverageWeight](docs/BioenergyAverageWeight.md)
 - [BioenergyBiofuelEnergy](docs/BioenergyBiofuelEnergy.md)
 - [BioenergyBiofuelVolume](docs/BioenergyBiofuelVolume.md)
 - [BioenergyBiofuelWeight](docs/BioenergyBiofuelWeight.md)
 - [BioenergyBiogasEnergy](docs/BioenergyBiogasEnergy.md)
 - [BioenergyBiogasWeight](docs/BioenergyBiogasWeight.md)
 - [BioenergyBiomassEnergy](docs/BioenergyBiomassEnergy.md)
 - [BioenergyBiomassWeight](docs/BioenergyBiomassWeight.md)
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
 - [CloudComputingAverageCpuHour](docs/CloudComputingAverageCpuHour.md)
 - [CloudComputingAverageGb](docs/CloudComputingAverageGb.md)
 - [CloudComputingAverageGbHour](docs/CloudComputingAverageGbHour.md)
 - [CloudComputingAverageTbHour](docs/CloudComputingAverageTbHour.md)
 - [CloudComputingCpuCpuHour](docs/CloudComputingCpuCpuHour.md)
 - [CloudComputingMemoryGbHour](docs/CloudComputingMemoryGbHour.md)
 - [CloudComputingNetworkGb](docs/CloudComputingNetworkGb.md)
 - [CloudComputingStorageTbHour](docs/CloudComputingStorageTbHour.md)
 - [EnergyConsumptionAverageEnergy](docs/EnergyConsumptionAverageEnergy.md)
 - [EnergyConsumptionByTypeEnergy](docs/EnergyConsumptionByTypeEnergy.md)
 - [FoodAverageCurrency](docs/FoodAverageCurrency.md)
 - [FoodBeveragesCurrency](docs/FoodBeveragesCurrency.md)
 - [FoodDairyProductsCurrency](docs/FoodDairyProductsCurrency.md)
 - [FoodFishProductsCurrency](docs/FoodFishProductsCurrency.md)
 - [FoodFoodProductsNotElsewhereSpecifiedCurrency](docs/FoodFoodProductsNotElsewhereSpecifiedCurrency.md)
 - [FoodMeatProductsBeefCurrency](docs/FoodMeatProductsBeefCurrency.md)
 - [FoodMeatProductsNotElsewhereSpecifiedCurrency](docs/FoodMeatProductsNotElsewhereSpecifiedCurrency.md)
 - [FoodMeatProductsPorkCurrency](docs/FoodMeatProductsPorkCurrency.md)
 - [FoodMeatProductsPoultryCurrency](docs/FoodMeatProductsPoultryCurrency.md)
 - [FoodProcessedRiceCurrency](docs/FoodProcessedRiceCurrency.md)
 - [FoodSugarCurrency](docs/FoodSugarCurrency.md)
 - [FoodTobaccoProductsCurrency](docs/FoodTobaccoProductsCurrency.md)
 - [FoodVegetableOilsAndFatsCurrency](docs/FoodVegetableOilsAndFatsCurrency.md)
 - [FreightingGoodsAverageDepartureAndDestination](docs/FreightingGoodsAverageDepartureAndDestination.md)
 - [FreightingGoodsAverageDistance](docs/FreightingGoodsAverageDistance.md)
 - [FreightingGoodsAverageWeightAndDistance](docs/FreightingGoodsAverageWeightAndDistance.md)
 - [FreightingGoodsCargoShipDepartureAndDestination](docs/FreightingGoodsCargoShipDepartureAndDestination.md)
 - [FreightingGoodsCargoShipWeightAndDistance](docs/FreightingGoodsCargoShipWeightAndDistance.md)
 - [FreightingGoodsFreightFlightsDepartureAndDestination](docs/FreightingGoodsFreightFlightsDepartureAndDestination.md)
 - [FreightingGoodsFreightFlightsWeightAndDistance](docs/FreightingGoodsFreightFlightsWeightAndDistance.md)
 - [FreightingGoodsHgvAllDieselDepartureAndDestination](docs/FreightingGoodsHgvAllDieselDepartureAndDestination.md)
 - [FreightingGoodsHgvAllDieselDistance](docs/FreightingGoodsHgvAllDieselDistance.md)
 - [FreightingGoodsHgvAllDieselWeightAndDistance](docs/FreightingGoodsHgvAllDieselWeightAndDistance.md)
 - [FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination](docs/FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination.md)
 - [FreightingGoodsHgvRefrigeratedAllDieselDistance](docs/FreightingGoodsHgvRefrigeratedAllDieselDistance.md)
 - [FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance](docs/FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance.md)
 - [FreightingGoodsRailDepartureAndDestination](docs/FreightingGoodsRailDepartureAndDestination.md)
 - [FreightingGoodsRailWeightAndDistance](docs/FreightingGoodsRailWeightAndDistance.md)
 - [FreightingGoodsRoadDepartureAndDestination](docs/FreightingGoodsRoadDepartureAndDestination.md)
 - [FreightingGoodsRoadWeightAndDistance](docs/FreightingGoodsRoadWeightAndDistance.md)
 - [FreightingGoodsSeaTankerDepartureAndDestination](docs/FreightingGoodsSeaTankerDepartureAndDestination.md)
 - [FreightingGoodsSeaTankerWeightAndDistance](docs/FreightingGoodsSeaTankerWeightAndDistance.md)
 - [FreightingGoodsVansDepartureAndDestination](docs/FreightingGoodsVansDepartureAndDestination.md)
 - [FreightingGoodsVansDistance](docs/FreightingGoodsVansDistance.md)
 - [FreightingGoodsVansWeightAndDistance](docs/FreightingGoodsVansWeightAndDistance.md)
 - [FuelsAverageVolume](docs/FuelsAverageVolume.md)
 - [FuelsAverageWeight](docs/FuelsAverageWeight.md)
 - [FuelsGaseousFuelsVolume](docs/FuelsGaseousFuelsVolume.md)
 - [FuelsGaseousFuelsWeight](docs/FuelsGaseousFuelsWeight.md)
 - [FuelsLiquidFuelsVolume](docs/FuelsLiquidFuelsVolume.md)
 - [FuelsLiquidFuelsWeight](docs/FuelsLiquidFuelsWeight.md)
 - [FuelsSolidFuelsWeight](docs/FuelsSolidFuelsWeight.md)
 - [GetMetricsRequest](docs/GetMetricsRequest.md)
 - [GetOrdersRequest](docs/GetOrdersRequest.md)
 - [GetOrdersRequestFilters](docs/GetOrdersRequestFilters.md)
 - [HeatAndSteamEnergy](docs/HeatAndSteamEnergy.md)
 - [HomeworkingPerFteWorkingHour](docs/HomeworkingPerFteWorkingHour.md)
 - [HotelStayRoomPerNight](docs/HotelStayRoomPerNight.md)
 - [IndividualFactor](docs/IndividualFactor.md)
 - [InfrastructureAverageCurrency](docs/InfrastructureAverageCurrency.md)
 - [InfrastructureRealEstateCurrency](docs/InfrastructureRealEstateCurrency.md)
 - [InvoiceDetails](docs/InvoiceDetails.md)
 - [InvoiceDetailsAddress](docs/InvoiceDetailsAddress.md)
 - [InvoiceDetailsTaxId](docs/InvoiceDetailsTaxId.md)
 - [LinkByCalculationRequest](docs/LinkByCalculationRequest.md)
 - [LinkByCarbonRequest](docs/LinkByCarbonRequest.md)
 - [LinkByPriceRequest](docs/LinkByPriceRequest.md)
 - [MaterialUseAverageCurrency](docs/MaterialUseAverageCurrency.md)
 - [MaterialUseAverageWeight](docs/MaterialUseAverageWeight.md)
 - [MaterialUseConstructionWeight](docs/MaterialUseConstructionWeight.md)
 - [MaterialUseElectricalItemsWeight](docs/MaterialUseElectricalItemsWeight.md)
 - [MaterialUseElectronicsCurrency](docs/MaterialUseElectronicsCurrency.md)
 - [MaterialUseFurnitureCurrency](docs/MaterialUseFurnitureCurrency.md)
 - [MaterialUseMetalWeight](docs/MaterialUseMetalWeight.md)
 - [MaterialUseOrganicWeight](docs/MaterialUseOrganicWeight.md)
 - [MaterialUseOtherWeight](docs/MaterialUseOtherWeight.md)
 - [MaterialUsePaperProductsCurrency](docs/MaterialUsePaperProductsCurrency.md)
 - [MaterialUsePaperWeight](docs/MaterialUsePaperWeight.md)
 - [MaterialUsePlasticWeight](docs/MaterialUsePlasticWeight.md)
 - [MaterialUseTextilesCurrency](docs/MaterialUseTextilesCurrency.md)
 - [MetadataOrders](docs/MetadataOrders.md)
 - [Order](docs/Order.md)
 - [OrderByCalculationRequest](docs/OrderByCalculationRequest.md)
 - [OrderCalculated](docs/OrderCalculated.md)
 - [OrderMetrics](docs/OrderMetrics.md)
 - [OrderRecipient](docs/OrderRecipient.md)
 - [PendingByCalculationRequest](docs/PendingByCalculationRequest.md)
 - [PendingByCalculationRequestCalculationOptionsInner](docs/PendingByCalculationRequestCalculationOptionsInner.md)
 - [PendingByCarbonRequest](docs/PendingByCarbonRequest.md)
 - [PendingByPriceRequest](docs/PendingByPriceRequest.md)
 - [PendingOrder](docs/PendingOrder.md)
 - [PendingOrderCalculated](docs/PendingOrderCalculated.md)
 - [PendingOrders](docs/PendingOrders.md)
 - [PendingOrdersCalculated](docs/PendingOrdersCalculated.md)
 - [ProcessOrder](docs/ProcessOrder.md)
 - [Product](docs/Product.md)
 - [Project](docs/Project.md)
 - [TravelAirAverageDepartureAndDestination](docs/TravelAirAverageDepartureAndDestination.md)
 - [TravelAirAveragePassengerDistance](docs/TravelAirAveragePassengerDistance.md)
 - [TravelAirFlightsDepartureAndDestination](docs/TravelAirFlightsDepartureAndDestination.md)
 - [TravelAirFlightsPassengerDistance](docs/TravelAirFlightsPassengerDistance.md)
 - [TravelLandAverageDepartureAndDestination](docs/TravelLandAverageDepartureAndDestination.md)
 - [TravelLandAverageDistance](docs/TravelLandAverageDistance.md)
 - [TravelLandAveragePassengerDistance](docs/TravelLandAveragePassengerDistance.md)
 - [TravelLandBusDepartureAndDestination](docs/TravelLandBusDepartureAndDestination.md)
 - [TravelLandBusPassengerDistance](docs/TravelLandBusPassengerDistance.md)
 - [TravelLandCarsByMarketSegmentDepartureAndDestination](docs/TravelLandCarsByMarketSegmentDepartureAndDestination.md)
 - [TravelLandCarsByMarketSegmentDistance](docs/TravelLandCarsByMarketSegmentDistance.md)
 - [TravelLandCarsBySizeDepartureAndDestination](docs/TravelLandCarsBySizeDepartureAndDestination.md)
 - [TravelLandCarsBySizeDistance](docs/TravelLandCarsBySizeDistance.md)
 - [TravelLandFootBikeDepartureAndDestination](docs/TravelLandFootBikeDepartureAndDestination.md)
 - [TravelLandFootBikePassengerDistance](docs/TravelLandFootBikePassengerDistance.md)
 - [TravelLandMotorbikeDepartureAndDestination](docs/TravelLandMotorbikeDepartureAndDestination.md)
 - [TravelLandMotorbikeDistance](docs/TravelLandMotorbikeDistance.md)
 - [TravelLandRailDepartureAndDestination](docs/TravelLandRailDepartureAndDestination.md)
 - [TravelLandRailPassengerDistance](docs/TravelLandRailPassengerDistance.md)
 - [TravelLandTaxisDepartureAndDestination](docs/TravelLandTaxisDepartureAndDestination.md)
 - [TravelLandTaxisDistance](docs/TravelLandTaxisDistance.md)
 - [TravelLandTaxisPassengerDistance](docs/TravelLandTaxisPassengerDistance.md)
 - [TravelSeaAverageDepartureAndDestination](docs/TravelSeaAverageDepartureAndDestination.md)
 - [TravelSeaAveragePassengerDistance](docs/TravelSeaAveragePassengerDistance.md)
 - [TravelSeaCruiseDays](docs/TravelSeaCruiseDays.md)
 - [TravelSeaFerryDepartureAndDestination](docs/TravelSeaFerryDepartureAndDestination.md)
 - [TravelSeaFerryPassengerDistance](docs/TravelSeaFerryPassengerDistance.md)
 - [WasteDisposalAverageWeight](docs/WasteDisposalAverageWeight.md)
 - [WasteDisposalConstructionWeight](docs/WasteDisposalConstructionWeight.md)
 - [WasteDisposalElectricalItemsWeight](docs/WasteDisposalElectricalItemsWeight.md)
 - [WasteDisposalMetalWeight](docs/WasteDisposalMetalWeight.md)
 - [WasteDisposalOtherWeight](docs/WasteDisposalOtherWeight.md)
 - [WasteDisposalPaperWeight](docs/WasteDisposalPaperWeight.md)
 - [WasteDisposalPlasticWeight](docs/WasteDisposalPlasticWeight.md)
 - [WasteDisposalRefuseWeight](docs/WasteDisposalRefuseWeight.md)
 - [WaterSupplyVolume](docs/WaterSupplyVolume.md)
 - [WaterTreatmentVolume](docs/WaterTreatmentVolume.md)


