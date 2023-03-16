# databricks_jobs.model.access_control_request_for_group.AccessControlRequestForGroup

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**group_name** | str,  | str,  | Group name. There are two built-in groups: &#x60;users&#x60; for all users, and &#x60;admins&#x60; for administrators. | [optional] 
**permission_level** | [**PermissionLevelForGroup**](PermissionLevelForGroup.md) | [**PermissionLevelForGroup**](PermissionLevelForGroup.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

