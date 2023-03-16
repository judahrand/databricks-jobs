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

from pydantic import BaseModel, Field, StrictBool, StrictStr

from databricks_jobs.models.run_life_cycle_state import RunLifeCycleState
from databricks_jobs.models.run_result_state import RunResultState


class RunState(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    life_cycle_state: Optional[RunLifeCycleState] = None
    result_state: Optional[RunResultState] = None
    user_cancelled_or_timedout: Optional[StrictBool] = Field(
        None,
        description="Whether a run was canceled manually by a user or by the scheduler because the run timed out.",
    )
    state_message: Optional[StrictStr] = Field(
        None,
        description="A descriptive message for the current state. This field is unstructured, and its exact format is subject to change.",
    )
    __properties = [
        "life_cycle_state",
        "result_state",
        "user_cancelled_or_timedout",
        "state_message",
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
    def from_json(cls, json_str: str) -> RunState:
        """Create an instance of RunState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RunState:
        """Create an instance of RunState from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RunState.parse_obj(obj)

        _obj = RunState.parse_obj(
            {
                "life_cycle_state": obj.get("life_cycle_state"),
                "result_state": obj.get("result_state"),
                "user_cancelled_or_timedout": obj.get("user_cancelled_or_timedout"),
                "state_message": obj.get("state_message"),
            }
        )
        return _obj
