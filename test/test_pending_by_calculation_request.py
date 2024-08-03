# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.pending_by_calculation_request import PendingByCalculationRequest

class TestPendingByCalculationRequest(unittest.TestCase):
    """PendingByCalculationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PendingByCalculationRequest:
        """Test PendingByCalculationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PendingByCalculationRequest`
        """
        model = PendingByCalculationRequest()
        if include_optional:
            return PendingByCalculationRequest(
                calculation_options = [
                    null
                    ],
                order_count = 1,
                metadata = {
                    'key' : ''
                    },
                fractional_digits = 0
            )
        else:
            return PendingByCalculationRequest(
                calculation_options = [
                    null
                    ],
        )
        """

    def testPendingByCalculationRequest(self):
        """Test PendingByCalculationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
