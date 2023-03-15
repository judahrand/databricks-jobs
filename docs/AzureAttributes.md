# AzureAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_on_demand** | **int** | The first &#x60;first_on_demand&#x60; nodes of the cluster are placed on on-demand instances. This value must be greater than 0, or else cluster creation validation fails. If this value is greater than or equal to the current cluster size, all nodes are placed on on-demand instances. If this value is less than the current cluster size, &#x60;first_on_demand&#x60; nodes are placed on on-demand instances and the remainder are placed on availability instances. This value does not affect cluster size and cannot be mutated over the lifetime of a cluster. | [optional] 
**availability** | **str** | Availability type used for all subsequent nodes past the &#x60;first_on_demand&#x60; ones.  &#x60;SPOT_AZURE&#x60;: use spot instances. &#x60;ON_DEMAND_AZURE&#x60;: use on demand instances. &#x60;SPOT_WITH_FALLBACK_AZURE&#x60;: preferably use spot instances, but fall back to on-demand instances if spot instances cannot be acquired (for example, if Azure spot prices are too high or out of quota). Does not apply to pool availability. | [optional] 
**spot_bid_max_price** | **float** | The max bid price used for Azure spot instances. You can set this to greater than or equal to the current spot price. You can also set this to -1 (the default), which specifies that the instance cannot be evicted on the basis of price. The price for the instance is the current price for spot instances or the price for a standard instance. You can view historical pricing and eviction rates in the Azure portal. | [optional] 

## Example

```python
from databricks_jobs.models.azure_attributes import AzureAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AzureAttributes from a JSON string
azure_attributes_instance = AzureAttributes.from_json(json)
# print the JSON string representation of the object
print AzureAttributes.to_json()

# convert the object into a dict
azure_attributes_dict = azure_attributes_instance.to_dict()
# create an instance of AzureAttributes from a dict
azure_attributes_form_dict = azure_attributes.from_dict(azure_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


