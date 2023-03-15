# ClusterInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The canonical identifier for the cluster used by a run. This field is always available for runs on existing clusters. For runs on new clusters, it becomes available once the cluster is created. This value can be used to view logs by browsing to &#x60;/#setting/sparkui/$cluster_id/driver-logs&#x60;. The logs continue to be available after the run completes.  The response won’t include this field if the identifier is not available yet. | [optional] 
**spark_context_id** | **str** | The canonical identifier for the Spark context used by a run. This field is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to &#x60;/#setting/sparkui/$cluster_id/$spark_context_id&#x60;. The Spark UI continues to be available after the run has completed.  The response won’t include this field if the identifier is not available yet. | [optional] 

## Example

```python
from databricks_jobs.models.cluster_instance import ClusterInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInstance from a JSON string
cluster_instance_instance = ClusterInstance.from_json(json)
# print the JSON string representation of the object
print ClusterInstance.to_json()

# convert the object into a dict
cluster_instance_dict = cluster_instance_instance.to_dict()
# create an instance of ClusterInstance from a dict
cluster_instance_form_dict = cluster_instance.from_dict(cluster_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


