# TerminationReason


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**TerminationCode**](TerminationCode.md) |  | [optional] 
**type** | [**TerminationType**](TerminationType.md) |  | [optional] 
**parameters** | **Dict[str, object]** | An object with additional information about why a cluster was terminated. The object keys are one of &#x60;TerminationParameter&#x60; and the value is the termination information. | [optional] 

## Example

```python
from databricks_jobs.models.termination_reason import TerminationReason

# TODO update the JSON string below
json = "{}"
# create an instance of TerminationReason from a JSON string
termination_reason_instance = TerminationReason.from_json(json)
# print the JSON string representation of the object
print TerminationReason.to_json()

# convert the object into a dict
termination_reason_dict = termination_reason_instance.to_dict()
# create an instance of TerminationReason from a dict
termination_reason_form_dict = termination_reason.from_dict(termination_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


