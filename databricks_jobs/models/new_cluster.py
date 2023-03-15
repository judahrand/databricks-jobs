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

from databricks_jobs.models.auto_scale import AutoScale
from databricks_jobs.models.azure_attributes import AzureAttributes
from databricks_jobs.models.cluster_log_conf import ClusterLogConf
from databricks_jobs.models.docker_image import DockerImage
from databricks_jobs.models.init_script_info import InitScriptInfo


class NewCluster(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    num_workers: Optional[StrictInt] = Field(
        None,
        description="If num_workers, number of worker nodes that this cluster must have. A cluster has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual current number of workers. For example, if a cluster is resized from 5 to 10 workers, this field immediately updates to reflect the target size of 10 workers, whereas the workers listed in `spark_info` gradually increase from 5 to 10 as the new nodes are provisioned.",
    )
    autoscale: Optional[AutoScale] = None
    spark_version: StrictStr = Field(
        ...,
        description="The Spark version of the cluster. A list of available Spark versions can be retrieved by using the [Runtime versions](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#runtime-versions) API call.",
    )
    spark_conf: Optional[Dict[str, Any]] = Field(
        None,
        description="An arbitrary object where the object key is a configuration propery name and the value is a configuration property value.",
    )
    azure_attributes: Optional[AzureAttributes] = None
    node_type_id: Optional[StrictStr] = Field(
        None,
        description="This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads A list of available node types can be retrieved by using the [List node types](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#list-node-types) API call.",
    )
    driver_node_type_id: Optional[StrictStr] = Field(
        None,
        description="The node type of the Spark driver. This field is optional; if unset, the driver node type is set as the same value as `node_type_id` defined above.",
    )
    custom_tags: Optional[Dict[str, StrictStr]] = Field(
        None,
        description="An object with key value pairs. The key length must be between 1 and 127 UTF-8 characters, inclusive. The value length must be less than or equal to 255 UTF-8 characters.",
    )
    cluster_log_conf: Optional[ClusterLogConf] = None
    init_scripts: Optional[List[InitScriptInfo]] = Field(
        None,
        description="The configuration for storing init scripts. Any number of scripts can be specified. The scripts are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script logs are sent to `<destination>/<cluster-id>/init_scripts`.",
    )
    spark_env_vars: Optional[Dict[str, Any]] = Field(
        None,
        description="An arbitrary object where the object key is an environment variable name and the value is an environment variable value.",
    )
    enable_elastic_disk: Optional[StrictBool] = Field(
        None,
        description="Autoscaling Local Storage: when enabled, this cluster dynamically acquires additional disk space when its Spark workers are running low on disk space. Refer to [Autoscaling local storage](https://docs.microsoft.com/azure/databricks/clusters/configure#autoscaling-local-storage-azure) for details.",
    )
    instance_pool_id: Optional[StrictStr] = Field(
        None,
        description="The optional ID of the instance pool to use for cluster nodes. If `driver_instance_pool_id` is present, `instance_pool_id` is used for worker nodes only. Otherwise, it is used for both the driver node and worker nodes. Refer to [Instance Pools API](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/instance-pools) for details.",
    )
    policy_id: Optional[StrictStr] = Field(
        None,
        description="A [cluster policy](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/policies) ID. Either `node_type_id` or `instance_pool_id` must be specified in the cluster policy if they are not specified in this job cluster object.",
    )
    enable_local_disk_encryption: Optional[StrictBool] = Field(
        None,
        description="Determines whether encryption of disks locally attached to the cluster is enabled.",
    )
    docker_image: Optional[DockerImage] = None
    runtime_engine: Optional[StrictStr] = Field(
        None,
        description="The type of runtime engine to use. If not specified, the runtime engine type is inferred based on the `spark_version` value. Allowed values include:  * `PHOTON`: Use the Photon runtime engine type. * `STANDARD`: Use the standard runtime engine type.  This field is optional.",
    )
    additional_properties: Dict[str, Any] = {}
    __properties = [
        "num_workers",
        "autoscale",
        "spark_version",
        "spark_conf",
        "azure_attributes",
        "node_type_id",
        "driver_node_type_id",
        "custom_tags",
        "cluster_log_conf",
        "init_scripts",
        "spark_env_vars",
        "enable_elastic_disk",
        "instance_pool_id",
        "policy_id",
        "enable_local_disk_encryption",
        "docker_image",
        "runtime_engine",
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
    def from_json(cls, json_str: str) -> NewCluster:
        """Create an instance of NewCluster from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True, exclude={"additional_properties"}, exclude_none=True
        )
        # override the default output from pydantic by calling `to_dict()` of autoscale
        if self.autoscale:
            _dict["autoscale"] = self.autoscale.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_attributes
        if self.azure_attributes:
            _dict["azure_attributes"] = self.azure_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cluster_log_conf
        if self.cluster_log_conf:
            _dict["cluster_log_conf"] = self.cluster_log_conf.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in init_scripts (list)
        _items = []
        if self.init_scripts:
            for _item in self.init_scripts:
                if _item:
                    _items.append(_item.to_dict())
            _dict["init_scripts"] = _items
        # override the default output from pydantic by calling `to_dict()` of docker_image
        if self.docker_image:
            _dict["docker_image"] = self.docker_image.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NewCluster:
        """Create an instance of NewCluster from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NewCluster.parse_obj(obj)

        _obj = NewCluster.parse_obj(
            {
                "num_workers": obj.get("num_workers"),
                "autoscale": AutoScale.from_dict(obj.get("autoscale"))
                if obj.get("autoscale") is not None
                else None,
                "spark_version": obj.get("spark_version"),
                "spark_conf": obj.get("spark_conf"),
                "azure_attributes": AzureAttributes.from_dict(
                    obj.get("azure_attributes")
                )
                if obj.get("azure_attributes") is not None
                else None,
                "node_type_id": obj.get("node_type_id"),
                "driver_node_type_id": obj.get("driver_node_type_id"),
                "custom_tags": obj.get("custom_tags"),
                "cluster_log_conf": ClusterLogConf.from_dict(
                    obj.get("cluster_log_conf")
                )
                if obj.get("cluster_log_conf") is not None
                else None,
                "init_scripts": [
                    InitScriptInfo.from_dict(_item) for _item in obj.get("init_scripts")
                ]
                if obj.get("init_scripts") is not None
                else None,
                "spark_env_vars": obj.get("spark_env_vars"),
                "enable_elastic_disk": obj.get("enable_elastic_disk"),
                "instance_pool_id": obj.get("instance_pool_id"),
                "policy_id": obj.get("policy_id"),
                "enable_local_disk_encryption": obj.get("enable_local_disk_encryption"),
                "docker_image": DockerImage.from_dict(obj.get("docker_image"))
                if obj.get("docker_image") is not None
                else None,
                "runtime_engine": obj.get("runtime_engine"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
