# databricks_jobs.model.event_details.EventDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**current_num_workers** | decimal.Decimal, int,  | decimal.Decimal,  | The number of nodes in the cluster. | [optional] value must be a 32 bit integer
**target_num_workers** | decimal.Decimal, int,  | decimal.Decimal,  | The targeted number of nodes in the cluster. | [optional] value must be a 32 bit integer
**previous_attributes** | [**AzureAttributes**](AzureAttributes.md) | [**AzureAttributes**](AzureAttributes.md) |  | [optional] 
**attributes** | [**AzureAttributes**](AzureAttributes.md) | [**AzureAttributes**](AzureAttributes.md) |  | [optional] 
**previous_cluster_size** | [**ClusterSize**](ClusterSize.md) | [**ClusterSize**](ClusterSize.md) |  | [optional] 
**cluster_size** | [**ClusterSize**](ClusterSize.md) | [**ClusterSize**](ClusterSize.md) |  | [optional] 
**cause** | [**ResizeCause**](ResizeCause.md) | [**ResizeCause**](ResizeCause.md) |  | [optional] 
**reason** | [**TerminationReason**](TerminationReason.md) | [**TerminationReason**](TerminationReason.md) |  | [optional] 
**user** | str,  | str,  | The user that caused the event to occur. (Empty if it was done by Azure Databricks.) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

