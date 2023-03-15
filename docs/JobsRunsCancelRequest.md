# JobsRunsCancelRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** | This field is required. | 

## Example

```python
from databricks_jobs.models.jobs_runs_cancel_request import JobsRunsCancelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobsRunsCancelRequest from a JSON string
jobs_runs_cancel_request_instance = JobsRunsCancelRequest.from_json(json)
# print the JSON string representation of the object
print JobsRunsCancelRequest.to_json()

# convert the object into a dict
jobs_runs_cancel_request_dict = jobs_runs_cancel_request_instance.to_dict()
# create an instance of JobsRunsCancelRequest from a dict
jobs_runs_cancel_request_form_dict = jobs_runs_cancel_request.from_dict(jobs_runs_cancel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


