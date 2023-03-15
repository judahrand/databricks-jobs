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

from databricks_jobs.models.maven_library import MavenLibrary
from databricks_jobs.models.python_py_pi_library import PythonPyPiLibrary
from databricks_jobs.models.r_cran_library import RCranLibrary


class Library(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    jar: Optional[StrictStr] = Field(
        None,
        description='If jar, URI of the JAR to be installed. DBFS and ADLS (`abfss`) URIs are supported. For example: `{ "jar": "dbfs:/mnt/databricks/library.jar" }` or `{ "jar": "abfss://my-bucket/library.jar" }`. If ADLS is used, make sure the cluster has read access on the library.',
    )
    egg: Optional[StrictStr] = Field(
        None,
        description='If egg, URI of the egg to be installed. DBFS and ADLS URIs are supported. For example: `{ "egg": "dbfs:/my/egg" }` or `{ "egg": "abfss://my-bucket/egg" }`.',
    )
    whl: Optional[StrictStr] = Field(
        None,
        description='If whl, URI of the wheel or zipped wheels to be installed. DBFS and ADLS URIs are supported. For example: `{ "whl": "dbfs:/my/whl" }` or `{ "whl": "abfss://my-bucket/whl" }`. If ADLS is used, make sure the cluster has read access on the library. Also the wheel file name needs to use the [correct convention](https://www.python.org/dev/peps/pep-0427/#file-format). If zipped wheels are to be installed, the file name suffix should be `.wheelhouse.zip`.',
    )
    pypi: Optional[PythonPyPiLibrary] = None
    maven: Optional[MavenLibrary] = None
    cran: Optional[RCranLibrary] = None
    __properties = ["jar", "egg", "whl", "pypi", "maven", "cran"]

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
    def from_json(cls, json_str: str) -> Library:
        """Create an instance of Library from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pypi
        if self.pypi:
            _dict["pypi"] = self.pypi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maven
        if self.maven:
            _dict["maven"] = self.maven.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cran
        if self.cran:
            _dict["cran"] = self.cran.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Library:
        """Create an instance of Library from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Library.parse_obj(obj)

        _obj = Library.parse_obj(
            {
                "jar": obj.get("jar"),
                "egg": obj.get("egg"),
                "whl": obj.get("whl"),
                "pypi": PythonPyPiLibrary.from_dict(obj.get("pypi"))
                if obj.get("pypi") is not None
                else None,
                "maven": MavenLibrary.from_dict(obj.get("maven"))
                if obj.get("maven") is not None
                else None,
                "cran": RCranLibrary.from_dict(obj.get("cran"))
                if obj.get("cran") is not None
                else None,
            }
        )
        return _obj
