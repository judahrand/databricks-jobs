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
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, StrictStr


class DbtOutput(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    artifacts_link: Optional[StrictStr] = Field(
        None,
        description="A pre-signed URL to download the (compressed) dbt artifacts. This link is valid for a limited time (30 minutes). This information is only available after the run has finished.",
    )
    artifacts_headers: Optional[Dict[str, Any]] = Field(
        None,
        description="An optional map of headers to send when retrieving the artifact from the `artifacts_link`.",
    )
    __properties = ["artifacts_link", "artifacts_headers"]

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
    def from_json(cls, json_str: str) -> DbtOutput:
        """Create an instance of DbtOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DbtOutput:
        """Create an instance of DbtOutput from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DbtOutput.parse_obj(obj)

        _obj = DbtOutput.parse_obj(
            {
                "artifacts_link": obj.get("artifacts_link"),
                "artifacts_headers": obj.get("artifacts_headers"),
            }
        )
        return _obj
