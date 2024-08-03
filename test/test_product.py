# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.product import Product

class TestProduct(unittest.TestCase):
    """Product unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Product:
        """Test Product
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Product`
        """
        model = Product()
        if include_optional:
            return Product(
                product_id = '',
                name = '',
                description = '',
                price = 1.337,
                categories = [
                    ''
                    ],
                tags = [
                    ''
                    ],
                weight = 1.337,
                weight_unit = 'kg',
                made_in = '',
                emission_factor = '',
                emission_multiplicator = 'price'
            )
        else:
            return Product(
                product_id = '',
                price = 1.337,
        )
        """

    def testProduct(self):
        """Test Product"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
