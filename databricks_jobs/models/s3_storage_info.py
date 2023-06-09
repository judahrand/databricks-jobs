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


class S3StorageInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    destination: Optional[StrictStr] = Field(
        None,
        description="S3 destination. For example: `s3://my-bucket/some-prefix` You must configure the cluster with an instance profile and the instance profile must have write access to the destination. You _cannot_ use AWS keys.",
    )
    region: Optional[StrictStr] = Field(
        None,
        description="S3 region. For example: `us-west-2`. Either region or endpoint must be set. If both are set, endpoint is used.",
    )
    endpoint: Optional[StrictStr] = Field(
        None,
        description="S3 endpoint. For example: `https://s3-us-west-2.amazonaws.com`. Either region or endpoint must be set. If both are set, endpoint is used.",
    )
    enable_encryption: Optional[StrictBool] = Field(
        None, description="(Optional)Enable server side encryption, `false` by default."
    )
    encryption_type: Optional[StrictStr] = Field(
        None,
        description="(Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It is used only when encryption is enabled and the default type is `sse-s3`.",
    )
    kms_key: Optional[StrictStr] = Field(
        None,
        description="(Optional) KMS key used if encryption is enabled and encryption type is set to `sse-kms`.",
    )
    canned_acl: Optional[StrictStr] = Field(
        None,
        description="(Optional) Set canned access control list. For example: `bucket-owner-full-control`. If canned_acl is set, the cluster instance profile must have `s3:PutObjectAcl` permission on the destination bucket and prefix. The full list of possible canned ACLs can be found at <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>. By default only the object owner gets full control. If you are using cross account role for writing data, you may want to set `bucket-owner-full-control` to make bucket owner able to read the logs.",
    )
    __properties = [
        "destination",
        "region",
        "endpoint",
        "enable_encryption",
        "encryption_type",
        "kms_key",
        "canned_acl",
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
    def from_json(cls, json_str: str) -> S3StorageInfo:
        """Create an instance of S3StorageInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> S3StorageInfo:
        """Create an instance of S3StorageInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return S3StorageInfo.parse_obj(obj)

        _obj = S3StorageInfo.parse_obj(
            {
                "destination": obj.get("destination"),
                "region": obj.get("region"),
                "endpoint": obj.get("endpoint"),
                "enable_encryption": obj.get("enable_encryption"),
                "encryption_type": obj.get("encryption_type"),
                "kms_key": obj.get("kms_key"),
                "canned_acl": obj.get("canned_acl"),
            }
        )
        return _obj
