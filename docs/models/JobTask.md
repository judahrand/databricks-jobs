# databricks_jobs.model.job_task.JobTask

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**notebook_task** | [**NotebookTask**](NotebookTask.md) | [**NotebookTask**](NotebookTask.md) |  | [optional] 
**spark_jar_task** | [**SparkJarTask**](SparkJarTask.md) | [**SparkJarTask**](SparkJarTask.md) |  | [optional] 
**spark_python_task** | [**SparkPythonTask**](SparkPythonTask.md) | [**SparkPythonTask**](SparkPythonTask.md) |  | [optional] 
**spark_submit_task** | [**SparkSubmitTask**](SparkSubmitTask.md) | [**SparkSubmitTask**](SparkSubmitTask.md) |  | [optional] 
**pipeline_task** | [**PipelineTask**](PipelineTask.md) | [**PipelineTask**](PipelineTask.md) |  | [optional] 
**python_wheel_task** | [**PythonWheelTask**](PythonWheelTask.md) | [**PythonWheelTask**](PythonWheelTask.md) |  | [optional] 
**sql_task** | [**SqlTask**](SqlTask.md) | [**SqlTask**](SqlTask.md) |  | [optional] 
**dbt_task** | [**DbtTask**](DbtTask.md) | [**DbtTask**](DbtTask.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

