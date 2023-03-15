from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cluster_state import ClusterState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_scale import AutoScale
    from ..models.azure_attributes import AzureAttributes
    from ..models.cluster_log_conf import ClusterLogConf
    from ..models.cluster_tag import ClusterTag
    from ..models.docker_image import DockerImage
    from ..models.init_script_info import InitScriptInfo
    from ..models.log_sync_status import LogSyncStatus
    from ..models.spark_conf_pair import SparkConfPair
    from ..models.spark_env_pair import SparkEnvPair
    from ..models.spark_node import SparkNode
    from ..models.termination_reason import TerminationReason


T = TypeVar("T", bound="ClusterInfo")


@attr.s(auto_attribs=True)
class ClusterInfo:
    """
    Attributes:
        num_workers (Union[Unset, int]): If num_workers, number of worker nodes that this cluster must have. A cluster
            has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. **Note:** When
            reading the properties of a cluster, this field reflects the desired number of workers rather than the actual
            number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field is immediately updated
            to reflect the target size of 10 workers, whereas the workers listed in `executors` gradually increase from 5 to
            10 as the new nodes are provisioned.
        autoscale (Union[Unset, AutoScale]):
        cluster_id (Union[Unset, str]): Canonical identifier for the cluster. This ID is retained during cluster
            restarts and resizes, while each new cluster has a globally unique ID.
        creator_user_name (Union[Unset, str]): Creator user name. The field won’t be included in the response if the
            user has already been deleted.
        driver (Union[Unset, SparkNode]):
        executors (Union[Unset, List['SparkNode']]): Nodes on which the Spark executors reside.
        spark_context_id (Union[Unset, int]): A canonical SparkContext identifier. This value _does_ change when the
            Spark driver restarts. The pair `(cluster_id, spark_context_id)` is a globally unique identifier over all Spark
            contexts.
        jdbc_port (Union[Unset, int]): Port on which Spark JDBC server is listening in the driver node. No service
            listens on this port in executor nodes.
        cluster_name (Union[Unset, str]): Cluster name requested by the user. This doesn’t have to be unique. If not
            specified at creation, the cluster name is an empty string.
        spark_version (Union[Unset, str]): The runtime version of the cluster. You can retrieve a list of available
            runtime versions by using the [Runtime versions](https://docs.microsoft.com/azure/databricks/dev-
            tools/api/latest/clusters#runtime-versions) API call.
        spark_conf (Union[Unset, SparkConfPair]): An arbitrary object where the object key is a configuration propery
            name and the value is a configuration property value.
        azure_attributes (Union[Unset, AzureAttributes]):
        node_type_id (Union[Unset, str]): This field encodes, through a single value, the resources available to each of
            the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or
            compute intensive workloads. A list of available node types can be retrieved by using the [List node
            types](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#list-node-types) API call.
        driver_node_type_id (Union[Unset, str]): The node type of the Spark driver. This field is optional; if unset,
            the driver node type is set as the same value as `node_type_id` defined above.
        custom_tags (Union[Unset, List['ClusterTag']]): An object containing a set of tags for cluster resources.
            Databricks tags all cluster resources (such as VMs) with these tags in addition to default_tags. **Note**: *
            Tags are not supported on legacy node types such as compute-optimized and memory-optimized * Databricks allows
            at most 45 custom tags
        cluster_log_conf (Union[Unset, ClusterLogConf]):
        init_scripts (Union[Unset, List['InitScriptInfo']]): The configuration for storing init scripts. Any number of
            destinations can be specified. The scripts are executed sequentially in the order provided. If
            `cluster_log_conf` is specified, init script logs are sent to `<destination>/<cluster-ID>/init_scripts`.
        docker_image (Union[Unset, DockerImage]):
        spark_env_vars (Union[Unset, SparkEnvPair]): An arbitrary object where the object key is an environment variable
            name and the value is an environment variable value.
        autotermination_minutes (Union[Unset, int]): Automatically terminates the cluster after it is inactive for this
            time in minutes. If not set, this cluster is not be automatically terminated. If specified, the threshold must
            be between 10 and 10000 minutes. You can also set this value to 0 to explicitly disable automatic termination.
        enable_elastic_disk (Union[Unset, bool]): Autoscaling Local Storage: when enabled, this cluster dynamically
            acquires additional disk space when its Spark workers are running low on disk space. See [Autoscaling local
            storage](https://docs.microsoft.com/azure/databricks/clusters/configure#autoscaling-local-storage-azure) for
            details.
        instance_pool_id (Union[Unset, str]): The optional ID of the instance pool to which the cluster belongs. Refer
            to [Pools](https://docs.microsoft.com/azure/databricks/clusters/pools) for details.
        state (Union[Unset, ClusterState]): * PENDING: Indicates that a cluster is in the process of being created.
            * RUNNING: Indicates that a cluster has been started and is ready for use.
            * RESTARTING: Indicates that a cluster is in the process of restarting.
            * RESIZING: Indicates that a cluster is in the process of adding or removing nodes.
            * TERMINATING: Indicates that a cluster is in the process of being destroyed.
            * TERMINATED: Indicates that a cluster has been successfully destroyed.
            * ERROR: This state is no longer used. It was used to indicate a cluster that failed to be created.
            `TERMINATING` and `TERMINATED` are used instead.
            * UNKNOWN: Indicates that a cluster is in an unknown state. A cluster should never be in this state.
        state_message (Union[Unset, str]): A message associated with the most recent state transition (for example, the
            reason why the cluster entered a `TERMINATED` state). This field is unstructured, and its exact format is
            subject to change.
        start_time (Union[Unset, int]): Time (in epoch milliseconds) when the cluster creation request was received
            (when the cluster entered a `PENDING` state).
        terminated_time (Union[Unset, int]): Time (in epoch milliseconds) when the cluster was terminated, if
            applicable.
        last_state_loss_time (Union[Unset, int]): Time when the cluster driver last lost its state (due to a restart or
            driver failure).
        last_activity_time (Union[Unset, int]): Time (in epoch milliseconds) when the cluster was last active. A cluster
            is active if there is at least one command that has not finished on the cluster. This field is available after
            the cluster has reached a `RUNNING` state. Updates to this field are made as best-effort attempts. Certain
            versions of Spark do not support reporting of cluster activity. Refer to [Automatic
            termination](https://docs.microsoft.com/azure/databricks/clusters/clusters-manage#automatic-termination) for
            details.
        cluster_memory_mb (Union[Unset, int]): Total amount of cluster memory, in megabytes.
        cluster_cores (Union[Unset, float]): Number of CPU cores available for this cluster. This can be fractional
            since certain node types are configured to share cores between Spark nodes on the same instance.
        default_tags (Union[Unset, ClusterTag]): An object with key value pairs. The key length must be between 1 and
            127 UTF-8 characters, inclusive. The value length must be less than or equal to 255 UTF-8 characters.
        cluster_log_status (Union[Unset, LogSyncStatus]):
        termination_reason (Union[Unset, TerminationReason]):
    """

    num_workers: Union[Unset, int] = UNSET
    autoscale: Union[Unset, "AutoScale"] = UNSET
    cluster_id: Union[Unset, str] = UNSET
    creator_user_name: Union[Unset, str] = UNSET
    driver: Union[Unset, "SparkNode"] = UNSET
    executors: Union[Unset, List["SparkNode"]] = UNSET
    spark_context_id: Union[Unset, int] = UNSET
    jdbc_port: Union[Unset, int] = UNSET
    cluster_name: Union[Unset, str] = UNSET
    spark_version: Union[Unset, str] = UNSET
    spark_conf: Union[Unset, "SparkConfPair"] = UNSET
    azure_attributes: Union[Unset, "AzureAttributes"] = UNSET
    node_type_id: Union[Unset, str] = UNSET
    driver_node_type_id: Union[Unset, str] = UNSET
    custom_tags: Union[Unset, List["ClusterTag"]] = UNSET
    cluster_log_conf: Union[Unset, "ClusterLogConf"] = UNSET
    init_scripts: Union[Unset, List["InitScriptInfo"]] = UNSET
    docker_image: Union[Unset, "DockerImage"] = UNSET
    spark_env_vars: Union[Unset, "SparkEnvPair"] = UNSET
    autotermination_minutes: Union[Unset, int] = UNSET
    enable_elastic_disk: Union[Unset, bool] = UNSET
    instance_pool_id: Union[Unset, str] = UNSET
    state: Union[Unset, ClusterState] = UNSET
    state_message: Union[Unset, str] = UNSET
    start_time: Union[Unset, int] = UNSET
    terminated_time: Union[Unset, int] = UNSET
    last_state_loss_time: Union[Unset, int] = UNSET
    last_activity_time: Union[Unset, int] = UNSET
    cluster_memory_mb: Union[Unset, int] = UNSET
    cluster_cores: Union[Unset, float] = UNSET
    default_tags: Union[Unset, "ClusterTag"] = UNSET
    cluster_log_status: Union[Unset, "LogSyncStatus"] = UNSET
    termination_reason: Union[Unset, "TerminationReason"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_workers = self.num_workers
        autoscale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.autoscale, Unset):
            autoscale = self.autoscale.to_dict()

        cluster_id = self.cluster_id
        creator_user_name = self.creator_user_name
        driver: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.driver, Unset):
            driver = self.driver.to_dict()

        executors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.executors, Unset):
            executors = []
            for executors_item_data in self.executors:
                executors_item = executors_item_data.to_dict()

                executors.append(executors_item)

        spark_context_id = self.spark_context_id
        jdbc_port = self.jdbc_port
        cluster_name = self.cluster_name
        spark_version = self.spark_version
        spark_conf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_conf, Unset):
            spark_conf = self.spark_conf.to_dict()

        azure_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.azure_attributes, Unset):
            azure_attributes = self.azure_attributes.to_dict()

        node_type_id = self.node_type_id
        driver_node_type_id = self.driver_node_type_id
        custom_tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_tags, Unset):
            custom_tags = []
            for custom_tags_item_data in self.custom_tags:
                custom_tags_item = custom_tags_item_data.to_dict()

                custom_tags.append(custom_tags_item)

        cluster_log_conf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_log_conf, Unset):
            cluster_log_conf = self.cluster_log_conf.to_dict()

        init_scripts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.init_scripts, Unset):
            init_scripts = []
            for init_scripts_item_data in self.init_scripts:
                init_scripts_item = init_scripts_item_data.to_dict()

                init_scripts.append(init_scripts_item)

        docker_image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.docker_image, Unset):
            docker_image = self.docker_image.to_dict()

        spark_env_vars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_env_vars, Unset):
            spark_env_vars = self.spark_env_vars.to_dict()

        autotermination_minutes = self.autotermination_minutes
        enable_elastic_disk = self.enable_elastic_disk
        instance_pool_id = self.instance_pool_id
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        state_message = self.state_message
        start_time = self.start_time
        terminated_time = self.terminated_time
        last_state_loss_time = self.last_state_loss_time
        last_activity_time = self.last_activity_time
        cluster_memory_mb = self.cluster_memory_mb
        cluster_cores = self.cluster_cores
        default_tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_tags, Unset):
            default_tags = self.default_tags.to_dict()

        cluster_log_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_log_status, Unset):
            cluster_log_status = self.cluster_log_status.to_dict()

        termination_reason: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.termination_reason, Unset):
            termination_reason = self.termination_reason.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_workers is not UNSET:
            field_dict["num_workers"] = num_workers
        if autoscale is not UNSET:
            field_dict["autoscale"] = autoscale
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if creator_user_name is not UNSET:
            field_dict["creator_user_name"] = creator_user_name
        if driver is not UNSET:
            field_dict["driver"] = driver
        if executors is not UNSET:
            field_dict["executors"] = executors
        if spark_context_id is not UNSET:
            field_dict["spark_context_id"] = spark_context_id
        if jdbc_port is not UNSET:
            field_dict["jdbc_port"] = jdbc_port
        if cluster_name is not UNSET:
            field_dict["cluster_name"] = cluster_name
        if spark_version is not UNSET:
            field_dict["spark_version"] = spark_version
        if spark_conf is not UNSET:
            field_dict["spark_conf"] = spark_conf
        if azure_attributes is not UNSET:
            field_dict["azure_attributes"] = azure_attributes
        if node_type_id is not UNSET:
            field_dict["node_type_id"] = node_type_id
        if driver_node_type_id is not UNSET:
            field_dict["driver_node_type_id"] = driver_node_type_id
        if custom_tags is not UNSET:
            field_dict["custom_tags"] = custom_tags
        if cluster_log_conf is not UNSET:
            field_dict["cluster_log_conf"] = cluster_log_conf
        if init_scripts is not UNSET:
            field_dict["init_scripts"] = init_scripts
        if docker_image is not UNSET:
            field_dict["docker_image"] = docker_image
        if spark_env_vars is not UNSET:
            field_dict["spark_env_vars"] = spark_env_vars
        if autotermination_minutes is not UNSET:
            field_dict["autotermination_minutes"] = autotermination_minutes
        if enable_elastic_disk is not UNSET:
            field_dict["enable_elastic_disk"] = enable_elastic_disk
        if instance_pool_id is not UNSET:
            field_dict["instance_pool_id"] = instance_pool_id
        if state is not UNSET:
            field_dict["state"] = state
        if state_message is not UNSET:
            field_dict["state_message"] = state_message
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if terminated_time is not UNSET:
            field_dict["terminated_time"] = terminated_time
        if last_state_loss_time is not UNSET:
            field_dict["last_state_loss_time"] = last_state_loss_time
        if last_activity_time is not UNSET:
            field_dict["last_activity_time"] = last_activity_time
        if cluster_memory_mb is not UNSET:
            field_dict["cluster_memory_mb"] = cluster_memory_mb
        if cluster_cores is not UNSET:
            field_dict["cluster_cores"] = cluster_cores
        if default_tags is not UNSET:
            field_dict["default_tags"] = default_tags
        if cluster_log_status is not UNSET:
            field_dict["cluster_log_status"] = cluster_log_status
        if termination_reason is not UNSET:
            field_dict["termination_reason"] = termination_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.auto_scale import AutoScale
        from ..models.azure_attributes import AzureAttributes
        from ..models.cluster_log_conf import ClusterLogConf
        from ..models.cluster_tag import ClusterTag
        from ..models.docker_image import DockerImage
        from ..models.init_script_info import InitScriptInfo
        from ..models.log_sync_status import LogSyncStatus
        from ..models.spark_conf_pair import SparkConfPair
        from ..models.spark_env_pair import SparkEnvPair
        from ..models.spark_node import SparkNode
        from ..models.termination_reason import TerminationReason

        d = src_dict.copy()
        num_workers = d.pop("num_workers", UNSET)

        _autoscale = d.pop("autoscale", UNSET)
        autoscale: Union[Unset, AutoScale]
        if isinstance(_autoscale, Unset):
            autoscale = UNSET
        else:
            autoscale = AutoScale.from_dict(_autoscale)

        cluster_id = d.pop("cluster_id", UNSET)

        creator_user_name = d.pop("creator_user_name", UNSET)

        _driver = d.pop("driver", UNSET)
        driver: Union[Unset, SparkNode]
        if isinstance(_driver, Unset):
            driver = UNSET
        else:
            driver = SparkNode.from_dict(_driver)

        executors = []
        _executors = d.pop("executors", UNSET)
        for executors_item_data in _executors or []:
            executors_item = SparkNode.from_dict(executors_item_data)

            executors.append(executors_item)

        spark_context_id = d.pop("spark_context_id", UNSET)

        jdbc_port = d.pop("jdbc_port", UNSET)

        cluster_name = d.pop("cluster_name", UNSET)

        spark_version = d.pop("spark_version", UNSET)

        _spark_conf = d.pop("spark_conf", UNSET)
        spark_conf: Union[Unset, SparkConfPair]
        if isinstance(_spark_conf, Unset):
            spark_conf = UNSET
        else:
            spark_conf = SparkConfPair.from_dict(_spark_conf)

        _azure_attributes = d.pop("azure_attributes", UNSET)
        azure_attributes: Union[Unset, AzureAttributes]
        if isinstance(_azure_attributes, Unset):
            azure_attributes = UNSET
        else:
            azure_attributes = AzureAttributes.from_dict(_azure_attributes)

        node_type_id = d.pop("node_type_id", UNSET)

        driver_node_type_id = d.pop("driver_node_type_id", UNSET)

        custom_tags = []
        _custom_tags = d.pop("custom_tags", UNSET)
        for custom_tags_item_data in _custom_tags or []:
            custom_tags_item = ClusterTag.from_dict(custom_tags_item_data)

            custom_tags.append(custom_tags_item)

        _cluster_log_conf = d.pop("cluster_log_conf", UNSET)
        cluster_log_conf: Union[Unset, ClusterLogConf]
        if isinstance(_cluster_log_conf, Unset):
            cluster_log_conf = UNSET
        else:
            cluster_log_conf = ClusterLogConf.from_dict(_cluster_log_conf)

        init_scripts = []
        _init_scripts = d.pop("init_scripts", UNSET)
        for init_scripts_item_data in _init_scripts or []:
            init_scripts_item = InitScriptInfo.from_dict(init_scripts_item_data)

            init_scripts.append(init_scripts_item)

        _docker_image = d.pop("docker_image", UNSET)
        docker_image: Union[Unset, DockerImage]
        if isinstance(_docker_image, Unset):
            docker_image = UNSET
        else:
            docker_image = DockerImage.from_dict(_docker_image)

        _spark_env_vars = d.pop("spark_env_vars", UNSET)
        spark_env_vars: Union[Unset, SparkEnvPair]
        if isinstance(_spark_env_vars, Unset):
            spark_env_vars = UNSET
        else:
            spark_env_vars = SparkEnvPair.from_dict(_spark_env_vars)

        autotermination_minutes = d.pop("autotermination_minutes", UNSET)

        enable_elastic_disk = d.pop("enable_elastic_disk", UNSET)

        instance_pool_id = d.pop("instance_pool_id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ClusterState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ClusterState(_state)

        state_message = d.pop("state_message", UNSET)

        start_time = d.pop("start_time", UNSET)

        terminated_time = d.pop("terminated_time", UNSET)

        last_state_loss_time = d.pop("last_state_loss_time", UNSET)

        last_activity_time = d.pop("last_activity_time", UNSET)

        cluster_memory_mb = d.pop("cluster_memory_mb", UNSET)

        cluster_cores = d.pop("cluster_cores", UNSET)

        _default_tags = d.pop("default_tags", UNSET)
        default_tags: Union[Unset, ClusterTag]
        if isinstance(_default_tags, Unset):
            default_tags = UNSET
        else:
            default_tags = ClusterTag.from_dict(_default_tags)

        _cluster_log_status = d.pop("cluster_log_status", UNSET)
        cluster_log_status: Union[Unset, LogSyncStatus]
        if isinstance(_cluster_log_status, Unset):
            cluster_log_status = UNSET
        else:
            cluster_log_status = LogSyncStatus.from_dict(_cluster_log_status)

        _termination_reason = d.pop("termination_reason", UNSET)
        termination_reason: Union[Unset, TerminationReason]
        if isinstance(_termination_reason, Unset):
            termination_reason = UNSET
        else:
            termination_reason = TerminationReason.from_dict(_termination_reason)

        cluster_info = cls(
            num_workers=num_workers,
            autoscale=autoscale,
            cluster_id=cluster_id,
            creator_user_name=creator_user_name,
            driver=driver,
            executors=executors,
            spark_context_id=spark_context_id,
            jdbc_port=jdbc_port,
            cluster_name=cluster_name,
            spark_version=spark_version,
            spark_conf=spark_conf,
            azure_attributes=azure_attributes,
            node_type_id=node_type_id,
            driver_node_type_id=driver_node_type_id,
            custom_tags=custom_tags,
            cluster_log_conf=cluster_log_conf,
            init_scripts=init_scripts,
            docker_image=docker_image,
            spark_env_vars=spark_env_vars,
            autotermination_minutes=autotermination_minutes,
            enable_elastic_disk=enable_elastic_disk,
            instance_pool_id=instance_pool_id,
            state=state,
            state_message=state_message,
            start_time=start_time,
            terminated_time=terminated_time,
            last_state_loss_time=last_state_loss_time,
            last_activity_time=last_activity_time,
            cluster_memory_mb=cluster_memory_mb,
            cluster_cores=cluster_cores,
            default_tags=default_tags,
            cluster_log_status=cluster_log_status,
            termination_reason=termination_reason,
        )

        cluster_info.additional_properties = d
        return cluster_info

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
