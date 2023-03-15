# RepairRunInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** | The job run ID of the run to repair. The run must not be in progress. | [optional] 
**rerun_tasks** | **List[str]** | The task keys of the task runs to repair. | [optional] 
**latest_repair_id** | **int** | The ID of the latest repair. This parameter is not required when repairing a run for the first time, but must be provided on subsequent requests to repair the same run. | [optional] 
**rerun_all_failed_tasks** | **bool** | If true, repair all failed tasks. Only one of rerun_tasks or rerun_all_failed_tasks can be used. | [optional] [default to False]

## Example

```python
from databricks_jobs.models.repair_run_input import RepairRunInput

# TODO update the JSON string below
json = "{}"
# create an instance of RepairRunInput from a JSON string
repair_run_input_instance = RepairRunInput.from_json(json)
# print the JSON string representation of the object
print RepairRunInput.to_json()

# convert the object into a dict
repair_run_input_dict = repair_run_input_instance.to_dict()
# create an instance of RepairRunInput from a dict
repair_run_input_form_dict = repair_run_input.from_dict(repair_run_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


