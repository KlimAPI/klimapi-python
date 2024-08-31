# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
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
from klimapi_python.models.heat_and_steam_energy import HeatAndSteamEnergy
from klimapi_python.models.homeworking_per_fte_working_hour import HomeworkingPerFteWorkingHour
from klimapi_python.models.hotel_stay_room_per_night import HotelStayRoomPerNight
from klimapi_python.models.individual_factor import IndividualFactor
from klimapi_python.models.infrastructure_average_currency import InfrastructureAverageCurrency
from klimapi_python.models.infrastructure_real_estate_currency import InfrastructureRealEstateCurrency
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
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

PENDINGBYCALCULATIONREQUESTCALCULATIONOPTIONSINNER_ANY_OF_SCHEMAS = ["BioenergyAverageEnergy", "BioenergyAverageVolume", "BioenergyAverageWeight", "BioenergyBiofuelEnergy", "BioenergyBiofuelVolume", "BioenergyBiofuelWeight", "BioenergyBiogasEnergy", "BioenergyBiogasWeight", "BioenergyBiomassEnergy", "BioenergyBiomassWeight", "CloudComputingAverageCpuHour", "CloudComputingAverageGb", "CloudComputingAverageGbHour", "CloudComputingAverageTbHour", "CloudComputingCpuCpuHour", "CloudComputingMemoryGbHour", "CloudComputingNetworkGb", "CloudComputingStorageTbHour", "EnergyConsumptionAverageEnergy", "EnergyConsumptionByTypeEnergy", "FoodAverageCurrency", "FoodBeveragesCurrency", "FoodDairyProductsCurrency", "FoodFishProductsCurrency", "FoodFoodProductsNotElsewhereSpecifiedCurrency", "FoodMeatProductsBeefCurrency", "FoodMeatProductsNotElsewhereSpecifiedCurrency", "FoodMeatProductsPorkCurrency", "FoodMeatProductsPoultryCurrency", "FoodProcessedRiceCurrency", "FoodSugarCurrency", "FoodTobaccoProductsCurrency", "FoodVegetableOilsAndFatsCurrency", "FreightingGoodsAverageDepartureAndDestination", "FreightingGoodsAverageDistance", "FreightingGoodsAverageWeightAndDistance", "FreightingGoodsCargoShipDepartureAndDestination", "FreightingGoodsCargoShipWeightAndDistance", "FreightingGoodsFreightFlightsDepartureAndDestination", "FreightingGoodsFreightFlightsWeightAndDistance", "FreightingGoodsHgvAllDieselDepartureAndDestination", "FreightingGoodsHgvAllDieselDistance", "FreightingGoodsHgvAllDieselWeightAndDistance", "FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination", "FreightingGoodsHgvRefrigeratedAllDieselDistance", "FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance", "FreightingGoodsRailDepartureAndDestination", "FreightingGoodsRailWeightAndDistance", "FreightingGoodsRoadDepartureAndDestination", "FreightingGoodsRoadWeightAndDistance", "FreightingGoodsSeaTankerDepartureAndDestination", "FreightingGoodsSeaTankerWeightAndDistance", "FreightingGoodsVansDepartureAndDestination", "FreightingGoodsVansDistance", "FreightingGoodsVansWeightAndDistance", "FuelsAverageVolume", "FuelsAverageWeight", "FuelsGaseousFuelsVolume", "FuelsGaseousFuelsWeight", "FuelsLiquidFuelsVolume", "FuelsLiquidFuelsWeight", "FuelsSolidFuelsWeight", "HeatAndSteamEnergy", "HomeworkingPerFteWorkingHour", "HotelStayRoomPerNight", "IndividualFactor", "InfrastructureAverageCurrency", "InfrastructureRealEstateCurrency", "MaterialUseAverageCurrency", "MaterialUseAverageWeight", "MaterialUseConstructionWeight", "MaterialUseElectricalItemsWeight", "MaterialUseElectronicsCurrency", "MaterialUseFurnitureCurrency", "MaterialUseMetalWeight", "MaterialUseOrganicWeight", "MaterialUseOtherWeight", "MaterialUsePaperProductsCurrency", "MaterialUsePaperWeight", "MaterialUsePlasticWeight", "MaterialUseTextilesCurrency", "TravelAirAverageDepartureAndDestination", "TravelAirAveragePassengerDistance", "TravelAirFlightsDepartureAndDestination", "TravelAirFlightsPassengerDistance", "TravelLandAverageDepartureAndDestination", "TravelLandAverageDistance", "TravelLandAveragePassengerDistance", "TravelLandBusDepartureAndDestination", "TravelLandBusPassengerDistance", "TravelLandCarsByMarketSegmentDepartureAndDestination", "TravelLandCarsByMarketSegmentDistance", "TravelLandCarsBySizeDepartureAndDestination", "TravelLandCarsBySizeDistance", "TravelLandFootBikeDepartureAndDestination", "TravelLandFootBikePassengerDistance", "TravelLandMotorbikeDepartureAndDestination", "TravelLandMotorbikeDistance", "TravelLandRailDepartureAndDestination", "TravelLandRailPassengerDistance", "TravelLandTaxisDepartureAndDestination", "TravelLandTaxisDistance", "TravelLandTaxisPassengerDistance", "TravelSeaAverageDepartureAndDestination", "TravelSeaAveragePassengerDistance", "TravelSeaCruiseDays", "TravelSeaFerryDepartureAndDestination", "TravelSeaFerryPassengerDistance", "WasteDisposalAverageWeight", "WasteDisposalConstructionWeight", "WasteDisposalElectricalItemsWeight", "WasteDisposalMetalWeight", "WasteDisposalOtherWeight", "WasteDisposalPaperWeight", "WasteDisposalPlasticWeight", "WasteDisposalRefuseWeight", "WaterSupplyVolume", "WaterTreatmentVolume"]

