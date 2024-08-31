# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.fuels_gaseous_fuels_weight import FuelsGaseousFuelsWeight

class TestFuelsGaseousFuelsWeight(unittest.TestCase):
    """FuelsGaseousFuelsWeight unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FuelsGaseousFuelsWeight:
        """Test FuelsGaseousFuelsWeight
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FuelsGaseousFuelsWeight`
        """
        model = FuelsGaseousFuelsWeight()
        if include_optional:
            return FuelsGaseousFuelsWeight(
                type = 'fuels',
                activity = 'gaseous_fuels',
                specification = 'average',
                value = 1.337,
                unit = 'metric tons'
            )
        else:
            return FuelsGaseousFuelsWeight(
                type = 'fuels',
                value = 1.337,
        )
        """

    def testFuelsGaseousFuelsWeight(self):
        """Test FuelsGaseousFuelsWeight"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
