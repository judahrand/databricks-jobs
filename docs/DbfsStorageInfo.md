# DbfsStorageInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | DBFS destination. Example: &#x60;dbfs:/my/path&#x60; | [optional] 

## Example

```python
from databricks_jobs.models.dbfs_storage_info import DbfsStorageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DbfsStorageInfo from a JSON string
dbfs_storage_info_instance = DbfsStorageInfo.from_json(json)
# print the JSON string representation of the object
print DbfsStorageInfo.to_json()

# convert the object into a dict
dbfs_storage_info_dict = dbfs_storage_info_instance.to_dict()
# create an instance of DbfsStorageInfo from a dict
dbfs_storage_info_form_dict = dbfs_storage_info.from_dict(dbfs_storage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


