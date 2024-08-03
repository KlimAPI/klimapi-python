# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.process_order import ProcessOrder

class TestProcessOrder(unittest.TestCase):
    """ProcessOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProcessOrder:
        """Test ProcessOrder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProcessOrder`
        """
        model = ProcessOrder()
        if include_optional:
            return ProcessOrder(
                recipient_name = '',
                recipient_email = '',
                send_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                metadata = {
                    'key' : ''
                    }
            )
        else:
            return ProcessOrder(
                recipient_name = '',
        )
        """

    def testProcessOrder(self):
        """Test ProcessOrder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
