# databricks_jobs.model.library.Library

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**jar** | str,  | str,  | If jar, URI of the JAR to be installed. DBFS and ADLS (&#x60;abfss&#x60;) URIs are supported. For example: &#x60;{ \&quot;jar\&quot;: \&quot;dbfs:/mnt/databricks/library.jar\&quot; }&#x60; or &#x60;{ \&quot;jar\&quot;: \&quot;abfss://my-bucket/library.jar\&quot; }&#x60;. If ADLS is used, make sure the cluster has read access on the library. | [optional] 
**egg** | str,  | str,  | If egg, URI of the egg to be installed. DBFS and ADLS URIs are supported. For example: &#x60;{ \&quot;egg\&quot;: \&quot;dbfs:/my/egg\&quot; }&#x60; or &#x60;{ \&quot;egg\&quot;: \&quot;abfss://my-bucket/egg\&quot; }&#x60;. | [optional] 
**whl** | str,  | str,  | If whl, URI of the wheel or zipped wheels to be installed. DBFS and ADLS URIs are supported. For example: &#x60;{ \&quot;whl\&quot;: \&quot;dbfs:/my/whl\&quot; }&#x60; or &#x60;{ \&quot;whl\&quot;: \&quot;abfss://my-bucket/whl\&quot; }&#x60;. If ADLS is used, make sure the cluster has read access on the library. Also the wheel file name needs to use the [correct convention](https://www.python.org/dev/peps/pep-0427/#file-format). If zipped wheels are to be installed, the file name suffix should be &#x60;.wheelhouse.zip&#x60;. | [optional] 
**pypi** | [**PythonPyPiLibrary**](PythonPyPiLibrary.md) | [**PythonPyPiLibrary**](PythonPyPiLibrary.md) |  | [optional] 
**maven** | [**MavenLibrary**](MavenLibrary.md) | [**MavenLibrary**](MavenLibrary.md) |  | [optional] 
**cran** | [**RCranLibrary**](RCranLibrary.md) | [**RCranLibrary**](RCranLibrary.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

