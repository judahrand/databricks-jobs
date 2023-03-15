# SqlAlertOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_text** | **str** | The text of the SQL query. Can Run permission of the SQL query associated with the SQL alert is required to view this field. | [optional] 
**warehouse_id** | **str** | The canonical identifier of the SQL warehouse. | [optional] 
**sql_statements** | [**SqlStatementOutput**](SqlStatementOutput.md) |  | [optional] 
**output_link** | **str** | The link to find the output results. | [optional] 

## Example

```python
from databricks_jobs.models.sql_alert_output import SqlAlertOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SqlAlertOutput from a JSON string
sql_alert_output_instance = SqlAlertOutput.from_json(json)
# print the JSON string representation of the object
print SqlAlertOutput.to_json()

# convert the object into a dict
sql_alert_output_dict = sql_alert_output_instance.to_dict()
# create an instance of SqlAlertOutput from a dict
sql_alert_output_form_dict = sql_alert_output.from_dict(sql_alert_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


