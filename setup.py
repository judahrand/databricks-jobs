# coding: utf-8

"""
    Jobs API 2.1

    The Jobs API allows you to create, edit, and delete jobs. You should never hard code secrets or store them in plain text. Use the [Secrets API](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/secrets) to manage secrets in the [Databricks CLI](https://docs.microsoft.com/azure/databricks/dev-tools/cli/index). Use the [Secrets utility](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-secrets) to reference secrets in notebooks and jobs.  # noqa: E501

    The version of the OpenAPI document: 2.1
    Generated by: https://openapi-generator.tech
"""
from setuptools import setup, find_packages  # noqa: H301

from databricks_jobs import __version__


setup(
    name="databricks-jobs",
    version=__version__,
    description="Databricks Jobs API 2.1 Client",
    author="Judah Rand",
    author_email="17158624+judahrand@users.noreply.github.com",
    url="https://github.com/judahrand/databricks-jobs",
    keywords=[
        "OpenAPI",
        "OpenAPI-Generator",
        "Databricks",
        "Jobs API 2.1",
    ],
    python_requires=">=3.8",
    install_requires=[
        "urllib3 >= 1.25.3",
        "python-dateutil",
        "pydantic",
        "aenum"
    ],
    packages=find_packages(exclude=["test", "tests"]),
    package_data={"databricks_jobs": ["py.typed"]},
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
)
