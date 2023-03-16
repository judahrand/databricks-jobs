# databricks_jobs.model.jobs_run_now200_response.JobsRunNow200Response

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**run_id** | decimal.Decimal, int,  | decimal.Decimal,  | The globally unique ID of the newly triggered run. | [optional] value must be a 64 bit integer
**number_in_job** | decimal.Decimal, int,  | decimal.Decimal,  | A unique identifier for this job run. This is set to the same value as &#x60;run_id&#x60;. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

