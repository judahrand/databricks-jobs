# SqlDashboardWidgetOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widget_id** | **str** | The canonical identifier of the SQL widget. | [optional] 
**widget_title** | **str** | The title of the SQL widget. | [optional] 
**output_link** | **str** | The link to find the output results. | [optional] 
**status** | **str** | The execution status of the SQL widget. | [optional] 
**error** | [**SqlOutputError**](SqlOutputError.md) |  | [optional] 
**start_time** | **int** | Time (in epoch milliseconds) when execution of the SQL widget starts. | [optional] 
**end_time** | **int** | Time (in epoch milliseconds) when execution of the SQL widget ends. | [optional] 

## Example

```python
from databricks_jobs.models.sql_dashboard_widget_output import SqlDashboardWidgetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SqlDashboardWidgetOutput from a JSON string
sql_dashboard_widget_output_instance = SqlDashboardWidgetOutput.from_json(json)
# print the JSON string representation of the object
print SqlDashboardWidgetOutput.to_json()

# convert the object into a dict
sql_dashboard_widget_output_dict = sql_dashboard_widget_output_instance.to_dict()
# create an instance of SqlDashboardWidgetOutput from a dict
sql_dashboard_widget_output_form_dict = sql_dashboard_widget_output.from_dict(sql_dashboard_widget_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


