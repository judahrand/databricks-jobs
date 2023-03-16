# databricks_jobs.model.dbt_task.DbtTask

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[commands](#commands)** | list, tuple,  | tuple,  | A list of dbt commands to execute. All commands must start with &#x60;dbt&#x60;. This parameter must not be empty. A maximum of up to 10 commands can be provided. | 
**project_directory** | str,  | str,  | Optional (relative) path to the project directory, if no value is provided, the root of the git repository is used. | [optional] 
**schema** | str,  | str,  | Optional schema to write to. This parameter is only used when a warehouse_id is also provided. If not provided, the &#x60;default&#x60; schema is used. | [optional] 
**warehouse_id** | str,  | str,  | ID of the SQL warehouse to connect to. If provided, we automatically generate and provide the profile and connection details to dbt. It can be overridden on a per-command basis by using the &#x60;--profiles-dir&#x60; command line argument. | [optional] 
**catalog** | str,  | str,  | Optional name of the catalog to use. The value is the top level in the 3-level namespace of Unity Catalog (catalog / schema / relation). The catalog value can only be specified if a warehouse_id is specified. Requires dbt-databricks &gt;&#x3D; 1.1.1. | [optional] 
**profiles_directory** | str,  | str,  | Optional (relative) path to the profiles directory. Can only be specified if no warehouse_id is specified. If no warehouse_id is specified and this folder is unset, the root directory is used. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# commands

A list of dbt commands to execute. All commands must start with `dbt`. This parameter must not be empty. A maximum of up to 10 commands can be provided.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of dbt commands to execute. All commands must start with &#x60;dbt&#x60;. This parameter must not be empty. A maximum of up to 10 commands can be provided. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

