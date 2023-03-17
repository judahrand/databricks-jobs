# AwsAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_on_demand** | **int** | The first first_on_demand nodes of the cluster are placed on on-demand instances. If this value is greater than 0, the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes are placed on on-demand instances. If this value is less than the current cluster size, first_on_demand nodes are placed on on-demand instances and the remainder are placed on &#x60;availability&#x60; instances. This value does not affect cluster size and cannot be mutated over the lifetime of a cluster. | [optional] 
**availability** | **str** | Availability type used for all subsequent nodes past the &#x60;first_on_demand&#x60; ones. **Note:** If &#x60;first_on_demand&#x60; is zero, this availability type is used for the entire cluster.  &#x60;SPOT&#x60;: use spot instances. &#x60;ON_DEMAND&#x60;: use on-demand instances. &#x60;SPOT_WITH_FALLBACK&#x60;: preferably use spot instances, but fall back to on-demand instances if spot instances cannot be acquired (for example, if AWS spot prices are too high). | [optional] 
**zone_id** | **str** | Identifier for the availability zone/datacenter in which the cluster resides. You have three options:  **Specify an availability zone as a string**, for example: “us-west-2a”. The provided availability zone must be in the same region as the Databricks deployment. For example, “us-west-2a” is not a valid zone ID if the Databricks deployment resides in the “us-east-1” region.  **Enable automatic availability zone selection (“Auto-AZ”)**, by setting the value “auto”. Databricks selects the AZ based on available IPs in the workspace subnets and retries in other availability zones if AWS returns insufficient capacity errors.  **Do not specify a value**. If not specified, a default zone is used.  The list of available zones as well as the default value can be found by using the [List zones](https://docs.databricks.com/dev-tools/api/latest/clusters.html#list-zones) API. | [optional] 
**instance_profile_arn** | **str** | Nodes for this cluster are only be placed on AWS instances with this instance profile. If omitted, nodes are placed on instances without an instance profile. The instance profile must have previously been added to the Databricks environment by an account administrator.  This feature may only be available to certain customer plans. | [optional] 
**spot_bid_price_percent** | **int** | The max price for AWS spot instances, as a percentage of the corresponding instance type’s on-demand price. For example, if this field is set to 50, and the cluster needs a new &#x60;i3.xlarge&#x60; spot instance, then the max price is half of the price of on-demand &#x60;i3.xlarge&#x60; instances. Similarly, if this field is set to 200, the max price is twice the price of on-demand &#x60;i3.xlarge&#x60; instances. If not specified, the default value is 100\\. When spot instances are requested for this cluster, only spot instances whose max price percentage matches this field is considered. For safety, we enforce this field to be no more than 10000. | [optional] 
**ebs_volume_type** | **str** | The type of EBS volume that is launched with this cluster.  &#x60;GENERAL_PURPOSE_SSD&#x60;: provision extra storage using AWS gp2 EBS volumes. &#x60;THROUGHPUT_OPTIMIZED_HDD&#x60;: provision extra storage using AWS st1 volumes. | [optional] 
**ebs_volume_count** | **int** | The number of volumes launched for each instance. You can choose up to 10 volumes. This feature is only enabled for supported node types. Legacy node types cannot specify custom EBS volumes. For node types with no instance store, at least one EBS volume needs to be specified; otherwise, cluster creation fails.  These EBS volumes are mounted at &#x60;/ebs0&#x60;, &#x60;/ebs1&#x60;, and etc. Instance store volumes are mounted at &#x60;/local_disk0&#x60;, &#x60;/local_disk1&#x60;, and etc.  If EBS volumes are attached, Databricks configures Spark to use only the EBS volumes for scratch storage because heterogeneously sized scratch devices can lead to inefficient disk utilization. If no EBS volumes are attached, Databricks configures Spark to use instance store volumes.  If EBS volumes are specified, then the Spark configuration &#x60;spark.local.dir&#x60; is overridden. | [optional] 
**ebs_volume_size** | **int** | The size of each EBS volume (in GiB) launched for each instance. For general purpose SSD, this value must be within the range 100 - 4096\\. For throughput optimized HDD, this value must be within the range 500 - 4096\\. Custom EBS volumes cannot be specified for the legacy node types (_memory-optimized_ and _compute-optimized_). | [optional] 
**ebs_volume_iops** | **int** | The number of IOPS per EBS gp3 volume.  This value must be between 3000 and 16000.  The value of IOPS and throughput is calculated based on AWS documentation to match the maximum performance of a gp2 volume with the same volume size.  For more information, see the [EBS volume limit calculator](https://github.com/awslabs/aws-support-tools/tree/master/EBS/VolumeLimitCalculator). | [optional] 
**ebs_volume_throughput** | **int** | The throughput per EBS gp3 volume, in MiB per second.  This value must be between 125 and 1000. | [optional] 

## Example

```python
from databricks_jobs.models.aws_attributes import AwsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAttributes from a JSON string
aws_attributes_instance = AwsAttributes.from_json(json)
# print the JSON string representation of the object
print AwsAttributes.to_json()

# convert the object into a dict
aws_attributes_dict = aws_attributes_instance.to_dict()
# create an instance of AwsAttributes from a dict
aws_attributes_form_dict = aws_attributes.from_dict(aws_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


