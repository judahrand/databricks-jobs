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


class SparkNode(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    private_ip: Optional[StrictStr] = Field(
        None,
        description="Private IP address (typically a 10.x.x.x address) of the Spark node. This is different from the private IP address of the host instance.",
    )
    public_dns: Optional[StrictStr] = Field(
        None,
        description="Public DNS address of this node. This address can be used to access the Spark JDBC server on the driver node.",
    )
    node_id: Optional[StrictStr] = Field(
        None, description="Globally unique identifier for this node."
    )
    instance_id: Optional[StrictStr] = Field(
        None,
        description="Globally unique identifier for the host instance from the cloud provider.",
    )
    start_timestamp: Optional[StrictInt] = Field(
        None,
        description="The timestamp (in millisecond) when the Spark node is launched.",
    )
    host_private_ip: Optional[StrictStr] = Field(
        None, description="The private IP address of the host instance."
    )
    __properties = [
        "private_ip",
        "public_dns",
        "node_id",
        "instance_id",
        "start_timestamp",
        "host_private_ip",
    ]

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
    def from_json(cls, json_str: str) -> SparkNode:
        """Create an instance of SparkNode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SparkNode:
        """Create an instance of SparkNode from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SparkNode.parse_obj(obj)

        _obj = SparkNode.parse_obj(
            {
                "private_ip": obj.get("private_ip"),
                "public_dns": obj.get("public_dns"),
                "node_id": obj.get("node_id"),
                "instance_id": obj.get("instance_id"),
                "start_timestamp": obj.get("start_timestamp"),
                "host_private_ip": obj.get("host_private_ip"),
            }
        )
        return _obj
