# coding: utf-8

# flake8: noqa
"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from klimapi_python.models.add_webhook_request import AddWebhookRequest
from klimapi_python.models.bioenergy_average_energy import BioenergyAverageEnergy
from klimapi_python.models.bioenergy_average_volume import BioenergyAverageVolume
from klimapi_python.models.bioenergy_average_weight import BioenergyAverageWeight
from klimapi_python.models.bioenergy_biofuel_energy import BioenergyBiofuelEnergy
from klimapi_python.models.bioenergy_biofuel_volume import BioenergyBiofuelVolume
from klimapi_python.models.bioenergy_biofuel_weight import BioenergyBiofuelWeight
from klimapi_python.models.bioenergy_biogas_energy import BioenergyBiogasEnergy
from klimapi_python.models.bioenergy_biogas_weight import BioenergyBiogasWeight
from klimapi_python.models.bioenergy_biomass_energy import BioenergyBiomassEnergy
from klimapi_python.models.bioenergy_biomass_weight import BioenergyBiomassWeight
from klimapi_python.models.buy_amount import BuyAmount
from klimapi_python.models.buy_price import BuyPrice
from klimapi_python.models.calculate_request import CalculateRequest
from klimapi_python.models.calculation_result import CalculationResult
from klimapi_python.models.calculation_results import CalculationResults
from klimapi_python.models.cart_item import CartItem
from klimapi_python.models.cart_result import CartResult
from klimapi_python.models.cart_result_calculation_results_inner import CartResultCalculationResultsInner
from klimapi_python.models.cart_result_settings import CartResultSettings
from klimapi_python.models.category import Category
from klimapi_python.models.certification_authority import CertificationAuthority
from klimapi_python.models.checkout_link import CheckoutLink
from klimapi_python.models.checkout_link_calculated import CheckoutLinkCalculated
from klimapi_python.models.checkout_links import CheckoutLinks
from klimapi_python.models.checkout_links_calculated import CheckoutLinksCalculated
from klimapi_python.models.cloud_computing_average_cpu_hour import CloudComputingAverageCpuHour
from klimapi_python.models.cloud_computing_average_gb import CloudComputingAverageGb
from klimapi_python.models.cloud_computing_average_gb_hour import CloudComputingAverageGbHour
from klimapi_python.models.cloud_computing_average_tb_hour import CloudComputingAverageTbHour
from klimapi_python.models.cloud_computing_cpu_cpu_hour import CloudComputingCpuCpuHour
from klimapi_python.models.cloud_computing_memory_gb_hour import CloudComputingMemoryGbHour
from klimapi_python.models.cloud_computing_network_gb import CloudComputingNetworkGb
from klimapi_python.models.cloud_computing_storage_tb_hour import CloudComputingStorageTbHour
from klimapi_python.models.energy_consumption_average_energy import EnergyConsumptionAverageEnergy
from klimapi_python.models.energy_consumption_by_type_energy import EnergyConsumptionByTypeEnergy
from klimapi_python.models.food_average_currency import FoodAverageCurrency
from klimapi_python.models.food_beverages_currency import FoodBeveragesCurrency
from klimapi_python.models.food_dairy_products_currency import FoodDairyProductsCurrency
from klimapi_python.models.food_fish_products_currency import FoodFishProductsCurrency
from klimapi_python.models.food_food_products_not_elsewhere_specified_currency import FoodFoodProductsNotElsewhereSpecifiedCurrency
from klimapi_python.models.food_meat_products_beef_currency import FoodMeatProductsBeefCurrency
from klimapi_python.models.food_meat_products_not_elsewhere_specified_currency import FoodMeatProductsNotElsewhereSpecifiedCurrency
from klimapi_python.models.food_meat_products_pork_currency import FoodMeatProductsPorkCurrency
from klimapi_python.models.food_meat_products_poultry_currency import FoodMeatProductsPoultryCurrency
from klimapi_python.models.food_processed_rice_currency import FoodProcessedRiceCurrency
from klimapi_python.models.food_sugar_currency import FoodSugarCurrency
from klimapi_python.models.food_tobacco_products_currency import FoodTobaccoProductsCurrency
from klimapi_python.models.food_vegetable_oils_and_fats_currency import FoodVegetableOilsAndFatsCurrency
from klimapi_python.models.freighting_goods_average_departure_and_destination import FreightingGoodsAverageDepartureAndDestination
from klimapi_python.models.freighting_goods_average_distance import FreightingGoodsAverageDistance
from klimapi_python.models.freighting_goods_average_weight_and_distance import FreightingGoodsAverageWeightAndDistance
from klimapi_python.models.freighting_goods_cargo_ship_departure_and_destination import FreightingGoodsCargoShipDepartureAndDestination
from klimapi_python.models.freighting_goods_cargo_ship_weight_and_distance import FreightingGoodsCargoShipWeightAndDistance
from klimapi_python.models.freighting_goods_freight_flights_departure_and_destination import FreightingGoodsFreightFlightsDepartureAndDestination
from klimapi_python.models.freighting_goods_freight_flights_weight_and_distance import FreightingGoodsFreightFlightsWeightAndDistance
from klimapi_python.models.freighting_goods_hgv_all_diesel_departure_and_destination import FreightingGoodsHgvAllDieselDepartureAndDestination
from klimapi_python.models.freighting_goods_hgv_all_diesel_distance import FreightingGoodsHgvAllDieselDistance
from klimapi_python.models.freighting_goods_hgv_all_diesel_weight_and_distance import FreightingGoodsHgvAllDieselWeightAndDistance
from klimapi_python.models.freighting_goods_hgv_refrigerated_all_diesel_departure_and_destination import FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination
from klimapi_python.models.freighting_goods_hgv_refrigerated_all_diesel_distance import FreightingGoodsHgvRefrigeratedAllDieselDistance
from klimapi_python.models.freighting_goods_hgv_refrigerated_all_diesel_weight_and_distance import FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance
from klimapi_python.models.freighting_goods_rail_departure_and_destination import FreightingGoodsRailDepartureAndDestination
from klimapi_python.models.freighting_goods_rail_weight_and_distance import FreightingGoodsRailWeightAndDistance
from klimapi_python.models.freighting_goods_road_departure_and_destination import FreightingGoodsRoadDepartureAndDestination
from klimapi_python.models.freighting_goods_road_weight_and_distance import FreightingGoodsRoadWeightAndDistance
from klimapi_python.models.freighting_goods_sea_tanker_departure_and_destination import FreightingGoodsSeaTankerDepartureAndDestination
from klimapi_python.models.freighting_goods_sea_tanker_weight_and_distance import FreightingGoodsSeaTankerWeightAndDistance
from klimapi_python.models.freighting_goods_vans_departure_and_destination import FreightingGoodsVansDepartureAndDestination
from klimapi_python.models.freighting_goods_vans_distance import FreightingGoodsVansDistance
from klimapi_python.models.freighting_goods_vans_weight_and_distance import FreightingGoodsVansWeightAndDistance
from klimapi_python.models.fuels_average_volume import FuelsAverageVolume
from klimapi_python.models.fuels_average_weight import FuelsAverageWeight
from klimapi_python.models.fuels_gaseous_fuels_volume import FuelsGaseousFuelsVolume
from klimapi_python.models.fuels_gaseous_fuels_weight import FuelsGaseousFuelsWeight
from klimapi_python.models.fuels_liquid_fuels_volume import FuelsLiquidFuelsVolume
from klimapi_python.models.fuels_liquid_fuels_weight import FuelsLiquidFuelsWeight
from klimapi_python.models.fuels_solid_fuels_weight import FuelsSolidFuelsWeight
from klimapi_python.models.get_metrics_request import GetMetricsRequest
from klimapi_python.models.get_orders_request import GetOrdersRequest
from klimapi_python.models.get_orders_request_filters import GetOrdersRequestFilters
from klimapi_python.models.heat_and_steam_energy import HeatAndSteamEnergy
from klimapi_python.models.homeworking_per_fte_working_hour import HomeworkingPerFteWorkingHour
from klimapi_python.models.hotel_stay_room_per_night import HotelStayRoomPerNight
from klimapi_python.models.individual_factor import IndividualFactor
from klimapi_python.models.infrastructure_average_currency import InfrastructureAverageCurrency
from klimapi_python.models.infrastructure_real_estate_currency import InfrastructureRealEstateCurrency
from klimapi_python.models.invoice_details import InvoiceDetails
from klimapi_python.models.invoice_details_address import InvoiceDetailsAddress
from klimapi_python.models.invoice_details_tax_id import InvoiceDetailsTaxId
from klimapi_python.models.link_by_calculation_request import LinkByCalculationRequest
from klimapi_python.models.link_by_carbon_request import LinkByCarbonRequest
from klimapi_python.models.link_by_price_request import LinkByPriceRequest
from klimapi_python.models.material_use_average_currency import MaterialUseAverageCurrency
from klimapi_python.models.material_use_average_weight import MaterialUseAverageWeight
from klimapi_python.models.material_use_construction_weight import MaterialUseConstructionWeight
from klimapi_python.models.material_use_electrical_items_weight import MaterialUseElectricalItemsWeight
from klimapi_python.models.material_use_electronics_currency import MaterialUseElectronicsCurrency
from klimapi_python.models.material_use_furniture_currency import MaterialUseFurnitureCurrency
from klimapi_python.models.material_use_metal_weight import MaterialUseMetalWeight
from klimapi_python.models.material_use_organic_weight import MaterialUseOrganicWeight
from klimapi_python.models.material_use_other_weight import MaterialUseOtherWeight
from klimapi_python.models.material_use_paper_products_currency import MaterialUsePaperProductsCurrency
from klimapi_python.models.material_use_paper_weight import MaterialUsePaperWeight
from klimapi_python.models.material_use_plastic_weight import MaterialUsePlasticWeight
from klimapi_python.models.material_use_textiles_currency import MaterialUseTextilesCurrency
from klimapi_python.models.metadata_orders import MetadataOrders
from klimapi_python.models.order import Order
from klimapi_python.models.order_by_calculation_request import OrderByCalculationRequest
from klimapi_python.models.order_calculated import OrderCalculated
from klimapi_python.models.order_metrics import OrderMetrics
from klimapi_python.models.order_recipient import OrderRecipient
from klimapi_python.models.pending_by_calculation_request import PendingByCalculationRequest
from klimapi_python.models.pending_by_calculation_request_calculation_options_inner import PendingByCalculationRequestCalculationOptionsInner
from klimapi_python.models.pending_by_carbon_request import PendingByCarbonRequest
from klimapi_python.models.pending_by_price_request import PendingByPriceRequest
from klimapi_python.models.pending_order import PendingOrder
from klimapi_python.models.pending_order_calculated import PendingOrderCalculated
from klimapi_python.models.pending_orders import PendingOrders
from klimapi_python.models.pending_orders_calculated import PendingOrdersCalculated
from klimapi_python.models.process_order import ProcessOrder
from klimapi_python.models.product import Product
from klimapi_python.models.project import Project
from klimapi_python.models.travel_air_average_departure_and_destination import TravelAirAverageDepartureAndDestination
from klimapi_python.models.travel_air_average_passenger_distance import TravelAirAveragePassengerDistance
from klimapi_python.models.travel_air_flights_departure_and_destination import TravelAirFlightsDepartureAndDestination
from klimapi_python.models.travel_air_flights_passenger_distance import TravelAirFlightsPassengerDistance
from klimapi_python.models.travel_land_average_departure_and_destination import TravelLandAverageDepartureAndDestination
from klimapi_python.models.travel_land_average_distance import TravelLandAverageDistance
from klimapi_python.models.travel_land_average_passenger_distance import TravelLandAveragePassengerDistance
from klimapi_python.models.travel_land_bus_departure_and_destination import TravelLandBusDepartureAndDestination
from klimapi_python.models.travel_land_bus_passenger_distance import TravelLandBusPassengerDistance
from klimapi_python.models.travel_land_cars_by_market_segment_departure_and_destination import TravelLandCarsByMarketSegmentDepartureAndDestination
from klimapi_python.models.travel_land_cars_by_market_segment_distance import TravelLandCarsByMarketSegmentDistance
from klimapi_python.models.travel_land_cars_by_size_departure_and_destination import TravelLandCarsBySizeDepartureAndDestination
from klimapi_python.models.travel_land_cars_by_size_distance import TravelLandCarsBySizeDistance
from klimapi_python.models.travel_land_foot_bike_departure_and_destination import TravelLandFootBikeDepartureAndDestination
from klimapi_python.models.travel_land_foot_bike_passenger_distance import TravelLandFootBikePassengerDistance
from klimapi_python.models.travel_land_motorbike_departure_and_destination import TravelLandMotorbikeDepartureAndDestination
from klimapi_python.models.travel_land_motorbike_distance import TravelLandMotorbikeDistance
from klimapi_python.models.travel_land_rail_departure_and_destination import TravelLandRailDepartureAndDestination
from klimapi_python.models.travel_land_rail_passenger_distance import TravelLandRailPassengerDistance
from klimapi_python.models.travel_land_taxis_departure_and_destination import TravelLandTaxisDepartureAndDestination
from klimapi_python.models.travel_land_taxis_distance import TravelLandTaxisDistance
from klimapi_python.models.travel_land_taxis_passenger_distance import TravelLandTaxisPassengerDistance
from klimapi_python.models.travel_sea_average_departure_and_destination import TravelSeaAverageDepartureAndDestination
from klimapi_python.models.travel_sea_average_passenger_distance import TravelSeaAveragePassengerDistance
from klimapi_python.models.travel_sea_cruise_days import TravelSeaCruiseDays
from klimapi_python.models.travel_sea_ferry_departure_and_destination import TravelSeaFerryDepartureAndDestination
from klimapi_python.models.travel_sea_ferry_passenger_distance import TravelSeaFerryPassengerDistance
from klimapi_python.models.waste_disposal_average_weight import WasteDisposalAverageWeight
from klimapi_python.models.waste_disposal_construction_weight import WasteDisposalConstructionWeight
from klimapi_python.models.waste_disposal_electrical_items_weight import WasteDisposalElectricalItemsWeight
from klimapi_python.models.waste_disposal_metal_weight import WasteDisposalMetalWeight
from klimapi_python.models.waste_disposal_other_weight import WasteDisposalOtherWeight
from klimapi_python.models.waste_disposal_paper_weight import WasteDisposalPaperWeight
from klimapi_python.models.waste_disposal_plastic_weight import WasteDisposalPlasticWeight
from klimapi_python.models.waste_disposal_refuse_weight import WasteDisposalRefuseWeight
from klimapi_python.models.water_supply_volume import WaterSupplyVolume
from klimapi_python.models.water_treatment_volume import WaterTreatmentVolume
