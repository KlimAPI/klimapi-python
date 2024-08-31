# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.travel_land_rail_departure_and_destination import TravelLandRailDepartureAndDestination

class TestTravelLandRailDepartureAndDestination(unittest.TestCase):
    """TravelLandRailDepartureAndDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelLandRailDepartureAndDestination:
        """Test TravelLandRailDepartureAndDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TravelLandRailDepartureAndDestination`
        """
        model = TravelLandRailDepartureAndDestination()
        if include_optional:
            return TravelLandRailDepartureAndDestination(
                type = 'travel-land',
                activity = 'rail',
                specification = 'average',
                departure = '',
                destination = '',
                return_trip = True,
                passengers = 56
            )
        else:
            return TravelLandRailDepartureAndDestination(
                type = 'travel-land',
                departure = '',
                destination = '',
        )
        """

    def testTravelLandRailDepartureAndDestination(self):
        """Test TravelLandRailDepartureAndDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
