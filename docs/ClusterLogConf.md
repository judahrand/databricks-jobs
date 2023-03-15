# ClusterLogConf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dbfs** | [**DbfsStorageInfo**](DbfsStorageInfo.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.cluster_log_conf import ClusterLogConf

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLogConf from a JSON string
cluster_log_conf_instance = ClusterLogConf.from_json(json)
# print the JSON string representation of the object
print ClusterLogConf.to_json()

# convert the object into a dict
cluster_log_conf_dict = cluster_log_conf_instance.to_dict()
# create an instance of ClusterLogConf from a dict
cluster_log_conf_form_dict = cluster_log_conf.from_dict(cluster_log_conf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


