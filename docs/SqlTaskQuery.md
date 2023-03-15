# SqlTaskQuery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** | The canonical identifier of the SQL query. | 

## Example

```python
from databricks_jobs.models.sql_task_query import SqlTaskQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SqlTaskQuery from a JSON string
sql_task_query_instance = SqlTaskQuery.from_json(json)
# print the JSON string representation of the object
print SqlTaskQuery.to_json()

# convert the object into a dict
sql_task_query_dict = sql_task_query_instance.to_dict()
# create an instance of SqlTaskQuery from a dict
sql_task_query_form_dict = sql_task_query.from_dict(sql_task_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


