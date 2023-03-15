# EventDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_num_workers** | **int** | The number of nodes in the cluster. | [optional] 
**target_num_workers** | **int** | The targeted number of nodes in the cluster. | [optional] 
**previous_attributes** | [**AzureAttributes**](AzureAttributes.md) |  | [optional] 
**attributes** | [**AzureAttributes**](AzureAttributes.md) |  | [optional] 
**previous_cluster_size** | [**ClusterSize**](ClusterSize.md) |  | [optional] 
**cluster_size** | [**ClusterSize**](ClusterSize.md) |  | [optional] 
**cause** | [**ResizeCause**](ResizeCause.md) |  | [optional] 
**reason** | [**TerminationReason**](TerminationReason.md) |  | [optional] 
**user** | **str** | The user that caused the event to occur. (Empty if it was done by Azure Databricks.) | [optional] 

## Example

```python
from databricks_jobs.models.event_details import EventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EventDetails from a JSON string
event_details_instance = EventDetails.from_json(json)
# print the JSON string representation of the object
print EventDetails.to_json()

# convert the object into a dict
event_details_dict = event_details_instance.to_dict()
# create an instance of EventDetails from a dict
event_details_form_dict = event_details.from_dict(event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


