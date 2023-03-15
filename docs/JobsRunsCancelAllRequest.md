# JobsRunsCancelAllRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The canonical identifier of the job to cancel all runs of. This field is required. | 

## Example

```python
from databricks_jobs.models.jobs_runs_cancel_all_request import JobsRunsCancelAllRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobsRunsCancelAllRequest from a JSON string
jobs_runs_cancel_all_request_instance = JobsRunsCancelAllRequest.from_json(json)
# print the JSON string representation of the object
print JobsRunsCancelAllRequest.to_json()

# convert the object into a dict
jobs_runs_cancel_all_request_dict = jobs_runs_cancel_all_request_instance.to_dict()
# create an instance of JobsRunsCancelAllRequest from a dict
jobs_runs_cancel_all_request_form_dict = jobs_runs_cancel_all_request.from_dict(jobs_runs_cancel_all_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


