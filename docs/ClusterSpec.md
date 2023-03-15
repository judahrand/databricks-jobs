# ClusterSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_cluster_id** | **str** | If existing_cluster_id, the ID of an existing cluster that is used for all runs of this job. When running jobs on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs on new clusters for greater reliability. | [optional] 
**new_cluster** | [**NewCluster**](NewCluster.md) |  | [optional] 
**libraries** | [**List[Library]**](Library.md) | An optional list of libraries to be installed on the cluster that executes the job. The default value is an empty list. | [optional] 

## Example

```python
from databricks_jobs.models.cluster_spec import ClusterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSpec from a JSON string
cluster_spec_instance = ClusterSpec.from_json(json)
# print the JSON string representation of the object
print ClusterSpec.to_json()

# convert the object into a dict
cluster_spec_dict = cluster_spec_instance.to_dict()
# create an instance of ClusterSpec from a dict
cluster_spec_form_dict = cluster_spec.from_dict(cluster_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


