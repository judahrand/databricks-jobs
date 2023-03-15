# coding: utf-8

"""
    Jobs API 2.1

    The Jobs API allows you to create, edit, and delete jobs. You should never hard code secrets or store them in plain text. Use the [Secrets API](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/secrets) to manage secrets in the [Databricks CLI](https://docs.microsoft.com/azure/databricks/dev-tools/cli/index). Use the [Secrets utility](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-secrets) to reference secrets in notebooks and jobs.  # noqa: E501

    The version of the OpenAPI document: 2.1
    Generated by: https://openapi-generator.tech
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg


class ClusterEventType(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    CREATING = "CREATING"
    DID_NOT_EXPAND_DISK = "DID_NOT_EXPAND_DISK"
    EXPANDED_DISK = "EXPANDED_DISK"
    FAILED_TO_EXPAND_DISK = "FAILED_TO_EXPAND_DISK"
    INIT_SCRIPTS_STARTING = "INIT_SCRIPTS_STARTING"
    INIT_SCRIPTS_FINISHED = "INIT_SCRIPTS_FINISHED"
    STARTING = "STARTING"
    RESTARTING = "RESTARTING"
    TERMINATING = "TERMINATING"
    EDITED = "EDITED"
    RUNNING = "RUNNING"
    RESIZING = "RESIZING"
    UPSIZE_COMPLETED = "UPSIZE_COMPLETED"
    NODES_LOST = "NODES_LOST"
    DRIVER_HEALTHY = "DRIVER_HEALTHY"
    DRIVER_UNAVAILABLE = "DRIVER_UNAVAILABLE"
    SPARK_EXCEPTION = "SPARK_EXCEPTION"
    DRIVER_NOT_RESPONDING = "DRIVER_NOT_RESPONDING"
    DBFS_DOWN = "DBFS_DOWN"
    METASTORE_DOWN = "METASTORE_DOWN"
    NODE_BLACKLISTED = "NODE_BLACKLISTED"
    PINNED = "PINNED"
    UNPINNED = "UNPINNED"
