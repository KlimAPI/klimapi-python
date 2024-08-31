# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.travel_air_flights_departure_and_destination import TravelAirFlightsDepartureAndDestination

class TestTravelAirFlightsDepartureAndDestination(unittest.TestCase):
    """TravelAirFlightsDepartureAndDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelAirFlightsDepartureAndDestination:
        """Test TravelAirFlightsDepartureAndDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TravelAirFlightsDepartureAndDestination`
        """
        model = TravelAirFlightsDepartureAndDestination()
        if include_optional:
            return TravelAirFlightsDepartureAndDestination(
                type = 'travel-air',
                activity = 'flights',
                specification = 'average',
                detail = 'average',
                departure = '',
                destination = '',
                return_trip = True,
                passengers = 56
            )
        else:
            return TravelAirFlightsDepartureAndDestination(
                type = 'travel-air',
                departure = '',
                destination = '',
        )
        """

    def testTravelAirFlightsDepartureAndDestination(self):
        """Test TravelAirFlightsDepartureAndDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
