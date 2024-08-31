# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.travel_land_foot_bike_departure_and_destination import TravelLandFootBikeDepartureAndDestination

class TestTravelLandFootBikeDepartureAndDestination(unittest.TestCase):
    """TravelLandFootBikeDepartureAndDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelLandFootBikeDepartureAndDestination:
        """Test TravelLandFootBikeDepartureAndDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TravelLandFootBikeDepartureAndDestination`
        """
        model = TravelLandFootBikeDepartureAndDestination()
        if include_optional:
            return TravelLandFootBikeDepartureAndDestination(
                type = 'travel-land',
                activity = 'foot_bike',
                departure = '',
                destination = '',
                return_trip = True,
                passengers = 56
            )
        else:
            return TravelLandFootBikeDepartureAndDestination(
                type = 'travel-land',
                departure = '',
                destination = '',
        )
        """

    def testTravelLandFootBikeDepartureAndDestination(self):
        """Test TravelLandFootBikeDepartureAndDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
