# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.homeworking_per_fte_working_hour import HomeworkingPerFteWorkingHour

class TestHomeworkingPerFteWorkingHour(unittest.TestCase):
    """HomeworkingPerFteWorkingHour unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HomeworkingPerFteWorkingHour:
        """Test HomeworkingPerFteWorkingHour
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HomeworkingPerFteWorkingHour`
        """
        model = HomeworkingPerFteWorkingHour()
        if include_optional:
            return HomeworkingPerFteWorkingHour(
                type = 'homeworking',
                activity = 'average',
                value = 1.337,
                unit = 'per_fte_working_hour'
            )
        else:
            return HomeworkingPerFteWorkingHour(
                type = 'homeworking',
                value = 1.337,
        )
        """

    def testHomeworkingPerFteWorkingHour(self):
        """Test HomeworkingPerFteWorkingHour"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
