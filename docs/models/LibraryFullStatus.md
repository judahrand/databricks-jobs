# databricks_jobs.model.library_full_status.LibraryFullStatus

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**library** | [**Library**](Library.md) | [**Library**](Library.md) |  | [optional] 
**status** | [**LibraryInstallStatus**](LibraryInstallStatus.md) | [**LibraryInstallStatus**](LibraryInstallStatus.md) |  | [optional] 
**[messages](#messages)** | list, tuple,  | tuple,  | All the info and warning messages that have occurred so far for this library. | [optional] 
**is_library_for_all_clusters** | bool,  | BoolClass,  | Whether the library was set to be installed on all clusters via the libraries UI. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# messages

All the info and warning messages that have occurred so far for this library.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | All the info and warning messages that have occurred so far for this library. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

