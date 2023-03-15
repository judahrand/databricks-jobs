# RepairHistoryItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The repair history item type. Indicates whether a run is the original run or a repair run. | [optional] 
**start_time** | **int** | The start time of the (repaired) run. | [optional] 
**end_time** | **int** | The end time of the (repaired) run. | [optional] 
**state** | [**RunState**](RunState.md) |  | [optional] 
**id** | **int** | The ID of the repair. Only returned for the items that represent a repair in &#x60;repair_history&#x60;. | [optional] 
**task_run_ids** | **List[int]** | The run IDs of the task runs that ran as part of this repair history item. | [optional] 

## Example

```python
from databricks_jobs.models.repair_history_item import RepairHistoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of RepairHistoryItem from a JSON string
repair_history_item_instance = RepairHistoryItem.from_json(json)
# print the JSON string representation of the object
print RepairHistoryItem.to_json()

# convert the object into a dict
repair_history_item_dict = repair_history_item_instance.to_dict()
# create an instance of RepairHistoryItem from a dict
repair_history_item_form_dict = repair_history_item.from_dict(repair_history_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


