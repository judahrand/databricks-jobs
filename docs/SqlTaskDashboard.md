# SqlTaskDashboard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_id** | **str** | The canonical identifier of the SQL dashboard. | 

## Example

```python
from databricks_jobs.models.sql_task_dashboard import SqlTaskDashboard

# TODO update the JSON string below
json = "{}"
# create an instance of SqlTaskDashboard from a JSON string
sql_task_dashboard_instance = SqlTaskDashboard.from_json(json)
# print the JSON string representation of the object
print SqlTaskDashboard.to_json()

# convert the object into a dict
sql_task_dashboard_dict = sql_task_dashboard_instance.to_dict()
# create an instance of SqlTaskDashboard from a dict
sql_task_dashboard_form_dict = sql_task_dashboard.from_dict(sql_task_dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


