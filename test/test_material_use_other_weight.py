# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.material_use_other_weight import MaterialUseOtherWeight

class TestMaterialUseOtherWeight(unittest.TestCase):
    """MaterialUseOtherWeight unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MaterialUseOtherWeight:
        """Test MaterialUseOtherWeight
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MaterialUseOtherWeight`
        """
        model = MaterialUseOtherWeight()
        if include_optional:
            return MaterialUseOtherWeight(
                type = 'material_use',
                activity = 'other',
                specification = 'average',
                detail = 'average',
                value = 1.337,
                unit = 'metric tons'
            )
        else:
            return MaterialUseOtherWeight(
                type = 'material_use',
                value = 1.337,
        )
        """

    def testMaterialUseOtherWeight(self):
        """Test MaterialUseOtherWeight"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
