# JobsRunsList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runs** | [**List[Run]**](Run.md) | A list of runs, from most recently started to least. | [optional] 
**has_more** | **bool** | If true, additional runs matching the provided filter are available for listing. | [optional] 

## Example

```python
from databricks_jobs.models.jobs_runs_list200_response import JobsRunsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JobsRunsList200Response from a JSON string
jobs_runs_list200_response_instance = JobsRunsList200Response.from_json(json)
# print the JSON string representation of the object
print JobsRunsList200Response.to_json()

# convert the object into a dict
jobs_runs_list200_response_dict = jobs_runs_list200_response_instance.to_dict()
# create an instance of JobsRunsList200Response from a dict
jobs_runs_list200_response_form_dict = jobs_runs_list200_response.from_dict(jobs_runs_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


