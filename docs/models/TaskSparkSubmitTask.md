# databricks_jobs.model.task_spark_submit_task.TaskSparkSubmitTask

If spark_submit_task, indicates that this task must be launched by the spark submit script. This task can run only on new clusters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | If spark_submit_task, indicates that this task must be launched by the spark submit script. This task can run only on new clusters. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[SparkSubmitTask](SparkSubmitTask.md) | [**SparkSubmitTask**](SparkSubmitTask.md) | [**SparkSubmitTask**](SparkSubmitTask.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

