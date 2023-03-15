# JobsCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | An optional name for the job. | [optional] [default to 'Untitled']
**tags** | **object** | A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job. | [optional] 
**tasks** | [**List[JobTaskSettings]**](JobTaskSettings.md) | A list of task specifications to be executed by this job. | [optional] 
**job_clusters** | [**List[JobCluster]**](JobCluster.md) | A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings. | [optional] 
**email_notifications** | [**JobEmailNotifications**](JobEmailNotifications.md) |  | [optional] 
**webhook_notifications** | [**WebhookNotifications**](WebhookNotifications.md) |  | [optional] 
**timeout_seconds** | **int** | An optional timeout applied to each run of this job. The default behavior is to have no timeout. | [optional] 
**schedule** | [**CronSchedule**](CronSchedule.md) |  | [optional] 
**max_concurrent_runs** | **int** | An optional maximum allowed number of concurrent runs of the job.  Set this value if you want to be able to execute multiple runs of the same job concurrently. This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters.  This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from then on, new runs are skipped unless there are fewer than 3 active runs.  This value cannot exceed 1000\\. Setting this value to 0 causes all new runs to be skipped. The default behavior is to allow only 1 concurrent run. | [optional] 
**git_source** | [**GitSource**](GitSource.md) |  | [optional] 
**format** | **str** | Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to &#x60;\&quot;MULTI_TASK\&quot;&#x60;. | [optional] 
**access_control_list** | [**List[AccessControlRequest]**](AccessControlRequest.md) | List of permissions to set on the job. | [optional] 

## Example

```python
from databricks_jobs.models.jobs_create_request import JobsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobsCreateRequest from a JSON string
jobs_create_request_instance = JobsCreateRequest.from_json(json)
# print the JSON string representation of the object
print JobsCreateRequest.to_json()

# convert the object into a dict
jobs_create_request_dict = jobs_create_request_instance.to_dict()
# create an instance of JobsCreateRequest from a dict
jobs_create_request_form_dict = jobs_create_request.from_dict(jobs_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


