# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.heat_and_steam_energy import HeatAndSteamEnergy

class TestHeatAndSteamEnergy(unittest.TestCase):
    """HeatAndSteamEnergy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HeatAndSteamEnergy:
        """Test HeatAndSteamEnergy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HeatAndSteamEnergy`
        """
        model = HeatAndSteamEnergy()
        if include_optional:
            return HeatAndSteamEnergy(
                type = 'heat_and_steam',
                activity = 'average',
                value = 1.337,
                unit = 'kWh'
            )
        else:
            return HeatAndSteamEnergy(
                type = 'heat_and_steam',
                value = 1.337,
        )
        """

    def testHeatAndSteamEnergy(self):
        """Test HeatAndSteamEnergy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
