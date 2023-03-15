# RunNowInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The ID of the job to be executed | [optional] 
**idempotency_token** | **str** | An optional token to guarantee the idempotency of job run requests. If a run with the provided token already exists, the request does not create a new run but returns the ID of the existing run instead. If a run with the provided token is deleted, an error is returned.  If you specify the idempotency token, upon failure you can retry until the request succeeds. Databricks guarantees that exactly one run is launched with that idempotency token.  This token must have at most 64 characters.  For more information, see [How to ensure idempotency for jobs](https://docs.microsoft.com/azure/databricks/kb/jobs/jobs-idempotency). | [optional] 

## Example

```python
from databricks_jobs.models.run_now_input import RunNowInput

# TODO update the JSON string below
json = "{}"
# create an instance of RunNowInput from a JSON string
run_now_input_instance = RunNowInput.from_json(json)
# print the JSON string representation of the object
print RunNowInput.to_json()

# convert the object into a dict
run_now_input_dict = run_now_input_instance.to_dict()
# create an instance of RunNowInput from a dict
run_now_input_form_dict = run_now_input.from_dict(run_now_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


