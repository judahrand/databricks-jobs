# JobsRunNowRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The ID of the job to be executed | [optional] 
**idempotency_token** | **str** | An optional token to guarantee the idempotency of job run requests. If a run with the provided token already exists, the request does not create a new run but returns the ID of the existing run instead. If a run with the provided token is deleted, an error is returned.  If you specify the idempotency token, upon failure you can retry until the request succeeds. Databricks guarantees that exactly one run is launched with that idempotency token.  This token must have at most 64 characters.  For more information, see [How to ensure idempotency for jobs](https://docs.microsoft.com/azure/databricks/kb/jobs/jobs-idempotency). | [optional] 
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
from databricks_jobs.models.jobs_run_now_request import JobsRunNowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobsRunNowRequest from a JSON string
jobs_run_now_request_instance = JobsRunNowRequest.from_json(json)
# print the JSON string representation of the object
print JobsRunNowRequest.to_json()

# convert the object into a dict
jobs_run_now_request_dict = jobs_run_now_request_instance.to_dict()
# create an instance of JobsRunNowRequest from a dict
jobs_run_now_request_form_dict = jobs_run_now_request.from_dict(jobs_run_now_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


