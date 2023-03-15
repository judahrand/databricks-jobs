# NewTaskCluster

If new_cluster, a description of a cluster that is created only for this task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_workers** | **int** | If num_workers, number of worker nodes that this cluster must have. A cluster has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual current number of workers. For example, if a cluster is resized from 5 to 10 workers, this field immediately updates to reflect the target size of 10 workers, whereas the workers listed in &#x60;spark_info&#x60; gradually increase from 5 to 10 as the new nodes are provisioned. | [optional] 
**autoscale** | [**AutoScale**](AutoScale.md) |  | [optional] 
**spark_version** | **str** | The Spark version of the cluster. A list of available Spark versions can be retrieved by using the [Runtime versions](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#runtime-versions) API call. | 
**spark_conf** | **Dict[str, object]** | An arbitrary object where the object key is a configuration propery name and the value is a configuration property value. | [optional] 
**azure_attributes** | [**AzureAttributes**](AzureAttributes.md) |  | [optional] 
**node_type_id** | **str** | This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads A list of available node types can be retrieved by using the [List node types](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#list-node-types) API call. | [optional] 
**driver_node_type_id** | **str** | The node type of the Spark driver. This field is optional; if unset, the driver node type is set as the same value as &#x60;node_type_id&#x60; defined above. | [optional] 
**custom_tags** | **Dict[str, str]** | An object with key value pairs. The key length must be between 1 and 127 UTF-8 characters, inclusive. The value length must be less than or equal to 255 UTF-8 characters. | [optional] 
**cluster_log_conf** | [**ClusterLogConf**](ClusterLogConf.md) |  | [optional] 
**init_scripts** | [**List[InitScriptInfo]**](InitScriptInfo.md) | The configuration for storing init scripts. Any number of scripts can be specified. The scripts are executed sequentially in the order provided. If &#x60;cluster_log_conf&#x60; is specified, init script logs are sent to &#x60;&lt;destination&gt;/&lt;cluster-id&gt;/init_scripts&#x60;. | [optional] 
**spark_env_vars** | **Dict[str, object]** | An arbitrary object where the object key is an environment variable name and the value is an environment variable value. | [optional] 
**enable_elastic_disk** | **bool** | Autoscaling Local Storage: when enabled, this cluster dynamically acquires additional disk space when its Spark workers are running low on disk space. Refer to [Autoscaling local storage](https://docs.microsoft.com/azure/databricks/clusters/configure#autoscaling-local-storage-azure) for details. | [optional] 
**instance_pool_id** | **str** | The optional ID of the instance pool to use for cluster nodes. If &#x60;driver_instance_pool_id&#x60; is present, &#x60;instance_pool_id&#x60; is used for worker nodes only. Otherwise, it is used for both the driver node and worker nodes. Refer to [Instance Pools API](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/instance-pools) for details. | [optional] 
**policy_id** | **str** | A [cluster policy](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/policies) ID. Either &#x60;node_type_id&#x60; or &#x60;instance_pool_id&#x60; must be specified in the cluster policy if they are not specified in this job cluster object. | [optional] 
**enable_local_disk_encryption** | **bool** | Determines whether encryption of disks locally attached to the cluster is enabled. | [optional] 
**docker_image** | [**DockerImage**](DockerImage.md) |  | [optional] 
**runtime_engine** | **str** | The type of runtime engine to use. If not specified, the runtime engine type is inferred based on the &#x60;spark_version&#x60; value. Allowed values include:  * &#x60;PHOTON&#x60;: Use the Photon runtime engine type. * &#x60;STANDARD&#x60;: Use the standard runtime engine type.  This field is optional. | [optional] 

## Example

```python
from databricks_jobs.models.new_task_cluster import NewTaskCluster

# TODO update the JSON string below
json = "{}"
# create an instance of NewTaskCluster from a JSON string
new_task_cluster_instance = NewTaskCluster.from_json(json)
# print the JSON string representation of the object
print NewTaskCluster.to_json()

# convert the object into a dict
new_task_cluster_dict = new_task_cluster_instance.to_dict()
# create an instance of NewTaskCluster from a dict
new_task_cluster_form_dict = new_task_cluster.from_dict(new_task_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


