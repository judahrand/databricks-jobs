# databricks_jobs.model.spark_version.SparkVersion

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**key** | str,  | str,  | [Databricks Runtime version](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/index#programmatic-version) key, for example &#x60;7.3.x-scala2.12&#x60;. The value that must be provided as the &#x60;spark_version&#x60; when creating a new cluster. The exact runtime version may change over time for a “wildcard” version (that is, &#x60;7.3.x-scala2.12&#x60; is a “wildcard” version) with minor bug fixes. | [optional] 
**name** | str,  | str,  | A descriptive name for the runtime version, for example “Databricks Runtime 7.3 LTS”. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

