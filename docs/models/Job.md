# databricks_jobs.model.job.Job

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**job_id** | decimal.Decimal, int,  | decimal.Decimal,  | The canonical identifier for this job. | [optional] value must be a 64 bit integer
**creator_user_name** | str,  | str,  | The creator user name. This field won’t be included in the response if the user has already been deleted. | [optional] 
**settings** | [**JobSettings**](JobSettings.md) | [**JobSettings**](JobSettings.md) |  | [optional] 
**created_time** | decimal.Decimal, int,  | decimal.Decimal,  | The time at which this job was created in epoch milliseconds (milliseconds since 1/1/1970 UTC). | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

