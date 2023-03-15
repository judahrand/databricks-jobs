# SqlQueryOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_text** | **str** | The text of the SQL query. Can Run permission of the SQL query is required to view this field. | [optional] 
**warehouse_id** | **str** | The canonical identifier of the SQL warehouse. | [optional] 
**sql_statements** | [**SqlStatementOutput**](SqlStatementOutput.md) |  | [optional] 
**output_link** | **str** | The link to find the output results. | [optional] 

## Example

```python
from databricks_jobs.models.sql_query_output import SqlQueryOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SqlQueryOutput from a JSON string
sql_query_output_instance = SqlQueryOutput.from_json(json)
# print the JSON string representation of the object
print SqlQueryOutput.to_json()

# convert the object into a dict
sql_query_output_dict = sql_query_output_instance.to_dict()
# create an instance of SqlQueryOutput from a dict
sql_query_output_form_dict = sql_query_output.from_dict(sql_query_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


