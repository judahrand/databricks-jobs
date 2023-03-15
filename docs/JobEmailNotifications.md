# JobEmailNotifications


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_start** | **List[str]** | A list of email addresses to be notified when a run begins. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent. | [optional] 
**on_success** | **List[str]** | A list of email addresses to be notified when a run successfully completes. A run is considered to have completed successfully if it ends with a &#x60;TERMINATED&#x60; &#x60;life_cycle_state&#x60; and a &#x60;SUCCESSFUL&#x60; result_state. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent. | [optional] 
**on_failure** | **List[str]** | A list of email addresses to notify when a run completes unsuccessfully. A run is considered unsuccessful if it ends with an &#x60;INTERNAL_ERROR&#x60; &#x60;life_cycle_state&#x60; or a &#x60;SKIPPED&#x60;, &#x60;FAILED&#x60;, or &#x60;TIMED_OUT&#x60; &#x60;result_state&#x60;. If not specified on job creation, reset, or update, or the list is empty, then notifications are not sent. Job-level failure notifications are sent only once after the entire job run (including all of its retries) has failed. Notifications are not sent when failed job runs are retried. To receive a failure notification after every failed task (including every failed retry), use task-level notifications instead. | [optional] 
**no_alert_for_skipped_runs** | **bool** | If true, do not send email to recipients specified in &#x60;on_failure&#x60; if the run is skipped. | [optional] 

## Example

```python
from databricks_jobs.models.job_email_notifications import JobEmailNotifications

# TODO update the JSON string below
json = "{}"
# create an instance of JobEmailNotifications from a JSON string
job_email_notifications_instance = JobEmailNotifications.from_json(json)
# print the JSON string representation of the object
print JobEmailNotifications.to_json()

# convert the object into a dict
job_email_notifications_dict = job_email_notifications_instance.to_dict()
# create an instance of JobEmailNotifications from a dict
job_email_notifications_form_dict = job_email_notifications.from_dict(job_email_notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


