# databricks_jobs.model.cluster_event.ClusterEvent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cluster_id** | str,  | str,  | Canonical identifier for the cluster. This field is required. | 
**details** | [**EventDetails**](EventDetails.md) | [**EventDetails**](EventDetails.md) |  | 
**type** | [**ClusterEventType**](ClusterEventType.md) | [**ClusterEventType**](ClusterEventType.md) |  | 
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp when the event occurred, stored as the number of milliseconds since the unix epoch. Assigned by the Timeline service. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

