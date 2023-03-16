# databricks_jobs.model.notebook_task.NotebookTask

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**notebook_path** | str,  | str,  | The path of the notebook to be run in the Azure Databricks workspace or remote repository. For notebooks stored in the Databricks workspace, the path must be absolute and begin with a slash. For notebooks stored in a remote repository, the path must be relative. This field is required. | 
**source** | str,  | str,  | Optional location type of the notebook. When set to &#x60;WORKSPACE&#x60;, the notebook will be retrieved from the local Azure Databricks workspace. When set to &#x60;GIT&#x60;, the notebook will be retrieved from a Git repository defined in &#x60;git_source&#x60;. If the value is empty, the task will use &#x60;GIT&#x60; if &#x60;git_source&#x60; is defined and &#x60;WORKSPACE&#x60; otherwise. | [optional] must be one of ["WORKSPACE", "GIT", ] 
**[base_parameters](#base_parameters)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Base parameters to be used for each run of this job. If the run is initiated by a call to [&#x60;run-now&#x60;](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsRunNow) with parameters specified, the two parameters maps are merged. If the same key is specified in &#x60;base_parameters&#x60; and in &#x60;run-now&#x60;, the value from &#x60;run-now&#x60; is used.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  If the notebook takes a parameter that is not specified in the job’s &#x60;base_parameters&#x60; or the &#x60;run-now&#x60; override parameters, the default value from the notebook is used.  Retrieve these parameters in a notebook using [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-widgets). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# base_parameters

Base parameters to be used for each run of this job. If the run is initiated by a call to [`run-now`](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsRunNow) with parameters specified, the two parameters maps are merged. If the same key is specified in `base_parameters` and in `run-now`, the value from `run-now` is used.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  If the notebook takes a parameter that is not specified in the job’s `base_parameters` or the `run-now` override parameters, the default value from the notebook is used.  Retrieve these parameters in a notebook using [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-widgets).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Base parameters to be used for each run of this job. If the run is initiated by a call to [&#x60;run-now&#x60;](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsRunNow) with parameters specified, the two parameters maps are merged. If the same key is specified in &#x60;base_parameters&#x60; and in &#x60;run-now&#x60;, the value from &#x60;run-now&#x60; is used.  Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set parameters containing information about job runs.  If the notebook takes a parameter that is not specified in the job’s &#x60;base_parameters&#x60; or the &#x60;run-now&#x60; override parameters, the default value from the notebook is used.  Retrieve these parameters in a notebook using [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-widgets). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

