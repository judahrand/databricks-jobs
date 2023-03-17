# ClusterAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | Cluster name requested by the user. This doesn’t have to be unique. If not specified at creation, the cluster name is an empty string. | [optional] 
**spark_version** | **str** | The runtime version of the cluster, for example “5.0.x-scala2.11”. You can retrieve a list of available runtime versions by using the [Runtime versions](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#runtime-versions) API call. | [optional] 
**spark_conf** | **Dict[str, object]** | An arbitrary object where the object key is a configuration propery name and the value is a configuration property value. | [optional] 
**aws_attributes** | [**AwsAttributes**](AwsAttributes.md) |  | [optional] 
**node_type_id** | **str** | This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads A list of available node types can be retrieved by using the [List node types](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#list-node-types) API call. | [optional] 
**driver_node_type_id** | **str** | The node type of the Spark driver. This field is optional; if unset, the driver node type is set as the same value as &#x60;node_type_id&#x60; defined above. | [optional] 
**ssh_public_keys** | **List[str]** |  | [optional] 
**custom_tags** | **Dict[str, str]** | An object with key value pairs. The key length must be between 1 and 127 UTF-8 characters, inclusive. The value length must be less than or equal to 255 UTF-8 characters. | [optional] 
**cluster_log_conf** | [**ClusterLogConf**](ClusterLogConf.md) |  | [optional] 
**init_scripts** | [**List[InitScriptInfo]**](InitScriptInfo.md) | The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If &#x60;cluster_log_conf&#x60; is specified, init script logs are sent to &#x60;&lt;destination&gt;/&lt;cluster-ID&gt;/init_scripts&#x60;. | [optional] 
**docker_image** | [**DockerImage**](DockerImage.md) |  | [optional] 
**runtime_engine** | **str** | The type of runtime engine to use. If not specified, the runtime engine type is inferred based on the &#x60;spark_version&#x60; value. Allowed values include  * &#x60;PHOTON&#x60;: Use the Photon runtime engine type. * &#x60;STANDARD&#x60;: Use the standard runtime engine type.  This field is optional. | [optional] 
**spark_env_vars** | **Dict[str, object]** | An arbitrary object where the object key is an environment variable name and the value is an environment variable value. | [optional] 
**autotermination_minutes** | **int** | Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster is not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. You can also set this value to 0 to explicitly disable automatic termination. | [optional] 
**enable_elastic_disk** | **bool** | Autoscaling Local Storage: when enabled, this cluster dynamically acquires additional disk space when its Spark workers are running low on disk space.null Refer to [Autoscaling local storage](https://docs.microsoft.com/azure/databricks/clusters/configure#autoscaling-local-storage) for details. | [optional] 
**instance_pool_id** | **str** | The optional ID of the instance pool to which the cluster belongs. Refer to [Pools](https://docs.microsoft.com/azure/databricks/clusters/pools) for details. | [optional] 
**cluster_source** | [**ClusterSource**](ClusterSource.md) |  | [optional] 
**policy_id** | **str** | A [cluster policy](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/policies) ID. | [optional] 
**enable_local_disk_encryption** | **bool** | Determines whether encryption of the disks attached to the cluster locally is enabled. | [optional] 
**gcp_attributes** | [**GcpAttributes**](GcpAttributes.md) |  | [optional] 
**azure_attributes** | [**AzureAttributes**](AzureAttributes.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.cluster_attributes import ClusterAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAttributes from a JSON string
cluster_attributes_instance = ClusterAttributes.from_json(json)
# print the JSON string representation of the object
print ClusterAttributes.to_json()

# convert the object into a dict
cluster_attributes_dict = cluster_attributes_instance.to_dict()
# create an instance of ClusterAttributes from a dict
cluster_attributes_form_dict = cluster_attributes.from_dict(cluster_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


