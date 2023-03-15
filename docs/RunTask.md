# RunTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** | The ID of the task run. | [optional] 
**task_key** | **str** | A unique name for the task. This field is used to refer to this task from other tasks. This field is required and must be unique within its parent job. On Update or Reset, this field is used to reference the tasks to be updated or reset. The maximum length is 100 characters. | [optional] 
**description** | **str** | An optional description for this task. The maximum length is 4096 bytes. | [optional] 
**state** | [**RunState**](RunState.md) |  | [optional] 
**depends_on** | [**List[TaskDependenciesInner]**](TaskDependenciesInner.md) | An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task. The key is &#x60;task_key&#x60;, and the value is the name assigned to the dependent task. This field is required when a job consists of more than one task. | [optional] 
**existing_cluster_id** | **str** | If existing_cluster_id, the ID of an existing cluster that is used for all runs of this job. When running jobs on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs on new clusters for greater reliability. | [optional] 
**new_cluster** | [**NewTaskCluster**](NewTaskCluster.md) |  | [optional] 
**libraries** | [**List[Library]**](Library.md) | An optional list of libraries to be installed on the cluster that executes the job. The default value is an empty list. | [optional] 
**notebook_task** | [**NotebookTask**](NotebookTask.md) |  | [optional] 
**spark_jar_task** | [**SparkJarTask**](SparkJarTask.md) |  | [optional] 
**spark_python_task** | [**SparkPythonTask**](SparkPythonTask.md) |  | [optional] 
**spark_submit_task** | [**TaskSparkSubmitTask**](TaskSparkSubmitTask.md) |  | [optional] 
**pipeline_task** | [**PipelineTask**](PipelineTask.md) |  | [optional] 
**python_wheel_task** | [**PythonWheelTask**](PythonWheelTask.md) |  | [optional] 
**sql_task** | [**SqlTask**](SqlTask.md) |  | [optional] 
**dbt_task** | [**DbtTask**](DbtTask.md) |  | [optional] 
**start_time** | **int** | The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued. | [optional] 
**setup_duration** | **int** | The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the &#x60;setup_duration&#x60;, &#x60;execution_duration&#x60;, and the &#x60;cleanup_duration&#x60;. The &#x60;setup_duration&#x60; field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the &#x60;run_duration&#x60; field. | [optional] 
**execution_duration** | **int** | The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. | [optional] 
**cleanup_duration** | **int** | The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The total duration of the run is the sum of the setup_duration, the execution_duration, and the cleanup_duration. | [optional] 
**end_time** | **int** | The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running. | [optional] 
**attempt_number** | **int** | The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0\\. If the initial run attempt fails, and the job has a retry policy (&#x60;max_retries&#x60; \\&gt; 0), subsequent runs are created with an &#x60;original_attempt_run_id&#x60; of the original attempt’s ID and an incrementing &#x60;attempt_number&#x60;. Runs are retried only until they succeed, and the maximum &#x60;attempt_number&#x60; is the same as the &#x60;max_retries&#x60; value for the job. | [optional] 
**cluster_instance** | [**ClusterInstance**](ClusterInstance.md) |  | [optional] 
**git_source** | [**GitSource**](GitSource.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.run_task import RunTask

# TODO update the JSON string below
json = "{}"
# create an instance of RunTask from a JSON string
run_task_instance = RunTask.from_json(json)
# print the JSON string representation of the object
print RunTask.to_json()

# convert the object into a dict
run_task_dict = run_task_instance.to_dict()
# create an instance of RunTask from a dict
run_task_form_dict = run_task.from_dict(run_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


