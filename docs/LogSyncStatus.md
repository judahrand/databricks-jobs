# LogSyncStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_attempted** | **int** | The timestamp of last attempt. If the last attempt fails, last_exception contains the exception in the last attempt. | [optional] 
**last_exception** | **str** | The exception thrown in the last attempt, it would be null (omitted in the response) if there is no exception in last attempted. | [optional] 

## Example

```python
from databricks_jobs.models.log_sync_status import LogSyncStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LogSyncStatus from a JSON string
log_sync_status_instance = LogSyncStatus.from_json(json)
# print the JSON string representation of the object
print LogSyncStatus.to_json()

# convert the object into a dict
log_sync_status_dict = log_sync_status_instance.to_dict()
# create an instance of LogSyncStatus from a dict
log_sync_status_form_dict = log_sync_status.from_dict(log_sync_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


