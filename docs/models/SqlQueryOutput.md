# databricks_jobs.model.sql_query_output.SqlQueryOutput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**query_text** | str,  | str,  | The text of the SQL query. Can Run permission of the SQL query is required to view this field. | [optional] 
**warehouse_id** | str,  | str,  | The canonical identifier of the SQL warehouse. | [optional] 
**sql_statements** | [**SqlStatementOutput**](SqlStatementOutput.md) | [**SqlStatementOutput**](SqlStatementOutput.md) |  | [optional] 
**output_link** | str,  | str,  | The link to find the output results. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

