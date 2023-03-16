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

from pydantic import BaseModel

from databricks_jobs.models.dbt_task import DbtTask
from databricks_jobs.models.notebook_task import NotebookTask
from databricks_jobs.models.pipeline_task import PipelineTask
from databricks_jobs.models.python_wheel_task import PythonWheelTask
from databricks_jobs.models.spark_jar_task import SparkJarTask
from databricks_jobs.models.spark_python_task import SparkPythonTask
from databricks_jobs.models.spark_submit_task import SparkSubmitTask
from databricks_jobs.models.sql_task import SqlTask


class JobTask(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    notebook_task: Optional[NotebookTask] = None
    spark_jar_task: Optional[SparkJarTask] = None
    spark_python_task: Optional[SparkPythonTask] = None
    spark_submit_task: Optional[SparkSubmitTask] = None
    pipeline_task: Optional[PipelineTask] = None
    python_wheel_task: Optional[PythonWheelTask] = None
    sql_task: Optional[SqlTask] = None
    dbt_task: Optional[DbtTask] = None
    __properties = [
        "notebook_task",
        "spark_jar_task",
        "spark_python_task",
        "spark_submit_task",
        "pipeline_task",
        "python_wheel_task",
        "sql_task",
        "dbt_task",
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
    def from_json(cls, json_str: str) -> JobTask:
        """Create an instance of JobTask from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of notebook_task
        if self.notebook_task:
            _dict["notebook_task"] = self.notebook_task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spark_jar_task
        if self.spark_jar_task:
            _dict["spark_jar_task"] = self.spark_jar_task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spark_python_task
        if self.spark_python_task:
            _dict["spark_python_task"] = self.spark_python_task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spark_submit_task
        if self.spark_submit_task:
            _dict["spark_submit_task"] = self.spark_submit_task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pipeline_task
        if self.pipeline_task:
            _dict["pipeline_task"] = self.pipeline_task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of python_wheel_task
        if self.python_wheel_task:
            _dict["python_wheel_task"] = self.python_wheel_task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sql_task
        if self.sql_task:
            _dict["sql_task"] = self.sql_task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dbt_task
        if self.dbt_task:
            _dict["dbt_task"] = self.dbt_task.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobTask:
        """Create an instance of JobTask from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return JobTask.parse_obj(obj)

        _obj = JobTask.parse_obj(
            {
                "notebook_task": NotebookTask.from_dict(obj.get("notebook_task"))
                if obj.get("notebook_task") is not None
                else None,
                "spark_jar_task": SparkJarTask.from_dict(obj.get("spark_jar_task"))
                if obj.get("spark_jar_task") is not None
                else None,
                "spark_python_task": SparkPythonTask.from_dict(
                    obj.get("spark_python_task")
                )
                if obj.get("spark_python_task") is not None
                else None,
                "spark_submit_task": SparkSubmitTask.from_dict(
                    obj.get("spark_submit_task")
                )
                if obj.get("spark_submit_task") is not None
                else None,
                "pipeline_task": PipelineTask.from_dict(obj.get("pipeline_task"))
                if obj.get("pipeline_task") is not None
                else None,
                "python_wheel_task": PythonWheelTask.from_dict(
                    obj.get("python_wheel_task")
                )
                if obj.get("python_wheel_task") is not None
                else None,
                "sql_task": SqlTask.from_dict(obj.get("sql_task"))
                if obj.get("sql_task") is not None
                else None,
                "dbt_task": DbtTask.from_dict(obj.get("dbt_task"))
                if obj.get("dbt_task") is not None
                else None,
            }
        )
        return _obj
