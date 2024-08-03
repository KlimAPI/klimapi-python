# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.link_by_price_request import LinkByPriceRequest

class TestLinkByPriceRequest(unittest.TestCase):
    """LinkByPriceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkByPriceRequest:
        """Test LinkByPriceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinkByPriceRequest`
        """
        model = LinkByPriceRequest()
        if include_optional:
            return LinkByPriceRequest(
                price_amount = 0.5,
                change_allowed = True,
                success_url = '',
                cancel_url = '',
                order_count = 1,
                metadata = {
                    'key' : ''
                    }
            )
        else:
            return LinkByPriceRequest(
                price_amount = 0.5,
                success_url = '',
                cancel_url = '',
        )
        """

    def testLinkByPriceRequest(self):
        """Test LinkByPriceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
