# JobsRunNow200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** | The globally unique ID of the newly triggered run. | [optional] 
**number_in_job** | **int** | A unique identifier for this job run. This is set to the same value as &#x60;run_id&#x60;. | [optional] 

## Example

```python
from databricks_jobs.models.jobs_run_now200_response import JobsRunNow200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JobsRunNow200Response from a JSON string
jobs_run_now200_response_instance = JobsRunNow200Response.from_json(json)
# print the JSON string representation of the object
print JobsRunNow200Response.to_json()

# convert the object into a dict
jobs_run_now200_response_dict = jobs_run_now200_response_instance.to_dict()
# create an instance of JobsRunNow200Response from a dict
jobs_run_now200_response_form_dict = jobs_run_now200_response.from_dict(jobs_run_now200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


