# databricks_jobs.model.git_source.GitSource

This functionality is in Public Preview.  An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This functionality is in Public Preview.  An optional specification for a remote repository containing the notebooks used by this job&#x27;s notebook tasks. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[GitBranchSource](GitBranchSource.md) | [**GitBranchSource**](GitBranchSource.md) | [**GitBranchSource**](GitBranchSource.md) |  | 
[GitTagSource](GitTagSource.md) | [**GitTagSource**](GitTagSource.md) | [**GitTagSource**](GitTagSource.md) |  | 
[GitCommitSource](GitCommitSource.md) | [**GitCommitSource**](GitCommitSource.md) | [**GitCommitSource**](GitCommitSource.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

