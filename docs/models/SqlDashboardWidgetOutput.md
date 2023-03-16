# databricks_jobs.model.sql_dashboard_widget_output.SqlDashboardWidgetOutput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**widget_id** | str,  | str,  | The canonical identifier of the SQL widget. | [optional] 
**widget_title** | str,  | str,  | The title of the SQL widget. | [optional] 
**output_link** | str,  | str,  | The link to find the output results. | [optional] 
**status** | str,  | str,  | The execution status of the SQL widget. | [optional] must be one of ["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED", ] 
**error** | [**SqlOutputError**](SqlOutputError.md) | [**SqlOutputError**](SqlOutputError.md) |  | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time (in epoch milliseconds) when execution of the SQL widget starts. | [optional] value must be a 64 bit integer
**end_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time (in epoch milliseconds) when execution of the SQL widget ends. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

