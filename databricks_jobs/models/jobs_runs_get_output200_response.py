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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from databricks_jobs.models.dbt_output import DbtOutput
from databricks_jobs.models.notebook_output import NotebookOutput
from databricks_jobs.models.run import Run
from databricks_jobs.models.sql_output import SqlOutput


class JobsRunsGetOutput200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    notebook_output: Optional[NotebookOutput] = None
    sql_output: Optional[SqlOutput] = None
    dbt_output: Optional[DbtOutput] = None
    logs: Optional[StrictStr] = Field(
        None,
        description="The output from tasks that write to standard streams (stdout/stderr) such as [SparkJarTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/SparkJarTask), [SparkPythonTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/SparkPythonTask, [PythonWheelTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/PythonWheelTask. It's not supported for the [NotebookTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/NotebookTask, [PipelineTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/PipelineTask, or [SparkSubmitTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/SparkSubmitTask. Azure Databricks restricts this API to return the last 5 MB of these logs.",
    )
    logs_truncated: Optional[StrictBool] = Field(
        None, description="Whether the logs are truncated."
    )
    error: Optional[StrictStr] = Field(
        None,
        description="An error message indicating why a task failed or why output is not available. The message is unstructured, and its exact format is subject to change.",
    )
    error_trace: Optional[StrictStr] = Field(
        None,
        description="If there was an error executing the run, this field contains any available stack traces.",
    )
    metadata: Optional[Run] = None
    __properties = [
        "notebook_output",
        "sql_output",
        "dbt_output",
        "logs",
        "logs_truncated",
        "error",
        "error_trace",
        "metadata",
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
    def from_json(cls, json_str: str) -> JobsRunsGetOutput200Response:
        """Create an instance of JobsRunsGetOutput200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of notebook_output
        if self.notebook_output:
            _dict["notebook_output"] = self.notebook_output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sql_output
        if self.sql_output:
            _dict["sql_output"] = self.sql_output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dbt_output
        if self.dbt_output:
            _dict["dbt_output"] = self.dbt_output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict["metadata"] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobsRunsGetOutput200Response:
        """Create an instance of JobsRunsGetOutput200Response from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return JobsRunsGetOutput200Response.parse_obj(obj)

        _obj = JobsRunsGetOutput200Response.parse_obj(
            {
                "notebook_output": NotebookOutput.from_dict(obj.get("notebook_output"))
                if obj.get("notebook_output") is not None
                else None,
                "sql_output": SqlOutput.from_dict(obj.get("sql_output"))
                if obj.get("sql_output") is not None
                else None,
                "dbt_output": DbtOutput.from_dict(obj.get("dbt_output"))
                if obj.get("dbt_output") is not None
                else None,
                "logs": obj.get("logs"),
                "logs_truncated": obj.get("logs_truncated"),
                "error": obj.get("error"),
                "error_trace": obj.get("error_trace"),
                "metadata": Run.from_dict(obj.get("metadata"))
                if obj.get("metadata") is not None
                else None,
            }
        )
        return _obj
