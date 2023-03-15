# SqlOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_output** | [**SqlQueryOutput**](SqlQueryOutput.md) |  | [optional] 
**dashboard_output** | [**SqlDashboardOutput**](SqlDashboardOutput.md) |  | [optional] 
**alert_output** | [**SqlAlertOutput**](SqlAlertOutput.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.sql_output import SqlOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SqlOutput from a JSON string
sql_output_instance = SqlOutput.from_json(json)
# print the JSON string representation of the object
print SqlOutput.to_json()

# convert the object into a dict
sql_output_dict = sql_output_instance.to_dict()
# create an instance of SqlOutput from a dict
sql_output_form_dict = sql_output.from_dict(sql_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


