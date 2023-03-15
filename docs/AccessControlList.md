# AccessControlList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control_list** | [**List[AccessControlRequest]**](AccessControlRequest.md) | List of permissions to set on the job. | [optional] 

## Example

```python
from databricks_jobs.models.access_control_list import AccessControlList

# TODO update the JSON string below
json = "{}"
# create an instance of AccessControlList from a JSON string
access_control_list_instance = AccessControlList.from_json(json)
# print the JSON string representation of the object
print AccessControlList.to_json()

# convert the object into a dict
access_control_list_dict = access_control_list_instance.to_dict()
# create an instance of AccessControlList from a dict
access_control_list_form_dict = access_control_list.from_dict(access_control_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


