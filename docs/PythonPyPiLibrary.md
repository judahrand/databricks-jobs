# PythonPyPiLibrary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | **str** | The name of the PyPI package to install. An optional exact version specification is also supported. Examples: &#x60;simplejson&#x60; and &#x60;simplejson&#x3D;&#x3D;3.8.0&#x60;. This field is required. | 
**repo** | **str** | The repository where the package can be found. If not specified, the default pip index is used. | [optional] 

## Example

```python
from databricks_jobs.models.python_py_pi_library import PythonPyPiLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of PythonPyPiLibrary from a JSON string
python_py_pi_library_instance = PythonPyPiLibrary.from_json(json)
# print the JSON string representation of the object
print PythonPyPiLibrary.to_json()

# convert the object into a dict
python_py_pi_library_dict = python_py_pi_library_instance.to_dict()
# create an instance of PythonPyPiLibrary from a dict
python_py_pi_library_form_dict = python_py_pi_library.from_dict(python_py_pi_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


