# databricks_jobs.model.job_task_settings.JobTaskSettings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**task_key** | [**TaskKey**](TaskKey.md) | [**TaskKey**](TaskKey.md) |  | 
**description** | [**TaskDescription**](TaskDescription.md) | [**TaskDescription**](TaskDescription.md) |  | [optional] 
**depends_on** | [**TaskDependencies**](TaskDependencies.md) | [**TaskDependencies**](TaskDependencies.md) |  | [optional] 
**existing_cluster_id** | str,  | str,  | If existing_cluster_id, the ID of an existing cluster that is used for all runs of this task. When running tasks on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs on new clusters for greater reliability. | [optional] 
**new_cluster** | [**NewTaskCluster**](NewTaskCluster.md) | [**NewTaskCluster**](NewTaskCluster.md) |  | [optional] 
**job_cluster_key** | str,  | str,  | If job_cluster_key, this task is executed reusing the cluster specified in &#x60;job.settings.job_clusters&#x60;. | [optional] 
**notebook_task** | [**NotebookTask**](NotebookTask.md) | [**NotebookTask**](NotebookTask.md) |  | [optional] 
**spark_jar_task** | [**SparkJarTask**](SparkJarTask.md) | [**SparkJarTask**](SparkJarTask.md) |  | [optional] 
**spark_python_task** | [**SparkPythonTask**](SparkPythonTask.md) | [**SparkPythonTask**](SparkPythonTask.md) |  | [optional] 
**spark_submit_task** | [**TaskSparkSubmitTask**](TaskSparkSubmitTask.md) | [**TaskSparkSubmitTask**](TaskSparkSubmitTask.md) |  | [optional] 
**pipeline_task** | [**PipelineTask**](PipelineTask.md) | [**PipelineTask**](PipelineTask.md) |  | [optional] 
**python_wheel_task** | [**PythonWheelTask**](PythonWheelTask.md) | [**PythonWheelTask**](PythonWheelTask.md) |  | [optional] 
**sql_task** | [**SqlTask**](SqlTask.md) | [**SqlTask**](SqlTask.md) |  | [optional] 
**dbt_task** | [**DbtTask**](DbtTask.md) | [**DbtTask**](DbtTask.md) |  | [optional] 
**[libraries](#libraries)** | list, tuple,  | tuple,  | An optional list of libraries to be installed on the cluster that executes the task. The default value is an empty list. | [optional] 
**email_notifications** | [**JobEmailNotifications**](JobEmailNotifications.md) | [**JobEmailNotifications**](JobEmailNotifications.md) |  | [optional] 
**timeout_seconds** | decimal.Decimal, int,  | decimal.Decimal,  | An optional timeout applied to each run of this job task. The default behavior is to have no timeout. | [optional] value must be a 32 bit integer
**max_retries** | decimal.Decimal, int,  | decimal.Decimal,  | An optional maximum number of times to retry an unsuccessful run. A run is considered to be unsuccessful if it completes with the &#x60;FAILED&#x60; result_state or &#x60;INTERNAL_ERROR&#x60; &#x60;life_cycle_state&#x60;. The value -1 means to retry indefinitely and the value 0 means to never retry. The default behavior is to never retry. | [optional] value must be a 32 bit integer
**min_retry_interval_millis** | decimal.Decimal, int,  | decimal.Decimal,  | An optional minimal interval in milliseconds between the start of the failed run and the subsequent retry run. The default behavior is that unsuccessful runs are immediately retried. | [optional] value must be a 32 bit integer
**retry_on_timeout** | bool,  | BoolClass,  | An optional policy to specify whether to retry a task when it times out. The default behavior is to not retry on timeout. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# libraries

An optional list of libraries to be installed on the cluster that executes the task. The default value is an empty list.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional list of libraries to be installed on the cluster that executes the task. The default value is an empty list. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Library**](Library.md) | [**Library**](Library.md) | [**Library**](Library.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

