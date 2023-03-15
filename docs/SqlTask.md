# SqlTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**SqlTaskQuery**](SqlTaskQuery.md) |  | [optional] 
**dashboard** | [**SqlTaskDashboard**](SqlTaskDashboard.md) |  | [optional] 
**alert** | [**SqlTaskAlert**](SqlTaskAlert.md) |  | [optional] 
**parameters** | **object** | Parameters to be used for each run of this job. The SQL alert task does not support custom parameters. | [optional] 
**warehouse_id** | **str** | The canonical identifier of the SQL warehouse. Only serverless and pro SQL warehouses are supported. | 

## Example

```python
from databricks_jobs.models.sql_task import SqlTask

# TODO update the JSON string below
json = "{}"
# create an instance of SqlTask from a JSON string
sql_task_instance = SqlTask.from_json(json)
# print the JSON string representation of the object
print SqlTask.to_json()

# convert the object into a dict
sql_task_dict = sql_task_instance.to_dict()
# create an instance of SqlTask from a dict
sql_task_form_dict = sql_task.from_dict(sql_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


