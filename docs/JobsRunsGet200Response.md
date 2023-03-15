# JobsRunsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The canonical identifier of the job that contains this run. | [optional] 
**run_id** | **int** | The canonical identifier of the run. This ID is unique across all runs of all jobs. | [optional] 
**number_in_job** | **int** | A unique identifier for this job run. This is set to the same value as &#x60;run_id&#x60;. | [optional] 
**creator_user_name** | **str** | The creator user name. This field won’t be included in the response if the user has already been deleted. | [optional] 
**original_attempt_run_id** | **int** | If this run is a retry of a prior run attempt, this field contains the run_id of the original attempt; otherwise, it is the same as the run_id. | [optional] 
**state** | [**RunState**](RunState.md) |  | [optional] 
**schedule** | [**CronSchedule**](CronSchedule.md) |  | [optional] 
**tasks** | [**List[RunTask]**](RunTask.md) | The list of tasks performed by the run. Each task has its own &#x60;run_id&#x60; which you can use to call &#x60;JobsGetOutput&#x60; to retrieve the run resutls. | [optional] 
**job_clusters** | [**List[JobCluster]**](JobCluster.md) | A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings. | [optional] 
**cluster_spec** | [**ClusterSpec**](ClusterSpec.md) |  | [optional] 
**cluster_instance** | [**ClusterInstance**](ClusterInstance.md) |  | [optional] 
**git_source** | [**GitSource**](GitSource.md) |  | [optional] 
**overriding_parameters** | [**RunParameters**](RunParameters.md) |  | [optional] 
**start_time** | **int** | The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued. | [optional] 
**setup_duration** | **int** | The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the &#x60;setup_duration&#x60;, &#x60;execution_duration&#x60;, and the &#x60;cleanup_duration&#x60;. The &#x60;setup_duration&#x60; field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the &#x60;run_duration&#x60; field. | [optional] 
**execution_duration** | **int** | The time in milliseconds it took to execute the commands in the JAR or notebook until they  completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the &#x60;setup_duration&#x60;, &#x60;execution_duration&#x60;, and the  &#x60;cleanup_duration&#x60;. The &#x60;execution_duration&#x60; field is set to 0 for multitask job runs. The total  duration of a multitask job run is the value of the &#x60;run_duration&#x60; field. | [optional] 
**cleanup_duration** | **int** | The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the &#x60;setup_duration&#x60;, &#x60;execution_duration&#x60;, and the &#x60;cleanup_duration&#x60;. The &#x60;cleanup_duration&#x60; field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the &#x60;run_duration&#x60; field. | [optional] 
**end_time** | **int** | The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running. | [optional] 
**run_duration** | **int** | The time in milliseconds it took the job run and all of its repairs to finish. This field is only set for multitask job runs and not task runs. The duration of a task run is the sum of the &#x60;setup_duration&#x60;, &#x60;execution_duration&#x60;, and the &#x60;cleanup_duration&#x60;. | [optional] 
**trigger** | [**TriggerType**](TriggerType.md) |  | [optional] 
**run_name** | **str** | An optional name for the run. The maximum allowed length is 4096 bytes in UTF-8 encoding. | [optional] [default to 'Untitled']
**run_page_url** | **str** | The URL to the detail page of the run. | [optional] 
**run_type** | [**RunType**](RunType.md) |  | [optional] 
**attempt_number** | **int** | The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0\\. If the initial run attempt fails, and the job has a retry policy (&#x60;max_retries&#x60; \\&gt; 0), subsequent runs are created with an &#x60;original_attempt_run_id&#x60; of the original attempt’s ID and an incrementing &#x60;attempt_number&#x60;. Runs are retried only until they succeed, and the maximum &#x60;attempt_number&#x60; is the same as the &#x60;max_retries&#x60; value for the job. | [optional] 
**repair_history** | [**List[RepairHistoryItem]**](RepairHistoryItem.md) | The repair history of the run. | [optional] 

## Example

```python
from databricks_jobs.models.jobs_runs_get200_response import JobsRunsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JobsRunsGet200Response from a JSON string
jobs_runs_get200_response_instance = JobsRunsGet200Response.from_json(json)
# print the JSON string representation of the object
print JobsRunsGet200Response.to_json()

# convert the object into a dict
jobs_runs_get200_response_dict = jobs_runs_get200_response_instance.to_dict()
# create an instance of JobsRunsGet200Response from a dict
jobs_runs_get200_response_form_dict = jobs_runs_get200_response.from_dict(jobs_runs_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


