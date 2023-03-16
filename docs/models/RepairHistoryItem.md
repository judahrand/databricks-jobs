# databricks_jobs.model.repair_history_item.RepairHistoryItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The repair history item type. Indicates whether a run is the original run or a repair run. | [optional] must be one of ["ORIGINAL", "REPAIR", ] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | The start time of the (repaired) run. | [optional] value must be a 64 bit integer
**end_time** | decimal.Decimal, int,  | decimal.Decimal,  | The end time of the (repaired) run. | [optional] value must be a 64 bit integer
**state** | [**RunState**](RunState.md) | [**RunState**](RunState.md) |  | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the repair. Only returned for the items that represent a repair in &#x60;repair_history&#x60;. | [optional] value must be a 64 bit integer
**[task_run_ids](#task_run_ids)** | list, tuple,  | tuple,  | The run IDs of the task runs that ran as part of this repair history item. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# task_run_ids

The run IDs of the task runs that ran as part of this repair history item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The run IDs of the task runs that ran as part of this repair history item. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

