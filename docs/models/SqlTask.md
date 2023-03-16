# databricks_jobs.model.sql_task.SqlTask

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**warehouse_id** | str,  | str,  | The canonical identifier of the SQL warehouse. Only serverless and pro SQL warehouses are supported. | 
**query** | [**SqlTaskQuery**](SqlTaskQuery.md) | [**SqlTaskQuery**](SqlTaskQuery.md) |  | [optional] 
**dashboard** | [**SqlTaskDashboard**](SqlTaskDashboard.md) | [**SqlTaskDashboard**](SqlTaskDashboard.md) |  | [optional] 
**alert** | [**SqlTaskAlert**](SqlTaskAlert.md) | [**SqlTaskAlert**](SqlTaskAlert.md) |  | [optional] 
**[parameters](#parameters)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Parameters to be used for each run of this job. The SQL alert task does not support custom parameters. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# parameters

Parameters to be used for each run of this job. The SQL alert task does not support custom parameters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Parameters to be used for each run of this job. The SQL alert task does not support custom parameters. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

