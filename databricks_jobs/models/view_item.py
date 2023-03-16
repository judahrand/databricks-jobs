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

from databricks_jobs.models.view_type import ViewType


class ViewItem(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    content: Optional[StrictStr] = Field(None, description="Content of the view.")
    name: Optional[StrictStr] = Field(
        None,
        description="Name of the view item. In the case of code view, it would be the notebook’s name. In the case of dashboard view, it would be the dashboard’s name.",
    )
    type: Optional[ViewType] = None
    __properties = ["content", "name", "type"]

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
    def from_json(cls, json_str: str) -> ViewItem:
        """Create an instance of ViewItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ViewItem:
        """Create an instance of ViewItem from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ViewItem.parse_obj(obj)

        _obj = ViewItem.parse_obj(
            {
                "content": obj.get("content"),
                "name": obj.get("name"),
                "type": obj.get("type"),
            }
        )
        return _obj
