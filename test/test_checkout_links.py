# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.checkout_links import CheckoutLinks

class TestCheckoutLinks(unittest.TestCase):
    """CheckoutLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckoutLinks:
        """Test CheckoutLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckoutLinks`
        """
        model = CheckoutLinks()
        if include_optional:
            return CheckoutLinks(
                checkout_links = [
                    {"payment_link":"https://klimapi.com/checkout/00000000-0000-0000-0000-000000000000","payment_link_id":"00000000-0000-0000-0000-000000000000","certificate_issued_at":"2022-01-01T00:00:00.000000Z","certificate_url":"https://certificates.klimahelden.eu/CA-0000-00000000","certificate_pdf":"https://certificates.klimahelden.eu/certificate/download?locale=en&order_id=CA-0000-00000000","order_id":"CA-0000-00000000","kgCO2e":500,"price":10,"currency":"EUR","payment_received":false,"project":{"id":"00000000-0000-0000-0000-000000000000","title":"Example Project","summary":"Example Summary","status":"Active","category_id":7,"certification_authority_id":3,"country":"Example Country","description":null,"goals":null,"images":["https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_1.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_2.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_3.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_4.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_5.jpeg"],"benefits":[8,13,15]}}
                    ]
            )
        else:
            return CheckoutLinks(
        )
        """

    def testCheckoutLinks(self):
        """Test CheckoutLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
