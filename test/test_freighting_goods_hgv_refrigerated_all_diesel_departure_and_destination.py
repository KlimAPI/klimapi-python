# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.freighting_goods_hgv_refrigerated_all_diesel_departure_and_destination import FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination

class TestFreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination(unittest.TestCase):
    """FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination:
        """Test FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination`
        """
        model = FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination()
        if include_optional:
            return FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination(
                type = 'freighting_goods',
                activity = 'hgv_refrigerated_all_diesel',
                specification = 'average',
                detail = 'average',
                departure = '',
                destination = '',
                return_trip = True
            )
        else:
            return FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination(
                type = 'freighting_goods',
                departure = '',
                destination = '',
        )
        """

    def testFreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination(self):
        """Test FreightingGoodsHgvRefrigeratedAllDieselDepartureAndDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
