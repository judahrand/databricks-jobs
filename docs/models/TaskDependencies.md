# databricks_jobs.model.task_dependencies.TaskDependencies

An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task. The key is `task_key`, and the value is the name assigned to the dependent task. This field is required when a job consists of more than one task.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task. The key is &#x60;task_key&#x60;, and the value is the name assigned to the dependent task. This field is required when a job consists of more than one task. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TaskDependenciesInner**](TaskDependenciesInner.md) | [**TaskDependenciesInner**](TaskDependenciesInner.md) | [**TaskDependenciesInner**](TaskDependenciesInner.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

