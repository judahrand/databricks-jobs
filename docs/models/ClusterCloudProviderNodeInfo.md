# databricks_jobs.model.cluster_cloud_provider_node_info.ClusterCloudProviderNodeInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**status** | [**ClusterCloudProviderNodeStatus**](ClusterCloudProviderNodeStatus.md) | [**ClusterCloudProviderNodeStatus**](ClusterCloudProviderNodeStatus.md) |  | [optional] 
**available_core_quota** | decimal.Decimal, int,  | decimal.Decimal,  | Available CPU core quota. | [optional] value must be a 32 bit integer
**total_core_quota** | decimal.Decimal, int,  | decimal.Decimal,  | Total CPU core quota. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

