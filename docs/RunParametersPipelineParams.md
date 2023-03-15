# RunParametersPipelineParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_refresh** | **bool** | If true, triggers a full refresh on the delta live table. | [optional] 

## Example

```python
from databricks_jobs.models.run_parameters_pipeline_params import RunParametersPipelineParams

# TODO update the JSON string below
json = "{}"
# create an instance of RunParametersPipelineParams from a JSON string
run_parameters_pipeline_params_instance = RunParametersPipelineParams.from_json(json)
# print the JSON string representation of the object
print RunParametersPipelineParams.to_json()

# convert the object into a dict
run_parameters_pipeline_params_dict = run_parameters_pipeline_params_instance.to_dict()
# create an instance of RunParametersPipelineParams from a dict
run_parameters_pipeline_params_form_dict = run_parameters_pipeline_params.from_dict(run_parameters_pipeline_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


