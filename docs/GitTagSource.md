# GitTagSource

This functionality is in Public Preview.  An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_url** | **str** | URL of the repository to be cloned by this job. The maximum length is 300 characters. | 
**git_provider** | [**GitProvider**](GitProvider.md) |  | 
**git_tag** | **str** | Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_commit. The maximum length is 255 characters. | 
**git_snapshot** | [**GitSnapshot**](GitSnapshot.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.git_tag_source import GitTagSource

# TODO update the JSON string below
json = "{}"
# create an instance of GitTagSource from a JSON string
git_tag_source_instance = GitTagSource.from_json(json)
# print the JSON string representation of the object
print GitTagSource.to_json()

# convert the object into a dict
git_tag_source_dict = git_tag_source_instance.to_dict()
# create an instance of GitTagSource from a dict
git_tag_source_form_dict = git_tag_source.from_dict(git_tag_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


