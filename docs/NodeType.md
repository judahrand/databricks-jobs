# NodeType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type_id** | **str** | Unique identifier for this node type. This field is required. | 
**memory_mb** | **int** | Memory (in MB) available for this node type. This field is required. | 
**num_cores** | **float** | Number of CPU cores available for this node type. This can be fractional if the number of cores on a machine instance is not divisible by the number of Spark nodes on that machine. This field is required. | [optional] 
**description** | **str** | A string description associated with this node type. This field is required. | 
**instance_type_id** | **str** | An identifier for the type of hardware that this node runs on. This field is required. | 
**is_deprecated** | **bool** | Whether the node type is deprecated. Non-deprecated node types offer greater performance. | [optional] 
**node_info** | [**ClusterCloudProviderNodeInfo**](ClusterCloudProviderNodeInfo.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.node_type import NodeType

# TODO update the JSON string below
json = "{}"
# create an instance of NodeType from a JSON string
node_type_instance = NodeType.from_json(json)
# print the JSON string representation of the object
print NodeType.to_json()

# convert the object into a dict
node_type_dict = node_type_instance.to_dict()
# create an instance of NodeType from a dict
node_type_form_dict = node_type.from_dict(node_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


