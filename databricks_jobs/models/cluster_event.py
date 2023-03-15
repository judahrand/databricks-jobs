# coding: utf-8

"""
    Jobs API 2.1

    The Jobs API allows you to create, edit, and delete jobs. You should never hard code secrets or store them in plain text. Use the [Secrets API](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/secrets) to manage secrets in the [Databricks CLI](https://docs.microsoft.com/azure/databricks/dev-tools/cli/index). Use the [Secrets utility](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-secrets) to reference secrets in notebooks and jobs.  # noqa: E501

    The version of the OpenAPI document: 2.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from databricks_jobs.models.cluster_event_type import ClusterEventType
from databricks_jobs.models.event_details import EventDetails


class ClusterEvent(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    cluster_id: StrictStr = Field(
        ..., description="Canonical identifier for the cluster. This field is required."
    )
    timestamp: Optional[StrictInt] = Field(
        None,
        description="The timestamp when the event occurred, stored as the number of milliseconds since the unix epoch. Assigned by the Timeline service.",
    )
    type: ClusterEventType = ...
    details: EventDetails = ...
    __properties = ["cluster_id", "timestamp", "type", "details"]

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
    def from_json(cls, json_str: str) -> ClusterEvent:
        """Create an instance of ClusterEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict["details"] = self.details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterEvent:
        """Create an instance of ClusterEvent from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ClusterEvent.parse_obj(obj)

        _obj = ClusterEvent.parse_obj(
            {
                "cluster_id": obj.get("cluster_id"),
                "timestamp": obj.get("timestamp"),
                "type": obj.get("type"),
                "details": EventDetails.from_dict(obj.get("details"))
                if obj.get("details") is not None
                else None,
            }
        )
        return _obj
