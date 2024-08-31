# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.material_use_electronics_currency import MaterialUseElectronicsCurrency

class TestMaterialUseElectronicsCurrency(unittest.TestCase):
    """MaterialUseElectronicsCurrency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MaterialUseElectronicsCurrency:
        """Test MaterialUseElectronicsCurrency
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MaterialUseElectronicsCurrency`
        """
        model = MaterialUseElectronicsCurrency()
        if include_optional:
            return MaterialUseElectronicsCurrency(
                type = 'material_use',
                activity = 'electronics',
                specification = 'average',
                value = 1.337,
                unit = 'EUR'
            )
        else:
            return MaterialUseElectronicsCurrency(
                type = 'material_use',
                value = 1.337,
        )
        """

    def testMaterialUseElectronicsCurrency(self):
        """Test MaterialUseElectronicsCurrency"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()