# databricks_jobs.model.cluster_attributes.ClusterAttributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cluster_name** | str,  | str,  | Cluster name requested by the user. This doesn’t have to be unique. If not specified at creation, the cluster name is an empty string. | [optional] 
**spark_version** | str,  | str,  | The runtime version of the cluster, for example “5.0.x-scala2.11”. You can retrieve a list of available runtime versions by using the [Runtime versions](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#runtime-versions) API call. | [optional] 
**spark_conf** | [**SparkConfPair**](SparkConfPair.md) | [**SparkConfPair**](SparkConfPair.md) |  | [optional] 
**azure_attributes** | [**AzureAttributes**](AzureAttributes.md) | [**AzureAttributes**](AzureAttributes.md) |  | [optional] 
**node_type_id** | str,  | str,  | This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads A list of available node types can be retrieved by using the [List node types](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#list-node-types) API call. | [optional] 
**driver_node_type_id** | str,  | str,  | The node type of the Spark driver. This field is optional; if unset, the driver node type is set as the same value as &#x60;node_type_id&#x60; defined above. | [optional] 
**[ssh_public_keys](#ssh_public_keys)** | list, tuple,  | tuple,  |  | [optional] 
**custom_tags** | [**ClusterTag**](ClusterTag.md) | [**ClusterTag**](ClusterTag.md) |  | [optional] 
**cluster_log_conf** | [**ClusterLogConf**](ClusterLogConf.md) | [**ClusterLogConf**](ClusterLogConf.md) |  | [optional] 
**[init_scripts](#init_scripts)** | list, tuple,  | tuple,  | The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If &#x60;cluster_log_conf&#x60; is specified, init script logs are sent to &#x60;&lt;destination&gt;/&lt;cluster-ID&gt;/init_scripts&#x60;. | [optional] 
**docker_image** | [**DockerImage**](DockerImage.md) | [**DockerImage**](DockerImage.md) |  | [optional] 
**runtime_engine** | str,  | str,  | The type of runtime engine to use. If not specified, the runtime engine type is inferred based on the &#x60;spark_version&#x60; value. Allowed values include  * &#x60;PHOTON&#x60;: Use the Photon runtime engine type. * &#x60;STANDARD&#x60;: Use the standard runtime engine type.  This field is optional. | [optional] 
**spark_env_vars** | [**SparkEnvPair**](SparkEnvPair.md) | [**SparkEnvPair**](SparkEnvPair.md) |  | [optional] 
**autotermination_minutes** | decimal.Decimal, int,  | decimal.Decimal,  | Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster is not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. You can also set this value to 0 to explicitly disable automatic termination. | [optional] value must be a 32 bit integer
**enable_elastic_disk** | bool,  | BoolClass,  | Autoscaling Local Storage: when enabled, this cluster dynamically acquires additional disk space when its Spark workers are running low on disk space.null Refer to [Autoscaling local storage](https://docs.microsoft.com/azure/databricks/clusters/configure#autoscaling-local-storage) for details. | [optional] 
**instance_pool_id** | str,  | str,  | The optional ID of the instance pool to which the cluster belongs. Refer to [Pools](https://docs.microsoft.com/azure/databricks/clusters/pools) for details. | [optional] 
**cluster_source** | [**ClusterSource**](ClusterSource.md) | [**ClusterSource**](ClusterSource.md) |  | [optional] 
**policy_id** | str,  | str,  | A [cluster policy](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/policies) ID. | [optional] 
**enable_local_disk_encryption** | bool,  | BoolClass,  | Determines whether encryption of the disks attached to the cluster locally is enabled. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ssh_public_keys

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

