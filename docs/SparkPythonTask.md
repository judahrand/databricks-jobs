# SparkPythonTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**python_file** | **str** | The Python file to be executed. Cloud file URIs (such as dbfs:/, s3:/, adls:/, gcs:/) and workspace paths are supported. For python files stored in the Databricks workspace, the path must be absolute and begin with &#x60;/Repos&#x60;. This field is required. | 
**parameters** | **List[str]** | Command line parameters passed to the Python file.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs. | [optional] 

## Example

```python
from databricks_jobs.models.spark_python_task import SparkPythonTask

# TODO update the JSON string below
json = "{}"
# create an instance of SparkPythonTask from a JSON string
spark_python_task_instance = SparkPythonTask.from_json(json)
# print the JSON string representation of the object
print SparkPythonTask.to_json()

# convert the object into a dict
spark_python_task_dict = spark_python_task_instance.to_dict()
# create an instance of SparkPythonTask from a dict
spark_python_task_form_dict = spark_python_task.from_dict(spark_python_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


