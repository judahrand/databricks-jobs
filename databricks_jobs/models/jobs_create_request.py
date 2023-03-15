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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from databricks_jobs.models.access_control_request import AccessControlRequest
from databricks_jobs.models.cron_schedule import CronSchedule
from databricks_jobs.models.git_source import GitSource
from databricks_jobs.models.job_cluster import JobCluster
from databricks_jobs.models.job_email_notifications import JobEmailNotifications
from databricks_jobs.models.job_task_settings import JobTaskSettings
from databricks_jobs.models.webhook_notifications import WebhookNotifications


class JobsCreateRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    name: Optional[StrictStr] = Field(
        "Untitled", description="An optional name for the job."
    )
    tags: Optional[Dict[str, Any]] = Field(
        None,
        description="A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job.",
    )
    tasks: Optional[conlist(JobTaskSettings, max_items=100)] = Field(
        None, description="A list of task specifications to be executed by this job."
    )
    job_clusters: Optional[conlist(JobCluster, max_items=100)] = Field(
        None,
        description="A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.",
    )
    email_notifications: Optional[JobEmailNotifications] = None
    webhook_notifications: Optional[WebhookNotifications] = None
    timeout_seconds: Optional[StrictInt] = Field(
        None,
        description="An optional timeout applied to each run of this job. The default behavior is to have no timeout.",
    )
    schedule: Optional[CronSchedule] = None
    max_concurrent_runs: Optional[StrictInt] = Field(
        None,
        description="An optional maximum allowed number of concurrent runs of the job.  Set this value if you want to be able to execute multiple runs of the same job concurrently. This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters.  This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from then on, new runs are skipped unless there are fewer than 3 active runs.  This value cannot exceed 1000\\. Setting this value to 0 causes all new runs to be skipped. The default behavior is to allow only 1 concurrent run.",
    )
    git_source: Optional[GitSource] = None
    format: Optional[StrictStr] = Field(
        None,
        description='Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`.',
    )
    access_control_list: Optional[List[AccessControlRequest]] = Field(
        None, description="List of permissions to set on the job."
    )
    __properties = [
        "name",
        "tags",
        "tasks",
        "job_clusters",
        "email_notifications",
        "webhook_notifications",
        "timeout_seconds",
        "schedule",
        "max_concurrent_runs",
        "git_source",
        "format",
        "access_control_list",
    ]

    @validator("format")
    def format_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ("SINGLE_TASK", "MULTI_TASK"):
            raise ValueError(
                "must validate the enum values ('SINGLE_TASK', 'MULTI_TASK')"
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
    def from_json(cls, json_str: str) -> JobsCreateRequest:
        """Create an instance of JobsCreateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tasks (list)
        _items = []
        if self.tasks:
            for _item in self.tasks:
                if _item:
                    _items.append(_item.to_dict())
            _dict["tasks"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in job_clusters (list)
        _items = []
        if self.job_clusters:
            for _item in self.job_clusters:
                if _item:
                    _items.append(_item.to_dict())
            _dict["job_clusters"] = _items
        # override the default output from pydantic by calling `to_dict()` of email_notifications
        if self.email_notifications:
            _dict["email_notifications"] = self.email_notifications.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webhook_notifications
        if self.webhook_notifications:
            _dict["webhook_notifications"] = self.webhook_notifications.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict["schedule"] = self.schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of git_source
        if self.git_source:
            _dict["git_source"] = self.git_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in access_control_list (list)
        _items = []
        if self.access_control_list:
            for _item in self.access_control_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["access_control_list"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobsCreateRequest:
        """Create an instance of JobsCreateRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return JobsCreateRequest.parse_obj(obj)

        _obj = JobsCreateRequest.parse_obj(
            {
                "name": obj.get("name") if obj.get("name") is not None else "Untitled",
                "tags": obj.get("tags"),
                "tasks": [
                    JobTaskSettings.from_dict(_item) for _item in obj.get("tasks")
                ]
                if obj.get("tasks") is not None
                else None,
                "job_clusters": [
                    JobCluster.from_dict(_item) for _item in obj.get("job_clusters")
                ]
                if obj.get("job_clusters") is not None
                else None,
                "email_notifications": JobEmailNotifications.from_dict(
                    obj.get("email_notifications")
                )
                if obj.get("email_notifications") is not None
                else None,
                "webhook_notifications": WebhookNotifications.from_dict(
                    obj.get("webhook_notifications")
                )
                if obj.get("webhook_notifications") is not None
                else None,
                "timeout_seconds": obj.get("timeout_seconds"),
                "schedule": CronSchedule.from_dict(obj.get("schedule"))
                if obj.get("schedule") is not None
                else None,
                "max_concurrent_runs": obj.get("max_concurrent_runs"),
                "git_source": GitSource.from_dict(obj.get("git_source"))
                if obj.get("git_source") is not None
                else None,
                "format": obj.get("format"),
                "access_control_list": [
                    AccessControlRequest.from_dict(_item)
                    for _item in obj.get("access_control_list")
                ]
                if obj.get("access_control_list") is not None
                else None,
            }
        )
        return _obj