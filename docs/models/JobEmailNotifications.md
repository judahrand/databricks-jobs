# databricks_jobs.model.job_email_notifications.JobEmailNotifications

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[on_start](#on_start)** | list, tuple,  | tuple,  | A list of email addresses to be notified when a run begins. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent. | [optional] 
**[on_success](#on_success)** | list, tuple,  | tuple,  | A list of email addresses to be notified when a run successfully completes. A run is considered to have completed successfully if it ends with a &#x60;TERMINATED&#x60; &#x60;life_cycle_state&#x60; and a &#x60;SUCCESSFUL&#x60; result_state. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent. | [optional] 
**[on_failure](#on_failure)** | list, tuple,  | tuple,  | A list of email addresses to notify when a run completes unsuccessfully. A run is considered unsuccessful if it ends with an &#x60;INTERNAL_ERROR&#x60; &#x60;life_cycle_state&#x60; or a &#x60;SKIPPED&#x60;, &#x60;FAILED&#x60;, or &#x60;TIMED_OUT&#x60; &#x60;result_state&#x60;. If not specified on job creation, reset, or update, or the list is empty, then notifications are not sent. Job-level failure notifications are sent only once after the entire job run (including all of its retries) has failed. Notifications are not sent when failed job runs are retried. To receive a failure notification after every failed task (including every failed retry), use task-level notifications instead. | [optional] 
**no_alert_for_skipped_runs** | bool,  | BoolClass,  | If true, do not send email to recipients specified in &#x60;on_failure&#x60; if the run is skipped. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# on_start

A list of email addresses to be notified when a run begins. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of email addresses to be notified when a run begins. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# on_success

A list of email addresses to be notified when a run successfully completes. A run is considered to have completed successfully if it ends with a `TERMINATED` `life_cycle_state` and a `SUCCESSFUL` result_state. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of email addresses to be notified when a run successfully completes. A run is considered to have completed successfully if it ends with a &#x60;TERMINATED&#x60; &#x60;life_cycle_state&#x60; and a &#x60;SUCCESSFUL&#x60; result_state. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# on_failure

A list of email addresses to notify when a run completes unsuccessfully. A run is considered unsuccessful if it ends with an `INTERNAL_ERROR` `life_cycle_state` or a `SKIPPED`, `FAILED`, or `TIMED_OUT` `result_state`. If not specified on job creation, reset, or update, or the list is empty, then notifications are not sent. Job-level failure notifications are sent only once after the entire job run (including all of its retries) has failed. Notifications are not sent when failed job runs are retried. To receive a failure notification after every failed task (including every failed retry), use task-level notifications instead.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of email addresses to notify when a run completes unsuccessfully. A run is considered unsuccessful if it ends with an &#x60;INTERNAL_ERROR&#x60; &#x60;life_cycle_state&#x60; or a &#x60;SKIPPED&#x60;, &#x60;FAILED&#x60;, or &#x60;TIMED_OUT&#x60; &#x60;result_state&#x60;. If not specified on job creation, reset, or update, or the list is empty, then notifications are not sent. Job-level failure notifications are sent only once after the entire job run (including all of its retries) has failed. Notifications are not sent when failed job runs are retried. To receive a failure notification after every failed task (including every failed retry), use task-level notifications instead. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

