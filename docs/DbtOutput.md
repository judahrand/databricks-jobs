# DbtOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts_link** | **str** | A pre-signed URL to download the (compressed) dbt artifacts. This link is valid for a limited time (30 minutes). This information is only available after the run has finished. | [optional] 
**artifacts_headers** | **object** | An optional map of headers to send when retrieving the artifact from the &#x60;artifacts_link&#x60;. | [optional] 

## Example

```python
from databricks_jobs.models.dbt_output import DbtOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DbtOutput from a JSON string
dbt_output_instance = DbtOutput.from_json(json)
# print the JSON string representation of the object
print DbtOutput.to_json()

# convert the object into a dict
dbt_output_dict = dbt_output_instance.to_dict()
# create an instance of DbtOutput from a dict
dbt_output_form_dict = dbt_output.from_dict(dbt_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


