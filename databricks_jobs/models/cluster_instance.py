# coding: utf-8

"""
    Jobs API 2.1

    The Jobs API allows you to create, edit, and delete jobs. You should never hard code secrets or store them in plain text. Use the [Secrets API](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/secrets) to manage secrets in the [Databricks CLI](https://docs.microsoft.com/azure/databricks/dev-tools/cli/index). Use the [Secrets utility](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-secrets) to reference secrets in notebooks and jobs.  # noqa: E501

    The version of the OpenAPI document: 2.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from inspect import getfullargspec
from typing import Optional

from pydantic import BaseModel, Field, StrictStr


class ClusterInstance(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    cluster_id: Optional[StrictStr] = Field(
        None,
        description="The canonical identifier for the cluster used by a run. This field is always available for runs on existing clusters. For runs on new clusters, it becomes available once the cluster is created. This value can be used to view logs by browsing to `/#setting/sparkui/$cluster_id/driver-logs`. The logs continue to be available after the run completes.  The response won’t include this field if the identifier is not available yet.",
    )
    spark_context_id: Optional[StrictStr] = Field(
        None,
        description="The canonical identifier for the Spark context used by a run. This field is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to `/#setting/sparkui/$cluster_id/$spark_context_id`. The Spark UI continues to be available after the run has completed.  The response won’t include this field if the identifier is not available yet.",
    )
    __properties = ["cluster_id", "spark_context_id"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ClusterInstance:
        """Create an instance of ClusterInstance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterInstance:
        """Create an instance of ClusterInstance from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ClusterInstance.parse_obj(obj)

        _obj = ClusterInstance.parse_obj(
            {
                "cluster_id": obj.get("cluster_id"),
                "spark_context_id": obj.get("spark_context_id"),
            }
        )
        return _obj
