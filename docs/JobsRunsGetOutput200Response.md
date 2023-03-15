# JobsRunsGetOutput200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notebook_output** | [**NotebookOutput**](NotebookOutput.md) |  | [optional] 
**sql_output** | [**SqlOutput**](SqlOutput.md) |  | [optional] 
**dbt_output** | [**DbtOutput**](DbtOutput.md) |  | [optional] 
**logs** | **str** | The output from tasks that write to standard streams (stdout/stderr) such as [SparkJarTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/SparkJarTask), [SparkPythonTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/SparkPythonTask, [PythonWheelTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/PythonWheelTask. It&#39;s not supported for the [NotebookTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/NotebookTask, [PipelineTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/PipelineTask, or [SparkSubmitTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/SparkSubmitTask. Azure Databricks restricts this API to return the last 5 MB of these logs. | [optional] 
**logs_truncated** | **bool** | Whether the logs are truncated. | [optional] 
**error** | **str** | An error message indicating why a task failed or why output is not available. The message is unstructured, and its exact format is subject to change. | [optional] 
**error_trace** | **str** | If there was an error executing the run, this field contains any available stack traces. | [optional] 
**metadata** | [**Run**](Run.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.jobs_runs_get_output200_response import JobsRunsGetOutput200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JobsRunsGetOutput200Response from a JSON string
jobs_runs_get_output200_response_instance = JobsRunsGetOutput200Response.from_json(json)
# print the JSON string representation of the object
print JobsRunsGetOutput200Response.to_json()

# convert the object into a dict
jobs_runs_get_output200_response_dict = jobs_runs_get_output200_response_instance.to_dict()
# create an instance of JobsRunsGetOutput200Response from a dict
jobs_runs_get_output200_response_form_dict = jobs_runs_get_output200_response.from_dict(jobs_runs_get_output200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


