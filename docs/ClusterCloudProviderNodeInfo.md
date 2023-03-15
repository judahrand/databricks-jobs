# ClusterCloudProviderNodeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ClusterCloudProviderNodeStatus**](ClusterCloudProviderNodeStatus.md) |  | [optional] 
**available_core_quota** | **int** | Available CPU core quota. | [optional] 
**total_core_quota** | **int** | Total CPU core quota. | [optional] 

## Example

```python
from databricks_jobs.models.cluster_cloud_provider_node_info import ClusterCloudProviderNodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCloudProviderNodeInfo from a JSON string
cluster_cloud_provider_node_info_instance = ClusterCloudProviderNodeInfo.from_json(json)
# print the JSON string representation of the object
print ClusterCloudProviderNodeInfo.to_json()

# convert the object into a dict
cluster_cloud_provider_node_info_dict = cluster_cloud_provider_node_info_instance.to_dict()
# create an instance of ClusterCloudProviderNodeInfo from a dict
cluster_cloud_provider_node_info_form_dict = cluster_cloud_provider_node_info.from_dict(cluster_cloud_provider_node_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


