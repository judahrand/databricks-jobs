# JobsDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The canonical identifier of the job to delete. This field is required. | 

## Example

```python
from databricks_jobs.models.jobs_delete_request import JobsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobsDeleteRequest from a JSON string
jobs_delete_request_instance = JobsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print JobsDeleteRequest.to_json()

# convert the object into a dict
jobs_delete_request_dict = jobs_delete_request_instance.to_dict()
# create an instance of JobsDeleteRequest from a dict
jobs_delete_request_form_dict = jobs_delete_request.from_dict(jobs_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


