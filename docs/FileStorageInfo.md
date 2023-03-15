# FileStorageInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | File destination. Example: &#x60;file:/my/file.sh&#x60; | [optional] 

## Example

```python
from databricks_jobs.models.file_storage_info import FileStorageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FileStorageInfo from a JSON string
file_storage_info_instance = FileStorageInfo.from_json(json)
# print the JSON string representation of the object
print FileStorageInfo.to_json()

# convert the object into a dict
file_storage_info_dict = file_storage_info_instance.to_dict()
# create an instance of FileStorageInfo from a dict
file_storage_info_form_dict = file_storage_info.from_dict(file_storage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


