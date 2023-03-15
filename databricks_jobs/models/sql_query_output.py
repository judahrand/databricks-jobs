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

from databricks_jobs.models.sql_statement_output import SqlStatementOutput


class SqlQueryOutput(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    query_text: Optional[StrictStr] = Field(
        None,
        description="The text of the SQL query. Can Run permission of the SQL query is required to view this field.",
    )
    warehouse_id: Optional[StrictStr] = Field(
        None, description="The canonical identifier of the SQL warehouse."
    )
    sql_statements: Optional[SqlStatementOutput] = None
    output_link: Optional[StrictStr] = Field(
        None, description="The link to find the output results."
    )
    __properties = ["query_text", "warehouse_id", "sql_statements", "output_link"]

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
    def from_json(cls, json_str: str) -> SqlQueryOutput:
        """Create an instance of SqlQueryOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of sql_statements
        if self.sql_statements:
            _dict["sql_statements"] = self.sql_statements.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SqlQueryOutput:
        """Create an instance of SqlQueryOutput from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SqlQueryOutput.parse_obj(obj)

        _obj = SqlQueryOutput.parse_obj(
            {
                "query_text": obj.get("query_text"),
                "warehouse_id": obj.get("warehouse_id"),
                "sql_statements": SqlStatementOutput.from_dict(
                    obj.get("sql_statements")
                )
                if obj.get("sql_statements") is not None
                else None,
                "output_link": obj.get("output_link"),
            }
        )
        return _obj
