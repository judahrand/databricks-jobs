# JobTaskSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_key** | **str** | A unique name for the task. This field is used to refer to this task from other tasks. This field is required and must be unique within its parent job. On Update or Reset, this field is used to reference the tasks to be updated or reset. The maximum length is 100 characters. | 
**description** | **str** | An optional description for this task. The maximum length is 4096 bytes. | [optional] 
**depends_on** | [**List[TaskDependenciesInner]**](TaskDependenciesInner.md) | An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task. The key is &#x60;task_key&#x60;, and the value is the name assigned to the dependent task. This field is required when a job consists of more than one task. | [optional] 
**existing_cluster_id** | **str** | If existing_cluster_id, the ID of an existing cluster that is used for all runs of this task. When running tasks on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs on new clusters for greater reliability. | [optional] 
**new_cluster** | [**NewTaskCluster**](NewTaskCluster.md) |  | [optional] 
**job_cluster_key** | **str** | If job_cluster_key, this task is executed reusing the cluster specified in &#x60;job.settings.job_clusters&#x60;. | [optional] 
**notebook_task** | [**NotebookTask**](NotebookTask.md) |  | [optional] 
**spark_jar_task** | [**SparkJarTask**](SparkJarTask.md) |  | [optional] 
**spark_python_task** | [**SparkPythonTask**](SparkPythonTask.md) |  | [optional] 
**spark_submit_task** | [**TaskSparkSubmitTask**](TaskSparkSubmitTask.md) |  | [optional] 
**pipeline_task** | [**PipelineTask**](PipelineTask.md) |  | [optional] 
**python_wheel_task** | [**PythonWheelTask**](PythonWheelTask.md) |  | [optional] 
**sql_task** | [**SqlTask**](SqlTask.md) |  | [optional] 
**dbt_task** | [**DbtTask**](DbtTask.md) |  | [optional] 
**libraries** | [**List[Library]**](Library.md) | An optional list of libraries to be installed on the cluster that executes the task. The default value is an empty list. | [optional] 
**email_notifications** | [**JobEmailNotifications**](JobEmailNotifications.md) |  | [optional] 
**timeout_seconds** | **int** | An optional timeout applied to each run of this job task. The default behavior is to have no timeout. | [optional] 
**max_retries** | **int** | An optional maximum number of times to retry an unsuccessful run. A run is considered to be unsuccessful if it completes with the &#x60;FAILED&#x60; result_state or &#x60;INTERNAL_ERROR&#x60; &#x60;life_cycle_state&#x60;. The value -1 means to retry indefinitely and the value 0 means to never retry. The default behavior is to never retry. | [optional] 
**min_retry_interval_millis** | **int** | An optional minimal interval in milliseconds between the start of the failed run and the subsequent retry run. The default behavior is that unsuccessful runs are immediately retried. | [optional] 
**retry_on_timeout** | **bool** | An optional policy to specify whether to retry a task when it times out. The default behavior is to not retry on timeout. | [optional] 

## Example

```python
from databricks_jobs.models.job_task_settings import JobTaskSettings

# TODO update the JSON string below
json = "{}"
# create an instance of JobTaskSettings from a JSON string
job_task_settings_instance = JobTaskSettings.from_json(json)
# print the JSON string representation of the object
print JobTaskSettings.to_json()

# convert the object into a dict
job_task_settings_dict = job_task_settings_instance.to_dict()
# create an instance of JobTaskSettings from a dict
job_task_settings_form_dict = job_task_settings.from_dict(job_task_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


