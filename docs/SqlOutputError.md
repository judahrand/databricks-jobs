# SqlOutputError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The error message when execution fails. | [optional] 

## Example

```python
from databricks_jobs.models.sql_output_error import SqlOutputError

# TODO update the JSON string below
json = "{}"
# create an instance of SqlOutputError from a JSON string
sql_output_error_instance = SqlOutputError.from_json(json)
# print the JSON string representation of the object
print SqlOutputError.to_json()

# convert the object into a dict
sql_output_error_dict = sql_output_error_instance.to_dict()
# create an instance of SqlOutputError from a dict
sql_output_error_form_dict = sql_output_error.from_dict(sql_output_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


