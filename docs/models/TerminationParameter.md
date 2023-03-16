# databricks_jobs.model.termination_parameter.TerminationParameter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**username** | str,  | str,  | The username of the user who terminated the cluster. | [optional] 
**azure_error_code** | str,  | str,  | The Azure provided error code describing why cluster nodes could not be provisioned. For reference, see: [https://docs.microsoft.com/azure/virtual-machines/windows/error-messages](https://docs.microsoft.com/azure/virtual-machines/windows/error-messages). | [optional] 
**azure_error_message** | str,  | str,  | Human-readable context of various failures from Azure. This field is unstructured, and its exact format is subject to change. | [optional] 
**databricks_error_message** | str,  | str,  | Additional context that may explain the reason for cluster termination. This field is unstructured, and its exact format is subject to change. | [optional] 
**inactivity_duration_min** | str,  | str,  | An idle cluster was shut down after being inactive for this duration. | [optional] 
**instance_id** | str,  | str,  | The ID of the instance that was hosting the Spark driver. | [optional] 
**instance_pool_id** | str,  | str,  | The ID of the instance pool the cluster is using. | [optional] 
**instance_pool_error_code** | str,  | str,  | The [error code](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#clusterterminationreasonpoolclusterterminationcode) for cluster failures specific to a pool. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

