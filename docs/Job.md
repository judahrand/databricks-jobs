# Job


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The canonical identifier for this job. | [optional] 
**creator_user_name** | **str** | The creator user name. This field won’t be included in the response if the user has already been deleted. | [optional] 
**settings** | [**JobSettings**](JobSettings.md) |  | [optional] 
**created_time** | **int** | The time at which this job was created in epoch milliseconds (milliseconds since 1/1/1970 UTC). | [optional] 

## Example

```python
from databricks_jobs.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print Job.to_json()

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_form_dict = job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


