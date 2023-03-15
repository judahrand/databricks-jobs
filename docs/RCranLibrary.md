# RCranLibrary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | **str** | The name of the CRAN package to install. This field is required. | 
**repo** | **str** | The repository where the package can be found. If not specified, the default CRAN repo is used. | [optional] 

## Example

```python
from databricks_jobs.models.r_cran_library import RCranLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of RCranLibrary from a JSON string
r_cran_library_instance = RCranLibrary.from_json(json)
# print the JSON string representation of the object
print RCranLibrary.to_json()

# convert the object into a dict
r_cran_library_dict = r_cran_library_instance.to_dict()
# create an instance of RCranLibrary from a dict
r_cran_library_form_dict = r_cran_library.from_dict(r_cran_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


