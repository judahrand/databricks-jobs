# S3StorageInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | S3 destination. For example: &#x60;s3://my-bucket/some-prefix&#x60; You must configure the cluster with an instance profile and the instance profile must have write access to the destination. You _cannot_ use AWS keys. | [optional] 
**region** | **str** | S3 region. For example: &#x60;us-west-2&#x60;. Either region or endpoint must be set. If both are set, endpoint is used. | [optional] 
**endpoint** | **str** | S3 endpoint. For example: &#x60;https://s3-us-west-2.amazonaws.com&#x60;. Either region or endpoint must be set. If both are set, endpoint is used. | [optional] 
**enable_encryption** | **bool** | (Optional)Enable server side encryption, &#x60;false&#x60; by default. | [optional] 
**encryption_type** | **str** | (Optional) The encryption type, it could be &#x60;sse-s3&#x60; or &#x60;sse-kms&#x60;. It is used only when encryption is enabled and the default type is &#x60;sse-s3&#x60;. | [optional] 
**kms_key** | **str** | (Optional) KMS key used if encryption is enabled and encryption type is set to &#x60;sse-kms&#x60;. | [optional] 
**canned_acl** | **str** | (Optional) Set canned access control list. For example: &#x60;bucket-owner-full-control&#x60;. If canned_acl is set, the cluster instance profile must have &#x60;s3:PutObjectAcl&#x60; permission on the destination bucket and prefix. The full list of possible canned ACLs can be found at &lt;https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl&gt;. By default only the object owner gets full control. If you are using cross account role for writing data, you may want to set &#x60;bucket-owner-full-control&#x60; to make bucket owner able to read the logs. | [optional] 

## Example

```python
from databricks_jobs.models.s3_storage_info import S3StorageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of S3StorageInfo from a JSON string
s3_storage_info_instance = S3StorageInfo.from_json(json)
# print the JSON string representation of the object
print S3StorageInfo.to_json()

# convert the object into a dict
s3_storage_info_dict = s3_storage_info_instance.to_dict()
# create an instance of S3StorageInfo from a dict
s3_storage_info_form_dict = s3_storage_info.from_dict(s3_storage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


