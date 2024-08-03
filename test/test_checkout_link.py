# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.checkout_link import CheckoutLink

class TestCheckoutLink(unittest.TestCase):
    """CheckoutLink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckoutLink:
        """Test CheckoutLink
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckoutLink`
        """
        model = CheckoutLink()
        if include_optional:
            return CheckoutLink(
                payment_link = '',
                payment_link_id = '',
                certificate_issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                certificate_url = '',
                certificate_pdf = '',
                order_id = '',
                kg_co2e = 56,
                price = 1.337,
                currency = 'EUR',
                payment_received = '',
                project = {"id":"00000000-0000-0000-0000-000000000000","title":"Example Project","summary":"Example Summary","status":"Active","category_id":7,"certification_authority_id":3,"country":"Example Country","description":null,"goals":null,"images":["https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_1.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_2.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_3.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_4.jpeg","https://cdn.klimapi.com/projects/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000_5.jpeg"],"benefits":[8,13,15]}
            )
        else:
            return CheckoutLink(
        )
        """

    def testCheckoutLink(self):
        """Test CheckoutLink"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
