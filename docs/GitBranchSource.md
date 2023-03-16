# GitBranchSource

This functionality is in Public Preview.  An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_url** | **str** | URL of the repository to be cloned by this job. The maximum length is 300 characters. | 
**git_provider** | [**GitProvider**](GitProvider.md) |  | 
**git_branch** | **str** | Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git_tag or git_commit. The maximum length is 255 characters. | 
**git_snapshot** | [**GitSnapshot**](GitSnapshot.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.git_branch_source import GitBranchSource

# TODO update the JSON string below
json = "{}"
# create an instance of GitBranchSource from a JSON string
git_branch_source_instance = GitBranchSource.from_json(json)
# print the JSON string representation of the object
print GitBranchSource.to_json()

# convert the object into a dict
git_branch_source_dict = git_branch_source_instance.to_dict()
# create an instance of GitBranchSource from a dict
git_branch_source_form_dict = git_branch_source.from_dict(git_branch_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


