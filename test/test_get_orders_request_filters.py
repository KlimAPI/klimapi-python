# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.get_orders_request_filters import GetOrdersRequestFilters

class TestGetOrdersRequestFilters(unittest.TestCase):
    """GetOrdersRequestFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetOrdersRequestFilters:
        """Test GetOrdersRequestFilters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetOrdersRequestFilters`
        """
        model = GetOrdersRequestFilters()
        if include_optional:
            return GetOrdersRequestFilters(
                metadata = {
                    'key' : ''
                    },
                status = 'processed',
                recipient_name = '',
                recipient_email = '',
                price = 1.337,
                currency = 'EUR',
                kg_co2e = 56
            )
        else:
            return GetOrdersRequestFilters(
        )
        """

    def testGetOrdersRequestFilters(self):
        """Test GetOrdersRequestFilters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
