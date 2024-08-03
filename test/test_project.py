# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from klimapi_python.models.project import Project

class TestProject(unittest.TestCase):
    """Project unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Project:
        """Test Project
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Project`
        """
        model = Project()
        if include_optional:
            return Project(
                id = '',
                title = '',
                summary = '',
                status = '',
                category_id = 56,
                certification_authority_id = 56,
                country = '',
                description = '',
                goals = '',
                images = [
                    ''
                    ],
                benefits = [
                    56
                    ]
            )
        else:
            return Project(
        )
        """

    def testProject(self):
        """Test Project"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
