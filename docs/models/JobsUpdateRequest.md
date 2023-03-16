# databricks_jobs.model.jobs_update_request.JobsUpdateRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**job_id** | decimal.Decimal, int,  | decimal.Decimal,  | The canonical identifier of the job to update. This field is required. | value must be a 64 bit integer
**new_settings** | [**JobSettings**](JobSettings.md) | [**JobSettings**](JobSettings.md) |  | [optional] 
**[fields_to_remove](#fields_to_remove)** | list, tuple,  | tuple,  | Remove top-level fields in the job settings. Removing nested fields is not supported. This field is optional. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fields_to_remove

Remove top-level fields in the job settings. Removing nested fields is not supported. This field is optional.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Remove top-level fields in the job settings. Removing nested fields is not supported. This field is optional. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

