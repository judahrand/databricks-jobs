# RunSubmitTaskSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_key** | **str** | A unique name for the task. This field is used to refer to this task from other tasks. This field is required and must be unique within its parent job. On Update or Reset, this field is used to reference the tasks to be updated or reset. The maximum length is 100 characters. | 
**depends_on** | [**List[TaskDependenciesInner]**](TaskDependenciesInner.md) | An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task. The key is &#x60;task_key&#x60;, and the value is the name assigned to the dependent task. This field is required when a job consists of more than one task. | [optional] 
**existing_cluster_id** | **str** | If existing_cluster_id, the ID of an existing cluster that is used for all runs of this task. When running tasks on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs on new clusters for greater reliability. | [optional] 
**new_cluster** | [**NewCluster**](NewCluster.md) |  | [optional] 
**notebook_task** | [**NotebookTask**](NotebookTask.md) |  | [optional] 
**spark_jar_task** | [**SparkJarTask**](SparkJarTask.md) |  | [optional] 
**spark_python_task** | [**SparkPythonTask**](SparkPythonTask.md) |  | [optional] 
**spark_submit_task** | [**TaskSparkSubmitTask**](TaskSparkSubmitTask.md) |  | [optional] 
**pipeline_task** | [**PipelineTask**](PipelineTask.md) |  | [optional] 
**python_wheel_task** | [**PythonWheelTask**](PythonWheelTask.md) |  | [optional] 
**sql_task** | [**SqlTask**](SqlTask.md) |  | [optional] 
**dbt_task** | [**DbtTask**](DbtTask.md) |  | [optional] 
**libraries** | [**List[Library]**](Library.md) | An optional list of libraries to be installed on the cluster that executes the task. The default value is an empty list. | [optional] 
**timeout_seconds** | **int** | An optional timeout applied to each run of this job task. The default behavior is to have no timeout. | [optional] 

## Example

```python
from databricks_jobs.models.run_submit_task_settings import RunSubmitTaskSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RunSubmitTaskSettings from a JSON string
run_submit_task_settings_instance = RunSubmitTaskSettings.from_json(json)
# print the JSON string representation of the object
print RunSubmitTaskSettings.to_json()

# convert the object into a dict
run_submit_task_settings_dict = run_submit_task_settings_instance.to_dict()
# create an instance of RunSubmitTaskSettings from a dict
run_submit_task_settings_form_dict = run_submit_task_settings.from_dict(run_submit_task_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


