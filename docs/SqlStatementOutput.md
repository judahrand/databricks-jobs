# SqlStatementOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lookup_key** | **str** | A key that can be used to look up query details. | [optional] 

## Example

```python
from databricks_jobs.models.sql_statement_output import SqlStatementOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SqlStatementOutput from a JSON string
sql_statement_output_instance = SqlStatementOutput.from_json(json)
# print the JSON string representation of the object
print SqlStatementOutput.to_json()

# convert the object into a dict
sql_statement_output_dict = sql_statement_output_instance.to_dict()
# create an instance of SqlStatementOutput from a dict
sql_statement_output_form_dict = sql_statement_output.from_dict(sql_statement_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


