# MavenLibrary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **str** | Gradle-style Maven coordinates. For example: &#x60;org.jsoup:jsoup:1.7.2&#x60;. This field is required. | 
**repo** | **str** | Maven repo to install the Maven package from. If omitted, both Maven Central Repository and Spark Packages are searched. | [optional] 
**exclusions** | **List[str]** | List of dependences to exclude. For example: &#x60;[\&quot;slf4j:slf4j\&quot;, \&quot;*:hadoop-client\&quot;]&#x60;.  Maven dependency exclusions: &lt;https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html&gt;. | [optional] 

## Example

```python
from databricks_jobs.models.maven_library import MavenLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of MavenLibrary from a JSON string
maven_library_instance = MavenLibrary.from_json(json)
# print the JSON string representation of the object
print MavenLibrary.to_json()

# convert the object into a dict
maven_library_dict = maven_library_instance.to_dict()
# create an instance of MavenLibrary from a dict
maven_library_form_dict = maven_library.from_dict(maven_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


