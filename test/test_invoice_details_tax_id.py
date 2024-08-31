# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.invoice_details_tax_id import InvoiceDetailsTaxId

class TestInvoiceDetailsTaxId(unittest.TestCase):
    """InvoiceDetailsTaxId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailsTaxId:
        """Test InvoiceDetailsTaxId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailsTaxId`
        """
        model = InvoiceDetailsTaxId()
        if include_optional:
            return InvoiceDetailsTaxId(
                type = 'eu_vat',
                value = ''
            )
        else:
            return InvoiceDetailsTaxId(
                type = 'eu_vat',
                value = '',
        )
        """

    def testInvoiceDetailsTaxId(self):
        """Test InvoiceDetailsTaxId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
