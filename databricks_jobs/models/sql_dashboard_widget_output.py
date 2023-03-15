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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from databricks_jobs.models.sql_output_error import SqlOutputError


class SqlDashboardWidgetOutput(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    widget_id: Optional[StrictStr] = Field(
        None, description="The canonical identifier of the SQL widget."
    )
    widget_title: Optional[StrictStr] = Field(
        None, description="The title of the SQL widget."
    )
    output_link: Optional[StrictStr] = Field(
        None, description="The link to find the output results."
    )
    status: Optional[StrictStr] = Field(
        None, description="The execution status of the SQL widget."
    )
    error: Optional[SqlOutputError] = None
    start_time: Optional[StrictInt] = Field(
        None,
        description="Time (in epoch milliseconds) when execution of the SQL widget starts.",
    )
    end_time: Optional[StrictInt] = Field(
        None,
        description="Time (in epoch milliseconds) when execution of the SQL widget ends.",
    )
    __properties = [
        "widget_id",
        "widget_title",
        "output_link",
        "status",
        "error",
        "start_time",
        "end_time",
    ]

    @validator("status")
    def status_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ("PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED"):
            raise ValueError(
                "must validate the enum values ('PENDING', 'RUNNING', 'SUCCESS', 'FAILED', 'CANCELLED')"
            )
        return v

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
    def from_json(cls, json_str: str) -> SqlDashboardWidgetOutput:
        """Create an instance of SqlDashboardWidgetOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SqlDashboardWidgetOutput:
        """Create an instance of SqlDashboardWidgetOutput from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SqlDashboardWidgetOutput.parse_obj(obj)

        _obj = SqlDashboardWidgetOutput.parse_obj(
            {
                "widget_id": obj.get("widget_id"),
                "widget_title": obj.get("widget_title"),
                "output_link": obj.get("output_link"),
                "status": obj.get("status"),
                "error": SqlOutputError.from_dict(obj.get("error"))
                if obj.get("error") is not None
                else None,
                "start_time": obj.get("start_time"),
                "end_time": obj.get("end_time"),
            }
        )
        return _obj
