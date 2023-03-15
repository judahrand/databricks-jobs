# TaskSparkSubmitTask

If spark_submit_task, indicates that this task must be launched by the spark submit script. This task can run only on new clusters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | **List[str]** | Command-line parameters passed to spark submit.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs. | [optional] 

## Example

```python
from databricks_jobs.models.task_spark_submit_task import TaskSparkSubmitTask

# TODO update the JSON string below
json = "{}"
# create an instance of TaskSparkSubmitTask from a JSON string
task_spark_submit_task_instance = TaskSparkSubmitTask.from_json(json)
# print the JSON string representation of the object
print TaskSparkSubmitTask.to_json()

# convert the object into a dict
task_spark_submit_task_dict = task_spark_submit_task_instance.to_dict()
# create an instance of TaskSparkSubmitTask from a dict
task_spark_submit_task_form_dict = task_spark_submit_task.from_dict(task_spark_submit_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


