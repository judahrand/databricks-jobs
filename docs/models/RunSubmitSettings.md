# databricks_jobs.model.run_submit_settings.RunSubmitSettings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[tasks](#tasks)** | list, tuple,  | tuple,  |  | [optional] 
**run_name** | str,  | str,  | An optional name for the run. The default value is &#x60;Untitled&#x60;. | [optional] 
**webhook_notifications** | [**WebhookNotifications**](WebhookNotifications.md) | [**WebhookNotifications**](WebhookNotifications.md) |  | [optional] 
**git_source** | [**GitSource**](GitSource.md) | [**GitSource**](GitSource.md) |  | [optional] 
**timeout_seconds** | decimal.Decimal, int,  | decimal.Decimal,  | An optional timeout applied to each run of this job. The default behavior is to have no timeout. | [optional] value must be a 32 bit integer
**idempotency_token** | str,  | str,  | An optional token that can be used to guarantee the idempotency of job run requests. If a run with the provided token already exists, the request does not create a new run but returns the ID of the existing run instead. If a run with the provided token is deleted, an error is returned.  If you specify the idempotency token, upon failure you can retry until the request succeeds. Databricks guarantees that exactly one run is launched with that idempotency token.  This token must have at most 64 characters.  For more information, see [How to ensure idempotency for jobs](https://docs.microsoft.com/azure/databricks/kb/jobs/jobs-idempotency). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tasks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RunSubmitTaskSettings**](RunSubmitTaskSettings.md) | [**RunSubmitTaskSettings**](RunSubmitTaskSettings.md) | [**RunSubmitTaskSettings**](RunSubmitTaskSettings.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

