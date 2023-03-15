# SqlTaskAlert


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** | The canonical identifier of the SQL alert. | 

## Example

```python
from databricks_jobs.models.sql_task_alert import SqlTaskAlert

# TODO update the JSON string below
json = "{}"
# create an instance of SqlTaskAlert from a JSON string
sql_task_alert_instance = SqlTaskAlert.from_json(json)
# print the JSON string representation of the object
print SqlTaskAlert.to_json()

# convert the object into a dict
sql_task_alert_dict = sql_task_alert_instance.to_dict()
# create an instance of SqlTaskAlert from a dict
sql_task_alert_form_dict = sql_task_alert.from_dict(sql_task_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


