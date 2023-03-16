# databricks_jobs.model.repair_run_input.RepairRunInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**run_id** | decimal.Decimal, int,  | decimal.Decimal,  | The job run ID of the run to repair. The run must not be in progress. | [optional] value must be a 64 bit integer
**[rerun_tasks](#rerun_tasks)** | list, tuple,  | tuple,  | The task keys of the task runs to repair. | [optional] 
**latest_repair_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the latest repair. This parameter is not required when repairing a run for the first time, but must be provided on subsequent requests to repair the same run. | [optional] value must be a 64 bit integer
**rerun_all_failed_tasks** | bool,  | BoolClass,  | If true, repair all failed tasks. Only one of rerun_tasks or rerun_all_failed_tasks can be used. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rerun_tasks

The task keys of the task runs to repair.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The task keys of the task runs to repair. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

