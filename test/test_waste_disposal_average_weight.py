# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.waste_disposal_average_weight import WasteDisposalAverageWeight

class TestWasteDisposalAverageWeight(unittest.TestCase):
    """WasteDisposalAverageWeight unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WasteDisposalAverageWeight:
        """Test WasteDisposalAverageWeight
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WasteDisposalAverageWeight`
        """
        model = WasteDisposalAverageWeight()
        if include_optional:
            return WasteDisposalAverageWeight(
                type = 'waste_disposal',
                value = 1.337,
                unit = 'metric tons'
            )
        else:
            return WasteDisposalAverageWeight(
                type = 'waste_disposal',
                value = 1.337,
        )
        """

    def testWasteDisposalAverageWeight(self):
        """Test WasteDisposalAverageWeight"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
