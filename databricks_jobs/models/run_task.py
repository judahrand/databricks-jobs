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

from pydantic import BaseModel, Field, StrictInt, StrictStr, constr, validator

from databricks_jobs.models.cluster_instance import ClusterInstance
from databricks_jobs.models.dbt_task import DbtTask
from databricks_jobs.models.git_source import GitSource
from databricks_jobs.models.library import Library
from databricks_jobs.models.new_task_cluster import NewTaskCluster
from databricks_jobs.models.notebook_task import NotebookTask
from databricks_jobs.models.pipeline_task import PipelineTask
from databricks_jobs.models.python_wheel_task import PythonWheelTask
from databricks_jobs.models.run_state import RunState
from databricks_jobs.models.spark_jar_task import SparkJarTask
from databricks_jobs.models.spark_python_task import SparkPythonTask
from databricks_jobs.models.sql_task import SqlTask
from databricks_jobs.models.task_dependencies_inner import TaskDependenciesInner
from databricks_jobs.models.task_spark_submit_task import TaskSparkSubmitTask


class RunTask(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    run_id: Optional[StrictInt] = Field(None, description="The ID of the task run.")
    task_key: Optional[constr(strict=True, max_length=100, min_length=1)] = Field(
        None,
        description="A unique name for the task. This field is used to refer to this task from other tasks. This field is required and must be unique within its parent job. On Update or Reset, this field is used to reference the tasks to be updated or reset. The maximum length is 100 characters.",
    )
    description: Optional[constr(strict=True, max_length=4096)] = Field(
        None,
        description="An optional description for this task. The maximum length is 4096 bytes.",
    )
    state: Optional[RunState] = None
    depends_on: Optional[List[TaskDependenciesInner]] = Field(
        None,
        description="An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task. The key is `task_key`, and the value is the name assigned to the dependent task. This field is required when a job consists of more than one task.",
    )
    existing_cluster_id: Optional[StrictStr] = Field(
        None,
        description="If existing_cluster_id, the ID of an existing cluster that is used for all runs of this job. When running jobs on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs on new clusters for greater reliability.",
    )
    new_cluster: Optional[NewTaskCluster] = None
    libraries: Optional[List[Library]] = Field(
        None,
        description="An optional list of libraries to be installed on the cluster that executes the job. The default value is an empty list.",
    )
    notebook_task: Optional[NotebookTask] = None
    spark_jar_task: Optional[SparkJarTask] = None
    spark_python_task: Optional[SparkPythonTask] = None
    spark_submit_task: Optional[TaskSparkSubmitTask] = None
    pipeline_task: Optional[PipelineTask] = None
    python_wheel_task: Optional[PythonWheelTask] = None
    sql_task: Optional[SqlTask] = None
    dbt_task: Optional[DbtTask] = None
    start_time: Optional[StrictInt] = Field(
        None,
        description="The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued.",
    )
    setup_duration: Optional[StrictInt] = Field(
        None,
        description="The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `setup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.",
    )
    execution_duration: Optional[StrictInt] = Field(
        None,
        description="The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error.",
    )
    cleanup_duration: Optional[StrictInt] = Field(
        None,
        description="The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The total duration of the run is the sum of the setup_duration, the execution_duration, and the cleanup_duration.",
    )
    end_time: Optional[StrictInt] = Field(
        None,
        description="The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running.",
    )
    attempt_number: Optional[StrictInt] = Field(
        None,
        description="The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0\\. If the initial run attempt fails, and the job has a retry policy (`max_retries` \\> 0), subsequent runs are created with an `original_attempt_run_id` of the original attempt’s ID and an incrementing `attempt_number`. Runs are retried only until they succeed, and the maximum `attempt_number` is the same as the `max_retries` value for the job.",
    )
    cluster_instance: Optional[ClusterInstance] = None
    git_source: Optional[GitSource] = None
    __properties = [
        "run_id",
        "task_key",
        "description",
        "state",
        "depends_on",
        "existing_cluster_id",
        "new_cluster",
        "libraries",
        "notebook_task",
        "spark_jar_task",
        "spark_python_task",
        "spark_submit_task",
        "pipeline_task",
        "python_wheel_task",
        "sql_task",
        "dbt_task",
        "start_time",
        "setup_duration",
        "execution_duration",
        "cleanup_duration",
        "end_time",
        "attempt_number",
        "cluster_instance",
        "git_source",
    ]

    @validator("task_key")
    def task_key_validate_regular_expression(cls, v):
        if not re.match(r"^[\w\-]+$", v):
            raise ValueError(r"must validate the regular expression /^[\w\-]+$/")
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
    def from_json(cls, json_str: str) -> RunTask:
        """Create an instance of RunTask from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict["state"] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in depends_on (list)
        _items = []
        if self.depends_on:
            for _item in self.depends_on:
                if _item:
                    _items.append(_item.to_dict())
            _dict["depends_on"] = _items
        # override the default output from pydantic by calling `to_dict()` of new_cluster
        if self.new_cluster:
            _dict["new_cluster"] = self.new_cluster.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in libraries (list)
        _items = []
        if self.libraries:
            for _item in self.libraries:
                if _item:
                    _items.append(_item.to_dict())
            _dict["libraries"] = _items
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
        # override the default output from pydantic by calling `to_dict()` of cluster_instance
        if self.cluster_instance:
            _dict["cluster_instance"] = self.cluster_instance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of git_source
        if self.git_source:
            _dict["git_source"] = self.git_source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RunTask:
        """Create an instance of RunTask from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RunTask.parse_obj(obj)

        _obj = RunTask.parse_obj(
            {
                "run_id": obj.get("run_id"),
                "task_key": obj.get("task_key"),
                "description": obj.get("description"),
                "state": RunState.from_dict(obj.get("state"))
                if obj.get("state") is not None
                else None,
                "depends_on": [
                    TaskDependenciesInner.from_dict(_item)
                    for _item in obj.get("depends_on")
                ]
                if obj.get("depends_on") is not None
                else None,
                "existing_cluster_id": obj.get("existing_cluster_id"),
                "new_cluster": NewTaskCluster.from_dict(obj.get("new_cluster"))
                if obj.get("new_cluster") is not None
                else None,
                "libraries": [
                    Library.from_dict(_item) for _item in obj.get("libraries")
                ]
                if obj.get("libraries") is not None
                else None,
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
                "spark_submit_task": TaskSparkSubmitTask.from_dict(
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
                "start_time": obj.get("start_time"),
                "setup_duration": obj.get("setup_duration"),
                "execution_duration": obj.get("execution_duration"),
                "cleanup_duration": obj.get("cleanup_duration"),
                "end_time": obj.get("end_time"),
                "attempt_number": obj.get("attempt_number"),
                "cluster_instance": ClusterInstance.from_dict(
                    obj.get("cluster_instance")
                )
                if obj.get("cluster_instance") is not None
                else None,
                "git_source": GitSource.from_dict(obj.get("git_source"))
                if obj.get("git_source") is not None
                else None,
            }
        )
        return _obj
