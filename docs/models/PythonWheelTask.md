# databricks_jobs.model.python_wheel_task.PythonWheelTask

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**package_name** | str,  | str,  | Name of the package to execute | [optional] 
**entry_point** | str,  | str,  | Named entry point to use, if it does not exist in the metadata of the package it executes the function from the package directly using &#x60;$packageName.$entryPoint()&#x60; | [optional] 
**[parameters](#parameters)** | list, tuple,  | tuple,  | Command-line parameters passed to Python wheel task. Leave it empty if &#x60;named_parameters&#x60; is not null. | [optional] 
**[named_parameters](#named_parameters)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Command-line parameters passed to Python wheel task in the form of &#x60;[\&quot;--name&#x3D;task\&quot;, \&quot;--data&#x3D;dbfs:/path/to/data.json\&quot;]&#x60;. Leave it empty if &#x60;parameters&#x60; is not null. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# parameters

Command-line parameters passed to Python wheel task. Leave it empty if `named_parameters` is not null.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Command-line parameters passed to Python wheel task. Leave it empty if &#x60;named_parameters&#x60; is not null. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# named_parameters

Command-line parameters passed to Python wheel task in the form of `[\"--name=task\", \"--data=dbfs:/path/to/data.json\"]`. Leave it empty if `parameters` is not null.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Command-line parameters passed to Python wheel task in the form of &#x60;[\&quot;--name&#x3D;task\&quot;, \&quot;--data&#x3D;dbfs:/path/to/data.json\&quot;]&#x60;. Leave it empty if &#x60;parameters&#x60; is not null. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

