# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.cart_result import CartResult

class TestCartResult(unittest.TestCase):
    """CartResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CartResult:
        """Test CartResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CartResult`
        """
        model = CartResult()
        if include_optional:
            return CartResult(
                kg_co2e = 1.337,
                settings = klimapi_python.models.cart_result_settings.CartResult_settings(
                    split = 0, 
                    default = True, ),
                calculation_results = [
                    klimapi_python.models.cart_result_calculation_results_inner.CartResult_calculation_results_inner(
                        product_id = '', 
                        source = 'factor', 
                        kg_co2e = 1.337, )
                    ],
                orders = [
                    {"order_id":"CA-0000-00000000","status":"pending","price":10,"currency":"EUR","kgCO2e":500,"metadata":{"utm_medium":"mail","utm_campaign":"newsletter-23"},"project":{"id":"00000000-0000-0000-0000-000000000000","title":"Example Project","summary":"Example Summary","status":"Active","category_id":7,"certification_authority_id":3,"country":"Example Country","description":null,"goals":null,"images":["https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_1.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_2.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_3.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_4.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_5.jpeg"],"benefits":[8,13,15]}}
                    ]
            )
        else:
            return CartResult(
        )
        """

    def testCartResult(self):
        """Test CartResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
