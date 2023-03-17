# SparkNode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_ip** | **str** | Private IP address (typically a 10.x.x.x address) of the Spark node. This is different from the private IP address of the host instance. | [optional] 
**public_dns** | **str** | Public DNS address of this node. This address can be used to access the Spark JDBC server on the driver node. | [optional] 
**node_id** | **str** | Globally unique identifier for this node. | [optional] 
**instance_id** | **str** | Globally unique identifier for the host instance from the cloud provider. | [optional] 
**start_timestamp** | **int** | The timestamp (in millisecond) when the Spark node is launched. | [optional] 
**node_aws_attributes** | [**SparkNodeAwsAttributes**](SparkNodeAwsAttributes.md) |  | [optional] 
**host_private_ip** | **str** | The private IP address of the host instance. | [optional] 

## Example

```python
from databricks_jobs.models.spark_node import SparkNode

# TODO update the JSON string below
json = "{}"
# create an instance of SparkNode from a JSON string
spark_node_instance = SparkNode.from_json(json)
# print the JSON string representation of the object
print SparkNode.to_json()

# convert the object into a dict
spark_node_dict = spark_node_instance.to_dict()
# create an instance of SparkNode from a dict
spark_node_form_dict = spark_node.from_dict(spark_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


