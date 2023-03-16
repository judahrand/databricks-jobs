# databricks_jobs.model.trigger_type.TriggerType

* `PERIODIC`: Schedules that periodically trigger runs, such as a cron scheduler. * `ONE_TIME`: One time triggers that fire a single run. This occurs you triggered a single run on demand through the UI or the API. * `RETRY`: Indicates a run that is triggered as a retry of a previously failed run. This occurs when you request to re-run the job in case of failures.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | * &#x60;PERIODIC&#x60;: Schedules that periodically trigger runs, such as a cron scheduler. * &#x60;ONE_TIME&#x60;: One time triggers that fire a single run. This occurs you triggered a single run on demand through the UI or the API. * &#x60;RETRY&#x60;: Indicates a run that is triggered as a retry of a previously failed run. This occurs when you request to re-run the job in case of failures. | must be one of ["PERIODIC", "ONE_TIME", "RETRY", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

