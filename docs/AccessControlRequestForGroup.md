# AccessControlRequestForGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** | Group name. There are two built-in groups: &#x60;users&#x60; for all users, and &#x60;admins&#x60; for administrators. | [optional] 
**permission_level** | [**PermissionLevelForGroup**](PermissionLevelForGroup.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.access_control_request_for_group import AccessControlRequestForGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AccessControlRequestForGroup from a JSON string
access_control_request_for_group_instance = AccessControlRequestForGroup.from_json(json)
# print the JSON string representation of the object
print AccessControlRequestForGroup.to_json()

# convert the object into a dict
access_control_request_for_group_dict = access_control_request_for_group_instance.to_dict()
# create an instance of AccessControlRequestForGroup from a dict
access_control_request_for_group_form_dict = access_control_request_for_group.from_dict(access_control_request_for_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


