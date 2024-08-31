# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.cloud_computing_memory_gb_hour import CloudComputingMemoryGbHour

class TestCloudComputingMemoryGbHour(unittest.TestCase):
    """CloudComputingMemoryGbHour unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CloudComputingMemoryGbHour:
        """Test CloudComputingMemoryGbHour
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudComputingMemoryGbHour`
        """
        model = CloudComputingMemoryGbHour()
        if include_optional:
            return CloudComputingMemoryGbHour(
                type = 'cloud_computing',
                activity = 'memory',
                specification = 'average',
                detail = 'average',
                value = 1.337,
                unit = 'gb-hour'
            )
        else:
            return CloudComputingMemoryGbHour(
                type = 'cloud_computing',
                value = 1.337,
        )
        """

    def testCloudComputingMemoryGbHour(self):
        """Test CloudComputingMemoryGbHour"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
