# TerminationParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The username of the user who terminated the cluster. | [optional] 
**azure_error_code** | **str** | The Azure provided error code describing why cluster nodes could not be provisioned. For reference, see: [https://docs.microsoft.com/azure/virtual-machines/windows/error-messages](https://docs.microsoft.com/azure/virtual-machines/windows/error-messages). | [optional] 
**azure_error_message** | **str** | Human-readable context of various failures from Azure. This field is unstructured, and its exact format is subject to change. | [optional] 
**databricks_error_message** | **str** | Additional context that may explain the reason for cluster termination. This field is unstructured, and its exact format is subject to change. | [optional] 
**inactivity_duration_min** | **str** | An idle cluster was shut down after being inactive for this duration. | [optional] 
**instance_id** | **str** | The ID of the instance that was hosting the Spark driver. | [optional] 
**instance_pool_id** | **str** | The ID of the instance pool the cluster is using. | [optional] 
**instance_pool_error_code** | **str** | The [error code](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#clusterterminationreasonpoolclusterterminationcode) for cluster failures specific to a pool. | [optional] 

## Example

```python
from databricks_jobs.models.termination_parameter import TerminationParameter

# TODO update the JSON string below
json = "{}"
# create an instance of TerminationParameter from a JSON string
termination_parameter_instance = TerminationParameter.from_json(json)
# print the JSON string representation of the object
print TerminationParameter.to_json()

# convert the object into a dict
termination_parameter_dict = termination_parameter_instance.to_dict()
# create an instance of TerminationParameter from a dict
termination_parameter_form_dict = termination_parameter.from_dict(termination_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


