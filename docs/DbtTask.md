# DbtTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_directory** | **str** | Optional (relative) path to the project directory, if no value is provided, the root of the git repository is used. | [optional] 
**commands** | **List[str]** | A list of dbt commands to execute. All commands must start with &#x60;dbt&#x60;. This parameter must not be empty. A maximum of up to 10 commands can be provided. | 
**var_schema** | **str** | Optional schema to write to. This parameter is only used when a warehouse_id is also provided. If not provided, the &#x60;default&#x60; schema is used. | [optional] 
**warehouse_id** | **str** | ID of the SQL warehouse to connect to. If provided, we automatically generate and provide the profile and connection details to dbt. It can be overridden on a per-command basis by using the &#x60;--profiles-dir&#x60; command line argument. | [optional] 
**catalog** | **str** | Optional name of the catalog to use. The value is the top level in the 3-level namespace of Unity Catalog (catalog / schema / relation). The catalog value can only be specified if a warehouse_id is specified. Requires dbt-databricks &gt;&#x3D; 1.1.1. | [optional] 
**profiles_directory** | **str** | Optional (relative) path to the profiles directory. Can only be specified if no warehouse_id is specified. If no warehouse_id is specified and this folder is unset, the root directory is used. | [optional] 

## Example

```python
from databricks_jobs.models.dbt_task import DbtTask

# TODO update the JSON string below
json = "{}"
# create an instance of DbtTask from a JSON string
dbt_task_instance = DbtTask.from_json(json)
# print the JSON string representation of the object
print DbtTask.to_json()

# convert the object into a dict
dbt_task_dict = dbt_task_instance.to_dict()
# create an instance of DbtTask from a dict
dbt_task_form_dict = dbt_task.from_dict(dbt_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


