# ClusterLibraryStatuses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Unique identifier for the cluster. | [optional] 
**library_statuses** | [**List[LibraryFullStatus]**](LibraryFullStatus.md) | Status of all libraries on the cluster. | [optional] 

## Example

```python
from databricks_jobs.models.cluster_library_statuses import ClusterLibraryStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLibraryStatuses from a JSON string
cluster_library_statuses_instance = ClusterLibraryStatuses.from_json(json)
# print the JSON string representation of the object
print ClusterLibraryStatuses.to_json()

# convert the object into a dict
cluster_library_statuses_dict = cluster_library_statuses_instance.to_dict()
# create an instance of ClusterLibraryStatuses from a dict
cluster_library_statuses_form_dict = cluster_library_statuses.from_dict(cluster_library_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


