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

from pydantic import BaseModel, Field

from databricks_jobs.models.adlsgen2_info import Adlsgen2Info
from databricks_jobs.models.dbfs_storage_info import DbfsStorageInfo
from databricks_jobs.models.file_storage_info import FileStorageInfo
from databricks_jobs.models.s3_storage_info import S3StorageInfo


class InitScriptInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    dbfs: Optional[DbfsStorageInfo] = None
    file: Optional[FileStorageInfo] = None
    s3: Optional[S3StorageInfo] = Field(None, alias="S3")
    abfss: Optional[Adlsgen2Info] = None
    __properties = ["dbfs", "file", "S3", "abfss"]

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
    def from_json(cls, json_str: str) -> InitScriptInfo:
        """Create an instance of InitScriptInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of dbfs
        if self.dbfs:
            _dict["dbfs"] = self.dbfs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict["file"] = self.file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of s3
        if self.s3:
            _dict["S3"] = self.s3.to_dict()
        # override the default output from pydantic by calling `to_dict()` of abfss
        if self.abfss:
            _dict["abfss"] = self.abfss.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InitScriptInfo:
        """Create an instance of InitScriptInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return InitScriptInfo.parse_obj(obj)

        _obj = InitScriptInfo.parse_obj(
            {
                "dbfs": DbfsStorageInfo.from_dict(obj.get("dbfs"))
                if obj.get("dbfs") is not None
                else None,
                "file": FileStorageInfo.from_dict(obj.get("file"))
                if obj.get("file") is not None
                else None,
                "s3": S3StorageInfo.from_dict(obj.get("S3"))
                if obj.get("S3") is not None
                else None,
                "abfss": Adlsgen2Info.from_dict(obj.get("abfss"))
                if obj.get("abfss") is not None
                else None,
            }
        )
        return _obj
