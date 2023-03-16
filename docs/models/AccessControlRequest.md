# databricks_jobs.model.access_control_request.AccessControlRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[AccessControlRequestForUser](AccessControlRequestForUser.md) | [**AccessControlRequestForUser**](AccessControlRequestForUser.md) | [**AccessControlRequestForUser**](AccessControlRequestForUser.md) |  | 
[AccessControlRequestForGroup](AccessControlRequestForGroup.md) | [**AccessControlRequestForGroup**](AccessControlRequestForGroup.md) | [**AccessControlRequestForGroup**](AccessControlRequestForGroup.md) |  | 
[AccessControlRequestForServicePrincipal](AccessControlRequestForServicePrincipal.md) | [**AccessControlRequestForServicePrincipal**](AccessControlRequestForServicePrincipal.md) | [**AccessControlRequestForServicePrincipal**](AccessControlRequestForServicePrincipal.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

