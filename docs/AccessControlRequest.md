# AccessControlRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Email address for the user. | [optional] 
**permission_level** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**group_name** | **str** | Group name. There are two built-in groups: &#x60;users&#x60; for all users, and &#x60;admins&#x60; for administrators. | [optional] 
**service_principal_name** | **str** | Name of an Azure service principal. | [optional] 

## Example

```python
from databricks_jobs.models.access_control_request import AccessControlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessControlRequest from a JSON string
access_control_request_instance = AccessControlRequest.from_json(json)
# print the JSON string representation of the object
print AccessControlRequest.to_json()

# convert the object into a dict
access_control_request_dict = access_control_request_instance.to_dict()
# create an instance of AccessControlRequest from a dict
access_control_request_form_dict = access_control_request.from_dict(access_control_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


