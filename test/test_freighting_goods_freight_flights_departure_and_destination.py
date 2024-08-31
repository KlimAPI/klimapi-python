# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.freighting_goods_freight_flights_departure_and_destination import FreightingGoodsFreightFlightsDepartureAndDestination

class TestFreightingGoodsFreightFlightsDepartureAndDestination(unittest.TestCase):
    """FreightingGoodsFreightFlightsDepartureAndDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FreightingGoodsFreightFlightsDepartureAndDestination:
        """Test FreightingGoodsFreightFlightsDepartureAndDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FreightingGoodsFreightFlightsDepartureAndDestination`
        """
        model = FreightingGoodsFreightFlightsDepartureAndDestination()
        if include_optional:
            return FreightingGoodsFreightFlightsDepartureAndDestination(
                type = 'freighting_goods',
                activity = 'freight_flights',
                specification = 'average',
                departure = '',
                destination = '',
                return_trip = True,
                weight = 1.337,
                weight_unit = 'metric tons'
            )
        else:
            return FreightingGoodsFreightFlightsDepartureAndDestination(
                type = 'freighting_goods',
                departure = '',
                destination = '',
        )
        """

    def testFreightingGoodsFreightFlightsDepartureAndDestination(self):
        """Test FreightingGoodsFreightFlightsDepartureAndDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
