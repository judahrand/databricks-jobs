# RunSubmitSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks** | [**List[RunSubmitTaskSettings]**](RunSubmitTaskSettings.md) |  | [optional] 
**run_name** | **str** | An optional name for the run. The default value is &#x60;Untitled&#x60;. | [optional] 
**webhook_notifications** | [**WebhookNotifications**](WebhookNotifications.md) |  | [optional] 
**git_source** | [**GitSource**](GitSource.md) |  | [optional] 
**timeout_seconds** | **int** | An optional timeout applied to each run of this job. The default behavior is to have no timeout. | [optional] 
**idempotency_token** | **str** | An optional token that can be used to guarantee the idempotency of job run requests. If a run with the provided token already exists, the request does not create a new run but returns the ID of the existing run instead. If a run with the provided token is deleted, an error is returned.  If you specify the idempotency token, upon failure you can retry until the request succeeds. Databricks guarantees that exactly one run is launched with that idempotency token.  This token must have at most 64 characters.  For more information, see [How to ensure idempotency for jobs](https://docs.microsoft.com/azure/databricks/kb/jobs/jobs-idempotency). | [optional] 

## Example

```python
from databricks_jobs.models.run_submit_settings import RunSubmitSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RunSubmitSettings from a JSON string
run_submit_settings_instance = RunSubmitSettings.from_json(json)
# print the JSON string representation of the object
print RunSubmitSettings.to_json()

# convert the object into a dict
run_submit_settings_dict = run_submit_settings_instance.to_dict()
# create an instance of RunSubmitSettings from a dict
run_submit_settings_form_dict = run_submit_settings.from_dict(run_submit_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


