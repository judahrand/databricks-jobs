# SqlDashboardOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widgets** | [**SqlDashboardWidgetOutput**](SqlDashboardWidgetOutput.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.sql_dashboard_output import SqlDashboardOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SqlDashboardOutput from a JSON string
sql_dashboard_output_instance = SqlDashboardOutput.from_json(json)
# print the JSON string representation of the object
print SqlDashboardOutput.to_json()

# convert the object into a dict
sql_dashboard_output_dict = sql_dashboard_output_instance.to_dict()
# create an instance of SqlDashboardOutput from a dict
sql_dashboard_output_form_dict = sql_dashboard_output.from_dict(sql_dashboard_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


