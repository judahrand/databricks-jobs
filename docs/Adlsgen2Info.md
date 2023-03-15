# Adlsgen2Info


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | abfss destination. Example: &#x60;abfss://&lt;container-name&gt;@&lt;storage-account-name&gt;.dfs.core.windows.net/&lt;directory-name&gt;&#x60; | [optional] 

## Example

```python
from databricks_jobs.models.adlsgen2_info import Adlsgen2Info

# TODO update the JSON string below
json = "{}"
# create an instance of Adlsgen2Info from a JSON string
adlsgen2_info_instance = Adlsgen2Info.from_json(json)
# print the JSON string representation of the object
print Adlsgen2Info.to_json()

# convert the object into a dict
adlsgen2_info_dict = adlsgen2_info_instance.to_dict()
# create an instance of Adlsgen2Info from a dict
adlsgen2_info_form_dict = adlsgen2_info.from_dict(adlsgen2_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


