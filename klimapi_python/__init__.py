# coding: utf-8

# flake8: noqa

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.1.27"

# import apis into sdk package
from klimapi_python.api.klim_api import KlimApi

# import ApiClient
from klimapi_python.api_response import ApiResponse
from klimapi_python.api_client import ApiClient
from klimapi_python.configuration import Configuration
from klimapi_python.exceptions import OpenApiException
from klimapi_python.exceptions import ApiTypeError
from klimapi_python.exceptions import ApiValueError
from klimapi_python.exceptions import ApiKeyError
from klimapi_python.exceptions import ApiAttributeError
from klimapi_python.exceptions import ApiException

# import models into sdk package
from klimapi_python.models.add_webhook_request import AddWebhookRequest
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
from klimapi_python.models.get_metrics_request import GetMetricsRequest
from klimapi_python.models.get_orders_request import GetOrdersRequest
from klimapi_python.models.get_orders_request_filters import GetOrdersRequestFilters
from klimapi_python.models.link_by_calculation_request import LinkByCalculationRequest
from klimapi_python.models.link_by_carbon_request import LinkByCarbonRequest
from klimapi_python.models.link_by_price_request import LinkByPriceRequest
from klimapi_python.models.metadata_orders import MetadataOrders
from klimapi_python.models.order import Order
from klimapi_python.models.order_by_calculation_request import OrderByCalculationRequest
from klimapi_python.models.order_calculated import OrderCalculated
from klimapi_python.models.order_metrics import OrderMetrics
from klimapi_python.models.order_recipient import OrderRecipient
from klimapi_python.models.pending_by_calculation_request import PendingByCalculationRequest
from klimapi_python.models.pending_by_carbon_request import PendingByCarbonRequest
from klimapi_python.models.pending_by_price_request import PendingByPriceRequest
from klimapi_python.models.pending_order import PendingOrder
from klimapi_python.models.pending_order_calculated import PendingOrderCalculated
from klimapi_python.models.pending_orders import PendingOrders
from klimapi_python.models.pending_orders_calculated import PendingOrdersCalculated
from klimapi_python.models.process_order import ProcessOrder
from klimapi_python.models.product import Product
from klimapi_python.models.project import Project
