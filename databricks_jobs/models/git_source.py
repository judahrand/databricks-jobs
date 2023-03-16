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
from typing import Any, List, Optional

from pydantic import BaseModel, Field, StrictStr, ValidationError, validator

from databricks_jobs.models.git_branch_source import GitBranchSource
from databricks_jobs.models.git_commit_source import GitCommitSource
from databricks_jobs.models.git_tag_source import GitTagSource

GITSOURCE_ONE_OF_SCHEMAS = ["GitBranchSource", "GitCommitSource", "GitTagSource"]


class GitSource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    # data type: GitBranchSource
    oneof_schema_1_validator: Optional[GitBranchSource] = None
    # data type: GitTagSource
    oneof_schema_2_validator: Optional[GitTagSource] = None
    # data type: GitCommitSource
    oneof_schema_3_validator: Optional[GitCommitSource] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(GITSOURCE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator("actual_instance")
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: GitBranchSource
        if type(v) is not GitBranchSource:
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `GitBranchSource`"
            )
        else:
            match += 1

        # validate data type: GitTagSource
        if type(v) is not GitTagSource:
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `GitTagSource`"
            )
        else:
            match += 1

        # validate data type: GitCommitSource
        if type(v) is not GitCommitSource:
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `GitCommitSource`"
            )
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError(
                "Multiple matches found when deserializing the JSON string into GitSource with oneOf schemas: GitBranchSource, GitCommitSource, GitTagSource. Details: "
                + ", ".join(error_messages)
            )
        elif match == 0:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into GitSource with oneOf schemas: GitBranchSource, GitCommitSource, GitTagSource. Details: "
                + ", ".join(error_messages)
            )
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> GitSource:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> GitSource:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into GitBranchSource
        try:
            instance.actual_instance = GitBranchSource.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into GitTagSource
        try:
            instance.actual_instance = GitTagSource.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into GitCommitSource
        try:
            instance.actual_instance = GitCommitSource.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError(
                "Multiple matches found when deserializing the JSON string into GitSource with oneOf schemas: GitBranchSource, GitCommitSource, GitTagSource. Details: "
                + ", ".join(error_messages)
            )
        elif match == 0:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into GitSource with oneOf schemas: GitBranchSource, GitCommitSource, GitTagSource. Details: "
                + ", ".join(error_messages)
            )
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())
