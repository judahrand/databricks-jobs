# databricks_jobs.model.jobs_runs_get_output200_response.JobsRunsGetOutput200Response

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**notebook_output** | [**NotebookOutput**](NotebookOutput.md) | [**NotebookOutput**](NotebookOutput.md) |  | [optional] 
**sql_output** | [**SqlOutput**](SqlOutput.md) | [**SqlOutput**](SqlOutput.md) |  | [optional] 
**dbt_output** | [**DbtOutput**](DbtOutput.md) | [**DbtOutput**](DbtOutput.md) |  | [optional] 
**logs** | str,  | str,  | The output from tasks that write to standard streams (stdout/stderr) such as [SparkJarTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/SparkJarTask), [SparkPythonTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/SparkPythonTask, [PythonWheelTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/PythonWheelTask. It&#x27;s not supported for the [NotebookTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/NotebookTask, [PipelineTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/PipelineTask, or [SparkSubmitTask](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#/components/schemas/SparkSubmitTask. Azure Databricks restricts this API to return the last 5 MB of these logs. | [optional] 
**logs_truncated** | bool,  | BoolClass,  | Whether the logs are truncated. | [optional] 
**error** | str,  | str,  | An error message indicating why a task failed or why output is not available. The message is unstructured, and its exact format is subject to change. | [optional] 
**error_trace** | str,  | str,  | If there was an error executing the run, this field contains any available stack traces. | [optional] 
**metadata** | [**Run**](Run.md) | [**Run**](Run.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

