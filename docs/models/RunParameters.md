# databricks_jobs.model.run_parameters.RunParameters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[jar_params](#jar_params)** | list, tuple,  | tuple,  | A list of parameters for jobs with Spark JAR tasks, for example &#x60;\&quot;jar_params\&quot;: [\&quot;john doe\&quot;, \&quot;35\&quot;]&#x60;. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon &#x60;run-now&#x60;, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example &#x60;{\&quot;jar_params\&quot;:[\&quot;john doe\&quot;,\&quot;35\&quot;]}&#x60;) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs. | [optional] 
**[notebook_params](#notebook_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A map from keys to values for jobs with notebook task, for example &#x60;\&quot;notebook_params\&quot;: {\&quot;name\&quot;: \&quot;john doe\&quot;, \&quot;age\&quot;: \&quot;35\&quot;}&#x60;. The map is passed to the notebook and is accessible through the [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-widgets) function.  If not specified upon &#x60;run-now&#x60;, the triggered run uses the job’s base parameters.  notebook_params cannot be specified in conjunction with jar_params.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  The JSON representation of this field (for example &#x60;{\&quot;notebook_params\&quot;:{\&quot;name\&quot;:\&quot;john doe\&quot;,\&quot;age\&quot;:\&quot;35\&quot;}}&#x60;) cannot exceed 10,000 bytes. | [optional] 
**[python_params](#python_params)** | list, tuple,  | tuple,  | A list of parameters for jobs with Python tasks, for example &#x60;\&quot;python_params\&quot;: [\&quot;john doe\&quot;, \&quot;35\&quot;]&#x60;. The parameters are passed to Python file as command-line parameters. If specified upon &#x60;run-now&#x60;, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example &#x60;{\&quot;python_params\&quot;:[\&quot;john doe\&quot;,\&quot;35\&quot;]}&#x60;) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  Important  These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. | [optional] 
**[spark_submit_params](#spark_submit_params)** | list, tuple,  | tuple,  | A list of parameters for jobs with spark submit task, for example &#x60;\&quot;spark_submit_params\&quot;: [\&quot;--class\&quot;, \&quot;org.apache.spark.examples.SparkPi\&quot;]&#x60;. The parameters are passed to spark-submit script as command-line parameters. If specified upon &#x60;run-now&#x60;, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example &#x60;{\&quot;python_params\&quot;:[\&quot;john doe\&quot;,\&quot;35\&quot;]}&#x60;) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  Important  These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. | [optional] 
**[python_named_params](#python_named_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A map from keys to values for jobs with Python wheel task, for example &#x60;\&quot;python_named_params\&quot;: {\&quot;name\&quot;: \&quot;task\&quot;, \&quot;data\&quot;: \&quot;dbfs:/path/to/data.json\&quot;}&#x60;. | [optional] 
**pipeline_params** | [**RunParametersPipelineParams**](RunParametersPipelineParams.md) | [**RunParametersPipelineParams**](RunParametersPipelineParams.md) |  | [optional] 
**[sql_params](#sql_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A map from keys to values for SQL tasks, for example &#x60;\&quot;sql_params\&quot;: {\&quot;name\&quot;: \&quot;john doe\&quot;, \&quot;age\&quot;: \&quot;35\&quot;}&#x60;. The SQL alert task does not support custom parameters. | [optional] 
**[dbt_commands](#dbt_commands)** | list, tuple,  | tuple,  | An array of commands to execute for jobs with the dbt task, for example &#x60;\&quot;dbt_commands\&quot;: [\&quot;dbt deps\&quot;, \&quot;dbt seed\&quot;, \&quot;dbt run\&quot;]&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# jar_params

A list of parameters for jobs with Spark JAR tasks, for example `\"jar_params\": [\"john doe\", \"35\"]`. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon `run-now`, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example `{\"jar_params\":[\"john doe\",\"35\"]}`) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of parameters for jobs with Spark JAR tasks, for example &#x60;\&quot;jar_params\&quot;: [\&quot;john doe\&quot;, \&quot;35\&quot;]&#x60;. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon &#x60;run-now&#x60;, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example &#x60;{\&quot;jar_params\&quot;:[\&quot;john doe\&quot;,\&quot;35\&quot;]}&#x60;) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# notebook_params

A map from keys to values for jobs with notebook task, for example `\"notebook_params\": {\"name\": \"john doe\", \"age\": \"35\"}`. The map is passed to the notebook and is accessible through the [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-widgets) function.  If not specified upon `run-now`, the triggered run uses the job’s base parameters.  notebook_params cannot be specified in conjunction with jar_params.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  The JSON representation of this field (for example `{\"notebook_params\":{\"name\":\"john doe\",\"age\":\"35\"}}`) cannot exceed 10,000 bytes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A map from keys to values for jobs with notebook task, for example &#x60;\&quot;notebook_params\&quot;: {\&quot;name\&quot;: \&quot;john doe\&quot;, \&quot;age\&quot;: \&quot;35\&quot;}&#x60;. The map is passed to the notebook and is accessible through the [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-widgets) function.  If not specified upon &#x60;run-now&#x60;, the triggered run uses the job’s base parameters.  notebook_params cannot be specified in conjunction with jar_params.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  The JSON representation of this field (for example &#x60;{\&quot;notebook_params\&quot;:{\&quot;name\&quot;:\&quot;john doe\&quot;,\&quot;age\&quot;:\&quot;35\&quot;}}&#x60;) cannot exceed 10,000 bytes. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# python_params

A list of parameters for jobs with Python tasks, for example `\"python_params\": [\"john doe\", \"35\"]`. The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `{\"python_params\":[\"john doe\",\"35\"]}`) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  Important  These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of parameters for jobs with Python tasks, for example &#x60;\&quot;python_params\&quot;: [\&quot;john doe\&quot;, \&quot;35\&quot;]&#x60;. The parameters are passed to Python file as command-line parameters. If specified upon &#x60;run-now&#x60;, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example &#x60;{\&quot;python_params\&quot;:[\&quot;john doe\&quot;,\&quot;35\&quot;]}&#x60;) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  Important  These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# spark_submit_params

A list of parameters for jobs with spark submit task, for example `\"spark_submit_params\": [\"--class\", \"org.apache.spark.examples.SparkPi\"]`. The parameters are passed to spark-submit script as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `{\"python_params\":[\"john doe\",\"35\"]}`) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  Important  These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of parameters for jobs with spark submit task, for example &#x60;\&quot;spark_submit_params\&quot;: [\&quot;--class\&quot;, \&quot;org.apache.spark.examples.SparkPi\&quot;]&#x60;. The parameters are passed to spark-submit script as command-line parameters. If specified upon &#x60;run-now&#x60;, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example &#x60;{\&quot;python_params\&quot;:[\&quot;john doe\&quot;,\&quot;35\&quot;]}&#x60;) cannot exceed 10,000 bytes.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  Important  These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# python_named_params

A map from keys to values for jobs with Python wheel task, for example `\"python_named_params\": {\"name\": \"task\", \"data\": \"dbfs:/path/to/data.json\"}`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A map from keys to values for jobs with Python wheel task, for example &#x60;\&quot;python_named_params\&quot;: {\&quot;name\&quot;: \&quot;task\&quot;, \&quot;data\&quot;: \&quot;dbfs:/path/to/data.json\&quot;}&#x60;. | 

# sql_params

A map from keys to values for SQL tasks, for example `\"sql_params\": {\"name\": \"john doe\", \"age\": \"35\"}`. The SQL alert task does not support custom parameters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A map from keys to values for SQL tasks, for example &#x60;\&quot;sql_params\&quot;: {\&quot;name\&quot;: \&quot;john doe\&quot;, \&quot;age\&quot;: \&quot;35\&quot;}&#x60;. The SQL alert task does not support custom parameters. | 

# dbt_commands

An array of commands to execute for jobs with the dbt task, for example `\"dbt_commands\": [\"dbt deps\", \"dbt seed\", \"dbt run\"]`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of commands to execute for jobs with the dbt task, for example &#x60;\&quot;dbt_commands\&quot;: [\&quot;dbt deps\&quot;, \&quot;dbt seed\&quot;, \&quot;dbt run\&quot;]&#x60; | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

