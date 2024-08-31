# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.pending_by_calculation_request_calculation_options_inner import PendingByCalculationRequestCalculationOptionsInner

class TestPendingByCalculationRequestCalculationOptionsInner(unittest.TestCase):
    """PendingByCalculationRequestCalculationOptionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PendingByCalculationRequestCalculationOptionsInner:
        """Test PendingByCalculationRequestCalculationOptionsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PendingByCalculationRequestCalculationOptionsInner`
        """
        model = PendingByCalculationRequestCalculationOptionsInner()
        if include_optional:
            return PendingByCalculationRequestCalculationOptionsInner(
                type = 'fuels',
                activity = '',
                specification = '',
                value = 1.337,
                unit = '',
                detail = 'average',
                departure = '',
                destination = '',
                return_trip = True,
                passengers = 56,
                weight = 1.337,
                weight_unit = 'metric tons',
                amount = 1,
                multiplier = 1
            )
        else:
            return PendingByCalculationRequestCalculationOptionsInner(
                type = 'fuels',
                activity = '',
                specification = '',
                value = 1.337,
                unit = '',
                departure = '',
                destination = '',
                amount = 1,
        )
        """

    def testPendingByCalculationRequestCalculationOptionsInner(self):
        """Test PendingByCalculationRequestCalculationOptionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
