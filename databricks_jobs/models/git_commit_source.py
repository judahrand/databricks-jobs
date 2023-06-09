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

from databricks_jobs.models.git_provider import GitProvider
from databricks_jobs.models.git_snapshot import GitSnapshot


class GitCommitSource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    git_url: StrictStr = Field(
        ...,
        description="URL of the repository to be cloned by this job. The maximum length is 300 characters.",
    )
    git_provider: GitProvider = ...
    git_commit: StrictStr = Field(
        ...,
        description="Commit to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_tag. The maximum length is 64 characters.",
    )
    git_snapshot: Optional[GitSnapshot] = None
    __properties = ["git_url", "git_provider", "git_commit", "git_snapshot"]

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
    def from_json(cls, json_str: str) -> GitCommitSource:
        """Create an instance of GitCommitSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of git_snapshot
        if self.git_snapshot:
            _dict["git_snapshot"] = self.git_snapshot.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GitCommitSource:
        """Create an instance of GitCommitSource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GitCommitSource.parse_obj(obj)

        _obj = GitCommitSource.parse_obj(
            {
                "git_url": obj.get("git_url"),
                "git_provider": obj.get("git_provider"),
                "git_commit": obj.get("git_commit"),
                "git_snapshot": GitSnapshot.from_dict(obj.get("git_snapshot"))
                if obj.get("git_snapshot") is not None
                else None,
            }
        )
        return _obj
