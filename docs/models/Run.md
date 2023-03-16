# databricks_jobs.model.run.Run

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**job_id** | decimal.Decimal, int,  | decimal.Decimal,  | The canonical identifier of the job that contains this run. | [optional] value must be a 64 bit integer
**run_id** | decimal.Decimal, int,  | decimal.Decimal,  | The canonical identifier of the run. This ID is unique across all runs of all jobs. | [optional] value must be a 64 bit integer
**number_in_job** | decimal.Decimal, int,  | decimal.Decimal,  | A unique identifier for this job run. This is set to the same value as &#x60;run_id&#x60;. | [optional] value must be a 64 bit integer
**creator_user_name** | str,  | str,  | The creator user name. This field won’t be included in the response if the user has already been deleted. | [optional] 
**original_attempt_run_id** | decimal.Decimal, int,  | decimal.Decimal,  | If this run is a retry of a prior run attempt, this field contains the run_id of the original attempt; otherwise, it is the same as the run_id. | [optional] value must be a 64 bit integer
**state** | [**RunState**](RunState.md) | [**RunState**](RunState.md) |  | [optional] 
**schedule** | [**CronSchedule**](CronSchedule.md) | [**CronSchedule**](CronSchedule.md) |  | [optional] 
**[tasks](#tasks)** | list, tuple,  | tuple,  | The list of tasks performed by the run. Each task has its own &#x60;run_id&#x60; which you can use to call &#x60;JobsGetOutput&#x60; to retrieve the run resutls. | [optional] 
**[job_clusters](#job_clusters)** | list, tuple,  | tuple,  | A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings. | [optional] 
**cluster_spec** | [**ClusterSpec**](ClusterSpec.md) | [**ClusterSpec**](ClusterSpec.md) |  | [optional] 
**cluster_instance** | [**ClusterInstance**](ClusterInstance.md) | [**ClusterInstance**](ClusterInstance.md) |  | [optional] 
**git_source** | [**GitSource**](GitSource.md) | [**GitSource**](GitSource.md) |  | [optional] 
**overriding_parameters** | [**RunParameters**](RunParameters.md) | [**RunParameters**](RunParameters.md) |  | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued. | [optional] value must be a 64 bit integer
**setup_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the &#x60;setup_duration&#x60;, &#x60;execution_duration&#x60;, and the &#x60;cleanup_duration&#x60;. The &#x60;setup_duration&#x60; field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the &#x60;run_duration&#x60; field. | [optional] value must be a 64 bit integer
**execution_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The time in milliseconds it took to execute the commands in the JAR or notebook until they  completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the &#x60;setup_duration&#x60;, &#x60;execution_duration&#x60;, and the  &#x60;cleanup_duration&#x60;. The &#x60;execution_duration&#x60; field is set to 0 for multitask job runs. The total  duration of a multitask job run is the value of the &#x60;run_duration&#x60; field. | [optional] value must be a 64 bit integer
**cleanup_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the &#x60;setup_duration&#x60;, &#x60;execution_duration&#x60;, and the &#x60;cleanup_duration&#x60;. The &#x60;cleanup_duration&#x60; field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the &#x60;run_duration&#x60; field. | [optional] value must be a 64 bit integer
**end_time** | decimal.Decimal, int,  | decimal.Decimal,  | The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running. | [optional] value must be a 64 bit integer
**run_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The time in milliseconds it took the job run and all of its repairs to finish. This field is only set for multitask job runs and not task runs. The duration of a task run is the sum of the &#x60;setup_duration&#x60;, &#x60;execution_duration&#x60;, and the &#x60;cleanup_duration&#x60;. | [optional] 
**trigger** | [**TriggerType**](TriggerType.md) | [**TriggerType**](TriggerType.md) |  | [optional] 
**run_name** | str,  | str,  | An optional name for the run. The maximum allowed length is 4096 bytes in UTF-8 encoding. | [optional] if omitted the server will use the default value of "Untitled"
**run_page_url** | str,  | str,  | The URL to the detail page of the run. | [optional] 
**run_type** | [**RunType**](RunType.md) | [**RunType**](RunType.md) |  | [optional] 
**attempt_number** | decimal.Decimal, int,  | decimal.Decimal,  | The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0\\. If the initial run attempt fails, and the job has a retry policy (&#x60;max_retries&#x60; \\&gt; 0), subsequent runs are created with an &#x60;original_attempt_run_id&#x60; of the original attempt’s ID and an incrementing &#x60;attempt_number&#x60;. Runs are retried only until they succeed, and the maximum &#x60;attempt_number&#x60; is the same as the &#x60;max_retries&#x60; value for the job. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tasks

The list of tasks performed by the run. Each task has its own `run_id` which you can use to call `JobsGetOutput` to retrieve the run resutls.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of tasks performed by the run. Each task has its own &#x60;run_id&#x60; which you can use to call &#x60;JobsGetOutput&#x60; to retrieve the run resutls. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RunTask**](RunTask.md) | [**RunTask**](RunTask.md) | [**RunTask**](RunTask.md) |  | 

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

