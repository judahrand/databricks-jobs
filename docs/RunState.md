# RunState

The result and lifecycle state of the run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**life_cycle_state** | [**RunLifeCycleState**](RunLifeCycleState.md) |  | [optional] 
**result_state** | [**RunResultState**](RunResultState.md) |  | [optional] 
**user_cancelled_or_timedout** | **bool** | Whether a run was canceled manually by a user or by the scheduler because the run timed out. | [optional] 
**state_message** | **str** | A descriptive message for the current state. This field is unstructured, and its exact format is subject to change. | [optional] 

## Example

```python
from databricks_jobs.models.run_state import RunState

# TODO update the JSON string below
json = "{}"
# create an instance of RunState from a JSON string
run_state_instance = RunState.from_json(json)
# print the JSON string representation of the object
print RunState.to_json()

# convert the object into a dict
run_state_dict = run_state_instance.to_dict()
# create an instance of RunState from a dict
run_state_form_dict = run_state.from_dict(run_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


