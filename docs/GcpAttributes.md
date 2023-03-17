# GcpAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_preemptible_executors** | **bool** | Use preemptible executors. | [optional] 
**google_service_account** | **str** | Google service account email address that the cluster uses to authenticate with Google Identity. This field is used for authentication with the [GCS](https://docs.gcp.databricks.com/data/data-sources/google/gcs.html) and [BigQuery](https://docs.gcp.databricks.com/data/data-sources/google/bigquery.html) data sources. | [optional] 

## Example

```python
from databricks_jobs.models.gcp_attributes import GcpAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of GcpAttributes from a JSON string
gcp_attributes_instance = GcpAttributes.from_json(json)
# print the JSON string representation of the object
print GcpAttributes.to_json()

# convert the object into a dict
gcp_attributes_dict = gcp_attributes_instance.to_dict()
# create an instance of GcpAttributes from a dict
gcp_attributes_form_dict = gcp_attributes.from_dict(gcp_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


