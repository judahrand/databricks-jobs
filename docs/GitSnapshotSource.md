# GitSnapshotSource

This functionality is in Public Preview.  An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_url** | **str** | URL of the repository to be cloned by this job. The maximum length is 300 characters. | 
**git_provider** | [**GitProvider**](GitProvider.md) |  | 
**git_snapshot** | [**GitSnapshotSource**](GitSnapshotSource.md) |  | 

## Example

```python
from databricks_jobs.models.git_snapshot_source import GitSnapshotSource

# TODO update the JSON string below
json = "{}"
# create an instance of GitSnapshotSource from a JSON string
git_snapshot_source_instance = GitSnapshotSource.from_json(json)
# print the JSON string representation of the object
print GitSnapshotSource.to_json()

# convert the object into a dict
git_snapshot_source_dict = git_snapshot_source_instance.to_dict()
# create an instance of GitSnapshotSource from a dict
git_snapshot_source_form_dict = git_snapshot_source.from_dict(git_snapshot_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


