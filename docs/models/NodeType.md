# databricks_jobs.model.node_type.NodeType

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**node_type_id** | str,  | str,  | Unique identifier for this node type. This field is required. | 
**description** | str,  | str,  | A string description associated with this node type. This field is required. | 
**memory_mb** | decimal.Decimal, int,  | decimal.Decimal,  | Memory (in MB) available for this node type. This field is required. | value must be a 32 bit integer
**instance_type_id** | str,  | str,  | An identifier for the type of hardware that this node runs on. This field is required. | 
**num_cores** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of CPU cores available for this node type. This can be fractional if the number of cores on a machine instance is not divisible by the number of Spark nodes on that machine. This field is required. | [optional] value must be a 32 bit float
**is_deprecated** | bool,  | BoolClass,  | Whether the node type is deprecated. Non-deprecated node types offer greater performance. | [optional] 
**node_info** | [**ClusterCloudProviderNodeInfo**](ClusterCloudProviderNodeInfo.md) | [**ClusterCloudProviderNodeInfo**](ClusterCloudProviderNodeInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

