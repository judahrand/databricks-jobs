# JobCluster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_cluster_key** | **str** | A unique name for the job cluster. This field is required and must be unique within the job. &#x60;JobTaskSettings&#x60; may refer to this field to determine which cluster to launch for the task execution. | 
**new_cluster** | [**NewCluster**](NewCluster.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.job_cluster import JobCluster

# TODO update the JSON string below
json = "{}"
# create an instance of JobCluster from a JSON string
job_cluster_instance = JobCluster.from_json(json)
# print the JSON string representation of the object
print JobCluster.to_json()

# convert the object into a dict
job_cluster_dict = job_cluster_instance.to_dict()
# create an instance of JobCluster from a dict
job_cluster_form_dict = job_cluster.from_dict(job_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


