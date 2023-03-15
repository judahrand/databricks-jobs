# SparkSubmitTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | **List[str]** | Command-line parameters passed to spark submit.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs. | [optional] 

## Example

```python
from databricks_jobs.models.spark_submit_task import SparkSubmitTask

# TODO update the JSON string below
json = "{}"
# create an instance of SparkSubmitTask from a JSON string
spark_submit_task_instance = SparkSubmitTask.from_json(json)
# print the JSON string representation of the object
print SparkSubmitTask.to_json()

# convert the object into a dict
spark_submit_task_dict = spark_submit_task_instance.to_dict()
# create an instance of SparkSubmitTask from a dict
spark_submit_task_form_dict = spark_submit_task.from_dict(spark_submit_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


