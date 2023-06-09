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

from pydantic import BaseModel, Field, StrictInt

from databricks_jobs.models.auto_scale import AutoScale


class ClusterSize(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    num_workers: Optional[StrictInt] = Field(
        None,
        description="If num_workers, number of worker nodes that this cluster must have. A cluster has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field is updated to reflect the target size of 10 workers, whereas the workers listed in executors gradually increase from 5 to 10 as the new nodes are provisioned.",
    )
    autoscale: Optional[AutoScale] = None
    __properties = ["num_workers", "autoscale"]

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
    def from_json(cls, json_str: str) -> ClusterSize:
        """Create an instance of ClusterSize from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of autoscale
        if self.autoscale:
            _dict["autoscale"] = self.autoscale.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterSize:
        """Create an instance of ClusterSize from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ClusterSize.parse_obj(obj)

        _obj = ClusterSize.parse_obj(
            {
                "num_workers": obj.get("num_workers"),
                "autoscale": AutoScale.from_dict(obj.get("autoscale"))
                if obj.get("autoscale") is not None
                else None,
            }
        )
        return _obj
