# databricks_jobs.model.azure_attributes.AzureAttributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**first_on_demand** | decimal.Decimal, int,  | decimal.Decimal,  | The first &#x60;first_on_demand&#x60; nodes of the cluster are placed on on-demand instances. This value must be greater than 0, or else cluster creation validation fails. If this value is greater than or equal to the current cluster size, all nodes are placed on on-demand instances. If this value is less than the current cluster size, &#x60;first_on_demand&#x60; nodes are placed on on-demand instances and the remainder are placed on availability instances. This value does not affect cluster size and cannot be mutated over the lifetime of a cluster. | [optional] value must be a 32 bit integer
**availability** | str,  | str,  | Availability type used for all subsequent nodes past the &#x60;first_on_demand&#x60; ones.  &#x60;SPOT_AZURE&#x60;: use spot instances. &#x60;ON_DEMAND_AZURE&#x60;: use on demand instances. &#x60;SPOT_WITH_FALLBACK_AZURE&#x60;: preferably use spot instances, but fall back to on-demand instances if spot instances cannot be acquired (for example, if Azure spot prices are too high or out of quota). Does not apply to pool availability. | [optional] must be one of ["SPOT_AZURE", "ON_DEMAND_AZURE", "SPOT_WITH_FALLBACK_AZURE", ] 
**spot_bid_max_price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The max bid price used for Azure spot instances. You can set this to greater than or equal to the current spot price. You can also set this to -1 (the default), which specifies that the instance cannot be evicted on the basis of price. The price for the instance is the current price for spot instances or the price for a standard instance. You can view historical pricing and eviction rates in the Azure portal. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

