# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.calculation_results import CalculationResults

class TestCalculationResults(unittest.TestCase):
    """CalculationResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CalculationResults:
        """Test CalculationResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CalculationResults`
        """
        model = CalculationResults()
        if include_optional:
            return CalculationResults(
                kg_co2e = 1.337,
                calculation_id = '',
                results = [
                    {"type":"travel-land","activity":"cars_by_market_segment","specification":"average","detail":"average","value":2000,"unit":"kilometers","kgCO2e":500}
                    ]
            )
        else:
            return CalculationResults(
        )
        """

    def testCalculationResults(self):
        """Test CalculationResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
