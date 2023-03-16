# databricks_jobs.model.notebook_output.NotebookOutput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**result** | str,  | str,  | The value passed to [dbutils.notebook.exit()](https://docs.microsoft.com/azure/databricks/notebooks/notebook-workflows#notebook-workflows-exit). Azure Databricks restricts this API to return the first 5 MB of the value. For a larger result, your job can store the results in a cloud storage service. This field is absent if &#x60;dbutils.notebook.exit()&#x60; was never called. | [optional] 
**truncated** | bool,  | BoolClass,  | Whether or not the result was truncated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

