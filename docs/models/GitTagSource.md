# databricks_jobs.model.git_tag_source.GitTagSource

This functionality is in Public Preview.  An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This functionality is in Public Preview.  An optional specification for a remote repository containing the notebooks used by this job&#x27;s notebook tasks. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**git_tag** | str,  | str,  | Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_commit. The maximum length is 255 characters. | 
**git_provider** | [**GitProvider**](GitProvider.md) | [**GitProvider**](GitProvider.md) |  | 
**git_url** | str,  | str,  | URL of the repository to be cloned by this job. The maximum length is 300 characters. | 
**git_snapshot** | [**GitSnapshot**](GitSnapshot.md) | [**GitSnapshot**](GitSnapshot.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

