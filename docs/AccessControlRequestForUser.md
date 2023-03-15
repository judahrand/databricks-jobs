# AccessControlRequestForUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Email address for the user. | [optional] 
**permission_level** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.access_control_request_for_user import AccessControlRequestForUser

# TODO update the JSON string below
json = "{}"
# create an instance of AccessControlRequestForUser from a JSON string
access_control_request_for_user_instance = AccessControlRequestForUser.from_json(json)
# print the JSON string representation of the object
print AccessControlRequestForUser.to_json()

# convert the object into a dict
access_control_request_for_user_dict = access_control_request_for_user_instance.to_dict()
# create an instance of AccessControlRequestForUser from a dict
access_control_request_for_user_form_dict = access_control_request_for_user.from_dict(access_control_request_for_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


