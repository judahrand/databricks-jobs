# SparkNodeAwsAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_spot** | **bool** | Whether this node is on an Amazon spot instance. | [optional] 

## Example

```python
from databricks_jobs.models.spark_node_aws_attributes import SparkNodeAwsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SparkNodeAwsAttributes from a JSON string
spark_node_aws_attributes_instance = SparkNodeAwsAttributes.from_json(json)
# print the JSON string representation of the object
print SparkNodeAwsAttributes.to_json()

# convert the object into a dict
spark_node_aws_attributes_dict = spark_node_aws_attributes_instance.to_dict()
# create an instance of SparkNodeAwsAttributes from a dict
spark_node_aws_attributes_form_dict = spark_node_aws_attributes.from_dict(spark_node_aws_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


