# DockerImage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL for the Docker image. | [optional] 
**basic_auth** | [**DockerBasicAuth**](DockerBasicAuth.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.docker_image import DockerImage

# TODO update the JSON string below
json = "{}"
# create an instance of DockerImage from a JSON string
docker_image_instance = DockerImage.from_json(json)
# print the JSON string representation of the object
print DockerImage.to_json()

# convert the object into a dict
docker_image_dict = docker_image_instance.to_dict()
# create an instance of DockerImage from a dict
docker_image_form_dict = docker_image.from_dict(docker_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


