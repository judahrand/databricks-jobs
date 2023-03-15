# JobsRunsSubmit200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** | The canonical identifier for the newly submitted run. | [optional] 

## Example

```python
from databricks_jobs.models.jobs_runs_submit200_response import JobsRunsSubmit200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JobsRunsSubmit200Response from a JSON string
jobs_runs_submit200_response_instance = JobsRunsSubmit200Response.from_json(json)
# print the JSON string representation of the object
print JobsRunsSubmit200Response.to_json()

# convert the object into a dict
jobs_runs_submit200_response_dict = jobs_runs_submit200_response_instance.to_dict()
# create an instance of JobsRunsSubmit200Response from a dict
jobs_runs_submit200_response_form_dict = jobs_runs_submit200_response.from_dict(jobs_runs_submit200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


