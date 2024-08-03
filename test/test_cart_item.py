# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.cart_item import CartItem

class TestCartItem(unittest.TestCase):
    """CartItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CartItem:
        """Test CartItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CartItem`
        """
        model = CartItem()
        if include_optional:
            return CartItem(
                amount = 56,
                total = 1.337,
                product = {"product_id":"sample-product","name":"Sample Product","description":"This is a sample product","price":10.99,"categories":["sample-category"],"tags":["sample-tag"],"weight":1.5,"weight_unit":"kg","made_in":"Germany","emission_factor":14,"emission_multiplicator":"price"}
            )
        else:
            return CartItem(
                amount = 56,
                total = 1.337,
                product = {"product_id":"sample-product","name":"Sample Product","description":"This is a sample product","price":10.99,"categories":["sample-category"],"tags":["sample-tag"],"weight":1.5,"weight_unit":"kg","made_in":"Germany","emission_factor":14,"emission_multiplicator":"price"},
        )
        """

    def testCartItem(self):
        """Test CartItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
