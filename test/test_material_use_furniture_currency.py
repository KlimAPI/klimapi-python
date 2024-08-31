# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.material_use_furniture_currency import MaterialUseFurnitureCurrency

class TestMaterialUseFurnitureCurrency(unittest.TestCase):
    """MaterialUseFurnitureCurrency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MaterialUseFurnitureCurrency:
        """Test MaterialUseFurnitureCurrency
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MaterialUseFurnitureCurrency`
        """
        model = MaterialUseFurnitureCurrency()
        if include_optional:
            return MaterialUseFurnitureCurrency(
                type = 'material_use',
                activity = 'furniture',
                specification = 'average',
                value = 1.337,
                unit = 'EUR'
            )
        else:
            return MaterialUseFurnitureCurrency(
                type = 'material_use',
                value = 1.337,
        )
        """

    def testMaterialUseFurnitureCurrency(self):
        """Test MaterialUseFurnitureCurrency"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()