# JobsUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The canonical identifier of the job to update. This field is required. | 
**new_settings** | [**JobSettings**](JobSettings.md) |  | [optional] 
**fields_to_remove** | **List[str]** | Remove top-level fields in the job settings. Removing nested fields is not supported. This field is optional. | [optional] 

## Example

```python
from databricks_jobs.models.jobs_update_request import JobsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobsUpdateRequest from a JSON string
jobs_update_request_instance = JobsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print JobsUpdateRequest.to_json()

# convert the object into a dict
jobs_update_request_dict = jobs_update_request_instance.to_dict()
# create an instance of JobsUpdateRequest from a dict
jobs_update_request_form_dict = jobs_update_request.from_dict(jobs_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


