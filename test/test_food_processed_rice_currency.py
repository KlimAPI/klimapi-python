# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.food_processed_rice_currency import FoodProcessedRiceCurrency

class TestFoodProcessedRiceCurrency(unittest.TestCase):
    """FoodProcessedRiceCurrency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FoodProcessedRiceCurrency:
        """Test FoodProcessedRiceCurrency
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FoodProcessedRiceCurrency`
        """
        model = FoodProcessedRiceCurrency()
        if include_optional:
            return FoodProcessedRiceCurrency(
                type = 'food',
                activity = 'processed_rice',
                specification = 'average',
                value = 1.337,
                unit = 'EUR'
            )
        else:
            return FoodProcessedRiceCurrency(
                type = 'food',
                value = 1.337,
        )
        """

    def testFoodProcessedRiceCurrency(self):
        """Test FoodProcessedRiceCurrency"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
