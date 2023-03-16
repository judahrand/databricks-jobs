<a name="__pageTop"></a>
# databricks_jobs.apis.tags.default_api.DefaultApi

All URIs are relative to *https://&lt;databricks-instance&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobs_create**](#jobs_create) | **post** /2.1/jobs/create | Create a new job
[**jobs_delete**](#jobs_delete) | **post** /2.1/jobs/delete | Delete a job
[**jobs_get**](#jobs_get) | **get** /2.1/jobs/get | Get a single job
[**jobs_list**](#jobs_list) | **get** /2.1/jobs/list | List all jobs
[**jobs_reset**](#jobs_reset) | **post** /2.1/jobs/reset | Overwrites all settings for a job
[**jobs_run_now**](#jobs_run_now) | **post** /2.1/jobs/run-now | Trigger a new job run
[**jobs_runs_cancel**](#jobs_runs_cancel) | **post** /2.1/jobs/runs/cancel | Cancel a job run
[**jobs_runs_cancel_all**](#jobs_runs_cancel_all) | **post** /2.1/jobs/runs/cancel-all | Cancel all runs of a job
[**jobs_runs_delete**](#jobs_runs_delete) | **post** /2.1/jobs/runs/delete | Delete a job run
[**jobs_runs_export**](#jobs_runs_export) | **get** /2.0/jobs/runs/export | Export and retrieve a job run
[**jobs_runs_get**](#jobs_runs_get) | **get** /2.1/jobs/runs/get | Get a single job run
[**jobs_runs_get_output**](#jobs_runs_get_output) | **get** /2.1/jobs/runs/get-output | Get the output for a single run
[**jobs_runs_list**](#jobs_runs_list) | **get** /2.1/jobs/runs/list | List runs for a job
[**jobs_runs_repair**](#jobs_runs_repair) | **post** /2.1/jobs/runs/repair | Repair a job run
[**jobs_runs_submit**](#jobs_runs_submit) | **post** /2.1/jobs/runs/submit | Create and trigger a one-time run
[**jobs_update**](#jobs_update) | **post** /2.1/jobs/update | Partially updates a job

# **jobs_create**
<a name="jobs_create"></a>
> JobsCreate200Response jobs_create(jobs_create_request)

Create a new job

Create a new job.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_create200_response import JobsCreate200Response
from databricks_jobs.model.jobs_create_request import JobsCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = JobsCreateRequest(None)
    try:
        # Create a new job
        api_response = api_instance.jobs_create(
            body=body,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsCreateRequest**](../../models/JobsCreateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_create.ApiResponseFor200) | Job was created successfully
400 | [ApiResponseFor400](#jobs_create.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_create.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_create.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsCreate200Response**](../../models/JobsCreate200Response.md) |  | 


#### jobs_create.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_create.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_create.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_delete**
<a name="jobs_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} jobs_delete(jobs_delete_request)

Delete a job

Deletes a job.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_delete_request import JobsDeleteRequest
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = JobsDeleteRequest(
        job_id=11223344,
    )
    try:
        # Delete a job
        api_response = api_instance.jobs_delete(
            body=body,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsDeleteRequest**](../../models/JobsDeleteRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_delete.ApiResponseFor200) | Job was deleted successfully.
400 | [ApiResponseFor400](#jobs_delete.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_delete.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_delete.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### jobs_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_get**
<a name="jobs_get"></a>
> JobsGet200Response jobs_get(job_id)

Get a single job

Retrieves the details for a single job.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_get200_response import JobsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'job_id': 11223344,
    }
    try:
        # Get a single job
        api_response = api_instance.jobs_get(
            query_params=query_params,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
job_id | JobIdSchema | | 


# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_get.ApiResponseFor200) | Job was retrieved successfully.
400 | [ApiResponseFor400](#jobs_get.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_get.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_get.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsGet200Response**](../../models/JobsGet200Response.md) |  | 


#### jobs_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_list**
<a name="jobs_list"></a>
> JobsList200Response jobs_list()

List all jobs

Retrieves a list of jobs.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_list200_response import JobsList200Response
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'limit': 25,
        'offset': 0,
        'name': "A%20multitask%20job",
        'expand_tasks': False,
    }
    try:
        # List all jobs
        api_response = api_instance.jobs_list(
            query_params=query_params,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
name | NameSchema | | optional
expand_tasks | ExpandTasksSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 20

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ExpandTasksSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_list.ApiResponseFor200) | List of jobs was retrieved successfully.
400 | [ApiResponseFor400](#jobs_list.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_list.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_list.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsList200Response**](../../models/JobsList200Response.md) |  | 


#### jobs_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_list.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_reset**
<a name="jobs_reset"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} jobs_reset(jobs_reset_request)

Overwrites all settings for a job

Overwrites all the settings for a specific job. Use the Update endpoint to update job settings partially.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_reset_request import JobsResetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = JobsResetRequest(
        job_id=11223344,
        new_settings=JobSettings(None),
    )
    try:
        # Overwrites all settings for a job
        api_response = api_instance.jobs_reset(
            body=body,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_reset: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsResetRequest**](../../models/JobsResetRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_reset.ApiResponseFor200) | Job was overwritten successfully.
400 | [ApiResponseFor400](#jobs_reset.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_reset.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_reset.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_reset.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### jobs_reset.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_reset.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_reset.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_run_now**
<a name="jobs_run_now"></a>
> JobsRunNow200Response jobs_run_now(jobs_run_now_request)

Trigger a new job run

Run a job and return the `run_id` of the triggered run.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_run_now200_response import JobsRunNow200Response
from databricks_jobs.model.jobs_run_now_request import JobsRunNowRequest
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = JobsRunNowRequest(None)
    try:
        # Trigger a new job run
        api_response = api_instance.jobs_run_now(
            body=body,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_run_now: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunNowRequest**](../../models/JobsRunNowRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_run_now.ApiResponseFor200) | Run was started successfully.
400 | [ApiResponseFor400](#jobs_run_now.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_run_now.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_run_now.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_run_now.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunNow200Response**](../../models/JobsRunNow200Response.md) |  | 


#### jobs_run_now.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_run_now.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_run_now.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_runs_cancel**
<a name="jobs_runs_cancel"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} jobs_runs_cancel(jobs_runs_cancel_request)

Cancel a job run

Cancels a job run. The run is canceled asynchronously, so it may still be running when this request completes.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_runs_cancel_request import JobsRunsCancelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = JobsRunsCancelRequest(
        run_id=455644833,
    )
    try:
        # Cancel a job run
        api_response = api_instance.jobs_runs_cancel(
            body=body,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_runs_cancel: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunsCancelRequest**](../../models/JobsRunsCancelRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_runs_cancel.ApiResponseFor200) | Run was cancelled successfully.
400 | [ApiResponseFor400](#jobs_runs_cancel.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_runs_cancel.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_runs_cancel.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_runs_cancel.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### jobs_runs_cancel.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_cancel.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_cancel.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_runs_cancel_all**
<a name="jobs_runs_cancel_all"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} jobs_runs_cancel_all(jobs_runs_cancel_all_request)

Cancel all runs of a job

Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new runs from being started.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_runs_cancel_all_request import JobsRunsCancelAllRequest
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = JobsRunsCancelAllRequest(
        job_id=11223344,
    )
    try:
        # Cancel all runs of a job
        api_response = api_instance.jobs_runs_cancel_all(
            body=body,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_runs_cancel_all: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunsCancelAllRequest**](../../models/JobsRunsCancelAllRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_runs_cancel_all.ApiResponseFor200) | All runs were cancelled successfully.
400 | [ApiResponseFor400](#jobs_runs_cancel_all.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_runs_cancel_all.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_runs_cancel_all.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_runs_cancel_all.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### jobs_runs_cancel_all.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_cancel_all.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_cancel_all.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_runs_delete**
<a name="jobs_runs_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} jobs_runs_delete(jobs_runs_delete_request)

Delete a job run

Deletes a non-active run. Returns an error if the run is active.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_runs_delete_request import JobsRunsDeleteRequest
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = JobsRunsDeleteRequest(
        run_id=455644833,
    )
    try:
        # Delete a job run
        api_response = api_instance.jobs_runs_delete(
            body=body,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_runs_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunsDeleteRequest**](../../models/JobsRunsDeleteRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_runs_delete.ApiResponseFor200) | Run was deleted successfully.
400 | [ApiResponseFor400](#jobs_runs_delete.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_runs_delete.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_runs_delete.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_runs_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### jobs_runs_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_runs_export**
<a name="jobs_runs_export"></a>
> JobsRunsExport200Response jobs_runs_export(run_id)

Export and retrieve a job run

Export and retrieve the job run task.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.views_to_export import ViewsToExport
from databricks_jobs.model.jobs_runs_export200_response import JobsRunsExport200Response
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'run_id': 455644833,
    }
    try:
        # Export and retrieve a job run
        api_response = api_instance.jobs_runs_export(
            query_params=query_params,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_runs_export: %s\n" % e)

    # example passing only optional values
    query_params = {
        'run_id': 455644833,
        'views_to_export': ViewsToExport("CODE"),
    }
    try:
        # Export and retrieve a job run
        api_response = api_instance.jobs_runs_export(
            query_params=query_params,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_runs_export: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
run_id | RunIdSchema | | 
views_to_export | ViewsToExportSchema | | optional


# RunIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# ViewsToExportSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ViewsToExport**](../../models/ViewsToExport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_runs_export.ApiResponseFor200) | Run was exported successfully.
400 | [ApiResponseFor400](#jobs_runs_export.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_runs_export.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_runs_export.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_runs_export.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunsExport200Response**](../../models/JobsRunsExport200Response.md) |  | 


#### jobs_runs_export.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_export.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_export.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_runs_get**
<a name="jobs_runs_get"></a>
> JobsRunsGet200Response jobs_runs_get(run_id)

Get a single job run

Retrieve the metadata of a run.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_runs_get200_response import JobsRunsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'run_id': 455644833,
    }
    try:
        # Get a single job run
        api_response = api_instance.jobs_runs_get(
            query_params=query_params,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_runs_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'run_id': 455644833,
        'include_history': True,
    }
    try:
        # Get a single job run
        api_response = api_instance.jobs_runs_get(
            query_params=query_params,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_runs_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
run_id | RunIdSchema | | 
include_history | IncludeHistorySchema | | optional


# RunIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# IncludeHistorySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_runs_get.ApiResponseFor200) | Run was retrieved successfully
400 | [ApiResponseFor400](#jobs_runs_get.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_runs_get.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_runs_get.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_runs_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunsGet200Response**](../../models/JobsRunsGet200Response.md) |  | 


#### jobs_runs_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_runs_get_output**
<a name="jobs_runs_get_output"></a>
> JobsRunsGetOutput200Response jobs_runs_get_output(run_id)

Get the output for a single run

Retrieve the output and metadata of a single task run. When a notebook task returns a value through the dbutils.notebook.exit() call, you can use this endpoint to retrieve that value. Azure Databricks restricts this API to return the first 5 MB of the output. To return a larger result, you can store job results in a cloud storage service. This endpoint validates that the run_id parameter is valid and returns an HTTP status code 400 if the run_id parameter is invalid. Runs are automatically removed after 60 days. If you to want to reference them beyond 60 days, you must save old run results before they expire. To export using the UI, see Export job run results. To export using the Jobs API, see Runs export.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_runs_get_output200_response import JobsRunsGetOutput200Response
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'run_id': 455644833,
    }
    try:
        # Get the output for a single run
        api_response = api_instance.jobs_runs_get_output(
            query_params=query_params,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_runs_get_output: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
run_id | RunIdSchema | | 


# RunIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_runs_get_output.ApiResponseFor200) | Run output was retrieved successfully.
400 | [ApiResponseFor400](#jobs_runs_get_output.ApiResponseFor400) | A job run with multiple tasks was provided.
401 | [ApiResponseFor401](#jobs_runs_get_output.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_runs_get_output.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_runs_get_output.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunsGetOutput200Response**](../../models/JobsRunsGetOutput200Response.md) |  | 


#### jobs_runs_get_output.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_get_output.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_get_output.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_runs_list**
<a name="jobs_runs_list"></a>
> JobsRunsList200Response jobs_runs_list()

List runs for a job

List runs in descending order by start time.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.jobs_runs_list200_response import JobsRunsList200Response
from databricks_jobs.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'active_only': False,
        'completed_only': False,
        'job_id': 11223344,
        'offset': 0,
        'limit': 25,
        'run_type': "JOB_RUN",
        'expand_tasks': False,
        'start_time_from': 1642521600000,
        'start_time_to': 1642608000000,
    }
    try:
        # List runs for a job
        api_response = api_instance.jobs_runs_list(
            query_params=query_params,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_runs_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
active_only | ActiveOnlySchema | | optional
completed_only | CompletedOnlySchema | | optional
job_id | JobIdSchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional
run_type | RunTypeSchema | | optional
expand_tasks | ExpandTasksSchema | | optional
start_time_from | StartTimeFromSchema | | optional
start_time_to | StartTimeToSchema | | optional


# ActiveOnlySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# CompletedOnlySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 25value must be a 32 bit integer

# RunTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["JOB_RUN", "WORKFLOW_RUN", "SUBMIT_RUN", ] 

# ExpandTasksSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# StartTimeFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StartTimeToSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_runs_list.ApiResponseFor200) | List of runs was retrieved successfully.
400 | [ApiResponseFor400](#jobs_runs_list.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_runs_list.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_runs_list.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_runs_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunsList200Response**](../../models/JobsRunsList200Response.md) |  | 


#### jobs_runs_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_list.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_runs_repair**
<a name="jobs_runs_repair"></a>
> JobsRunsRepair200Response jobs_runs_repair(jobs_runs_repair_request)

Repair a job run

Re-run one or more tasks. Tasks are re-run as part of the original job run, use the current job and task settings, and can be viewed in the history for the original job run.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_runs_repair200_response import JobsRunsRepair200Response
from databricks_jobs.model.jobs_runs_repair_request import JobsRunsRepairRequest
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = JobsRunsRepairRequest(None)
    try:
        # Repair a job run
        api_response = api_instance.jobs_runs_repair(
            body=body,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_runs_repair: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunsRepairRequest**](../../models/JobsRunsRepairRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_runs_repair.ApiResponseFor200) | Run repair was initiated.
400 | [ApiResponseFor400](#jobs_runs_repair.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_runs_repair.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_runs_repair.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_runs_repair.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunsRepair200Response**](../../models/JobsRunsRepair200Response.md) |  | 


#### jobs_runs_repair.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_repair.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_repair.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_runs_submit**
<a name="jobs_runs_submit"></a>
> JobsRunsSubmit200Response jobs_runs_submit(jobs_runs_submit_request)

Create and trigger a one-time run

Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job. Use the `jobs/runs/get` API to check the run state after the job is submitted.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_runs_submit_request import JobsRunsSubmitRequest
from databricks_jobs.model.jobs_runs_submit200_response import JobsRunsSubmit200Response
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = JobsRunsSubmitRequest(None)
    try:
        # Create and trigger a one-time run
        api_response = api_instance.jobs_runs_submit(
            body=body,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_runs_submit: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunsSubmitRequest**](../../models/JobsRunsSubmitRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_runs_submit.ApiResponseFor200) | Run was created and started successfully.
400 | [ApiResponseFor400](#jobs_runs_submit.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_runs_submit.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_runs_submit.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_runs_submit.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsRunsSubmit200Response**](../../models/JobsRunsSubmit200Response.md) |  | 


#### jobs_runs_submit.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_submit.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_runs_submit.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **jobs_update**
<a name="jobs_update"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} jobs_update(jobs_update_request)

Partially updates a job

Add, update, or remove specific settings of an existing job. Use the Reset endpoint to overwrite all job settings.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
import databricks_jobs
from databricks_jobs.apis.tags import default_api
from databricks_jobs.model.error import Error
from databricks_jobs.model.jobs_update_request import JobsUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://<databricks-instance>/api
# See configuration.py for a list of all supported configuration parameters.
configuration = databricks_jobs.Configuration(
    host = "https://<databricks-instance>/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_token): bearerAuth
configuration = databricks_jobs.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = JobsUpdateRequest(
        job_id=11223344,
        new_settings=JobSettings(None),
        fields_to_remove=["libraries","schedule"],
    )
    try:
        # Partially updates a job
        api_response = api_instance.jobs_update(
            body=body,
        )
        pprint(api_response)
    except databricks_jobs.ApiException as e:
        print("Exception when calling DefaultApi->jobs_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobsUpdateRequest**](../../models/JobsUpdateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jobs_update.ApiResponseFor200) | Job was updated successfully.
400 | [ApiResponseFor400](#jobs_update.ApiResponseFor400) | The request was malformed. See JSON response for error details.
401 | [ApiResponseFor401](#jobs_update.ApiResponseFor401) | The request was unauthorized.
500 | [ApiResponseFor500](#jobs_update.ApiResponseFor500) | The request was not handled correctly due to a server error.

#### jobs_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### jobs_update.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_update.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### jobs_update.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

