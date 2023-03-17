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

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

from databricks_jobs.models.auto_scale import AutoScale
from databricks_jobs.models.aws_attributes import AwsAttributes
from databricks_jobs.models.azure_attributes import AzureAttributes
from databricks_jobs.models.cluster_log_conf import ClusterLogConf
from databricks_jobs.models.cluster_source import ClusterSource
from databricks_jobs.models.cluster_state import ClusterState
from databricks_jobs.models.docker_image import DockerImage
from databricks_jobs.models.gcp_attributes import GcpAttributes
from databricks_jobs.models.init_script_info import InitScriptInfo
from databricks_jobs.models.log_sync_status import LogSyncStatus
from databricks_jobs.models.spark_node import SparkNode
from databricks_jobs.models.termination_reason import TerminationReason


class ClusterInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    num_workers: Optional[StrictInt] = Field(
        None,
        description="If num_workers, number of worker nodes that this cluster must have. A cluster has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. **Note:** When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field is immediately updated to reflect the target size of 10 workers, whereas the workers listed in `executors` gradually increase from 5 to 10 as the new nodes are provisioned.",
    )
    autoscale: Optional[AutoScale] = None
    cluster_id: Optional[StrictStr] = Field(
        None,
        description="Canonical identifier for the cluster. This ID is retained during cluster restarts and resizes, while each new cluster has a globally unique ID.",
    )
    creator_user_name: Optional[StrictStr] = Field(
        None,
        description="Creator user name. The field won’t be included in the response if the user has already been deleted.",
    )
    driver: Optional[SparkNode] = None
    executors: Optional[List[SparkNode]] = Field(
        None, description="Nodes on which the Spark executors reside."
    )
    spark_context_id: Optional[StrictInt] = Field(
        None,
        description="A canonical SparkContext identifier. This value _does_ change when the Spark driver restarts. The pair `(cluster_id, spark_context_id)` is a globally unique identifier over all Spark contexts.",
    )
    jdbc_port: Optional[StrictInt] = Field(
        None,
        description="Port on which Spark JDBC server is listening in the driver node. No service listens on this port in executor nodes.",
    )
    cluster_name: Optional[StrictStr] = Field(
        None,
        description="Cluster name requested by the user. This doesn’t have to be unique. If not specified at creation, the cluster name is an empty string.",
    )
    spark_version: Optional[StrictStr] = Field(
        None,
        description="The runtime version of the cluster. You can retrieve a list of available runtime versions by using the [Runtime versions](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#runtime-versions) API call.",
    )
    spark_conf: Optional[Dict[str, Any]] = Field(
        None,
        description="An arbitrary object where the object key is a configuration propery name and the value is a configuration property value.",
    )
    aws_attributes: Optional[AwsAttributes] = None
    node_type_id: Optional[StrictStr] = Field(
        None,
        description="This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the [List node types](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#list-node-types) API call.",
    )
    driver_node_type_id: Optional[StrictStr] = Field(
        None,
        description="The node type of the Spark driver. This field is optional; if unset, the driver node type is set as the same value as `node_type_id` defined above.",
    )
    ssh_public_keys: Optional[List[StrictStr]] = Field(
        None, description="Set to empty array. Cluster SSH is not supported."
    )
    custom_tags: Optional[List[Dict[str, StrictStr]]] = Field(
        None,
        description="An object containing a set of tags for cluster resources. Databricks tags all cluster resources (such as VMs) with these tags in addition to default_tags. **Note**: * Tags are not supported on legacy node types such as compute-optimized and memory-optimized * Databricks allows at most 45 custom tags",
    )
    cluster_log_conf: Optional[ClusterLogConf] = None
    init_scripts: Optional[List[InitScriptInfo]] = Field(
        None,
        description="The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script logs are sent to `<destination>/<cluster-ID>/init_scripts`.",
    )
    docker_image: Optional[DockerImage] = None
    spark_env_vars: Optional[Dict[str, Any]] = Field(
        None,
        description="An arbitrary object where the object key is an environment variable name and the value is an environment variable value.",
    )
    autotermination_minutes: Optional[StrictInt] = Field(
        None,
        description="Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster is not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. You can also set this value to 0 to explicitly disable automatic termination.",
    )
    enable_elastic_disk: Optional[StrictBool] = Field(
        None,
        description="Autoscaling Local Storage: when enabled, this cluster dynamically acquires additional disk space when its Spark workers are running low on disk space. See [Autoscaling local storage](https://docs.microsoft.com/azure/databricks/clusters/configure#autoscaling-local-storage-azure) for details.",
    )
    instance_pool_id: Optional[StrictStr] = Field(
        None,
        description="The optional ID of the instance pool to which the cluster belongs. Refer to [Pools](https://docs.microsoft.com/azure/databricks/clusters/pools) for details.",
    )
    cluster_source: Optional[ClusterSource] = None
    state: Optional[ClusterState] = None
    state_message: Optional[StrictStr] = Field(
        None,
        description="A message associated with the most recent state transition (for example, the reason why the cluster entered a `TERMINATED` state). This field is unstructured, and its exact format is subject to change.",
    )
    start_time: Optional[StrictInt] = Field(
        None,
        description="Time (in epoch milliseconds) when the cluster creation request was received (when the cluster entered a `PENDING` state).",
    )
    terminated_time: Optional[StrictInt] = Field(
        None,
        description="Time (in epoch milliseconds) when the cluster was terminated, if applicable.",
    )
    last_state_loss_time: Optional[StrictInt] = Field(
        None,
        description="Time when the cluster driver last lost its state (due to a restart or driver failure).",
    )
    last_activity_time: Optional[StrictInt] = Field(
        None,
        description="Time (in epoch milliseconds) when the cluster was last active. A cluster is active if there is at least one command that has not finished on the cluster. This field is available after the cluster has reached a `RUNNING` state. Updates to this field are made as best-effort attempts. Certain versions of Spark do not support reporting of cluster activity. Refer to [Automatic termination](https://docs.microsoft.com/azure/databricks/clusters/clusters-manage#automatic-termination) for details.",
    )
    cluster_memory_mb: Optional[StrictInt] = Field(
        None, description="Total amount of cluster memory, in megabytes."
    )
    cluster_cores: Optional[StrictFloat] = Field(
        None,
        description="Number of CPU cores available for this cluster. This can be fractional since certain node types are configured to share cores between Spark nodes on the same instance.",
    )
    default_tags: Optional[Dict[str, StrictStr]] = Field(
        None,
        description="An object with key value pairs. The key length must be between 1 and 127 UTF-8 characters, inclusive. The value length must be less than or equal to 255 UTF-8 characters.",
    )
    cluster_log_status: Optional[LogSyncStatus] = None
    termination_reason: Optional[TerminationReason] = None
    gcp_attributes: Optional[GcpAttributes] = None
    azure_attributes: Optional[AzureAttributes] = None
    __properties = [
        "num_workers",
        "autoscale",
        "cluster_id",
        "creator_user_name",
        "driver",
        "executors",
        "spark_context_id",
        "jdbc_port",
        "cluster_name",
        "spark_version",
        "spark_conf",
        "aws_attributes",
        "node_type_id",
        "driver_node_type_id",
        "ssh_public_keys",
        "custom_tags",
        "cluster_log_conf",
        "init_scripts",
        "docker_image",
        "spark_env_vars",
        "autotermination_minutes",
        "enable_elastic_disk",
        "instance_pool_id",
        "cluster_source",
        "state",
        "state_message",
        "start_time",
        "terminated_time",
        "last_state_loss_time",
        "last_activity_time",
        "cluster_memory_mb",
        "cluster_cores",
        "default_tags",
        "cluster_log_status",
        "termination_reason",
        "gcp_attributes",
        "azure_attributes",
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
    def from_json(cls, json_str: str) -> ClusterInfo:
        """Create an instance of ClusterInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of autoscale
        if self.autoscale:
            _dict["autoscale"] = self.autoscale.to_dict()
        # override the default output from pydantic by calling `to_dict()` of driver
        if self.driver:
            _dict["driver"] = self.driver.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in executors (list)
        _items = []
        if self.executors:
            for _item in self.executors:
                if _item:
                    _items.append(_item.to_dict())
            _dict["executors"] = _items
        # override the default output from pydantic by calling `to_dict()` of aws_attributes
        if self.aws_attributes:
            _dict["aws_attributes"] = self.aws_attributes.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of cluster_log_status
        if self.cluster_log_status:
            _dict["cluster_log_status"] = self.cluster_log_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of termination_reason
        if self.termination_reason:
            _dict["termination_reason"] = self.termination_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_attributes
        if self.gcp_attributes:
            _dict["gcp_attributes"] = self.gcp_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_attributes
        if self.azure_attributes:
            _dict["azure_attributes"] = self.azure_attributes.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterInfo:
        """Create an instance of ClusterInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ClusterInfo.parse_obj(obj)

        _obj = ClusterInfo.parse_obj(
            {
                "num_workers": obj.get("num_workers"),
                "autoscale": AutoScale.from_dict(obj.get("autoscale"))
                if obj.get("autoscale") is not None
                else None,
                "cluster_id": obj.get("cluster_id"),
                "creator_user_name": obj.get("creator_user_name"),
                "driver": SparkNode.from_dict(obj.get("driver"))
                if obj.get("driver") is not None
                else None,
                "executors": [
                    SparkNode.from_dict(_item) for _item in obj.get("executors")
                ]
                if obj.get("executors") is not None
                else None,
                "spark_context_id": obj.get("spark_context_id"),
                "jdbc_port": obj.get("jdbc_port"),
                "cluster_name": obj.get("cluster_name"),
                "spark_version": obj.get("spark_version"),
                "spark_conf": obj.get("spark_conf"),
                "aws_attributes": AwsAttributes.from_dict(obj.get("aws_attributes"))
                if obj.get("aws_attributes") is not None
                else None,
                "node_type_id": obj.get("node_type_id"),
                "driver_node_type_id": obj.get("driver_node_type_id"),
                "ssh_public_keys": obj.get("ssh_public_keys"),
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
                "docker_image": DockerImage.from_dict(obj.get("docker_image"))
                if obj.get("docker_image") is not None
                else None,
                "spark_env_vars": obj.get("spark_env_vars"),
                "autotermination_minutes": obj.get("autotermination_minutes"),
                "enable_elastic_disk": obj.get("enable_elastic_disk"),
                "instance_pool_id": obj.get("instance_pool_id"),
                "cluster_source": obj.get("cluster_source"),
                "state": obj.get("state"),
                "state_message": obj.get("state_message"),
                "start_time": obj.get("start_time"),
                "terminated_time": obj.get("terminated_time"),
                "last_state_loss_time": obj.get("last_state_loss_time"),
                "last_activity_time": obj.get("last_activity_time"),
                "cluster_memory_mb": obj.get("cluster_memory_mb"),
                "cluster_cores": obj.get("cluster_cores"),
                "default_tags": obj.get("default_tags"),
                "cluster_log_status": LogSyncStatus.from_dict(
                    obj.get("cluster_log_status")
                )
                if obj.get("cluster_log_status") is not None
                else None,
                "termination_reason": TerminationReason.from_dict(
                    obj.get("termination_reason")
                )
                if obj.get("termination_reason") is not None
                else None,
                "gcp_attributes": GcpAttributes.from_dict(obj.get("gcp_attributes"))
                if obj.get("gcp_attributes") is not None
                else None,
                "azure_attributes": AzureAttributes.from_dict(
                    obj.get("azure_attributes")
                )
                if obj.get("azure_attributes") is not None
                else None,
            }
        )
        return _obj
