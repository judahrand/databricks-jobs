# GitCommitSource

This functionality is in Public Preview.  An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_url** | **str** | URL of the repository to be cloned by this job. The maximum length is 300 characters. | 
**git_provider** | [**GitProvider**](GitProvider.md) |  | 
**git_commit** | **str** | Commit to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_tag. The maximum length is 64 characters. | 

## Example

```python
from databricks_jobs.models.git_commit_source import GitCommitSource

# TODO update the JSON string below
json = "{}"
# create an instance of GitCommitSource from a JSON string
git_commit_source_instance = GitCommitSource.from_json(json)
# print the JSON string representation of the object
print GitCommitSource.to_json()

# convert the object into a dict
git_commit_source_dict = git_commit_source_instance.to_dict()
# create an instance of GitCommitSource from a dict
git_commit_source_form_dict = git_commit_source.from_dict(git_commit_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


