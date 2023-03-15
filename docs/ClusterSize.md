# ClusterSize


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_workers** | **int** | If num_workers, number of worker nodes that this cluster must have. A cluster has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field is updated to reflect the target size of 10 workers, whereas the workers listed in executors gradually increase from 5 to 10 as the new nodes are provisioned. | [optional] 
**autoscale** | [**AutoScale**](AutoScale.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.cluster_size import ClusterSize

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSize from a JSON string
cluster_size_instance = ClusterSize.from_json(json)
# print the JSON string representation of the object
print ClusterSize.to_json()

# convert the object into a dict
cluster_size_dict = cluster_size_instance.to_dict()
# create an instance of ClusterSize from a dict
cluster_size_form_dict = cluster_size.from_dict(cluster_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


