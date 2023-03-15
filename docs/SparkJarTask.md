# SparkJarTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main_class_name** | **str** | The full name of the class containing the main method to be executed. This class must be contained in a JAR provided as a library.  The code must use &#x60;SparkContext.getOrCreate&#x60; to obtain a Spark context; otherwise, runs of the job fail. | [optional] 
**parameters** | **List[str]** | Parameters passed to the main method.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs. | [optional] 
**jar_uri** | **str** | Deprecated since 04/2016\\. Provide a &#x60;jar&#x60; through the &#x60;libraries&#x60; field instead. For an example, see [Create](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsCreate). | [optional] 

## Example

```python
from databricks_jobs.models.spark_jar_task import SparkJarTask

# TODO update the JSON string below
json = "{}"
# create an instance of SparkJarTask from a JSON string
spark_jar_task_instance = SparkJarTask.from_json(json)
# print the JSON string representation of the object
print SparkJarTask.to_json()

# convert the object into a dict
spark_jar_task_dict = spark_jar_task_instance.to_dict()
# create an instance of SparkJarTask from a dict
spark_jar_task_form_dict = spark_jar_task.from_dict(spark_jar_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


