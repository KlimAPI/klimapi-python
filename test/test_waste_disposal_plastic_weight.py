# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.waste_disposal_plastic_weight import WasteDisposalPlasticWeight

class TestWasteDisposalPlasticWeight(unittest.TestCase):
    """WasteDisposalPlasticWeight unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WasteDisposalPlasticWeight:
        """Test WasteDisposalPlasticWeight
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WasteDisposalPlasticWeight`
        """
        model = WasteDisposalPlasticWeight()
        if include_optional:
            return WasteDisposalPlasticWeight(
                type = 'waste_disposal',
                activity = 'plastic',
                specification = 'average',
                detail = 'average',
                value = 1.337,
                unit = 'metric tons'
            )
        else:
            return WasteDisposalPlasticWeight(
                type = 'waste_disposal',
                value = 1.337,
        )
        """

    def testWasteDisposalPlasticWeight(self):
        """Test WasteDisposalPlasticWeight"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
