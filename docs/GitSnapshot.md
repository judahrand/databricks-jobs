# GitSnapshot

Read-only state of the remote repository at the time the job was run. This field is only included on job runs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_commit** | **str** | Commit that was used to execute the run. If git_branch was specified, this points to the HEAD of the branch at the time of the run; if git_tag was specified, this points to the commit the tag points to. | 

## Example

```python
from databricks_jobs.models.git_snapshot import GitSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of GitSnapshot from a JSON string
git_snapshot_instance = GitSnapshot.from_json(json)
# print the JSON string representation of the object
print GitSnapshot.to_json()

# convert the object into a dict
git_snapshot_dict = git_snapshot_instance.to_dict()
# create an instance of GitSnapshot from a dict
git_snapshot_form_dict = git_snapshot.from_dict(git_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


