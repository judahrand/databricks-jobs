# JobsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The canonical identifier for this job. | [optional] 
**creator_user_name** | **str** | The creator user name. This field won’t be included in the response if the user has been deleted. | [optional] 
**run_as_user_name** | **str** | The user name that the job runs as. &#x60;run_as_user_name&#x60; is based on the current job settings, and is set to the creator of the job if job access control is disabled, or the &#x60;is_owner&#x60; permission if job access control is enabled. | [optional] 
**settings** | [**JobSettings**](JobSettings.md) |  | [optional] 
**created_time** | **int** | The time at which this job was created in epoch milliseconds (milliseconds since 1/1/1970 UTC). | [optional] 

## Example

```python
from databricks_jobs.models.jobs_get200_response import JobsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JobsGet200Response from a JSON string
jobs_get200_response_instance = JobsGet200Response.from_json(json)
# print the JSON string representation of the object
print JobsGet200Response.to_json()

# convert the object into a dict
jobs_get200_response_dict = jobs_get200_response_instance.to_dict()
# create an instance of JobsGet200Response from a dict
jobs_get200_response_form_dict = jobs_get200_response.from_dict(jobs_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


