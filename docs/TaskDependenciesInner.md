# TaskDependenciesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_key** | **str** |  | [optional] 

## Example

```python
from databricks_jobs.models.task_dependencies_inner import TaskDependenciesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDependenciesInner from a JSON string
task_dependencies_inner_instance = TaskDependenciesInner.from_json(json)
# print the JSON string representation of the object
print TaskDependenciesInner.to_json()

# convert the object into a dict
task_dependencies_inner_dict = task_dependencies_inner_instance.to_dict()
# create an instance of TaskDependenciesInner from a dict
task_dependencies_inner_form_dict = task_dependencies_inner.from_dict(task_dependencies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


