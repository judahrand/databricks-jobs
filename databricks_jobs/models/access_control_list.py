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
from typing import List, Optional

from pydantic import BaseModel, Field

from databricks_jobs.models.access_control_request import AccessControlRequest


class AccessControlList(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    access_control_list: Optional[List[AccessControlRequest]] = Field(
        None, description="List of permissions to set on the job."
    )
    __properties = ["access_control_list"]

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
    def from_json(cls, json_str: str) -> AccessControlList:
        """Create an instance of AccessControlList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in access_control_list (list)
        _items = []
        if self.access_control_list:
            for _item in self.access_control_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["access_control_list"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessControlList:
        """Create an instance of AccessControlList from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AccessControlList.parse_obj(obj)

        _obj = AccessControlList.parse_obj(
            {
                "access_control_list": [
                    AccessControlRequest.from_dict(_item)
                    for _item in obj.get("access_control_list")
                ]
                if obj.get("access_control_list") is not None
                else None
            }
        )
        return _obj
