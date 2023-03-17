# ClusterInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_workers** | **int** | If num_workers, number of worker nodes that this cluster must have. A cluster has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. **Note:** When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field is immediately updated to reflect the target size of 10 workers, whereas the workers listed in &#x60;executors&#x60; gradually increase from 5 to 10 as the new nodes are provisioned. | [optional] 
**autoscale** | [**AutoScale**](AutoScale.md) |  | [optional] 
**cluster_id** | **str** | Canonical identifier for the cluster. This ID is retained during cluster restarts and resizes, while each new cluster has a globally unique ID. | [optional] 
**creator_user_name** | **str** | Creator user name. The field won’t be included in the response if the user has already been deleted. | [optional] 
**driver** | [**SparkNode**](SparkNode.md) |  | [optional] 
**executors** | [**List[SparkNode]**](SparkNode.md) | Nodes on which the Spark executors reside. | [optional] 
**spark_context_id** | **int** | A canonical SparkContext identifier. This value _does_ change when the Spark driver restarts. The pair &#x60;(cluster_id, spark_context_id)&#x60; is a globally unique identifier over all Spark contexts. | [optional] 
**jdbc_port** | **int** | Port on which Spark JDBC server is listening in the driver node. No service listens on this port in executor nodes. | [optional] 
**cluster_name** | **str** | Cluster name requested by the user. This doesn’t have to be unique. If not specified at creation, the cluster name is an empty string. | [optional] 
**spark_version** | **str** | The runtime version of the cluster. You can retrieve a list of available runtime versions by using the [Runtime versions](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#runtime-versions) API call. | [optional] 
**spark_conf** | **Dict[str, object]** | An arbitrary object where the object key is a configuration propery name and the value is a configuration property value. | [optional] 
**aws_attributes** | [**AwsAttributes**](AwsAttributes.md) |  | [optional] 
**node_type_id** | **str** | This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the [List node types](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#list-node-types) API call. | [optional] 
**driver_node_type_id** | **str** | The node type of the Spark driver. This field is optional; if unset, the driver node type is set as the same value as &#x60;node_type_id&#x60; defined above. | [optional] 
**ssh_public_keys** | **List[str]** | Set to empty array. Cluster SSH is not supported. | [optional] 
**custom_tags** | **List[Dict]** | An object containing a set of tags for cluster resources. Databricks tags all cluster resources (such as VMs) with these tags in addition to default_tags. **Note**: * Tags are not supported on legacy node types such as compute-optimized and memory-optimized * Databricks allows at most 45 custom tags | [optional] 
**cluster_log_conf** | [**ClusterLogConf**](ClusterLogConf.md) |  | [optional] 
**init_scripts** | [**List[InitScriptInfo]**](InitScriptInfo.md) | The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If &#x60;cluster_log_conf&#x60; is specified, init script logs are sent to &#x60;&lt;destination&gt;/&lt;cluster-ID&gt;/init_scripts&#x60;. | [optional] 
**docker_image** | [**DockerImage**](DockerImage.md) |  | [optional] 
**spark_env_vars** | **Dict[str, object]** | An arbitrary object where the object key is an environment variable name and the value is an environment variable value. | [optional] 
**autotermination_minutes** | **int** | Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster is not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. You can also set this value to 0 to explicitly disable automatic termination. | [optional] 
**enable_elastic_disk** | **bool** | Autoscaling Local Storage: when enabled, this cluster dynamically acquires additional disk space when its Spark workers are running low on disk space. See [Autoscaling local storage](https://docs.microsoft.com/azure/databricks/clusters/configure#autoscaling-local-storage-azure) for details. | [optional] 
**instance_pool_id** | **str** | The optional ID of the instance pool to which the cluster belongs. Refer to [Pools](https://docs.microsoft.com/azure/databricks/clusters/pools) for details. | [optional] 
**cluster_source** | [**ClusterSource**](ClusterSource.md) |  | [optional] 
**state** | [**ClusterState**](ClusterState.md) |  | [optional] 
**state_message** | **str** | A message associated with the most recent state transition (for example, the reason why the cluster entered a &#x60;TERMINATED&#x60; state). This field is unstructured, and its exact format is subject to change. | [optional] 
**start_time** | **int** | Time (in epoch milliseconds) when the cluster creation request was received (when the cluster entered a &#x60;PENDING&#x60; state). | [optional] 
**terminated_time** | **int** | Time (in epoch milliseconds) when the cluster was terminated, if applicable. | [optional] 
**last_state_loss_time** | **int** | Time when the cluster driver last lost its state (due to a restart or driver failure). | [optional] 
**last_activity_time** | **int** | Time (in epoch milliseconds) when the cluster was last active. A cluster is active if there is at least one command that has not finished on the cluster. This field is available after the cluster has reached a &#x60;RUNNING&#x60; state. Updates to this field are made as best-effort attempts. Certain versions of Spark do not support reporting of cluster activity. Refer to [Automatic termination](https://docs.microsoft.com/azure/databricks/clusters/clusters-manage#automatic-termination) for details. | [optional] 
**cluster_memory_mb** | **int** | Total amount of cluster memory, in megabytes. | [optional] 
**cluster_cores** | **float** | Number of CPU cores available for this cluster. This can be fractional since certain node types are configured to share cores between Spark nodes on the same instance. | [optional] 
**default_tags** | **Dict[str, str]** | An object with key value pairs. The key length must be between 1 and 127 UTF-8 characters, inclusive. The value length must be less than or equal to 255 UTF-8 characters. | [optional] 
**cluster_log_status** | [**LogSyncStatus**](LogSyncStatus.md) |  | [optional] 
**termination_reason** | [**TerminationReason**](TerminationReason.md) |  | [optional] 
**gcp_attributes** | [**GcpAttributes**](GcpAttributes.md) |  | [optional] 
**azure_attributes** | [**AzureAttributes**](AzureAttributes.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.cluster_info import ClusterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInfo from a JSON string
cluster_info_instance = ClusterInfo.from_json(json)
# print the JSON string representation of the object
print ClusterInfo.to_json()

# convert the object into a dict
cluster_info_dict = cluster_info_instance.to_dict()
# create an instance of ClusterInfo from a dict
cluster_info_form_dict = cluster_info.from_dict(cluster_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


