# GitSource

This functionality is in Public Preview.  An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_url** | **str** | URL of the repository to be cloned by this job. The maximum length is 300 characters. | 
**git_provider** | [**GitProvider**](GitProvider.md) |  | 
**git_branch** | **str** | Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git_tag or git_commit. The maximum length is 255 characters. | 
**git_tag** | **str** | Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_commit. The maximum length is 255 characters. | 
**git_commit** | **str** | Commit to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_tag. The maximum length is 64 characters. | 
**git_snapshot** | [**GitSnapshotSource**](GitSnapshotSource.md) |  | 

## Example

```python
from databricks_jobs.models.git_source import GitSource

# TODO update the JSON string below
json = "{}"
# create an instance of GitSource from a JSON string
git_source_instance = GitSource.from_json(json)
# print the JSON string representation of the object
print GitSource.to_json()

# convert the object into a dict
git_source_dict = git_source_instance.to_dict()
# create an instance of GitSource from a dict
git_source_form_dict = git_source.from_dict(git_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


