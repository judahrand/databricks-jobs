# databricks_jobs.model.init_script_info.InitScriptInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dbfs** | [**DbfsStorageInfo**](DbfsStorageInfo.md) | [**DbfsStorageInfo**](DbfsStorageInfo.md) |  | [optional] 
**file** | [**FileStorageInfo**](FileStorageInfo.md) | [**FileStorageInfo**](FileStorageInfo.md) |  | [optional] 
**abfss** | [**Adlsgen2Info**](Adlsgen2Info.md) | [**Adlsgen2Info**](Adlsgen2Info.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

