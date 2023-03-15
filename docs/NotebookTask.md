# NotebookTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notebook_path** | **str** | The path of the notebook to be run in the Azure Databricks workspace or remote repository. For notebooks stored in the Databricks workspace, the path must be absolute and begin with a slash. For notebooks stored in a remote repository, the path must be relative. This field is required. | 
**source** | **str** | Optional location type of the notebook. When set to &#x60;WORKSPACE&#x60;, the notebook will be retrieved from the local Azure Databricks workspace. When set to &#x60;GIT&#x60;, the notebook will be retrieved from a Git repository defined in &#x60;git_source&#x60;. If the value is empty, the task will use &#x60;GIT&#x60; if &#x60;git_source&#x60; is defined and &#x60;WORKSPACE&#x60; otherwise. | [optional] 
**base_parameters** | **Dict[str, object]** | Base parameters to be used for each run of this job. If the run is initiated by a call to [&#x60;run-now&#x60;](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsRunNow) with parameters specified, the two parameters maps are merged. If the same key is specified in &#x60;base_parameters&#x60; and in &#x60;run-now&#x60;, the value from &#x60;run-now&#x60; is used.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  If the notebook takes a parameter that is not specified in the job’s &#x60;base_parameters&#x60; or the &#x60;run-now&#x60; override parameters, the default value from the notebook is used.  Retrieve these parameters in a notebook using [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-widgets). | [optional] 

## Example

```python
from databricks_jobs.models.notebook_task import NotebookTask

# TODO update the JSON string below
json = "{}"
# create an instance of NotebookTask from a JSON string
notebook_task_instance = NotebookTask.from_json(json)
# print the JSON string representation of the object
print NotebookTask.to_json()

# convert the object into a dict
notebook_task_dict = notebook_task_instance.to_dict()
# create an instance of NotebookTask from a dict
notebook_task_form_dict = notebook_task.from_dict(notebook_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


