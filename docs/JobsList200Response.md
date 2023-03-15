# JobsList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[Job]**](Job.md) | The list of jobs. | [optional] 
**has_more** | **bool** |  | [optional] 

## Example

```python
from databricks_jobs.models.jobs_list200_response import JobsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JobsList200Response from a JSON string
jobs_list200_response_instance = JobsList200Response.from_json(json)
# print the JSON string representation of the object
print JobsList200Response.to_json()

# convert the object into a dict
jobs_list200_response_dict = jobs_list200_response_instance.to_dict()
# create an instance of JobsList200Response from a dict
jobs_list200_response_form_dict = jobs_list200_response.from_dict(jobs_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


