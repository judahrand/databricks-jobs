# databricks_jobs.model.cluster_info.ClusterInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**num_workers** | decimal.Decimal, int,  | decimal.Decimal,  | If num_workers, number of worker nodes that this cluster must have. A cluster has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. **Note:** When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field is immediately updated to reflect the target size of 10 workers, whereas the workers listed in &#x60;executors&#x60; gradually increase from 5 to 10 as the new nodes are provisioned. | [optional] value must be a 32 bit integer
**autoscale** | [**AutoScale**](AutoScale.md) | [**AutoScale**](AutoScale.md) |  | [optional] 
**cluster_id** | str,  | str,  | Canonical identifier for the cluster. This ID is retained during cluster restarts and resizes, while each new cluster has a globally unique ID. | [optional] 
**creator_user_name** | str,  | str,  | Creator user name. The field won’t be included in the response if the user has already been deleted. | [optional] 
**driver** | [**SparkNode**](SparkNode.md) | [**SparkNode**](SparkNode.md) |  | [optional] 
**[executors](#executors)** | list, tuple,  | tuple,  | Nodes on which the Spark executors reside. | [optional] 
**spark_context_id** | decimal.Decimal, int,  | decimal.Decimal,  | A canonical SparkContext identifier. This value _does_ change when the Spark driver restarts. The pair &#x60;(cluster_id, spark_context_id)&#x60; is a globally unique identifier over all Spark contexts. | [optional] value must be a 64 bit integer
**jdbc_port** | decimal.Decimal, int,  | decimal.Decimal,  | Port on which Spark JDBC server is listening in the driver node. No service listens on this port in executor nodes. | [optional] value must be a 32 bit integer
**cluster_name** | str,  | str,  | Cluster name requested by the user. This doesn’t have to be unique. If not specified at creation, the cluster name is an empty string. | [optional] 
**spark_version** | str,  | str,  | The runtime version of the cluster. You can retrieve a list of available runtime versions by using the [Runtime versions](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#runtime-versions) API call. | [optional] 
**spark_conf** | [**SparkConfPair**](SparkConfPair.md) | [**SparkConfPair**](SparkConfPair.md) |  | [optional] 
**azure_attributes** | [**AzureAttributes**](AzureAttributes.md) | [**AzureAttributes**](AzureAttributes.md) |  | [optional] 
**node_type_id** | str,  | str,  | This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the [List node types](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#list-node-types) API call. | [optional] 
**driver_node_type_id** | str,  | str,  | The node type of the Spark driver. This field is optional; if unset, the driver node type is set as the same value as &#x60;node_type_id&#x60; defined above. | [optional] 
**[custom_tags](#custom_tags)** | list, tuple,  | tuple,  | An object containing a set of tags for cluster resources. Databricks tags all cluster resources (such as VMs) with these tags in addition to default_tags. **Note**: * Tags are not supported on legacy node types such as compute-optimized and memory-optimized * Databricks allows at most 45 custom tags | [optional] 
**cluster_log_conf** | [**ClusterLogConf**](ClusterLogConf.md) | [**ClusterLogConf**](ClusterLogConf.md) |  | [optional] 
**[init_scripts](#init_scripts)** | list, tuple,  | tuple,  | The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If &#x60;cluster_log_conf&#x60; is specified, init script logs are sent to &#x60;&lt;destination&gt;/&lt;cluster-ID&gt;/init_scripts&#x60;. | [optional] 
**docker_image** | [**DockerImage**](DockerImage.md) | [**DockerImage**](DockerImage.md) |  | [optional] 
**spark_env_vars** | [**SparkEnvPair**](SparkEnvPair.md) | [**SparkEnvPair**](SparkEnvPair.md) |  | [optional] 
**autotermination_minutes** | decimal.Decimal, int,  | decimal.Decimal,  | Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster is not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. You can also set this value to 0 to explicitly disable automatic termination. | [optional] value must be a 32 bit integer
**enable_elastic_disk** | bool,  | BoolClass,  | Autoscaling Local Storage: when enabled, this cluster dynamically acquires additional disk space when its Spark workers are running low on disk space. See [Autoscaling local storage](https://docs.microsoft.com/azure/databricks/clusters/configure#autoscaling-local-storage-azure) for details. | [optional] 
**instance_pool_id** | str,  | str,  | The optional ID of the instance pool to which the cluster belongs. Refer to [Pools](https://docs.microsoft.com/azure/databricks/clusters/pools) for details. | [optional] 
**state** | [**ClusterState**](ClusterState.md) | [**ClusterState**](ClusterState.md) |  | [optional] 
**state_message** | str,  | str,  | A message associated with the most recent state transition (for example, the reason why the cluster entered a &#x60;TERMINATED&#x60; state). This field is unstructured, and its exact format is subject to change. | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time (in epoch milliseconds) when the cluster creation request was received (when the cluster entered a &#x60;PENDING&#x60; state). | [optional] value must be a 64 bit integer
**terminated_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time (in epoch milliseconds) when the cluster was terminated, if applicable. | [optional] value must be a 64 bit integer
**last_state_loss_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time when the cluster driver last lost its state (due to a restart or driver failure). | [optional] value must be a 64 bit integer
**last_activity_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time (in epoch milliseconds) when the cluster was last active. A cluster is active if there is at least one command that has not finished on the cluster. This field is available after the cluster has reached a &#x60;RUNNING&#x60; state. Updates to this field are made as best-effort attempts. Certain versions of Spark do not support reporting of cluster activity. Refer to [Automatic termination](https://docs.microsoft.com/azure/databricks/clusters/clusters-manage#automatic-termination) for details. | [optional] value must be a 64 bit integer
**cluster_memory_mb** | decimal.Decimal, int,  | decimal.Decimal,  | Total amount of cluster memory, in megabytes. | [optional] value must be a 64 bit integer
**cluster_cores** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of CPU cores available for this cluster. This can be fractional since certain node types are configured to share cores between Spark nodes on the same instance. | [optional] value must be a 32 bit float
**default_tags** | [**ClusterTag**](ClusterTag.md) | [**ClusterTag**](ClusterTag.md) |  | [optional] 
**cluster_log_status** | [**LogSyncStatus**](LogSyncStatus.md) | [**LogSyncStatus**](LogSyncStatus.md) |  | [optional] 
**termination_reason** | [**TerminationReason**](TerminationReason.md) | [**TerminationReason**](TerminationReason.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# executors

Nodes on which the Spark executors reside.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Nodes on which the Spark executors reside. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SparkNode**](SparkNode.md) | [**SparkNode**](SparkNode.md) | [**SparkNode**](SparkNode.md) |  | 

# custom_tags

An object containing a set of tags for cluster resources. Databricks tags all cluster resources (such as VMs) with these tags in addition to default_tags. **Note**: * Tags are not supported on legacy node types such as compute-optimized and memory-optimized * Databricks allows at most 45 custom tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An object containing a set of tags for cluster resources. Databricks tags all cluster resources (such as VMs) with these tags in addition to default_tags. **Note**: * Tags are not supported on legacy node types such as compute-optimized and memory-optimized * Databricks allows at most 45 custom tags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClusterTag**](ClusterTag.md) | [**ClusterTag**](ClusterTag.md) | [**ClusterTag**](ClusterTag.md) |  | 

# init_scripts

The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script logs are sent to `<destination>/<cluster-ID>/init_scripts`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If &#x60;cluster_log_conf&#x60; is specified, init script logs are sent to &#x60;&lt;destination&gt;/&lt;cluster-ID&gt;/init_scripts&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InitScriptInfo**](InitScriptInfo.md) | [**InitScriptInfo**](InitScriptInfo.md) | [**InitScriptInfo**](InitScriptInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

