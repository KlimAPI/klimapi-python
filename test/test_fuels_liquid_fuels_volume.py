# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.fuels_liquid_fuels_volume import FuelsLiquidFuelsVolume

class TestFuelsLiquidFuelsVolume(unittest.TestCase):
    """FuelsLiquidFuelsVolume unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FuelsLiquidFuelsVolume:
        """Test FuelsLiquidFuelsVolume
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FuelsLiquidFuelsVolume`
        """
        model = FuelsLiquidFuelsVolume()
        if include_optional:
            return FuelsLiquidFuelsVolume(
                type = 'fuels',
                activity = 'liquid_fuels',
                specification = 'average',
                value = 1.337,
                unit = 'cubic meters'
            )
        else:
            return FuelsLiquidFuelsVolume(
                type = 'fuels',
                value = 1.337,
        )
        """

    def testFuelsLiquidFuelsVolume(self):
        """Test FuelsLiquidFuelsVolume"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
