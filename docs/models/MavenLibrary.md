# databricks_jobs.model.maven_library.MavenLibrary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**coordinates** | str,  | str,  | Gradle-style Maven coordinates. For example: &#x60;org.jsoup:jsoup:1.7.2&#x60;. This field is required. | 
**repo** | str,  | str,  | Maven repo to install the Maven package from. If omitted, both Maven Central Repository and Spark Packages are searched. | [optional] 
**[exclusions](#exclusions)** | list, tuple,  | tuple,  | List of dependences to exclude. For example: &#x60;[\&quot;slf4j:slf4j\&quot;, \&quot;*:hadoop-client\&quot;]&#x60;.  Maven dependency exclusions: &lt;https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html&gt;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# exclusions

List of dependences to exclude. For example: `[\"slf4j:slf4j\", \"*:hadoop-client\"]`.  Maven dependency exclusions: <https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of dependences to exclude. For example: &#x60;[\&quot;slf4j:slf4j\&quot;, \&quot;*:hadoop-client\&quot;]&#x60;.  Maven dependency exclusions: &lt;https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html&gt;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

