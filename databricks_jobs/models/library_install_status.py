# coding: utf-8

"""
    Jobs API 2.1

    The Jobs API allows you to create, edit, and delete jobs. You should never hard code secrets or store them in plain text. Use the [Secrets API](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/secrets) to manage secrets in the [Databricks CLI](https://docs.microsoft.com/azure/databricks/dev-tools/cli/index). Use the [Secrets utility](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-secrets) to reference secrets in notebooks and jobs.  # noqa: E501

    The version of the OpenAPI document: 2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401
from inspect import getfullargspec

from aenum import Enum, no_arg


class LibraryInstallStatus(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    PENDING = "PENDING"
    RESOLVING = "RESOLVING"
    INSTALLING = "INSTALLING"
    INSTALLED = "INSTALLED"
    SKIPPED = "SKIPPED"
    FAILED = "FAILED"
    UNINSTALL_ON_RESTART = "UNINSTALL_ON_RESTART"