class PendingByCalculationRequestCalculationOptionsInner(BaseModel):
    """
    PendingByCalculationRequestCalculationOptionsInner
    """

    # data type: FuelsGaseousFuelsWeight
    anyof_schema_1_validator: Optional[FuelsGaseousFuelsWeight] = None
    # data type: FuelsGaseousFuelsVolume
    anyof_schema_2_validator: Optional[FuelsGaseousFuelsVolume] = None
    # data type: FuelsLiquidFuelsWeight
    anyof_schema_3_validator: Optional[FuelsLiquidFuelsWeight] = None
    # data type: FuelsLiquidFuelsVolume
    anyof_schema_4_validator: Optional[FuelsLiquidFuelsVolume] = None
    # data type: FuelsSolidFuelsWeight
    anyof_schema_5_validator: Optional[FuelsSolidFuelsWeight] = None
    # data type: FuelsAverageWeight
    anyof_schema_6_validator: Optional[FuelsAverageWeight] = None
    # data type: FuelsAverageVolume
    anyof_schema_7_validator: Optional[FuelsAverageVolume] = None
    # data type: BioenergyBiofuelVolume
    anyof_schema_8_validator: Optional[BioenergyBiofuelVolume] = None
    # data type: BioenergyBiofuelEnergy
    anyof_schema_9_validator: Optional[BioenergyBiofuelEnergy] = None
    # data type: BioenergyBiofuelWeight
    anyof_schema_10_validator: Optional[BioenergyBiofuelWeight] = None
    # data type: BioenergyBiomassWeight
    anyof_schema_11_validator: Optional[BioenergyBiomassWeight] = None
    # data type: BioenergyBiomassEnergy
    anyof_schema_12_validator: Optional[BioenergyBiomassEnergy] = None
    # data type: BioenergyBiogasWeight
    anyof_schema_13_validator: Optional[BioenergyBiogasWeight] = None
    # data type: BioenergyBiogasEnergy
    anyof_schema_14_validator: Optional[BioenergyBiogasEnergy] = None
    # data type: BioenergyAverageEnergy
    anyof_schema_15_validator: Optional[BioenergyAverageEnergy] = None
    # data type: BioenergyAverageWeight
    anyof_schema_16_validator: Optional[BioenergyAverageWeight] = None
    # data type: BioenergyAverageVolume
    anyof_schema_17_validator: Optional[BioenergyAverageVolume] = None
    # data type: HeatAndSteamEnergy
    anyof_schema_18_validator: Optional[HeatAndSteamEnergy] = None
    # data type: WaterSupplyVolume
    anyof_schema_19_validator: Optional[WaterSupplyVolume] = None
    # data type: WaterTreatmentVolume
    anyof_schema_20_validator: Optional[WaterTreatmentVolume] = None
    # data type: MaterialUseConstructionWeight
    anyof_schema_21_validator: Optional[MaterialUseConstructionWeight] = None
    # data type: MaterialUseOtherWeight
    anyof_schema_22_validator: Optional[MaterialUseOtherWeight] = None
    # data type: MaterialUseOrganicWeight
    anyof_schema_23_validator: Optional[MaterialUseOrganicWeight] = None
    # data type: MaterialUseElectricalItemsWeight
    anyof_schema_24_validator: Optional[MaterialUseElectricalItemsWeight] = None
    # data type: MaterialUsePlasticWeight
    anyof_schema_25_validator: Optional[MaterialUsePlasticWeight] = None
    # data type: MaterialUseMetalWeight
    anyof_schema_26_validator: Optional[MaterialUseMetalWeight] = None
    # data type: MaterialUsePaperWeight
    anyof_schema_27_validator: Optional[MaterialUsePaperWeight] = None
    # data type: MaterialUseTextilesCurrency
    anyof_schema_28_validator: Optional[MaterialUseTextilesCurrency] = None
    # data type: MaterialUseElectronicsCurrency
    anyof_schema_29_validator: Optional[MaterialUseElectronicsCurrency] = None
    # data type: MaterialUsePaperProductsCurrency
    anyof_schema_30_validator: Optional[MaterialUsePaperProductsCurrency] = None
    # data type: MaterialUseFurnitureCurrency
    anyof_schema_31_validator: Optional[MaterialUseFurnitureCurrency] = None
    # data type: MaterialUseAverageCurrency
    anyof_schema_32_validator: Optional[MaterialUseAverageCurrency] = None
    # data type: MaterialUseAverageWeight
    anyof_schema_33_validator: Optional[MaterialUseAverageWeight] = None
    # data type: WasteDisposalConstructionWeight
    anyof_schema_34_validator: Optional[WasteDisposalConstructionWeight] = None
    # data type: WasteDisposalOtherWeight
    anyof_schema_35_validator: Optional[WasteDisposalOtherWeight] = None
    # data type: WasteDisposalRefuseWeight
    anyof_schema_36_validator: Optional[WasteDisposalRefuseWeight] = None
    # data type: WasteDisposalElectricalItemsWeight
    anyof_schema_37_validator: Optional[WasteDisposalElectricalItemsWeight] = None
    # data type: WasteDisposalMetalWeight
    anyof_schema_38_validator: Optional[WasteDisposalMetalWeight] = None
    # data type: WasteDisposalPlasticWeight
    anyof_schema_39_validator: Optional[WasteDisposalPlasticWeight] = None
    # data type: WasteDisposalPaperWeight
    anyof_schema_40_validator: Optional[WasteDisposalPaperWeight] = None
    # data type: WasteDisposalAverageWeight
    anyof_schema_41_validator: Optional[WasteDisposalAverageWeight] = None
    # data type: HotelStayRoomPerNight
    anyof_schema_42_validator: Optional[HotelStayRoomPerNight] = None
    # data type: TravelAirFlightsPassengerDistance
    anyof_schema_43_validator: Optional[TravelAirFlightsPassengerDistance] = None
    # data type: TravelAirFlightsDepartureAndDestination
    anyof_schema_44_validator: Optional[TravelAirFlightsDepartureAndDestination] = None
    # data type: TravelAirAveragePassengerDistance
    anyof_schema_45_validator: Optional[TravelAirAveragePassengerDistance] = None
    # data type: TravelAirAverageDepartureAndDestination
    anyof_schema_46_validator: Optional[TravelAirAverageDepartureAndDestination] = None
    # data type: TravelSeaFerryPassengerDistance
    anyof_schema_47_validator: Optional[TravelSeaFerryPassengerDistance] = None
    # data type: TravelSeaFerryDepartureAndDestination
    anyof_schema_48_validator: Optional[TravelSeaFerryDepartureAndDestination] = None
    # data type: TravelSeaCruiseDays
    anyof_schema_49_validator: Optional[TravelSeaCruiseDays] = None
    # data type: TravelSeaAveragePassengerDistance
    anyof_schema_50_validator: Optional[TravelSeaAveragePassengerDistance] = None
    # data type: TravelSeaAverageDepartureAndDestination
    anyof_schema_51_validator: Optional[TravelSeaAverageDepartureAndDestination] = None
    # data type: TravelLandCarsByMarketSegmentDistance
    anyof_schema_52_validator: Optional[TravelLandCarsByMarketSegmentDistance] = None
    # data type: TravelLandCarsByMarketSegmentDepartureAndDestination
    anyof_schema_53_validator: Optional[TravelLandCarsByMarketSegmentDepartureAndDestination] = None
    # data type: TravelLandTaxisPassengerDistance
    anyof_schema_54_validator: Optional[TravelLandTaxisPassengerDistance] = None
    # data type: TravelLandTaxisDepartureAndDestination
    anyof_schema_55_validator: Optional[TravelLandTaxisDepartureAndDestination] = None
    # data type: TravelLandTaxisDistance
    anyof_schema_56_validator: Optional[TravelLandTaxisDistance] = None
    # data type: TravelLandCarsBySizeDistance
    anyof_schema_57_validator: Optional[TravelLandCarsBySizeDistance] = None
    # data type: TravelLandCarsBySizeDepartureAndDestination
    anyof_schema_58_validator: Optional[TravelLandCarsBySizeDepartureAndDestination] = None
    # data type: TravelLandMotorbikeDistance
    anyof_schema_59_validator: Optional[TravelLandMotorbikeDistance] = None
    # data type: TravelLandMotorbikeDepartureAndDestination
    anyof_schema_60_validator: Optional[TravelLandMotorbikeDepartureAndDestination] = None
    # data type: TravelLandBusPassengerDistance
    anyof_schema_61_validator: Optional[TravelLandBusPassengerDistance] = None
    # data type: TravelLandBusDepartureAndDestination
    anyof_schema_62_validator: Optional[TravelLandBusDepartureAndDestination] = None
    # data type: TravelLandRailPassengerDistance
    anyof_schema_63_validator: Optional[TravelLandRailPassengerDistance] = None
    # data type: TravelLandRailDepartureAndDestination
    anyof_schema_64_validator: Optional[TravelLandRailDepartureAndDestination] = None
    # data type: TravelLandFootBikePassengerDistance
    anyof_schema_65_validator: Optional[TravelLandFootBikePassengerDistance] = None
    # data type: TravelLandFootBikeDepartureAndDestination
    anyof_schema_66_validator: Optional[TravelLandFootBikeDepartureAndDestination] = None
    # data type: TravelLandAverageDistance
    anyof_schema_67_validator: Optional[TravelLandAverageDistance] = None
    # data type: TravelLandAverageDepartureAndDestination
    anyof_schema_68_validator: Optional[TravelLandAverageDepartureAndDestination] = None
    # data type: TravelLandAveragePassengerDistance
    anyof_schema_69_validator: Optional[TravelLandAveragePassengerDistance] = None
    # data type: FreightingGoodsVansWeightAndDistance
    anyof_schema_70_validator: Optional[FreightingGoodsVansWeightAndDistance] = None
    # data type: FreightingGoodsVansDepartureAndDestination
    anyof_schema_71_validator: Optional[FreightingGoodsVansDepartureAndDestination] = None
    # data type: FreightingGoodsVansDistance
    anyof_schema_72_validator: Optional[FreightingGoodsVansDistance] = None
    # data type: FreightingGoodsHgvAllDieselWeightAndDistance
    anyof_schema_73_validator: Optional[FreightingGoodsHgvAllDieselWeightAndDistance] = None
    # data type: FreightingGoodsHgvAllDieselDepartureAndDestination
    anyof_schema_74_validator: Optional[FreightingGoodsHgvAllDieselDepartureAndDestination] = None
    # data type: FreightingGoodsHgvAllDieselDistance
    anyof_schema_75_validator: Optional[FreightingGoodsHgvAllDieselDistance] = None
    # data type: FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance
    anyof_schema_76_validator: Optional[FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance] = None
    # data type: FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination
    anyof_schema_77_validator: Optional[FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination] = None
    # data type: FreightingGoodsHgvRefrigeratedAllDieselDistance
    anyof_schema_78_validator: Optional[FreightingGoodsHgvRefrigeratedAllDieselDistance] = None
    # data type: FreightingGoodsFreightFlightsWeightAndDistance
    anyof_schema_79_validator: Optional[FreightingGoodsFreightFlightsWeightAndDistance] = None
    # data type: FreightingGoodsFreightFlightsDepartureAndDestination
    anyof_schema_80_validator: Optional[FreightingGoodsFreightFlightsDepartureAndDestination] = None
    # data type: FreightingGoodsRailWeightAndDistance
    anyof_schema_81_validator: Optional[FreightingGoodsRailWeightAndDistance] = None
    # data type: FreightingGoodsRailDepartureAndDestination
    anyof_schema_82_validator: Optional[FreightingGoodsRailDepartureAndDestination] = None
    # data type: FreightingGoodsSeaTankerWeightAndDistance
    anyof_schema_83_validator: Optional[FreightingGoodsSeaTankerWeightAndDistance] = None
    # data type: FreightingGoodsSeaTankerDepartureAndDestination
    anyof_schema_84_validator: Optional[FreightingGoodsSeaTankerDepartureAndDestination] = None
    # data type: FreightingGoodsCargoShipWeightAndDistance
    anyof_schema_85_validator: Optional[FreightingGoodsCargoShipWeightAndDistance] = None
    # data type: FreightingGoodsCargoShipDepartureAndDestination
    anyof_schema_86_validator: Optional[FreightingGoodsCargoShipDepartureAndDestination] = None
    # data type: FreightingGoodsRoadWeightAndDistance
    anyof_schema_87_validator: Optional[FreightingGoodsRoadWeightAndDistance] = None
    # data type: FreightingGoodsRoadDepartureAndDestination
    anyof_schema_88_validator: Optional[FreightingGoodsRoadDepartureAndDestination] = None
    # data type: FreightingGoodsAverageWeightAndDistance
    anyof_schema_89_validator: Optional[FreightingGoodsAverageWeightAndDistance] = None
    # data type: FreightingGoodsAverageDepartureAndDestination
    anyof_schema_90_validator: Optional[FreightingGoodsAverageDepartureAndDestination] = None
    # data type: FreightingGoodsAverageDistance
    anyof_schema_91_validator: Optional[FreightingGoodsAverageDistance] = None
    # data type: HomeworkingPerFteWorkingHour
    anyof_schema_92_validator: Optional[HomeworkingPerFteWorkingHour] = None
    # data type: InfrastructureRealEstateCurrency
    anyof_schema_93_validator: Optional[InfrastructureRealEstateCurrency] = None
    # data type: InfrastructureAverageCurrency
    anyof_schema_94_validator: Optional[InfrastructureAverageCurrency] = None
    # data type: CloudComputingCpuCpuHour
    anyof_schema_95_validator: Optional[CloudComputingCpuCpuHour] = None
    # data type: CloudComputingMemoryGbHour
    anyof_schema_96_validator: Optional[CloudComputingMemoryGbHour] = None
    # data type: CloudComputingNetworkGb
    anyof_schema_97_validator: Optional[CloudComputingNetworkGb] = None
    # data type: CloudComputingStorageTbHour
    anyof_schema_98_validator: Optional[CloudComputingStorageTbHour] = None
    # data type: CloudComputingAverageTbHour
    anyof_schema_99_validator: Optional[CloudComputingAverageTbHour] = None
    # data type: CloudComputingAverageGb
    anyof_schema_100_validator: Optional[CloudComputingAverageGb] = None
    # data type: CloudComputingAverageGbHour
    anyof_schema_101_validator: Optional[CloudComputingAverageGbHour] = None
    # data type: CloudComputingAverageCpuHour
    anyof_schema_102_validator: Optional[CloudComputingAverageCpuHour] = None
    # data type: FoodBeveragesCurrency
    anyof_schema_103_validator: Optional[FoodBeveragesCurrency] = None
    # data type: FoodDairyProductsCurrency
    anyof_schema_104_validator: Optional[FoodDairyProductsCurrency] = None
    # data type: FoodFishProductsCurrency
    anyof_schema_105_validator: Optional[FoodFishProductsCurrency] = None
    # data type: FoodFoodProductsNotElsewhereSpecifiedCurrency
    anyof_schema_106_validator: Optional[FoodFoodProductsNotElsewhereSpecifiedCurrency] = None
    # data type: FoodMeatProductsBeefCurrency
    anyof_schema_107_validator: Optional[FoodMeatProductsBeefCurrency] = None
    # data type: FoodMeatProductsNotElsewhereSpecifiedCurrency
    anyof_schema_108_validator: Optional[FoodMeatProductsNotElsewhereSpecifiedCurrency] = None
    # data type: FoodMeatProductsPorkCurrency
    anyof_schema_109_validator: Optional[FoodMeatProductsPorkCurrency] = None
    # data type: FoodMeatProductsPoultryCurrency
    anyof_schema_110_validator: Optional[FoodMeatProductsPoultryCurrency] = None
    # data type: FoodSugarCurrency
    anyof_schema_111_validator: Optional[FoodSugarCurrency] = None
    # data type: FoodProcessedRiceCurrency
    anyof_schema_112_validator: Optional[FoodProcessedRiceCurrency] = None
    # data type: FoodTobaccoProductsCurrency
    anyof_schema_113_validator: Optional[FoodTobaccoProductsCurrency] = None
    # data type: FoodVegetableOilsAndFatsCurrency
    anyof_schema_114_validator: Optional[FoodVegetableOilsAndFatsCurrency] = None
    # data type: FoodAverageCurrency
    anyof_schema_115_validator: Optional[FoodAverageCurrency] = None
    # data type: EnergyConsumptionByTypeEnergy
    anyof_schema_116_validator: Optional[EnergyConsumptionByTypeEnergy] = None
    # data type: EnergyConsumptionAverageEnergy
    anyof_schema_117_validator: Optional[EnergyConsumptionAverageEnergy] = None
    # data type: IndividualFactor
    anyof_schema_118_validator: Optional[IndividualFactor] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[BioenergyAverageEnergy, BioenergyAverageVolume, BioenergyAverageWeight, BioenergyBiofuelEnergy, BioenergyBiofuelVolume, BioenergyBiofuelWeight, BioenergyBiogasEnergy, BioenergyBiogasWeight, BioenergyBiomassEnergy, BioenergyBiomassWeight, CloudComputingAverageCpuHour, CloudComputingAverageGb, CloudComputingAverageGbHour, CloudComputingAverageTbHour, CloudComputingCpuCpuHour, CloudComputingMemoryGbHour, CloudComputingNetworkGb, CloudComputingStorageTbHour, EnergyConsumptionAverageEnergy, EnergyConsumptionByTypeEnergy, FoodAverageCurrency, FoodBeveragesCurrency, FoodDairyProductsCurrency, FoodFishProductsCurrency, FoodFoodProductsNotElsewhereSpecifiedCurrency, FoodMeatProductsBeefCurrency, FoodMeatProductsNotElsewhereSpecifiedCurrency, FoodMeatProductsPorkCurrency, FoodMeatProductsPoultryCurrency, FoodProcessedRiceCurrency, FoodSugarCurrency, FoodTobaccoProductsCurrency, FoodVegetableOilsAndFatsCurrency, FreightingGoodsAverageDepartureAndDestination, FreightingGoodsAverageDistance, FreightingGoodsAverageWeightAndDistance, FreightingGoodsCargoShipDepartureAndDestination, FreightingGoodsCargoShipWeightAndDistance, FreightingGoodsFreightFlightsDepartureAndDestination, FreightingGoodsFreightFlightsWeightAndDistance, FreightingGoodsHgvAllDieselDepartureAndDestination, FreightingGoodsHgvAllDieselDistance, FreightingGoodsHgvAllDieselWeightAndDistance, FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination, FreightingGoodsHgvRefrigeratedAllDieselDistance, FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance, FreightingGoodsRailDepartureAndDestination, FreightingGoodsRailWeightAndDistance, FreightingGoodsRoadDepartureAndDestination, FreightingGoodsRoadWeightAndDistance, FreightingGoodsSeaTankerDepartureAndDestination, FreightingGoodsSeaTankerWeightAndDistance, FreightingGoodsVansDepartureAndDestination, FreightingGoodsVansDistance, FreightingGoodsVansWeightAndDistance, FuelsAverageVolume, FuelsAverageWeight, FuelsGaseousFuelsVolume, FuelsGaseousFuelsWeight, FuelsLiquidFuelsVolume, FuelsLiquidFuelsWeight, FuelsSolidFuelsWeight, HeatAndSteamEnergy, HomeworkingPerFteWorkingHour, HotelStayRoomPerNight, IndividualFactor, InfrastructureAverageCurrency, InfrastructureRealEstateCurrency, MaterialUseAverageCurrency, MaterialUseAverageWeight, MaterialUseConstructionWeight, MaterialUseElectricalItemsWeight, MaterialUseElectronicsCurrency, MaterialUseFurnitureCurrency, MaterialUseMetalWeight, MaterialUseOrganicWeight, MaterialUseOtherWeight, MaterialUsePaperProductsCurrency, MaterialUsePaperWeight, MaterialUsePlasticWeight, MaterialUseTextilesCurrency, TravelAirAverageDepartureAndDestination, TravelAirAveragePassengerDistance, TravelAirFlightsDepartureAndDestination, TravelAirFlightsPassengerDistance, TravelLandAverageDepartureAndDestination, TravelLandAverageDistance, TravelLandAveragePassengerDistance, TravelLandBusDepartureAndDestination, TravelLandBusPassengerDistance, TravelLandCarsByMarketSegmentDepartureAndDestination, TravelLandCarsByMarketSegmentDistance, TravelLandCarsBySizeDepartureAndDestination, TravelLandCarsBySizeDistance, TravelLandFootBikeDepartureAndDestination, TravelLandFootBikePassengerDistance, TravelLandMotorbikeDepartureAndDestination, TravelLandMotorbikeDistance, TravelLandRailDepartureAndDestination, TravelLandRailPassengerDistance, TravelLandTaxisDepartureAndDestination, TravelLandTaxisDistance, TravelLandTaxisPassengerDistance, TravelSeaAverageDepartureAndDestination, TravelSeaAveragePassengerDistance, TravelSeaCruiseDays, TravelSeaFerryDepartureAndDestination, TravelSeaFerryPassengerDistance, WasteDisposalAverageWeight, WasteDisposalConstructionWeight, WasteDisposalElectricalItemsWeight, WasteDisposalMetalWeight, WasteDisposalOtherWeight, WasteDisposalPaperWeight, WasteDisposalPlasticWeight, WasteDisposalRefuseWeight, WaterSupplyVolume, WaterTreatmentVolume]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "BioenergyAverageEnergy", "BioenergyAverageVolume", "BioenergyAverageWeight", "BioenergyBiofuelEnergy", "BioenergyBiofuelVolume", "BioenergyBiofuelWeight", "BioenergyBiogasEnergy", "BioenergyBiogasWeight", "BioenergyBiomassEnergy", "BioenergyBiomassWeight", "CloudComputingAverageCpuHour", "CloudComputingAverageGb", "CloudComputingAverageGbHour", "CloudComputingAverageTbHour", "CloudComputingCpuCpuHour", "CloudComputingMemoryGbHour", "CloudComputingNetworkGb", "CloudComputingStorageTbHour", "EnergyConsumptionAverageEnergy", "EnergyConsumptionByTypeEnergy", "FoodAverageCurrency", "FoodBeveragesCurrency", "FoodDairyProductsCurrency", "FoodFishProductsCurrency", "FoodFoodProductsNotElsewhereSpecifiedCurrency", "FoodMeatProductsBeefCurrency", "FoodMeatProductsNotElsewhereSpecifiedCurrency", "FoodMeatProductsPorkCurrency", "FoodMeatProductsPoultryCurrency", "FoodProcessedRiceCurrency", "FoodSugarCurrency", "FoodTobaccoProductsCurrency", "FoodVegetableOilsAndFatsCurrency", "FreightingGoodsAverageDepartureAndDestination", "FreightingGoodsAverageDistance", "FreightingGoodsAverageWeightAndDistance", "FreightingGoodsCargoShipDepartureAndDestination", "FreightingGoodsCargoShipWeightAndDistance", "FreightingGoodsFreightFlightsDepartureAndDestination", "FreightingGoodsFreightFlightsWeightAndDistance", "FreightingGoodsHgvAllDieselDepartureAndDestination", "FreightingGoodsHgvAllDieselDistance", "FreightingGoodsHgvAllDieselWeightAndDistance", "FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination", "FreightingGoodsHgvRefrigeratedAllDieselDistance", "FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance", "FreightingGoodsRailDepartureAndDestination", "FreightingGoodsRailWeightAndDistance", "FreightingGoodsRoadDepartureAndDestination", "FreightingGoodsRoadWeightAndDistance", "FreightingGoodsSeaTankerDepartureAndDestination", "FreightingGoodsSeaTankerWeightAndDistance", "FreightingGoodsVansDepartureAndDestination", "FreightingGoodsVansDistance", "FreightingGoodsVansWeightAndDistance", "FuelsAverageVolume", "FuelsAverageWeight", "FuelsGaseousFuelsVolume", "FuelsGaseousFuelsWeight", "FuelsLiquidFuelsVolume", "FuelsLiquidFuelsWeight", "FuelsSolidFuelsWeight", "HeatAndSteamEnergy", "HomeworkingPerFteWorkingHour", "HotelStayRoomPerNight", "IndividualFactor", "InfrastructureAverageCurrency", "InfrastructureRealEstateCurrency", "MaterialUseAverageCurrency", "MaterialUseAverageWeight", "MaterialUseConstructionWeight", "MaterialUseElectricalItemsWeight", "MaterialUseElectronicsCurrency", "MaterialUseFurnitureCurrency", "MaterialUseMetalWeight", "MaterialUseOrganicWeight", "MaterialUseOtherWeight", "MaterialUsePaperProductsCurrency", "MaterialUsePaperWeight", "MaterialUsePlasticWeight", "MaterialUseTextilesCurrency", "TravelAirAverageDepartureAndDestination", "TravelAirAveragePassengerDistance", "TravelAirFlightsDepartureAndDestination", "TravelAirFlightsPassengerDistance", "TravelLandAverageDepartureAndDestination", "TravelLandAverageDistance", "TravelLandAveragePassengerDistance", "TravelLandBusDepartureAndDestination", "TravelLandBusPassengerDistance", "TravelLandCarsByMarketSegmentDepartureAndDestination", "TravelLandCarsByMarketSegmentDistance", "TravelLandCarsBySizeDepartureAndDestination", "TravelLandCarsBySizeDistance", "TravelLandFootBikeDepartureAndDestination", "TravelLandFootBikePassengerDistance", "TravelLandMotorbikeDepartureAndDestination", "TravelLandMotorbikeDistance", "TravelLandRailDepartureAndDestination", "TravelLandRailPassengerDistance", "TravelLandTaxisDepartureAndDestination", "TravelLandTaxisDistance", "TravelLandTaxisPassengerDistance", "TravelSeaAverageDepartureAndDestination", "TravelSeaAveragePassengerDistance", "TravelSeaCruiseDays", "TravelSeaFerryDepartureAndDestination", "TravelSeaFerryPassengerDistance", "WasteDisposalAverageWeight", "WasteDisposalConstructionWeight", "WasteDisposalElectricalItemsWeight", "WasteDisposalMetalWeight", "WasteDisposalOtherWeight", "WasteDisposalPaperWeight", "WasteDisposalPlasticWeight", "WasteDisposalRefuseWeight", "WaterSupplyVolume", "WaterTreatmentVolume" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = PendingByCalculationRequestCalculationOptionsInner.model_construct()
        error_messages = []
        # validate data type: FuelsGaseousFuelsWeight
        if not isinstance(v, FuelsGaseousFuelsWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FuelsGaseousFuelsWeight`")
        else:
            return v

        # validate data type: FuelsGaseousFuelsVolume
        if not isinstance(v, FuelsGaseousFuelsVolume):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FuelsGaseousFuelsVolume`")
        else:
            return v

        # validate data type: FuelsLiquidFuelsWeight
        if not isinstance(v, FuelsLiquidFuelsWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FuelsLiquidFuelsWeight`")
        else:
            return v

        # validate data type: FuelsLiquidFuelsVolume
        if not isinstance(v, FuelsLiquidFuelsVolume):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FuelsLiquidFuelsVolume`")
        else:
            return v

        # validate data type: FuelsSolidFuelsWeight
        if not isinstance(v, FuelsSolidFuelsWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FuelsSolidFuelsWeight`")
        else:
            return v

        # validate data type: FuelsAverageWeight
        if not isinstance(v, FuelsAverageWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FuelsAverageWeight`")
        else:
            return v

        # validate data type: FuelsAverageVolume
        if not isinstance(v, FuelsAverageVolume):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FuelsAverageVolume`")
        else:
            return v

        # validate data type: BioenergyBiofuelVolume
        if not isinstance(v, BioenergyBiofuelVolume):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BioenergyBiofuelVolume`")
        else:
            return v

        # validate data type: BioenergyBiofuelEnergy
        if not isinstance(v, BioenergyBiofuelEnergy):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BioenergyBiofuelEnergy`")
        else:
            return v

        # validate data type: BioenergyBiofuelWeight
        if not isinstance(v, BioenergyBiofuelWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BioenergyBiofuelWeight`")
        else:
            return v

        # validate data type: BioenergyBiomassWeight
        if not isinstance(v, BioenergyBiomassWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BioenergyBiomassWeight`")
        else:
            return v

        # validate data type: BioenergyBiomassEnergy
        if not isinstance(v, BioenergyBiomassEnergy):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BioenergyBiomassEnergy`")
        else:
            return v

        # validate data type: BioenergyBiogasWeight
        if not isinstance(v, BioenergyBiogasWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BioenergyBiogasWeight`")
        else:
            return v

        # validate data type: BioenergyBiogasEnergy
        if not isinstance(v, BioenergyBiogasEnergy):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BioenergyBiogasEnergy`")
        else:
            return v

        # validate data type: BioenergyAverageEnergy
        if not isinstance(v, BioenergyAverageEnergy):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BioenergyAverageEnergy`")
        else:
            return v

        # validate data type: BioenergyAverageWeight
        if not isinstance(v, BioenergyAverageWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BioenergyAverageWeight`")
        else:
            return v

        # validate data type: BioenergyAverageVolume
        if not isinstance(v, BioenergyAverageVolume):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BioenergyAverageVolume`")
        else:
            return v

        # validate data type: HeatAndSteamEnergy
        if not isinstance(v, HeatAndSteamEnergy):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HeatAndSteamEnergy`")
        else:
            return v

        # validate data type: WaterSupplyVolume
        if not isinstance(v, WaterSupplyVolume):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WaterSupplyVolume`")
        else:
            return v

        # validate data type: WaterTreatmentVolume
        if not isinstance(v, WaterTreatmentVolume):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WaterTreatmentVolume`")
        else:
            return v

        # validate data type: MaterialUseConstructionWeight
        if not isinstance(v, MaterialUseConstructionWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUseConstructionWeight`")
        else:
            return v

        # validate data type: MaterialUseOtherWeight
        if not isinstance(v, MaterialUseOtherWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUseOtherWeight`")
        else:
            return v

        # validate data type: MaterialUseOrganicWeight
        if not isinstance(v, MaterialUseOrganicWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUseOrganicWeight`")
        else:
            return v

        # validate data type: MaterialUseElectricalItemsWeight
        if not isinstance(v, MaterialUseElectricalItemsWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUseElectricalItemsWeight`")
        else:
            return v

        # validate data type: MaterialUsePlasticWeight
        if not isinstance(v, MaterialUsePlasticWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUsePlasticWeight`")
        else:
            return v

        # validate data type: MaterialUseMetalWeight
        if not isinstance(v, MaterialUseMetalWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUseMetalWeight`")
        else:
            return v

        # validate data type: MaterialUsePaperWeight
        if not isinstance(v, MaterialUsePaperWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUsePaperWeight`")
        else:
            return v

        # validate data type: MaterialUseTextilesCurrency
        if not isinstance(v, MaterialUseTextilesCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUseTextilesCurrency`")
        else:
            return v

        # validate data type: MaterialUseElectronicsCurrency
        if not isinstance(v, MaterialUseElectronicsCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUseElectronicsCurrency`")
        else:
            return v

        # validate data type: MaterialUsePaperProductsCurrency
        if not isinstance(v, MaterialUsePaperProductsCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUsePaperProductsCurrency`")
        else:
            return v

        # validate data type: MaterialUseFurnitureCurrency
        if not isinstance(v, MaterialUseFurnitureCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUseFurnitureCurrency`")
        else:
            return v

        # validate data type: MaterialUseAverageCurrency
        if not isinstance(v, MaterialUseAverageCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUseAverageCurrency`")
        else:
            return v

        # validate data type: MaterialUseAverageWeight
        if not isinstance(v, MaterialUseAverageWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaterialUseAverageWeight`")
        else:
            return v

        # validate data type: WasteDisposalConstructionWeight
        if not isinstance(v, WasteDisposalConstructionWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WasteDisposalConstructionWeight`")
        else:
            return v

        # validate data type: WasteDisposalOtherWeight
        if not isinstance(v, WasteDisposalOtherWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WasteDisposalOtherWeight`")
        else:
            return v

        # validate data type: WasteDisposalRefuseWeight
        if not isinstance(v, WasteDisposalRefuseWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WasteDisposalRefuseWeight`")
        else:
            return v

        # validate data type: WasteDisposalElectricalItemsWeight
        if not isinstance(v, WasteDisposalElectricalItemsWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WasteDisposalElectricalItemsWeight`")
        else:
            return v

        # validate data type: WasteDisposalMetalWeight
        if not isinstance(v, WasteDisposalMetalWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WasteDisposalMetalWeight`")
        else:
            return v

        # validate data type: WasteDisposalPlasticWeight
        if not isinstance(v, WasteDisposalPlasticWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WasteDisposalPlasticWeight`")
        else:
            return v

        # validate data type: WasteDisposalPaperWeight
        if not isinstance(v, WasteDisposalPaperWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WasteDisposalPaperWeight`")
        else:
            return v

        # validate data type: WasteDisposalAverageWeight
        if not isinstance(v, WasteDisposalAverageWeight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WasteDisposalAverageWeight`")
        else:
            return v

        # validate data type: HotelStayRoomPerNight
        if not isinstance(v, HotelStayRoomPerNight):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HotelStayRoomPerNight`")
        else:
            return v

        # validate data type: TravelAirFlightsPassengerDistance
        if not isinstance(v, TravelAirFlightsPassengerDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelAirFlightsPassengerDistance`")
        else:
            return v

        # validate data type: TravelAirFlightsDepartureAndDestination
        if not isinstance(v, TravelAirFlightsDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelAirFlightsDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelAirAveragePassengerDistance
        if not isinstance(v, TravelAirAveragePassengerDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelAirAveragePassengerDistance`")
        else:
            return v

        # validate data type: TravelAirAverageDepartureAndDestination
        if not isinstance(v, TravelAirAverageDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelAirAverageDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelSeaFerryPassengerDistance
        if not isinstance(v, TravelSeaFerryPassengerDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelSeaFerryPassengerDistance`")
        else:
            return v

        # validate data type: TravelSeaFerryDepartureAndDestination
        if not isinstance(v, TravelSeaFerryDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelSeaFerryDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelSeaCruiseDays
        if not isinstance(v, TravelSeaCruiseDays):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelSeaCruiseDays`")
        else:
            return v

        # validate data type: TravelSeaAveragePassengerDistance
        if not isinstance(v, TravelSeaAveragePassengerDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelSeaAveragePassengerDistance`")
        else:
            return v

        # validate data type: TravelSeaAverageDepartureAndDestination
        if not isinstance(v, TravelSeaAverageDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelSeaAverageDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelLandCarsByMarketSegmentDistance
        if not isinstance(v, TravelLandCarsByMarketSegmentDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandCarsByMarketSegmentDistance`")
        else:
            return v

        # validate data type: TravelLandCarsByMarketSegmentDepartureAndDestination
        if not isinstance(v, TravelLandCarsByMarketSegmentDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandCarsByMarketSegmentDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelLandTaxisPassengerDistance
        if not isinstance(v, TravelLandTaxisPassengerDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandTaxisPassengerDistance`")
        else:
            return v

        # validate data type: TravelLandTaxisDepartureAndDestination
        if not isinstance(v, TravelLandTaxisDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandTaxisDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelLandTaxisDistance
        if not isinstance(v, TravelLandTaxisDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandTaxisDistance`")
        else:
            return v

        # validate data type: TravelLandCarsBySizeDistance
        if not isinstance(v, TravelLandCarsBySizeDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandCarsBySizeDistance`")
        else:
            return v

        # validate data type: TravelLandCarsBySizeDepartureAndDestination
        if not isinstance(v, TravelLandCarsBySizeDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandCarsBySizeDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelLandMotorbikeDistance
        if not isinstance(v, TravelLandMotorbikeDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandMotorbikeDistance`")
        else:
            return v

        # validate data type: TravelLandMotorbikeDepartureAndDestination
        if not isinstance(v, TravelLandMotorbikeDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandMotorbikeDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelLandBusPassengerDistance
        if not isinstance(v, TravelLandBusPassengerDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandBusPassengerDistance`")
        else:
            return v

        # validate data type: TravelLandBusDepartureAndDestination
        if not isinstance(v, TravelLandBusDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandBusDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelLandRailPassengerDistance
        if not isinstance(v, TravelLandRailPassengerDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandRailPassengerDistance`")
        else:
            return v

        # validate data type: TravelLandRailDepartureAndDestination
        if not isinstance(v, TravelLandRailDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandRailDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelLandFootBikePassengerDistance
        if not isinstance(v, TravelLandFootBikePassengerDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandFootBikePassengerDistance`")
        else:
            return v

        # validate data type: TravelLandFootBikeDepartureAndDestination
        if not isinstance(v, TravelLandFootBikeDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandFootBikeDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelLandAverageDistance
        if not isinstance(v, TravelLandAverageDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandAverageDistance`")
        else:
            return v

        # validate data type: TravelLandAverageDepartureAndDestination
        if not isinstance(v, TravelLandAverageDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandAverageDepartureAndDestination`")
        else:
            return v

        # validate data type: TravelLandAveragePassengerDistance
        if not isinstance(v, TravelLandAveragePassengerDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TravelLandAveragePassengerDistance`")
        else:
            return v

        # validate data type: FreightingGoodsVansWeightAndDistance
        if not isinstance(v, FreightingGoodsVansWeightAndDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsVansWeightAndDistance`")
        else:
            return v

        # validate data type: FreightingGoodsVansDepartureAndDestination
        if not isinstance(v, FreightingGoodsVansDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsVansDepartureAndDestination`")
        else:
            return v

        # validate data type: FreightingGoodsVansDistance
        if not isinstance(v, FreightingGoodsVansDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsVansDistance`")
        else:
            return v

        # validate data type: FreightingGoodsHgvAllDieselWeightAndDistance
        if not isinstance(v, FreightingGoodsHgvAllDieselWeightAndDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsHgvAllDieselWeightAndDistance`")
        else:
            return v

        # validate data type: FreightingGoodsHgvAllDieselDepartureAndDestination
        if not isinstance(v, FreightingGoodsHgvAllDieselDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsHgvAllDieselDepartureAndDestination`")
        else:
            return v

        # validate data type: FreightingGoodsHgvAllDieselDistance
        if not isinstance(v, FreightingGoodsHgvAllDieselDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsHgvAllDieselDistance`")
        else:
            return v

        # validate data type: FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance
        if not isinstance(v, FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance`")
        else:
            return v

        # validate data type: FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination
        if not isinstance(v, FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination`")
        else:
            return v

        # validate data type: FreightingGoodsHgvRefrigeratedAllDieselDistance
        if not isinstance(v, FreightingGoodsHgvRefrigeratedAllDieselDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsHgvRefrigeratedAllDieselDistance`")
        else:
            return v

        # validate data type: FreightingGoodsFreightFlightsWeightAndDistance
        if not isinstance(v, FreightingGoodsFreightFlightsWeightAndDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsFreightFlightsWeightAndDistance`")
        else:
            return v

        # validate data type: FreightingGoodsFreightFlightsDepartureAndDestination
        if not isinstance(v, FreightingGoodsFreightFlightsDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsFreightFlightsDepartureAndDestination`")
        else:
            return v

        # validate data type: FreightingGoodsRailWeightAndDistance
        if not isinstance(v, FreightingGoodsRailWeightAndDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsRailWeightAndDistance`")
        else:
            return v

        # validate data type: FreightingGoodsRailDepartureAndDestination
        if not isinstance(v, FreightingGoodsRailDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsRailDepartureAndDestination`")
        else:
            return v

        # validate data type: FreightingGoodsSeaTankerWeightAndDistance
        if not isinstance(v, FreightingGoodsSeaTankerWeightAndDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsSeaTankerWeightAndDistance`")
        else:
            return v

        # validate data type: FreightingGoodsSeaTankerDepartureAndDestination
        if not isinstance(v, FreightingGoodsSeaTankerDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsSeaTankerDepartureAndDestination`")
        else:
            return v

        # validate data type: FreightingGoodsCargoShipWeightAndDistance
        if not isinstance(v, FreightingGoodsCargoShipWeightAndDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsCargoShipWeightAndDistance`")
        else:
            return v

        # validate data type: FreightingGoodsCargoShipDepartureAndDestination
        if not isinstance(v, FreightingGoodsCargoShipDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsCargoShipDepartureAndDestination`")
        else:
            return v

        # validate data type: FreightingGoodsRoadWeightAndDistance
        if not isinstance(v, FreightingGoodsRoadWeightAndDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsRoadWeightAndDistance`")
        else:
            return v

        # validate data type: FreightingGoodsRoadDepartureAndDestination
        if not isinstance(v, FreightingGoodsRoadDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsRoadDepartureAndDestination`")
        else:
            return v

        # validate data type: FreightingGoodsAverageWeightAndDistance
        if not isinstance(v, FreightingGoodsAverageWeightAndDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsAverageWeightAndDistance`")
        else:
            return v

        # validate data type: FreightingGoodsAverageDepartureAndDestination
        if not isinstance(v, FreightingGoodsAverageDepartureAndDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsAverageDepartureAndDestination`")
        else:
            return v

        # validate data type: FreightingGoodsAverageDistance
        if not isinstance(v, FreightingGoodsAverageDistance):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FreightingGoodsAverageDistance`")
        else:
            return v

        # validate data type: HomeworkingPerFteWorkingHour
        if not isinstance(v, HomeworkingPerFteWorkingHour):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HomeworkingPerFteWorkingHour`")
        else:
            return v

        # validate data type: InfrastructureRealEstateCurrency
        if not isinstance(v, InfrastructureRealEstateCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InfrastructureRealEstateCurrency`")
        else:
            return v

        # validate data type: InfrastructureAverageCurrency
        if not isinstance(v, InfrastructureAverageCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InfrastructureAverageCurrency`")
        else:
            return v

        # validate data type: CloudComputingCpuCpuHour
        if not isinstance(v, CloudComputingCpuCpuHour):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CloudComputingCpuCpuHour`")
        else:
            return v

        # validate data type: CloudComputingMemoryGbHour
        if not isinstance(v, CloudComputingMemoryGbHour):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CloudComputingMemoryGbHour`")
        else:
            return v

        # validate data type: CloudComputingNetworkGb
        if not isinstance(v, CloudComputingNetworkGb):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CloudComputingNetworkGb`")
        else:
            return v

        # validate data type: CloudComputingStorageTbHour
        if not isinstance(v, CloudComputingStorageTbHour):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CloudComputingStorageTbHour`")
        else:
            return v

        # validate data type: CloudComputingAverageTbHour
        if not isinstance(v, CloudComputingAverageTbHour):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CloudComputingAverageTbHour`")
        else:
            return v

        # validate data type: CloudComputingAverageGb
        if not isinstance(v, CloudComputingAverageGb):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CloudComputingAverageGb`")
        else:
            return v

        # validate data type: CloudComputingAverageGbHour
        if not isinstance(v, CloudComputingAverageGbHour):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CloudComputingAverageGbHour`")
        else:
            return v

        # validate data type: CloudComputingAverageCpuHour
        if not isinstance(v, CloudComputingAverageCpuHour):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CloudComputingAverageCpuHour`")
        else:
            return v

        # validate data type: FoodBeveragesCurrency
        if not isinstance(v, FoodBeveragesCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodBeveragesCurrency`")
        else:
            return v

        # validate data type: FoodDairyProductsCurrency
        if not isinstance(v, FoodDairyProductsCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodDairyProductsCurrency`")
        else:
            return v

        # validate data type: FoodFishProductsCurrency
        if not isinstance(v, FoodFishProductsCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodFishProductsCurrency`")
        else:
            return v

        # validate data type: FoodFoodProductsNotElsewhereSpecifiedCurrency
        if not isinstance(v, FoodFoodProductsNotElsewhereSpecifiedCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodFoodProductsNotElsewhereSpecifiedCurrency`")
        else:
            return v

        # validate data type: FoodMeatProductsBeefCurrency
        if not isinstance(v, FoodMeatProductsBeefCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodMeatProductsBeefCurrency`")
        else:
            return v

        # validate data type: FoodMeatProductsNotElsewhereSpecifiedCurrency
        if not isinstance(v, FoodMeatProductsNotElsewhereSpecifiedCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodMeatProductsNotElsewhereSpecifiedCurrency`")
        else:
            return v

        # validate data type: FoodMeatProductsPorkCurrency
        if not isinstance(v, FoodMeatProductsPorkCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodMeatProductsPorkCurrency`")
        else:
            return v

        # validate data type: FoodMeatProductsPoultryCurrency
        if not isinstance(v, FoodMeatProductsPoultryCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodMeatProductsPoultryCurrency`")
        else:
            return v

        # validate data type: FoodSugarCurrency
        if not isinstance(v, FoodSugarCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodSugarCurrency`")
        else:
            return v

        # validate data type: FoodProcessedRiceCurrency
        if not isinstance(v, FoodProcessedRiceCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodProcessedRiceCurrency`")
        else:
            return v

        # validate data type: FoodTobaccoProductsCurrency
        if not isinstance(v, FoodTobaccoProductsCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodTobaccoProductsCurrency`")
        else:
            return v

        # validate data type: FoodVegetableOilsAndFatsCurrency
        if not isinstance(v, FoodVegetableOilsAndFatsCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodVegetableOilsAndFatsCurrency`")
        else:
            return v

        # validate data type: FoodAverageCurrency
        if not isinstance(v, FoodAverageCurrency):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoodAverageCurrency`")
        else:
            return v

        # validate data type: EnergyConsumptionByTypeEnergy
        if not isinstance(v, EnergyConsumptionByTypeEnergy):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EnergyConsumptionByTypeEnergy`")
        else:
            return v

        # validate data type: EnergyConsumptionAverageEnergy
        if not isinstance(v, EnergyConsumptionAverageEnergy):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EnergyConsumptionAverageEnergy`")
        else:
            return v

        # validate data type: IndividualFactor
        if not isinstance(v, IndividualFactor):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IndividualFactor`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in PendingByCalculationRequestCalculationOptionsInner with anyOf schemas: BioenergyAverageEnergy, BioenergyAverageVolume, BioenergyAverageWeight, BioenergyBiofuelEnergy, BioenergyBiofuelVolume, BioenergyBiofuelWeight, BioenergyBiogasEnergy, BioenergyBiogasWeight, BioenergyBiomassEnergy, BioenergyBiomassWeight, CloudComputingAverageCpuHour, CloudComputingAverageGb, CloudComputingAverageGbHour, CloudComputingAverageTbHour, CloudComputingCpuCpuHour, CloudComputingMemoryGbHour, CloudComputingNetworkGb, CloudComputingStorageTbHour, EnergyConsumptionAverageEnergy, EnergyConsumptionByTypeEnergy, FoodAverageCurrency, FoodBeveragesCurrency, FoodDairyProductsCurrency, FoodFishProductsCurrency, FoodFoodProductsNotElsewhereSpecifiedCurrency, FoodMeatProductsBeefCurrency, FoodMeatProductsNotElsewhereSpecifiedCurrency, FoodMeatProductsPorkCurrency, FoodMeatProductsPoultryCurrency, FoodProcessedRiceCurrency, FoodSugarCurrency, FoodTobaccoProductsCurrency, FoodVegetableOilsAndFatsCurrency, FreightingGoodsAverageDepartureAndDestination, FreightingGoodsAverageDistance, FreightingGoodsAverageWeightAndDistance, FreightingGoodsCargoShipDepartureAndDestination, FreightingGoodsCargoShipWeightAndDistance, FreightingGoodsFreightFlightsDepartureAndDestination, FreightingGoodsFreightFlightsWeightAndDistance, FreightingGoodsHgvAllDieselDepartureAndDestination, FreightingGoodsHgvAllDieselDistance, FreightingGoodsHgvAllDieselWeightAndDistance, FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination, FreightingGoodsHgvRefrigeratedAllDieselDistance, FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance, FreightingGoodsRailDepartureAndDestination, FreightingGoodsRailWeightAndDistance, FreightingGoodsRoadDepartureAndDestination, FreightingGoodsRoadWeightAndDistance, FreightingGoodsSeaTankerDepartureAndDestination, FreightingGoodsSeaTankerWeightAndDistance, FreightingGoodsVansDepartureAndDestination, FreightingGoodsVansDistance, FreightingGoodsVansWeightAndDistance, FuelsAverageVolume, FuelsAverageWeight, FuelsGaseousFuelsVolume, FuelsGaseousFuelsWeight, FuelsLiquidFuelsVolume, FuelsLiquidFuelsWeight, FuelsSolidFuelsWeight, HeatAndSteamEnergy, HomeworkingPerFteWorkingHour, HotelStayRoomPerNight, IndividualFactor, InfrastructureAverageCurrency, InfrastructureRealEstateCurrency, MaterialUseAverageCurrency, MaterialUseAverageWeight, MaterialUseConstructionWeight, MaterialUseElectricalItemsWeight, MaterialUseElectronicsCurrency, MaterialUseFurnitureCurrency, MaterialUseMetalWeight, MaterialUseOrganicWeight, MaterialUseOtherWeight, MaterialUsePaperProductsCurrency, MaterialUsePaperWeight, MaterialUsePlasticWeight, MaterialUseTextilesCurrency, TravelAirAverageDepartureAndDestination, TravelAirAveragePassengerDistance, TravelAirFlightsDepartureAndDestination, TravelAirFlightsPassengerDistance, TravelLandAverageDepartureAndDestination, TravelLandAverageDistance, TravelLandAveragePassengerDistance, TravelLandBusDepartureAndDestination, TravelLandBusPassengerDistance, TravelLandCarsByMarketSegmentDepartureAndDestination, TravelLandCarsByMarketSegmentDistance, TravelLandCarsBySizeDepartureAndDestination, TravelLandCarsBySizeDistance, TravelLandFootBikeDepartureAndDestination, TravelLandFootBikePassengerDistance, TravelLandMotorbikeDepartureAndDestination, TravelLandMotorbikeDistance, TravelLandRailDepartureAndDestination, TravelLandRailPassengerDistance, TravelLandTaxisDepartureAndDestination, TravelLandTaxisDistance, TravelLandTaxisPassengerDistance, TravelSeaAverageDepartureAndDestination, TravelSeaAveragePassengerDistance, TravelSeaCruiseDays, TravelSeaFerryDepartureAndDestination, TravelSeaFerryPassengerDistance, WasteDisposalAverageWeight, WasteDisposalConstructionWeight, WasteDisposalElectricalItemsWeight, WasteDisposalMetalWeight, WasteDisposalOtherWeight, WasteDisposalPaperWeight, WasteDisposalPlasticWeight, WasteDisposalRefuseWeight, WaterSupplyVolume, WaterTreatmentVolume. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[FuelsGaseousFuelsWeight] = None
        try:
            instance.actual_instance = FuelsGaseousFuelsWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[FuelsGaseousFuelsVolume] = None
        try:
            instance.actual_instance = FuelsGaseousFuelsVolume.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[FuelsLiquidFuelsWeight] = None
        try:
            instance.actual_instance = FuelsLiquidFuelsWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[FuelsLiquidFuelsVolume] = None
        try:
            instance.actual_instance = FuelsLiquidFuelsVolume.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[FuelsSolidFuelsWeight] = None
        try:
            instance.actual_instance = FuelsSolidFuelsWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_6_validator: Optional[FuelsAverageWeight] = None
        try:
            instance.actual_instance = FuelsAverageWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_7_validator: Optional[FuelsAverageVolume] = None
        try:
            instance.actual_instance = FuelsAverageVolume.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_8_validator: Optional[BioenergyBiofuelVolume] = None
        try:
            instance.actual_instance = BioenergyBiofuelVolume.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_9_validator: Optional[BioenergyBiofuelEnergy] = None
        try:
            instance.actual_instance = BioenergyBiofuelEnergy.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_10_validator: Optional[BioenergyBiofuelWeight] = None
        try:
            instance.actual_instance = BioenergyBiofuelWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_11_validator: Optional[BioenergyBiomassWeight] = None
        try:
            instance.actual_instance = BioenergyBiomassWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_12_validator: Optional[BioenergyBiomassEnergy] = None
        try:
            instance.actual_instance = BioenergyBiomassEnergy.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_13_validator: Optional[BioenergyBiogasWeight] = None
        try:
            instance.actual_instance = BioenergyBiogasWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_14_validator: Optional[BioenergyBiogasEnergy] = None
        try:
            instance.actual_instance = BioenergyBiogasEnergy.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_15_validator: Optional[BioenergyAverageEnergy] = None
        try:
            instance.actual_instance = BioenergyAverageEnergy.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_16_validator: Optional[BioenergyAverageWeight] = None
        try:
            instance.actual_instance = BioenergyAverageWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_17_validator: Optional[BioenergyAverageVolume] = None
        try:
            instance.actual_instance = BioenergyAverageVolume.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_18_validator: Optional[HeatAndSteamEnergy] = None
        try:
            instance.actual_instance = HeatAndSteamEnergy.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_19_validator: Optional[WaterSupplyVolume] = None
        try:
            instance.actual_instance = WaterSupplyVolume.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_20_validator: Optional[WaterTreatmentVolume] = None
        try:
            instance.actual_instance = WaterTreatmentVolume.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_21_validator: Optional[MaterialUseConstructionWeight] = None
        try:
            instance.actual_instance = MaterialUseConstructionWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_22_validator: Optional[MaterialUseOtherWeight] = None
        try:
            instance.actual_instance = MaterialUseOtherWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_23_validator: Optional[MaterialUseOrganicWeight] = None
        try:
            instance.actual_instance = MaterialUseOrganicWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_24_validator: Optional[MaterialUseElectricalItemsWeight] = None
        try:
            instance.actual_instance = MaterialUseElectricalItemsWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_25_validator: Optional[MaterialUsePlasticWeight] = None
        try:
            instance.actual_instance = MaterialUsePlasticWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_26_validator: Optional[MaterialUseMetalWeight] = None
        try:
            instance.actual_instance = MaterialUseMetalWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_27_validator: Optional[MaterialUsePaperWeight] = None
        try:
            instance.actual_instance = MaterialUsePaperWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_28_validator: Optional[MaterialUseTextilesCurrency] = None
        try:
            instance.actual_instance = MaterialUseTextilesCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_29_validator: Optional[MaterialUseElectronicsCurrency] = None
        try:
            instance.actual_instance = MaterialUseElectronicsCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_30_validator: Optional[MaterialUsePaperProductsCurrency] = None
        try:
            instance.actual_instance = MaterialUsePaperProductsCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_31_validator: Optional[MaterialUseFurnitureCurrency] = None
        try:
            instance.actual_instance = MaterialUseFurnitureCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_32_validator: Optional[MaterialUseAverageCurrency] = None
        try:
            instance.actual_instance = MaterialUseAverageCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_33_validator: Optional[MaterialUseAverageWeight] = None
        try:
            instance.actual_instance = MaterialUseAverageWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_34_validator: Optional[WasteDisposalConstructionWeight] = None
        try:
            instance.actual_instance = WasteDisposalConstructionWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_35_validator: Optional[WasteDisposalOtherWeight] = None
        try:
            instance.actual_instance = WasteDisposalOtherWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_36_validator: Optional[WasteDisposalRefuseWeight] = None
        try:
            instance.actual_instance = WasteDisposalRefuseWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_37_validator: Optional[WasteDisposalElectricalItemsWeight] = None
        try:
            instance.actual_instance = WasteDisposalElectricalItemsWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_38_validator: Optional[WasteDisposalMetalWeight] = None
        try:
            instance.actual_instance = WasteDisposalMetalWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_39_validator: Optional[WasteDisposalPlasticWeight] = None
        try:
            instance.actual_instance = WasteDisposalPlasticWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_40_validator: Optional[WasteDisposalPaperWeight] = None
        try:
            instance.actual_instance = WasteDisposalPaperWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_41_validator: Optional[WasteDisposalAverageWeight] = None
        try:
            instance.actual_instance = WasteDisposalAverageWeight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_42_validator: Optional[HotelStayRoomPerNight] = None
        try:
            instance.actual_instance = HotelStayRoomPerNight.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_43_validator: Optional[TravelAirFlightsPassengerDistance] = None
        try:
            instance.actual_instance = TravelAirFlightsPassengerDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_44_validator: Optional[TravelAirFlightsDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelAirFlightsDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_45_validator: Optional[TravelAirAveragePassengerDistance] = None
        try:
            instance.actual_instance = TravelAirAveragePassengerDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_46_validator: Optional[TravelAirAverageDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelAirAverageDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_47_validator: Optional[TravelSeaFerryPassengerDistance] = None
        try:
            instance.actual_instance = TravelSeaFerryPassengerDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_48_validator: Optional[TravelSeaFerryDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelSeaFerryDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_49_validator: Optional[TravelSeaCruiseDays] = None
        try:
            instance.actual_instance = TravelSeaCruiseDays.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_50_validator: Optional[TravelSeaAveragePassengerDistance] = None
        try:
            instance.actual_instance = TravelSeaAveragePassengerDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_51_validator: Optional[TravelSeaAverageDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelSeaAverageDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_52_validator: Optional[TravelLandCarsByMarketSegmentDistance] = None
        try:
            instance.actual_instance = TravelLandCarsByMarketSegmentDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_53_validator: Optional[TravelLandCarsByMarketSegmentDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelLandCarsByMarketSegmentDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_54_validator: Optional[TravelLandTaxisPassengerDistance] = None
        try:
            instance.actual_instance = TravelLandTaxisPassengerDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_55_validator: Optional[TravelLandTaxisDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelLandTaxisDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_56_validator: Optional[TravelLandTaxisDistance] = None
        try:
            instance.actual_instance = TravelLandTaxisDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_57_validator: Optional[TravelLandCarsBySizeDistance] = None
        try:
            instance.actual_instance = TravelLandCarsBySizeDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_58_validator: Optional[TravelLandCarsBySizeDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelLandCarsBySizeDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_59_validator: Optional[TravelLandMotorbikeDistance] = None
        try:
            instance.actual_instance = TravelLandMotorbikeDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_60_validator: Optional[TravelLandMotorbikeDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelLandMotorbikeDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_61_validator: Optional[TravelLandBusPassengerDistance] = None
        try:
            instance.actual_instance = TravelLandBusPassengerDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_62_validator: Optional[TravelLandBusDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelLandBusDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_63_validator: Optional[TravelLandRailPassengerDistance] = None
        try:
            instance.actual_instance = TravelLandRailPassengerDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_64_validator: Optional[TravelLandRailDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelLandRailDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_65_validator: Optional[TravelLandFootBikePassengerDistance] = None
        try:
            instance.actual_instance = TravelLandFootBikePassengerDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_66_validator: Optional[TravelLandFootBikeDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelLandFootBikeDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_67_validator: Optional[TravelLandAverageDistance] = None
        try:
            instance.actual_instance = TravelLandAverageDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_68_validator: Optional[TravelLandAverageDepartureAndDestination] = None
        try:
            instance.actual_instance = TravelLandAverageDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_69_validator: Optional[TravelLandAveragePassengerDistance] = None
        try:
            instance.actual_instance = TravelLandAveragePassengerDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_70_validator: Optional[FreightingGoodsVansWeightAndDistance] = None
        try:
            instance.actual_instance = FreightingGoodsVansWeightAndDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_71_validator: Optional[FreightingGoodsVansDepartureAndDestination] = None
        try:
            instance.actual_instance = FreightingGoodsVansDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_72_validator: Optional[FreightingGoodsVansDistance] = None
        try:
            instance.actual_instance = FreightingGoodsVansDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_73_validator: Optional[FreightingGoodsHgvAllDieselWeightAndDistance] = None
        try:
            instance.actual_instance = FreightingGoodsHgvAllDieselWeightAndDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_74_validator: Optional[FreightingGoodsHgvAllDieselDepartureAndDestination] = None
        try:
            instance.actual_instance = FreightingGoodsHgvAllDieselDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_75_validator: Optional[FreightingGoodsHgvAllDieselDistance] = None
        try:
            instance.actual_instance = FreightingGoodsHgvAllDieselDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_76_validator: Optional[FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance] = None
        try:
            instance.actual_instance = FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_77_validator: Optional[FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination] = None
        try:
            instance.actual_instance = FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_78_validator: Optional[FreightingGoodsHgvRefrigeratedAllDieselDistance] = None
        try:
            instance.actual_instance = FreightingGoodsHgvRefrigeratedAllDieselDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_79_validator: Optional[FreightingGoodsFreightFlightsWeightAndDistance] = None
        try:
            instance.actual_instance = FreightingGoodsFreightFlightsWeightAndDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_80_validator: Optional[FreightingGoodsFreightFlightsDepartureAndDestination] = None
        try:
            instance.actual_instance = FreightingGoodsFreightFlightsDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_81_validator: Optional[FreightingGoodsRailWeightAndDistance] = None
        try:
            instance.actual_instance = FreightingGoodsRailWeightAndDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_82_validator: Optional[FreightingGoodsRailDepartureAndDestination] = None
        try:
            instance.actual_instance = FreightingGoodsRailDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_83_validator: Optional[FreightingGoodsSeaTankerWeightAndDistance] = None
        try:
            instance.actual_instance = FreightingGoodsSeaTankerWeightAndDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_84_validator: Optional[FreightingGoodsSeaTankerDepartureAndDestination] = None
        try:
            instance.actual_instance = FreightingGoodsSeaTankerDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_85_validator: Optional[FreightingGoodsCargoShipWeightAndDistance] = None
        try:
            instance.actual_instance = FreightingGoodsCargoShipWeightAndDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_86_validator: Optional[FreightingGoodsCargoShipDepartureAndDestination] = None
        try:
            instance.actual_instance = FreightingGoodsCargoShipDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_87_validator: Optional[FreightingGoodsRoadWeightAndDistance] = None
        try:
            instance.actual_instance = FreightingGoodsRoadWeightAndDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_88_validator: Optional[FreightingGoodsRoadDepartureAndDestination] = None
        try:
            instance.actual_instance = FreightingGoodsRoadDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_89_validator: Optional[FreightingGoodsAverageWeightAndDistance] = None
        try:
            instance.actual_instance = FreightingGoodsAverageWeightAndDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_90_validator: Optional[FreightingGoodsAverageDepartureAndDestination] = None
        try:
            instance.actual_instance = FreightingGoodsAverageDepartureAndDestination.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_91_validator: Optional[FreightingGoodsAverageDistance] = None
        try:
            instance.actual_instance = FreightingGoodsAverageDistance.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_92_validator: Optional[HomeworkingPerFteWorkingHour] = None
        try:
            instance.actual_instance = HomeworkingPerFteWorkingHour.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_93_validator: Optional[InfrastructureRealEstateCurrency] = None
        try:
            instance.actual_instance = InfrastructureRealEstateCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_94_validator: Optional[InfrastructureAverageCurrency] = None
        try:
            instance.actual_instance = InfrastructureAverageCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_95_validator: Optional[CloudComputingCpuCpuHour] = None
        try:
            instance.actual_instance = CloudComputingCpuCpuHour.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_96_validator: Optional[CloudComputingMemoryGbHour] = None
        try:
            instance.actual_instance = CloudComputingMemoryGbHour.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_97_validator: Optional[CloudComputingNetworkGb] = None
        try:
            instance.actual_instance = CloudComputingNetworkGb.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_98_validator: Optional[CloudComputingStorageTbHour] = None
        try:
            instance.actual_instance = CloudComputingStorageTbHour.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_99_validator: Optional[CloudComputingAverageTbHour] = None
        try:
            instance.actual_instance = CloudComputingAverageTbHour.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_100_validator: Optional[CloudComputingAverageGb] = None
        try:
            instance.actual_instance = CloudComputingAverageGb.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_101_validator: Optional[CloudComputingAverageGbHour] = None
        try:
            instance.actual_instance = CloudComputingAverageGbHour.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_102_validator: Optional[CloudComputingAverageCpuHour] = None
        try:
            instance.actual_instance = CloudComputingAverageCpuHour.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_103_validator: Optional[FoodBeveragesCurrency] = None
        try:
            instance.actual_instance = FoodBeveragesCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_104_validator: Optional[FoodDairyProductsCurrency] = None
        try:
            instance.actual_instance = FoodDairyProductsCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_105_validator: Optional[FoodFishProductsCurrency] = None
        try:
            instance.actual_instance = FoodFishProductsCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_106_validator: Optional[FoodFoodProductsNotElsewhereSpecifiedCurrency] = None
        try:
            instance.actual_instance = FoodFoodProductsNotElsewhereSpecifiedCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_107_validator: Optional[FoodMeatProductsBeefCurrency] = None
        try:
            instance.actual_instance = FoodMeatProductsBeefCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_108_validator: Optional[FoodMeatProductsNotElsewhereSpecifiedCurrency] = None
        try:
            instance.actual_instance = FoodMeatProductsNotElsewhereSpecifiedCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_109_validator: Optional[FoodMeatProductsPorkCurrency] = None
        try:
            instance.actual_instance = FoodMeatProductsPorkCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_110_validator: Optional[FoodMeatProductsPoultryCurrency] = None
        try:
            instance.actual_instance = FoodMeatProductsPoultryCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_111_validator: Optional[FoodSugarCurrency] = None
        try:
            instance.actual_instance = FoodSugarCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_112_validator: Optional[FoodProcessedRiceCurrency] = None
        try:
            instance.actual_instance = FoodProcessedRiceCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_113_validator: Optional[FoodTobaccoProductsCurrency] = None
        try:
            instance.actual_instance = FoodTobaccoProductsCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_114_validator: Optional[FoodVegetableOilsAndFatsCurrency] = None
        try:
            instance.actual_instance = FoodVegetableOilsAndFatsCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_115_validator: Optional[FoodAverageCurrency] = None
        try:
            instance.actual_instance = FoodAverageCurrency.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_116_validator: Optional[EnergyConsumptionByTypeEnergy] = None
        try:
            instance.actual_instance = EnergyConsumptionByTypeEnergy.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_117_validator: Optional[EnergyConsumptionAverageEnergy] = None
        try:
            instance.actual_instance = EnergyConsumptionAverageEnergy.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_118_validator: Optional[IndividualFactor] = None
        try:
            instance.actual_instance = IndividualFactor.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PendingByCalculationRequestCalculationOptionsInner with anyOf schemas: BioenergyAverageEnergy, BioenergyAverageVolume, BioenergyAverageWeight, BioenergyBiofuelEnergy, BioenergyBiofuelVolume, BioenergyBiofuelWeight, BioenergyBiogasEnergy, BioenergyBiogasWeight, BioenergyBiomassEnergy, BioenergyBiomassWeight, CloudComputingAverageCpuHour, CloudComputingAverageGb, CloudComputingAverageGbHour, CloudComputingAverageTbHour, CloudComputingCpuCpuHour, CloudComputingMemoryGbHour, CloudComputingNetworkGb, CloudComputingStorageTbHour, EnergyConsumptionAverageEnergy, EnergyConsumptionByTypeEnergy, FoodAverageCurrency, FoodBeveragesCurrency, FoodDairyProductsCurrency, FoodFishProductsCurrency, FoodFoodProductsNotElsewhereSpecifiedCurrency, FoodMeatProductsBeefCurrency, FoodMeatProductsNotElsewhereSpecifiedCurrency, FoodMeatProductsPorkCurrency, FoodMeatProductsPoultryCurrency, FoodProcessedRiceCurrency, FoodSugarCurrency, FoodTobaccoProductsCurrency, FoodVegetableOilsAndFatsCurrency, FreightingGoodsAverageDepartureAndDestination, FreightingGoodsAverageDistance, FreightingGoodsAverageWeightAndDistance, FreightingGoodsCargoShipDepartureAndDestination, FreightingGoodsCargoShipWeightAndDistance, FreightingGoodsFreightFlightsDepartureAndDestination, FreightingGoodsFreightFlightsWeightAndDistance, FreightingGoodsHgvAllDieselDepartureAndDestination, FreightingGoodsHgvAllDieselDistance, FreightingGoodsHgvAllDieselWeightAndDistance, FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination, FreightingGoodsHgvRefrigeratedAllDieselDistance, FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance, FreightingGoodsRailDepartureAndDestination, FreightingGoodsRailWeightAndDistance, FreightingGoodsRoadDepartureAndDestination, FreightingGoodsRoadWeightAndDistance, FreightingGoodsSeaTankerDepartureAndDestination, FreightingGoodsSeaTankerWeightAndDistance, FreightingGoodsVansDepartureAndDestination, FreightingGoodsVansDistance, FreightingGoodsVansWeightAndDistance, FuelsAverageVolume, FuelsAverageWeight, FuelsGaseousFuelsVolume, FuelsGaseousFuelsWeight, FuelsLiquidFuelsVolume, FuelsLiquidFuelsWeight, FuelsSolidFuelsWeight, HeatAndSteamEnergy, HomeworkingPerFteWorkingHour, HotelStayRoomPerNight, IndividualFactor, InfrastructureAverageCurrency, InfrastructureRealEstateCurrency, MaterialUseAverageCurrency, MaterialUseAverageWeight, MaterialUseConstructionWeight, MaterialUseElectricalItemsWeight, MaterialUseElectronicsCurrency, MaterialUseFurnitureCurrency, MaterialUseMetalWeight, MaterialUseOrganicWeight, MaterialUseOtherWeight, MaterialUsePaperProductsCurrency, MaterialUsePaperWeight, MaterialUsePlasticWeight, MaterialUseTextilesCurrency, TravelAirAverageDepartureAndDestination, TravelAirAveragePassengerDistance, TravelAirFlightsDepartureAndDestination, TravelAirFlightsPassengerDistance, TravelLandAverageDepartureAndDestination, TravelLandAverageDistance, TravelLandAveragePassengerDistance, TravelLandBusDepartureAndDestination, TravelLandBusPassengerDistance, TravelLandCarsByMarketSegmentDepartureAndDestination, TravelLandCarsByMarketSegmentDistance, TravelLandCarsBySizeDepartureAndDestination, TravelLandCarsBySizeDistance, TravelLandFootBikeDepartureAndDestination, TravelLandFootBikePassengerDistance, TravelLandMotorbikeDepartureAndDestination, TravelLandMotorbikeDistance, TravelLandRailDepartureAndDestination, TravelLandRailPassengerDistance, TravelLandTaxisDepartureAndDestination, TravelLandTaxisDistance, TravelLandTaxisPassengerDistance, TravelSeaAverageDepartureAndDestination, TravelSeaAveragePassengerDistance, TravelSeaCruiseDays, TravelSeaFerryDepartureAndDestination, TravelSeaFerryPassengerDistance, WasteDisposalAverageWeight, WasteDisposalConstructionWeight, WasteDisposalElectricalItemsWeight, WasteDisposalMetalWeight, WasteDisposalOtherWeight, WasteDisposalPaperWeight, WasteDisposalPlasticWeight, WasteDisposalRefuseWeight, WaterSupplyVolume, WaterTreatmentVolume. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], BioenergyAverageEnergy, BioenergyAverageVolume, BioenergyAverageWeight, BioenergyBiofuelEnergy, BioenergyBiofuelVolume, BioenergyBiofuelWeight, BioenergyBiogasEnergy, BioenergyBiogasWeight, BioenergyBiomassEnergy, BioenergyBiomassWeight, CloudComputingAverageCpuHour, CloudComputingAverageGb, CloudComputingAverageGbHour, CloudComputingAverageTbHour, CloudComputingCpuCpuHour, CloudComputingMemoryGbHour, CloudComputingNetworkGb, CloudComputingStorageTbHour, EnergyConsumptionAverageEnergy, EnergyConsumptionByTypeEnergy, FoodAverageCurrency, FoodBeveragesCurrency, FoodDairyProductsCurrency, FoodFishProductsCurrency, FoodFoodProductsNotElsewhereSpecifiedCurrency, FoodMeatProductsBeefCurrency, FoodMeatProductsNotElsewhereSpecifiedCurrency, FoodMeatProductsPorkCurrency, FoodMeatProductsPoultryCurrency, FoodProcessedRiceCurrency, FoodSugarCurrency, FoodTobaccoProductsCurrency, FoodVegetableOilsAndFatsCurrency, FreightingGoodsAverageDepartureAndDestination, FreightingGoodsAverageDistance, FreightingGoodsAverageWeightAndDistance, FreightingGoodsCargoShipDepartureAndDestination, FreightingGoodsCargoShipWeightAndDistance, FreightingGoodsFreightFlightsDepartureAndDestination, FreightingGoodsFreightFlightsWeightAndDistance, FreightingGoodsHgvAllDieselDepartureAndDestination, FreightingGoodsHgvAllDieselDistance, FreightingGoodsHgvAllDieselWeightAndDistance, FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination, FreightingGoodsHgvRefrigeratedAllDieselDistance, FreightingGoodsHgvRefrigeratedAllDieselWeightAndDistance, FreightingGoodsRailDepartureAndDestination, FreightingGoodsRailWeightAndDistance, FreightingGoodsRoadDepartureAndDestination, FreightingGoodsRoadWeightAndDistance, FreightingGoodsSeaTankerDepartureAndDestination, FreightingGoodsSeaTankerWeightAndDistance, FreightingGoodsVansDepartureAndDestination, FreightingGoodsVansDistance, FreightingGoodsVansWeightAndDistance, FuelsAverageVolume, FuelsAverageWeight, FuelsGaseousFuelsVolume, FuelsGaseousFuelsWeight, FuelsLiquidFuelsVolume, FuelsLiquidFuelsWeight, FuelsSolidFuelsWeight, HeatAndSteamEnergy, HomeworkingPerFteWorkingHour, HotelStayRoomPerNight, IndividualFactor, InfrastructureAverageCurrency, InfrastructureRealEstateCurrency, MaterialUseAverageCurrency, MaterialUseAverageWeight, MaterialUseConstructionWeight, MaterialUseElectricalItemsWeight, MaterialUseElectronicsCurrency, MaterialUseFurnitureCurrency, MaterialUseMetalWeight, MaterialUseOrganicWeight, MaterialUseOtherWeight, MaterialUsePaperProductsCurrency, MaterialUsePaperWeight, MaterialUsePlasticWeight, MaterialUseTextilesCurrency, TravelAirAverageDepartureAndDestination, TravelAirAveragePassengerDistance, TravelAirFlightsDepartureAndDestination, TravelAirFlightsPassengerDistance, TravelLandAverageDepartureAndDestination, TravelLandAverageDistance, TravelLandAveragePassengerDistance, TravelLandBusDepartureAndDestination, TravelLandBusPassengerDistance, TravelLandCarsByMarketSegmentDepartureAndDestination, TravelLandCarsByMarketSegmentDistance, TravelLandCarsBySizeDepartureAndDestination, TravelLandCarsBySizeDistance, TravelLandFootBikeDepartureAndDestination, TravelLandFootBikePassengerDistance, TravelLandMotorbikeDepartureAndDestination, TravelLandMotorbikeDistance, TravelLandRailDepartureAndDestination, TravelLandRailPassengerDistance, TravelLandTaxisDepartureAndDestination, TravelLandTaxisDistance, TravelLandTaxisPassengerDistance, TravelSeaAverageDepartureAndDestination, TravelSeaAveragePassengerDistance, TravelSeaCruiseDays, TravelSeaFerryDepartureAndDestination, TravelSeaFerryPassengerDistance, WasteDisposalAverageWeight, WasteDisposalConstructionWeight, WasteDisposalElectricalItemsWeight, WasteDisposalMetalWeight, WasteDisposalOtherWeight, WasteDisposalPaperWeight, WasteDisposalPlasticWeight, WasteDisposalRefuseWeight, WaterSupplyVolume, WaterTreatmentVolume]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


