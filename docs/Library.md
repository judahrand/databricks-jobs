# Library


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jar** | **str** | If jar, URI of the JAR to be installed. DBFS and ADLS (&#x60;abfss&#x60;) URIs are supported. For example: &#x60;{ \&quot;jar\&quot;: \&quot;dbfs:/mnt/databricks/library.jar\&quot; }&#x60; or &#x60;{ \&quot;jar\&quot;: \&quot;abfss://my-bucket/library.jar\&quot; }&#x60;. If ADLS is used, make sure the cluster has read access on the library. | [optional] 
**egg** | **str** | If egg, URI of the egg to be installed. DBFS and ADLS URIs are supported. For example: &#x60;{ \&quot;egg\&quot;: \&quot;dbfs:/my/egg\&quot; }&#x60; or &#x60;{ \&quot;egg\&quot;: \&quot;abfss://my-bucket/egg\&quot; }&#x60;. | [optional] 
**whl** | **str** | If whl, URI of the wheel or zipped wheels to be installed. DBFS and ADLS URIs are supported. For example: &#x60;{ \&quot;whl\&quot;: \&quot;dbfs:/my/whl\&quot; }&#x60; or &#x60;{ \&quot;whl\&quot;: \&quot;abfss://my-bucket/whl\&quot; }&#x60;. If ADLS is used, make sure the cluster has read access on the library. Also the wheel file name needs to use the [correct convention](https://www.python.org/dev/peps/pep-0427/#file-format). If zipped wheels are to be installed, the file name suffix should be &#x60;.wheelhouse.zip&#x60;. | [optional] 
**pypi** | [**PythonPyPiLibrary**](PythonPyPiLibrary.md) |  | [optional] 
**maven** | [**MavenLibrary**](MavenLibrary.md) |  | [optional] 
**cran** | [**RCranLibrary**](RCranLibrary.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.library import Library

# TODO update the JSON string below
json = "{}"
# create an instance of Library from a JSON string
library_instance = Library.from_json(json)
# print the JSON string representation of the object
print Library.to_json()

# convert the object into a dict
library_dict = library_instance.to_dict()
# create an instance of Library from a dict
library_form_dict = library.from_dict(library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


