# AccessControlRequestForServicePrincipal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_principal_name** | **str** | Name of an Azure service principal. | [optional] 
**permission_level** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.access_control_request_for_service_principal import AccessControlRequestForServicePrincipal

# TODO update the JSON string below
json = "{}"
# create an instance of AccessControlRequestForServicePrincipal from a JSON string
access_control_request_for_service_principal_instance = AccessControlRequestForServicePrincipal.from_json(json)
# print the JSON string representation of the object
print AccessControlRequestForServicePrincipal.to_json()

# convert the object into a dict
access_control_request_for_service_principal_dict = access_control_request_for_service_principal_instance.to_dict()
# create an instance of AccessControlRequestForServicePrincipal from a dict
access_control_request_for_service_principal_form_dict = access_control_request_for_service_principal.from_dict(access_control_request_for_service_principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


