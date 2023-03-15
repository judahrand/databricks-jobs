# NotebookOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | The value passed to [dbutils.notebook.exit()](https://docs.microsoft.com/azure/databricks/notebooks/notebook-workflows#notebook-workflows-exit). Azure Databricks restricts this API to return the first 5 MB of the value. For a larger result, your job can store the results in a cloud storage service. This field is absent if &#x60;dbutils.notebook.exit()&#x60; was never called. | [optional] 
**truncated** | **bool** | Whether or not the result was truncated. | [optional] 

## Example

```python
from databricks_jobs.models.notebook_output import NotebookOutput

# TODO update the JSON string below
json = "{}"
# create an instance of NotebookOutput from a JSON string
notebook_output_instance = NotebookOutput.from_json(json)
# print the JSON string representation of the object
print NotebookOutput.to_json()

# convert the object into a dict
notebook_output_dict = notebook_output_instance.to_dict()
# create an instance of NotebookOutput from a dict
notebook_output_form_dict = notebook_output.from_dict(notebook_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


