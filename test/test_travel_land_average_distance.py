# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.travel_land_average_distance import TravelLandAverageDistance

class TestTravelLandAverageDistance(unittest.TestCase):
    """TravelLandAverageDistance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelLandAverageDistance:
        """Test TravelLandAverageDistance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TravelLandAverageDistance`
        """
        model = TravelLandAverageDistance()
        if include_optional:
            return TravelLandAverageDistance(
                type = 'travel-land',
                value = 1.337,
                unit = 'kilometers'
            )
        else:
            return TravelLandAverageDistance(
                type = 'travel-land',
                value = 1.337,
        )
        """

    def testTravelLandAverageDistance(self):
        """Test TravelLandAverageDistance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
