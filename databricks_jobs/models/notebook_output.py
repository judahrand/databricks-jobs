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

from pydantic import BaseModel, Field, StrictBool, StrictStr


class NotebookOutput(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    result: Optional[StrictStr] = Field(
        None,
        description="The value passed to [dbutils.notebook.exit()](https://docs.microsoft.com/azure/databricks/notebooks/notebook-workflows#notebook-workflows-exit). Azure Databricks restricts this API to return the first 5 MB of the value. For a larger result, your job can store the results in a cloud storage service. This field is absent if `dbutils.notebook.exit()` was never called.",
    )
    truncated: Optional[StrictBool] = Field(
        None, description="Whether or not the result was truncated."
    )
    __properties = ["result", "truncated"]

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
    def from_json(cls, json_str: str) -> NotebookOutput:
        """Create an instance of NotebookOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NotebookOutput:
        """Create an instance of NotebookOutput from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NotebookOutput.parse_obj(obj)

        _obj = NotebookOutput.parse_obj(
            {"result": obj.get("result"), "truncated": obj.get("truncated")}
        )
        return _obj
