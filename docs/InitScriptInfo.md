# InitScriptInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dbfs** | [**DbfsStorageInfo**](DbfsStorageInfo.md) |  | [optional] 
**file** | [**FileStorageInfo**](FileStorageInfo.md) |  | [optional] 
**s3** | [**S3StorageInfo**](S3StorageInfo.md) |  | [optional] 
**abfss** | [**Adlsgen2Info**](Adlsgen2Info.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.init_script_info import InitScriptInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InitScriptInfo from a JSON string
init_script_info_instance = InitScriptInfo.from_json(json)
# print the JSON string representation of the object
print InitScriptInfo.to_json()

# convert the object into a dict
init_script_info_dict = init_script_info_instance.to_dict()
# create an instance of InitScriptInfo from a dict
init_script_info_form_dict = init_script_info.from_dict(init_script_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


