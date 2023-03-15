# PipelineTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_id** | **str** | The full name of the pipeline task to execute. | [optional] 
**full_refresh** | **bool** | If true, a full refresh will be triggered on the delta live table. | [optional] [default to False]

## Example

```python
from databricks_jobs.models.pipeline_task import PipelineTask

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineTask from a JSON string
pipeline_task_instance = PipelineTask.from_json(json)
# print the JSON string representation of the object
print PipelineTask.to_json()

# convert the object into a dict
pipeline_task_dict = pipeline_task_instance.to_dict()
# create an instance of PipelineTask from a dict
pipeline_task_form_dict = pipeline_task.from_dict(pipeline_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


