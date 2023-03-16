# databricks_jobs.model.run_task.RunTask

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**run_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the task run. | [optional] value must be a 64 bit integer
**task_key** | [**TaskKey**](TaskKey.md) | [**TaskKey**](TaskKey.md) |  | [optional] 
**description** | [**TaskDescription**](TaskDescription.md) | [**TaskDescription**](TaskDescription.md) |  | [optional] 
**state** | [**RunState**](RunState.md) | [**RunState**](RunState.md) |  | [optional] 
**depends_on** | [**TaskDependencies**](TaskDependencies.md) | [**TaskDependencies**](TaskDependencies.md) |  | [optional] 
**existing_cluster_id** | str,  | str,  | If existing_cluster_id, the ID of an existing cluster that is used for all runs of this job. When running jobs on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs on new clusters for greater reliability. | [optional] 
**new_cluster** | [**NewTaskCluster**](NewTaskCluster.md) | [**NewTaskCluster**](NewTaskCluster.md) |  | [optional] 
**[libraries](#libraries)** | list, tuple,  | tuple,  | An optional list of libraries to be installed on the cluster that executes the job. The default value is an empty list. | [optional] 
**notebook_task** | [**NotebookTask**](NotebookTask.md) | [**NotebookTask**](NotebookTask.md) |  | [optional] 
**spark_jar_task** | [**SparkJarTask**](SparkJarTask.md) | [**SparkJarTask**](SparkJarTask.md) |  | [optional] 
**spark_python_task** | [**SparkPythonTask**](SparkPythonTask.md) | [**SparkPythonTask**](SparkPythonTask.md) |  | [optional] 
**spark_submit_task** | [**TaskSparkSubmitTask**](TaskSparkSubmitTask.md) | [**TaskSparkSubmitTask**](TaskSparkSubmitTask.md) |  | [optional] 
**pipeline_task** | [**PipelineTask**](PipelineTask.md) | [**PipelineTask**](PipelineTask.md) |  | [optional] 
**python_wheel_task** | [**PythonWheelTask**](PythonWheelTask.md) | [**PythonWheelTask**](PythonWheelTask.md) |  | [optional] 
**sql_task** | [**SqlTask**](SqlTask.md) | [**SqlTask**](SqlTask.md) |  | [optional] 
**dbt_task** | [**DbtTask**](DbtTask.md) | [**DbtTask**](DbtTask.md) |  | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued. | [optional] value must be a 64 bit integer
**setup_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the &#x60;setup_duration&#x60;, &#x60;execution_duration&#x60;, and the &#x60;cleanup_duration&#x60;. The &#x60;setup_duration&#x60; field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the &#x60;run_duration&#x60; field. | [optional] value must be a 64 bit integer
**execution_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. | [optional] value must be a 64 bit integer
**cleanup_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The total duration of the run is the sum of the setup_duration, the execution_duration, and the cleanup_duration. | [optional] value must be a 64 bit integer
**end_time** | decimal.Decimal, int,  | decimal.Decimal,  | The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running. | [optional] value must be a 64 bit integer
**attempt_number** | decimal.Decimal, int,  | decimal.Decimal,  | The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0\\. If the initial run attempt fails, and the job has a retry policy (&#x60;max_retries&#x60; \\&gt; 0), subsequent runs are created with an &#x60;original_attempt_run_id&#x60; of the original attempt’s ID and an incrementing &#x60;attempt_number&#x60;. Runs are retried only until they succeed, and the maximum &#x60;attempt_number&#x60; is the same as the &#x60;max_retries&#x60; value for the job. | [optional] value must be a 32 bit integer
**cluster_instance** | [**ClusterInstance**](ClusterInstance.md) | [**ClusterInstance**](ClusterInstance.md) |  | [optional] 
**git_source** | [**GitSource**](GitSource.md) | [**GitSource**](GitSource.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# libraries

An optional list of libraries to be installed on the cluster that executes the job. The default value is an empty list.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional list of libraries to be installed on the cluster that executes the job. The default value is an empty list. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Library**](Library.md) | [**Library**](Library.md) | [**Library**](Library.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

