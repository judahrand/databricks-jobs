# RepairHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repair_history** | [**List[RepairHistoryItem]**](RepairHistoryItem.md) | The repair history of the run. | [optional] 

## Example

```python
from databricks_jobs.models.repair_history import RepairHistory

# TODO update the JSON string below
json = "{}"
# create an instance of RepairHistory from a JSON string
repair_history_instance = RepairHistory.from_json(json)
# print the JSON string representation of the object
print RepairHistory.to_json()

# convert the object into a dict
repair_history_dict = repair_history_instance.to_dict()
# create an instance of RepairHistory from a dict
repair_history_form_dict = repair_history.from_dict(repair_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


