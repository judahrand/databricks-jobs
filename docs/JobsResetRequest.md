# JobsResetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The canonical identifier of the job to reset. This field is required. | 
**new_settings** | [**JobSettings**](JobSettings.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.jobs_reset_request import JobsResetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobsResetRequest from a JSON string
jobs_reset_request_instance = JobsResetRequest.from_json(json)
# print the JSON string representation of the object
print JobsResetRequest.to_json()

# convert the object into a dict
jobs_reset_request_dict = jobs_reset_request_instance.to_dict()
# create an instance of JobsResetRequest from a dict
jobs_reset_request_form_dict = jobs_reset_request.from_dict(jobs_reset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


