# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.travel_land_motorbike_distance import TravelLandMotorbikeDistance

class TestTravelLandMotorbikeDistance(unittest.TestCase):
    """TravelLandMotorbikeDistance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelLandMotorbikeDistance:
        """Test TravelLandMotorbikeDistance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TravelLandMotorbikeDistance`
        """
        model = TravelLandMotorbikeDistance()
        if include_optional:
            return TravelLandMotorbikeDistance(
                type = 'travel-land',
                activity = 'motorbike',
                specification = 'average',
                value = 1.337,
                unit = 'kilometers'
            )
        else:
            return TravelLandMotorbikeDistance(
                type = 'travel-land',
                value = 1.337,
        )
        """

    def testTravelLandMotorbikeDistance(self):
        """Test TravelLandMotorbikeDistance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
