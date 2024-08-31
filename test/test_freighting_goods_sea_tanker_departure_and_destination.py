# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.freighting_goods_sea_tanker_departure_and_destination import FreightingGoodsSeaTankerDepartureAndDestination

class TestFreightingGoodsSeaTankerDepartureAndDestination(unittest.TestCase):
    """FreightingGoodsSeaTankerDepartureAndDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FreightingGoodsSeaTankerDepartureAndDestination:
        """Test FreightingGoodsSeaTankerDepartureAndDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FreightingGoodsSeaTankerDepartureAndDestination`
        """
        model = FreightingGoodsSeaTankerDepartureAndDestination()
        if include_optional:
            return FreightingGoodsSeaTankerDepartureAndDestination(
                type = 'freighting_goods',
                activity = 'sea_tanker',
                specification = 'average',
                detail = 'average',
                departure = '',
                destination = '',
                return_trip = True,
                weight = 1.337,
                weight_unit = 'metric tons'
            )
        else:
            return FreightingGoodsSeaTankerDepartureAndDestination(
                type = 'freighting_goods',
                departure = '',
                destination = '',
        )
        """

    def testFreightingGoodsSeaTankerDepartureAndDestination(self):
        """Test FreightingGoodsSeaTankerDepartureAndDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
