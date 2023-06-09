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
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

from databricks_jobs.models.run_parameters_pipeline_params import (
    RunParametersPipelineParams,
)


class JobsRunsRepairRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    run_id: Optional[StrictInt] = Field(
        None,
        description="The job run ID of the run to repair. The run must not be in progress.",
    )
    rerun_tasks: Optional[List[StrictStr]] = Field(
        None, description="The task keys of the task runs to repair."
    )
    latest_repair_id: Optional[StrictInt] = Field(
        None,
        description="The ID of the latest repair. This parameter is not required when repairing a run for the first time, but must be provided on subsequent requests to repair the same run.",
    )
    rerun_all_failed_tasks: Optional[StrictBool] = Field(
        False,
        description="If true, repair all failed tasks. Only one of rerun_tasks or rerun_all_failed_tasks can be used.",
    )
    jar_params: Optional[List[StrictStr]] = Field(
        None,
        description='A list of parameters for jobs with Spark JAR tasks, for example `"jar_params": ["john doe", "35"]`. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon `run-now`, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example `{"jar_params":["john doe","35"]}`) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.',
    )
    notebook_params: Optional[Dict[str, Any]] = Field(
        None,
        description='A map from keys to values for jobs with notebook task, for example `"notebook_params": {"name": "john doe", "age": "35"}`. The map is passed to the notebook and is accessible through the [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-widgets) function.  If not specified upon `run-now`, the triggered run uses the job’s base parameters.  notebook_params cannot be specified in conjunction with jar_params.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  The JSON representation of this field (for example `{"notebook_params":{"name":"john doe","age":"35"}}`) cannot exceed 10,000 bytes.',
    )
    python_params: Optional[List[StrictStr]] = Field(
        None,
        description='A list of parameters for jobs with Python tasks, for example `"python_params": ["john doe", "35"]`. The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `{"python_params":["john doe","35"]}`) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  Important  These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis.',
    )
    spark_submit_params: Optional[List[StrictStr]] = Field(
        None,
        description='A list of parameters for jobs with spark submit task, for example `"spark_submit_params": ["--class", "org.apache.spark.examples.SparkPi"]`. The parameters are passed to spark-submit script as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `{"python_params":["john doe","35"]}`) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  Important  These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis.',
    )
    python_named_params: Optional[Dict[str, Any]] = Field(
        None,
        description='A map from keys to values for jobs with Python wheel task, for example `"python_named_params": {"name": "task", "data": "dbfs:/path/to/data.json"}`.',
    )
    pipeline_params: Optional[RunParametersPipelineParams] = None
    sql_params: Optional[Dict[str, Any]] = Field(
        None,
        description='A map from keys to values for SQL tasks, for example `"sql_params": {"name": "john doe", "age": "35"}`. The SQL alert task does not support custom parameters.',
    )
    dbt_commands: Optional[List[StrictStr]] = Field(
        None,
        description='An array of commands to execute for jobs with the dbt task, for example `"dbt_commands": ["dbt deps", "dbt seed", "dbt run"]`',
    )
    __properties = [
        "run_id",
        "rerun_tasks",
        "latest_repair_id",
        "rerun_all_failed_tasks",
        "jar_params",
        "notebook_params",
        "python_params",
        "spark_submit_params",
        "python_named_params",
        "pipeline_params",
        "sql_params",
        "dbt_commands",
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
    def from_json(cls, json_str: str) -> JobsRunsRepairRequest:
        """Create an instance of JobsRunsRepairRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pipeline_params
        if self.pipeline_params:
            _dict["pipeline_params"] = self.pipeline_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobsRunsRepairRequest:
        """Create an instance of JobsRunsRepairRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return JobsRunsRepairRequest.parse_obj(obj)

        _obj = JobsRunsRepairRequest.parse_obj(
            {
                "run_id": obj.get("run_id"),
                "rerun_tasks": obj.get("rerun_tasks"),
                "latest_repair_id": obj.get("latest_repair_id"),
                "rerun_all_failed_tasks": obj.get("rerun_all_failed_tasks")
                if obj.get("rerun_all_failed_tasks") is not None
                else False,
                "jar_params": obj.get("jar_params"),
                "notebook_params": obj.get("notebook_params"),
                "python_params": obj.get("python_params"),
                "spark_submit_params": obj.get("spark_submit_params"),
                "python_named_params": obj.get("python_named_params"),
                "pipeline_params": RunParametersPipelineParams.from_dict(
                    obj.get("pipeline_params")
                )
                if obj.get("pipeline_params") is not None
                else None,
                "sql_params": obj.get("sql_params"),
                "dbt_commands": obj.get("dbt_commands"),
            }
        )
        return _obj
