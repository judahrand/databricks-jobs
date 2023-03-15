# AutoScale


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_workers** | **int** | The minimum number of workers to which the cluster can scale down when underutilized. It is also the initial number of workers the cluster has after creation. | [optional] 
**max_workers** | **int** | The maximum number of workers to which the cluster can scale up when overloaded. max_workers must be strictly greater than min_workers. | [optional] 

## Example

```python
from databricks_jobs.models.auto_scale import AutoScale

# TODO update the JSON string below
json = "{}"
# create an instance of AutoScale from a JSON string
auto_scale_instance = AutoScale.from_json(json)
# print the JSON string representation of the object
print AutoScale.to_json()

# convert the object into a dict
auto_scale_dict = auto_scale_instance.to_dict()
# create an instance of AutoScale from a dict
auto_scale_form_dict = auto_scale.from_dict(auto_scale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


