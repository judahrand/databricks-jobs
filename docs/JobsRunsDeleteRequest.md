# JobsRunsDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** | The canonical identifier of the run for which to retrieve the metadata. | [optional] 

## Example

```python
from databricks_jobs.models.jobs_runs_delete_request import JobsRunsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobsRunsDeleteRequest from a JSON string
jobs_runs_delete_request_instance = JobsRunsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print JobsRunsDeleteRequest.to_json()

# convert the object into a dict
jobs_runs_delete_request_dict = jobs_runs_delete_request_instance.to_dict()
# create an instance of JobsRunsDeleteRequest from a dict
jobs_runs_delete_request_form_dict = jobs_runs_delete_request.from_dict(jobs_runs_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


