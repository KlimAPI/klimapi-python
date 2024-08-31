# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "klimapi-python"
VERSION = "1.1.29"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="KlimAPI - Calculation &amp; Compensation API",
    author="KlimAPI Team",
    author_email="tech@klimapi.com",
    url="https://github.com/KlimAPI/klimapi-python",
    keywords=["klimapi"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.
    """,  # noqa: E501
    package_data={"klimapi_python": ["py.typed"]},
)
