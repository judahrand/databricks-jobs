# LibraryFullStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**library** | [**Library**](Library.md) |  | [optional] 
**status** | [**LibraryInstallStatus**](LibraryInstallStatus.md) |  | [optional] 
**messages** | **List[str]** | All the info and warning messages that have occurred so far for this library. | [optional] 
**is_library_for_all_clusters** | **bool** | Whether the library was set to be installed on all clusters via the libraries UI. | [optional] 

## Example

```python
from databricks_jobs.models.library_full_status import LibraryFullStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryFullStatus from a JSON string
library_full_status_instance = LibraryFullStatus.from_json(json)
# print the JSON string representation of the object
print LibraryFullStatus.to_json()

# convert the object into a dict
library_full_status_dict = library_full_status_instance.to_dict()
# create an instance of LibraryFullStatus from a dict
library_full_status_form_dict = library_full_status.from_dict(library_full_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


