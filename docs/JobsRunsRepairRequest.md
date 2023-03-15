# JobsRunsRepairRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** | The job run ID of the run to repair. The run must not be in progress. | [optional] 
**rerun_tasks** | **List[str]** | The task keys of the task runs to repair. | [optional] 
**latest_repair_id** | **int** | The ID of the latest repair. This parameter is not required when repairing a run for the first time, but must be provided on subsequent requests to repair the same run. | [optional] 
**rerun_all_failed_tasks** | **bool** | If true, repair all failed tasks. Only one of rerun_tasks or rerun_all_failed_tasks can be used. | [optional] [default to False]
**jar_params** | **List[str]** | A list of parameters for jobs with Spark JAR tasks, for example &#x60;\&quot;jar_params\&quot;: [\&quot;john doe\&quot;, \&quot;35\&quot;]&#x60;. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon &#x60;run-now&#x60;, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example &#x60;{\&quot;jar_params\&quot;:[\&quot;john doe\&quot;,\&quot;35\&quot;]}&#x60;) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs. | [optional] 
**notebook_params** | **Dict[str, object]** | A map from keys to values for jobs with notebook task, for example &#x60;\&quot;notebook_params\&quot;: {\&quot;name\&quot;: \&quot;john doe\&quot;, \&quot;age\&quot;: \&quot;35\&quot;}&#x60;. The map is passed to the notebook and is accessible through the [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-widgets) function.  If not specified upon &#x60;run-now&#x60;, the triggered run uses the job’s base parameters.  notebook_params cannot be specified in conjunction with jar_params.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  The JSON representation of this field (for example &#x60;{\&quot;notebook_params\&quot;:{\&quot;name\&quot;:\&quot;john doe\&quot;,\&quot;age\&quot;:\&quot;35\&quot;}}&#x60;) cannot exceed 10,000 bytes. | [optional] 
**python_params** | **List[str]** | A list of parameters for jobs with Python tasks, for example &#x60;\&quot;python_params\&quot;: [\&quot;john doe\&quot;, \&quot;35\&quot;]&#x60;. The parameters are passed to Python file as command-line parameters. If specified upon &#x60;run-now&#x60;, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example &#x60;{\&quot;python_params\&quot;:[\&quot;john doe\&quot;,\&quot;35\&quot;]}&#x60;) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  Important  These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. | [optional] 
**spark_submit_params** | **List[str]** | A list of parameters for jobs with spark submit task, for example &#x60;\&quot;spark_submit_params\&quot;: [\&quot;--class\&quot;, \&quot;org.apache.spark.examples.SparkPi\&quot;]&#x60;. The parameters are passed to spark-submit script as command-line parameters. If specified upon &#x60;run-now&#x60;, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example &#x60;{\&quot;python_params\&quot;:[\&quot;john doe\&quot;,\&quot;35\&quot;]}&#x60;) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  Important  These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. | [optional] 
**python_named_params** | **object** | A map from keys to values for jobs with Python wheel task, for example &#x60;\&quot;python_named_params\&quot;: {\&quot;name\&quot;: \&quot;task\&quot;, \&quot;data\&quot;: \&quot;dbfs:/path/to/data.json\&quot;}&#x60;. | [optional] 
**pipeline_params** | [**RunParametersPipelineParams**](RunParametersPipelineParams.md) |  | [optional] 
**sql_params** | **object** | A map from keys to values for SQL tasks, for example &#x60;\&quot;sql_params\&quot;: {\&quot;name\&quot;: \&quot;john doe\&quot;, \&quot;age\&quot;: \&quot;35\&quot;}&#x60;. The SQL alert task does not support custom parameters. | [optional] 
**dbt_commands** | **List[str]** | An array of commands to execute for jobs with the dbt task, for example &#x60;\&quot;dbt_commands\&quot;: [\&quot;dbt deps\&quot;, \&quot;dbt seed\&quot;, \&quot;dbt run\&quot;]&#x60; | [optional] 

## Example

```python
from databricks_jobs.models.jobs_runs_repair_request import JobsRunsRepairRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobsRunsRepairRequest from a JSON string
jobs_runs_repair_request_instance = JobsRunsRepairRequest.from_json(json)
# print the JSON string representation of the object
print JobsRunsRepairRequest.to_json()

# convert the object into a dict
jobs_runs_repair_request_dict = jobs_runs_repair_request_instance.to_dict()
# create an instance of JobsRunsRepairRequest from a dict
jobs_runs_repair_request_form_dict = jobs_runs_repair_request.from_dict(jobs_runs_repair_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


