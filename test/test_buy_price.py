# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.buy_price import BuyPrice

class TestBuyPrice(unittest.TestCase):
    """BuyPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BuyPrice:
        """Test BuyPrice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuyPrice`
        """
        model = BuyPrice()
        if include_optional:
            return BuyPrice(
                price_amount = 0.5,
                recipient_name = '',
                recipient_email = '',
                send_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                metadata = {
                    'key' : ''
                    }
            )
        else:
            return BuyPrice(
                price_amount = 0.5,
                recipient_name = '',
        )
        """

    def testBuyPrice(self):
        """Test BuyPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
