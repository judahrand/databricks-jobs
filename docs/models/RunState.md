# databricks_jobs.model.run_state.RunState

The result and lifecycle state of the run.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The result and lifecycle state of the run. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**life_cycle_state** | [**RunLifeCycleState**](RunLifeCycleState.md) | [**RunLifeCycleState**](RunLifeCycleState.md) |  | [optional] 
**result_state** | [**RunResultState**](RunResultState.md) | [**RunResultState**](RunResultState.md) |  | [optional] 
**user_cancelled_or_timedout** | bool,  | BoolClass,  | Whether a run was canceled manually by a user or by the scheduler because the run timed out. | [optional] 
**state_message** | str,  | str,  | A descriptive message for the current state. This field is unstructured, and its exact format is subject to change. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

