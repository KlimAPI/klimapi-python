# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.infrastructure_average_currency import InfrastructureAverageCurrency

class TestInfrastructureAverageCurrency(unittest.TestCase):
    """InfrastructureAverageCurrency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InfrastructureAverageCurrency:
        """Test InfrastructureAverageCurrency
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InfrastructureAverageCurrency`
        """
        model = InfrastructureAverageCurrency()
        if include_optional:
            return InfrastructureAverageCurrency(
                type = 'infrastructure',
                value = 1.337,
                unit = 'EUR'
            )
        else:
            return InfrastructureAverageCurrency(
                type = 'infrastructure',
                value = 1.337,
        )
        """

    def testInfrastructureAverageCurrency(self):
        """Test InfrastructureAverageCurrency"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
