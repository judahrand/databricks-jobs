from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_scale import AutoScale
    from ..models.azure_attributes import AzureAttributes
    from ..models.cluster_log_conf import ClusterLogConf
    from ..models.cluster_tag import ClusterTag
    from ..models.docker_image import DockerImage
    from ..models.init_script_info import InitScriptInfo
    from ..models.spark_conf_pair import SparkConfPair
    from ..models.spark_env_pair import SparkEnvPair


T = TypeVar("T", bound="NewCluster")


@attr.s(auto_attribs=True)
class NewCluster:
    """
    Attributes:
        spark_version (str): The Spark version of the cluster. A list of available Spark versions can be retrieved by
            using the [Runtime versions](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#runtime-
            versions) API call.
        num_workers (Union[Unset, int]): If num_workers, number of worker nodes that this cluster must have. A cluster
            has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. When reading the
            properties of a cluster, this field reflects the desired number of workers rather than the actual current number
            of workers. For example, if a cluster is resized from 5 to 10 workers, this field immediately updates to reflect
            the target size of 10 workers, whereas the workers listed in `spark_info` gradually increase from 5 to 10 as the
            new nodes are provisioned.
        autoscale (Union[Unset, AutoScale]):
        spark_conf (Union[Unset, SparkConfPair]): An arbitrary object where the object key is a configuration propery
            name and the value is a configuration property value.
        azure_attributes (Union[Unset, AzureAttributes]):
        node_type_id (Union[Unset, str]): This field encodes, through a single value, the resources available to each of
            the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or
            compute intensive workloads A list of available node types can be retrieved by using the [List node
            types](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#list-node-types) API call.
        driver_node_type_id (Union[Unset, str]): The node type of the Spark driver. This field is optional; if unset,
            the driver node type is set as the same value as `node_type_id` defined above.
        custom_tags (Union[Unset, ClusterTag]): An object with key value pairs. The key length must be between 1 and 127
            UTF-8 characters, inclusive. The value length must be less than or equal to 255 UTF-8 characters.
        cluster_log_conf (Union[Unset, ClusterLogConf]):
        init_scripts (Union[Unset, List['InitScriptInfo']]): The configuration for storing init scripts. Any number of
            scripts can be specified. The scripts are executed sequentially in the order provided. If `cluster_log_conf` is
            specified, init script logs are sent to `<destination>/<cluster-id>/init_scripts`.
        spark_env_vars (Union[Unset, SparkEnvPair]): An arbitrary object where the object key is an environment variable
            name and the value is an environment variable value.
        enable_elastic_disk (Union[Unset, bool]): Autoscaling Local Storage: when enabled, this cluster dynamically
            acquires additional disk space when its Spark workers are running low on disk space. Refer to [Autoscaling local
            storage](https://docs.microsoft.com/azure/databricks/clusters/configure#autoscaling-local-storage-azure) for
            details.
        instance_pool_id (Union[Unset, str]): The optional ID of the instance pool to use for cluster nodes. If
            `driver_instance_pool_id` is present, `instance_pool_id` is used for worker nodes only. Otherwise, it is used
            for both the driver node and worker nodes. Refer to [Instance Pools
            API](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/instance-pools) for details.
        policy_id (Union[Unset, str]): A [cluster policy](https://docs.microsoft.com/azure/databricks/dev-
            tools/api/latest/policies) ID. Either `node_type_id` or `instance_pool_id` must be specified in the cluster
            policy if they are not specified in this job cluster object.
        enable_local_disk_encryption (Union[Unset, bool]): Determines whether encryption of disks locally attached to
            the cluster is enabled.
        docker_image (Union[Unset, DockerImage]):
        runtime_engine (Union[Unset, str]): The type of runtime engine to use. If not specified, the runtime engine type
            is inferred based on the `spark_version` value. Allowed values include:

            * `PHOTON`: Use the Photon runtime engine type.
            * `STANDARD`: Use the standard runtime engine type.

            This field is optional.
    """

    spark_version: str
    num_workers: Union[Unset, int] = UNSET
    autoscale: Union[Unset, "AutoScale"] = UNSET
    spark_conf: Union[Unset, "SparkConfPair"] = UNSET
    azure_attributes: Union[Unset, "AzureAttributes"] = UNSET
    node_type_id: Union[Unset, str] = UNSET
    driver_node_type_id: Union[Unset, str] = UNSET
    custom_tags: Union[Unset, "ClusterTag"] = UNSET
    cluster_log_conf: Union[Unset, "ClusterLogConf"] = UNSET
    init_scripts: Union[Unset, List["InitScriptInfo"]] = UNSET
    spark_env_vars: Union[Unset, "SparkEnvPair"] = UNSET
    enable_elastic_disk: Union[Unset, bool] = UNSET
    instance_pool_id: Union[Unset, str] = UNSET
    policy_id: Union[Unset, str] = UNSET
    enable_local_disk_encryption: Union[Unset, bool] = UNSET
    docker_image: Union[Unset, "DockerImage"] = UNSET
    runtime_engine: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        spark_version = self.spark_version
        num_workers = self.num_workers
        autoscale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.autoscale, Unset):
            autoscale = self.autoscale.to_dict()

        spark_conf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_conf, Unset):
            spark_conf = self.spark_conf.to_dict()

        azure_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.azure_attributes, Unset):
            azure_attributes = self.azure_attributes.to_dict()

        node_type_id = self.node_type_id
        driver_node_type_id = self.driver_node_type_id
        custom_tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_tags, Unset):
            custom_tags = self.custom_tags.to_dict()

        cluster_log_conf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_log_conf, Unset):
            cluster_log_conf = self.cluster_log_conf.to_dict()

        init_scripts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.init_scripts, Unset):
            init_scripts = []
            for init_scripts_item_data in self.init_scripts:
                init_scripts_item = init_scripts_item_data.to_dict()

                init_scripts.append(init_scripts_item)

        spark_env_vars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_env_vars, Unset):
            spark_env_vars = self.spark_env_vars.to_dict()

        enable_elastic_disk = self.enable_elastic_disk
        instance_pool_id = self.instance_pool_id
        policy_id = self.policy_id
        enable_local_disk_encryption = self.enable_local_disk_encryption
        docker_image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.docker_image, Unset):
            docker_image = self.docker_image.to_dict()

        runtime_engine = self.runtime_engine

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spark_version": spark_version,
            }
        )
        if num_workers is not UNSET:
            field_dict["num_workers"] = num_workers
        if autoscale is not UNSET:
            field_dict["autoscale"] = autoscale
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
        if spark_env_vars is not UNSET:
            field_dict["spark_env_vars"] = spark_env_vars
        if enable_elastic_disk is not UNSET:
            field_dict["enable_elastic_disk"] = enable_elastic_disk
        if instance_pool_id is not UNSET:
            field_dict["instance_pool_id"] = instance_pool_id
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id
        if enable_local_disk_encryption is not UNSET:
            field_dict["enable_local_disk_encryption"] = enable_local_disk_encryption
        if docker_image is not UNSET:
            field_dict["docker_image"] = docker_image
        if runtime_engine is not UNSET:
            field_dict["runtime_engine"] = runtime_engine

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.auto_scale import AutoScale
        from ..models.azure_attributes import AzureAttributes
        from ..models.cluster_log_conf import ClusterLogConf
        from ..models.cluster_tag import ClusterTag
        from ..models.docker_image import DockerImage
        from ..models.init_script_info import InitScriptInfo
        from ..models.spark_conf_pair import SparkConfPair
        from ..models.spark_env_pair import SparkEnvPair

        d = src_dict.copy()
        spark_version = d.pop("spark_version")

        num_workers = d.pop("num_workers", UNSET)

        _autoscale = d.pop("autoscale", UNSET)
        autoscale: Union[Unset, AutoScale]
        if isinstance(_autoscale, Unset):
            autoscale = UNSET
        else:
            autoscale = AutoScale.from_dict(_autoscale)

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

        _custom_tags = d.pop("custom_tags", UNSET)
        custom_tags: Union[Unset, ClusterTag]
        if isinstance(_custom_tags, Unset):
            custom_tags = UNSET
        else:
            custom_tags = ClusterTag.from_dict(_custom_tags)

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

        _spark_env_vars = d.pop("spark_env_vars", UNSET)
        spark_env_vars: Union[Unset, SparkEnvPair]
        if isinstance(_spark_env_vars, Unset):
            spark_env_vars = UNSET
        else:
            spark_env_vars = SparkEnvPair.from_dict(_spark_env_vars)

        enable_elastic_disk = d.pop("enable_elastic_disk", UNSET)

        instance_pool_id = d.pop("instance_pool_id", UNSET)

        policy_id = d.pop("policy_id", UNSET)

        enable_local_disk_encryption = d.pop("enable_local_disk_encryption", UNSET)

        _docker_image = d.pop("docker_image", UNSET)
        docker_image: Union[Unset, DockerImage]
        if isinstance(_docker_image, Unset):
            docker_image = UNSET
        else:
            docker_image = DockerImage.from_dict(_docker_image)

        runtime_engine = d.pop("runtime_engine", UNSET)

        new_cluster = cls(
            spark_version=spark_version,
            num_workers=num_workers,
            autoscale=autoscale,
            spark_conf=spark_conf,
            azure_attributes=azure_attributes,
            node_type_id=node_type_id,
            driver_node_type_id=driver_node_type_id,
            custom_tags=custom_tags,
            cluster_log_conf=cluster_log_conf,
            init_scripts=init_scripts,
            spark_env_vars=spark_env_vars,
            enable_elastic_disk=enable_elastic_disk,
            instance_pool_id=instance_pool_id,
            policy_id=policy_id,
            enable_local_disk_encryption=enable_local_disk_encryption,
            docker_image=docker_image,
            runtime_engine=runtime_engine,
        )

        new_cluster.additional_properties = d
        return new_cluster

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
