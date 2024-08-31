# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.invoice_details import InvoiceDetails

class TestInvoiceDetails(unittest.TestCase):
    """InvoiceDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetails:
        """Test InvoiceDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetails`
        """
        model = InvoiceDetails()
        if include_optional:
            return InvoiceDetails(
                name = '',
                email = '',
                address = klimapi_python.models.invoice_details_address.InvoiceDetails_address(
                    city = '', 
                    country = '', 
                    line1 = '', 
                    line2 = '', 
                    postal_code = '', 
                    state = '', ),
                tax_id = klimapi_python.models.invoice_details_tax_id.InvoiceDetails_tax_id(
                    type = 'eu_vat', 
                    value = '', )
            )
        else:
            return InvoiceDetails(
                name = '',
                email = '',
                address = klimapi_python.models.invoice_details_address.InvoiceDetails_address(
                    city = '', 
                    country = '', 
                    line1 = '', 
                    line2 = '', 
                    postal_code = '', 
                    state = '', ),
        )
        """

    def testInvoiceDetails(self):
        """Test InvoiceDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
