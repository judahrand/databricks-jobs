# PythonWheelTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_name** | **str** | Name of the package to execute | [optional] 
**entry_point** | **str** | Named entry point to use, if it does not exist in the metadata of the package it executes the function from the package directly using &#x60;$packageName.$entryPoint()&#x60; | [optional] 
**parameters** | **List[str]** | Command-line parameters passed to Python wheel task. Leave it empty if &#x60;named_parameters&#x60; is not null. | [optional] 
**named_parameters** | **object** | Command-line parameters passed to Python wheel task in the form of &#x60;[\&quot;--name&#x3D;task\&quot;, \&quot;--data&#x3D;dbfs:/path/to/data.json\&quot;]&#x60;. Leave it empty if &#x60;parameters&#x60; is not null. | [optional] 

## Example

```python
from databricks_jobs.models.python_wheel_task import PythonWheelTask

# TODO update the JSON string below
json = "{}"
# create an instance of PythonWheelTask from a JSON string
python_wheel_task_instance = PythonWheelTask.from_json(json)
# print the JSON string representation of the object
print PythonWheelTask.to_json()

# convert the object into a dict
python_wheel_task_dict = python_wheel_task_instance.to_dict()
# create an instance of PythonWheelTask from a dict
python_wheel_task_form_dict = python_wheel_task.from_dict(python_wheel_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


