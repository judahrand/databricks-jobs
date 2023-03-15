# ClusterEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Canonical identifier for the cluster. This field is required. | 
**timestamp** | **int** | The timestamp when the event occurred, stored as the number of milliseconds since the unix epoch. Assigned by the Timeline service. | [optional] 
**type** | [**ClusterEventType**](ClusterEventType.md) |  | 
**details** | [**EventDetails**](EventDetails.md) |  | 

## Example

```python
from databricks_jobs.models.cluster_event import ClusterEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEvent from a JSON string
cluster_event_instance = ClusterEvent.from_json(json)
# print the JSON string representation of the object
print ClusterEvent.to_json()

# convert the object into a dict
cluster_event_dict = cluster_event_instance.to_dict()
# create an instance of ClusterEvent from a dict
cluster_event_form_dict = cluster_event.from_dict(cluster_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


