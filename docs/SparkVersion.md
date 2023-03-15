# SparkVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | [Databricks Runtime version](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/index#programmatic-version) key, for example &#x60;7.3.x-scala2.12&#x60;. The value that must be provided as the &#x60;spark_version&#x60; when creating a new cluster. The exact runtime version may change over time for a “wildcard” version (that is, &#x60;7.3.x-scala2.12&#x60; is a “wildcard” version) with minor bug fixes. | [optional] 
**name** | **str** | A descriptive name for the runtime version, for example “Databricks Runtime 7.3 LTS”. | [optional] 

## Example

```python
from databricks_jobs.models.spark_version import SparkVersion

# TODO update the JSON string below
json = "{}"
# create an instance of SparkVersion from a JSON string
spark_version_instance = SparkVersion.from_json(json)
# print the JSON string representation of the object
print SparkVersion.to_json()

# convert the object into a dict
spark_version_dict = spark_version_instance.to_dict()
# create an instance of SparkVersion from a dict
spark_version_form_dict = spark_version.from_dict(spark_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


