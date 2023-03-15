# DockerBasicAuth


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | User name for the Docker repository. | [optional] 
**password** | **str** | Password for the Docker repository. | [optional] 

## Example

```python
from databricks_jobs.models.docker_basic_auth import DockerBasicAuth

# TODO update the JSON string below
json = "{}"
# create an instance of DockerBasicAuth from a JSON string
docker_basic_auth_instance = DockerBasicAuth.from_json(json)
# print the JSON string representation of the object
print DockerBasicAuth.to_json()

# convert the object into a dict
docker_basic_auth_dict = docker_basic_auth_instance.to_dict()
# create an instance of DockerBasicAuth from a dict
docker_basic_auth_form_dict = docker_basic_auth.from_dict(docker_basic_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


