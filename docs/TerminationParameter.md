# TerminationParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The username of the user who terminated the cluster. | [optional] 
**aws_api_error_code** | **str** | The AWS provided error code describing why cluster nodes could not be provisioned. For example, &#x60;InstanceLimitExceeded&#x60; indicates that the limit of EC2 instances for a specific instance type has been exceeded. For reference, see: &lt;https://docs.aws.amazon.com/AWSEC2/latest/APIReference/query-api-troubleshooting.html&gt;. | [optional] 
**aws_instance_state_reason** | **str** | The AWS provided state reason describing why the driver node was terminated. For example, &#x60;Client.VolumeLimitExceeded&#x60; indicates that the limit of EBS volumes or total EBS volume storage has been exceeded. For reference, see &lt;https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StateReason.html&gt;. | [optional] 
**aws_spot_request_status** | **str** | Describes why a spot request could not be fulfilled. For example, &#x60;price-too-low&#x60; indicates that the max price was lower than the current spot price. For reference, see: &lt;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-bid-status.html#spot-instance-bid-status-understand&gt;. | [optional] 
**aws_spot_request_fault_code** | **str** | Provides additional details when a spot request fails. For example &#x60;InsufficientFreeAddressesInSubnet&#x60; indicates the subnet does not have free IP addresses to accommodate the new instance. For reference, see &lt;https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-spot-instance-requests.html&gt;. | [optional] 
**aws_impaired_status_details** | **str** | The AWS provided status check which failed and induced a node loss. This status may correspond to a failed instance or system check. For reference, see &lt;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html&gt;. | [optional] 
**aws_instance_status_event** | **str** | The AWS provided scheduled event (for example reboot) which induced a node loss. For reference, see &lt;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html&gt;. | [optional] 
**aws_error_message** | **str** | Human-readable context of various failures from AWS. This field is unstructured, and its exact format is subject to change. | [optional] 
**databricks_error_message** | **str** | Additional context that may explain the reason for cluster termination. This field is unstructured, and its exact format is subject to change. | [optional] 
**inactivity_duration_min** | **str** | An idle cluster was shut down after being inactive for this duration. | [optional] 
**instance_id** | **str** | The ID of the instance that was hosting the Spark driver. | [optional] 
**instance_pool_id** | **str** | The ID of the instance pool the cluster is using. | [optional] 
**instance_pool_error_code** | **str** | The [error code](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/clusters#clusterterminationreasonpoolclusterterminationcode) for cluster failures specific to a pool. | [optional] 
**azure_error_code** | **str** | The Azure provided error code describing why cluster nodes could not be provisioned. For reference, see: [https://docs.microsoft.com/azure/virtual-machines/windows/error-messages](https://docs.microsoft.com/azure/virtual-machines/windows/error-messages). | [optional] 
**azure_error_message** | **str** | Human-readable context of various failures from Azure. This field is unstructured, and its exact format is subject to change. | [optional] 

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


