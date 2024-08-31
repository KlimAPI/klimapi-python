# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.travel_land_cars_by_size_departure_and_destination import TravelLandCarsBySizeDepartureAndDestination

class TestTravelLandCarsBySizeDepartureAndDestination(unittest.TestCase):
    """TravelLandCarsBySizeDepartureAndDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelLandCarsBySizeDepartureAndDestination:
        """Test TravelLandCarsBySizeDepartureAndDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TravelLandCarsBySizeDepartureAndDestination`
        """
        model = TravelLandCarsBySizeDepartureAndDestination()
        if include_optional:
            return TravelLandCarsBySizeDepartureAndDestination(
                type = 'travel-land',
                activity = 'cars_by_size',
                specification = 'average',
                detail = 'average',
                departure = '',
                destination = '',
                return_trip = True
            )
        else:
            return TravelLandCarsBySizeDepartureAndDestination(
                type = 'travel-land',
                departure = '',
                destination = '',
        )
        """

    def testTravelLandCarsBySizeDepartureAndDestination(self):
        """Test TravelLandCarsBySizeDepartureAndDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
