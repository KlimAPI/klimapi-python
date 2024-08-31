# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.freighting_goods_cargo_ship_departure_and_destination import FreightingGoodsCargoShipDepartureAndDestination

class TestFreightingGoodsCargoShipDepartureAndDestination(unittest.TestCase):
    """FreightingGoodsCargoShipDepartureAndDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FreightingGoodsCargoShipDepartureAndDestination:
        """Test FreightingGoodsCargoShipDepartureAndDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FreightingGoodsCargoShipDepartureAndDestination`
        """
        model = FreightingGoodsCargoShipDepartureAndDestination()
        if include_optional:
            return FreightingGoodsCargoShipDepartureAndDestination(
                type = 'freighting_goods',
                activity = 'cargo_ship',
                specification = 'average',
                detail = 'average',
                departure = '',
                destination = '',
                return_trip = True,
                weight = 1.337,
                weight_unit = 'metric tons'
            )
        else:
            return FreightingGoodsCargoShipDepartureAndDestination(
                type = 'freighting_goods',
                departure = '',
                destination = '',
        )
        """

    def testFreightingGoodsCargoShipDepartureAndDestination(self):
        """Test FreightingGoodsCargoShipDepartureAndDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
