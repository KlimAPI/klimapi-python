# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.api.klim_api import KlimApi


class TestKlimApi(unittest.TestCase):
    """KlimApi unit test stubs"""

    def setUp(self) -> None:
        self.api = KlimApi()

    def tearDown(self) -> None:
        pass

    def test_add_webhook(self) -> None:
        """Test case for add_webhook

        Add Webhook
        """
        pass

    def test_calculate(self) -> None:
        """Test case for calculate

        Calculate
        """
        pass

    def test_calculate_cart(self) -> None:
        """Test case for calculate_cart

        Calculate
        """
        pass

    def test_get_categories(self) -> None:
        """Test case for get_categories

        Get all Categories
        """
        pass

    def test_get_certification_authorities(self) -> None:
        """Test case for get_certification_authorities

        Get all Certification Authorities
        """
        pass

    def test_get_metrics(self) -> None:
        """Test case for get_metrics

        Order Metrics
        """
        pass

    def test_get_order(self) -> None:
        """Test case for get_order

        Get Order
        """
        pass

    def test_get_orders(self) -> None:
        """Test case for get_orders

        Get Orders
        """
        pass

    def test_get_payment_link(self) -> None:
        """Test case for get_payment_link

        Get Checkout Link
        """
        pass

    def test_get_project(self) -> None:
        """Test case for get_project

        Get Project
        """
        pass

    def test_get_projects(self) -> None:
        """Test case for get_projects

        Get all supported Projects
        """
        pass

    def test_link_by_calculation(self) -> None:
        """Test case for link_by_calculation

        By calculation
        """
        pass

    def test_link_by_carbon(self) -> None:
        """Test case for link_by_carbon

        By carbon
        """
        pass

    def test_link_by_price(self) -> None:
        """Test case for link_by_price

        By price
        """
        pass

    def test_me(self) -> None:
        """Test case for me

        Get Authenticated User
        """
        pass

    def test_order_by_calculation(self) -> None:
        """Test case for order_by_calculation

        By calculation
        """
        pass

    def test_order_by_carbon(self) -> None:
        """Test case for order_by_carbon

        By carbon
        """
        pass

    def test_order_by_price(self) -> None:
        """Test case for order_by_price

        By price
        """
        pass

    def test_pending_by_calculation(self) -> None:
        """Test case for pending_by_calculation

        By calculation
        """
        pass

    def test_pending_by_carbon(self) -> None:
        """Test case for pending_by_carbon

        By carbon
        """
        pass

    def test_pending_by_price(self) -> None:
        """Test case for pending_by_price

        By price
        """
        pass

    def test_process(self) -> None:
        """Test case for process

        Process pending Order
        """
        pass

    def test_process_cart(self) -> None:
        """Test case for process_cart

        Process cart
        """
        pass

    def test_refund(self) -> None:
        """Test case for refund

        Refund Order
        """
        pass

    def test_remove_webhook(self) -> None:
        """Test case for remove_webhook

        Remove Webhook
        """
        pass

    def test_sync_bulk_store(self) -> None:
        """Test case for sync_bulk_store

        Sync multiple Products
        """
        pass

    def test_sync_store(self) -> None:
        """Test case for sync_store

        Sync a single Product
        """
        pass


if __name__ == '__main__':
    unittest.main()
