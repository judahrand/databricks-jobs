# JobTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notebook_task** | [**NotebookTask**](NotebookTask.md) |  | [optional] 
**spark_jar_task** | [**SparkJarTask**](SparkJarTask.md) |  | [optional] 
**spark_python_task** | [**SparkPythonTask**](SparkPythonTask.md) |  | [optional] 
**spark_submit_task** | [**SparkSubmitTask**](SparkSubmitTask.md) |  | [optional] 
**pipeline_task** | [**PipelineTask**](PipelineTask.md) |  | [optional] 
**python_wheel_task** | [**PythonWheelTask**](PythonWheelTask.md) |  | [optional] 
**sql_task** | [**SqlTask**](SqlTask.md) |  | [optional] 
**dbt_task** | [**DbtTask**](DbtTask.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.job_task import JobTask

# TODO update the JSON string below
json = "{}"
# create an instance of JobTask from a JSON string
job_task_instance = JobTask.from_json(json)
# print the JSON string representation of the object
print JobTask.to_json()

# convert the object into a dict
job_task_dict = job_task_instance.to_dict()
# create an instance of JobTask from a dict
job_task_form_dict = job_task.from_dict(job_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


