# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.buy_amount import BuyAmount

class TestBuyAmount(unittest.TestCase):
    """BuyAmount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BuyAmount:
        """Test BuyAmount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuyAmount`
        """
        model = BuyAmount()
        if include_optional:
            return BuyAmount(
                kg_co2e = 56,
                recipient_name = '',
                recipient_email = '',
                send_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                price_limit = 0.5,
                metadata = {
                    'key' : ''
                    }
            )
        else:
            return BuyAmount(
                kg_co2e = 56,
                recipient_name = '',
        )
        """

    def testBuyAmount(self):
        """Test BuyAmount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
