# databricks_jobs.model.spark_node.SparkNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**private_ip** | str,  | str,  | Private IP address (typically a 10.x.x.x address) of the Spark node. This is different from the private IP address of the host instance. | [optional] 
**public_dns** | str,  | str,  | Public DNS address of this node. This address can be used to access the Spark JDBC server on the driver node. | [optional] 
**node_id** | str,  | str,  | Globally unique identifier for this node. | [optional] 
**instance_id** | str,  | str,  | Globally unique identifier for the host instance from the cloud provider. | [optional] 
**start_timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp (in millisecond) when the Spark node is launched. | [optional] value must be a 64 bit integer
**host_private_ip** | str,  | str,  | The private IP address of the host instance. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

