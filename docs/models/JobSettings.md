# databricks_jobs.model.job_settings.JobSettings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | An optional name for the job. | [optional] if omitted the server will use the default value of "Untitled"
**[tags](#tags)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job. | [optional] if omitted the server will use the default value of {}
**[tasks](#tasks)** | list, tuple,  | tuple,  | A list of task specifications to be executed by this job. | [optional] 
**[job_clusters](#job_clusters)** | list, tuple,  | tuple,  | A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings. | [optional] 
**email_notifications** | [**JobEmailNotifications**](JobEmailNotifications.md) | [**JobEmailNotifications**](JobEmailNotifications.md) |  | [optional] 
**webhook_notifications** | [**WebhookNotifications**](WebhookNotifications.md) | [**WebhookNotifications**](WebhookNotifications.md) |  | [optional] 
**timeout_seconds** | decimal.Decimal, int,  | decimal.Decimal,  | An optional timeout applied to each run of this job. The default behavior is to have no timeout. | [optional] value must be a 32 bit integer
**schedule** | [**CronSchedule**](CronSchedule.md) | [**CronSchedule**](CronSchedule.md) |  | [optional] 
**max_concurrent_runs** | decimal.Decimal, int,  | decimal.Decimal,  | An optional maximum allowed number of concurrent runs of the job.  Set this value if you want to be able to execute multiple runs of the same job concurrently. This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters.  This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from then on, new runs are skipped unless there are fewer than 3 active runs.  This value cannot exceed 1000\\. Setting this value to 0 causes all new runs to be skipped. The default behavior is to allow only 1 concurrent run. | [optional] value must be a 32 bit integer
**git_source** | [**GitSource**](GitSource.md) | [**GitSource**](GitSource.md) |  | [optional] 
**format** | str,  | str,  | Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to &#x60;\&quot;MULTI_TASK\&quot;&#x60;. | [optional] must be one of ["SINGLE_TASK", "MULTI_TASK", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job. | if omitted the server will use the default value of {}

# tasks

A list of task specifications to be executed by this job.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of task specifications to be executed by this job. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**JobTaskSettings**](JobTaskSettings.md) | [**JobTaskSettings**](JobTaskSettings.md) | [**JobTaskSettings**](JobTaskSettings.md) |  | 

# job_clusters

A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**JobCluster**](JobCluster.md) | [**JobCluster**](JobCluster.md) | [**JobCluster**](JobCluster.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

