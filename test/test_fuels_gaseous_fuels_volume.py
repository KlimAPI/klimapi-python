# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.fuels_gaseous_fuels_volume import FuelsGaseousFuelsVolume

class TestFuelsGaseousFuelsVolume(unittest.TestCase):
    """FuelsGaseousFuelsVolume unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FuelsGaseousFuelsVolume:
        """Test FuelsGaseousFuelsVolume
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FuelsGaseousFuelsVolume`
        """
        model = FuelsGaseousFuelsVolume()
        if include_optional:
            return FuelsGaseousFuelsVolume(
                type = 'fuels',
                activity = 'gaseous_fuels',
                specification = 'average',
                value = 1.337,
                unit = 'cubic meters'
            )
        else:
            return FuelsGaseousFuelsVolume(
                type = 'fuels',
                value = 1.337,
        )
        """

    def testFuelsGaseousFuelsVolume(self):
        """Test FuelsGaseousFuelsVolume"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
