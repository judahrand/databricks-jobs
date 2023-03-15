# databricks_jobs.DefaultApi

All URIs are relative to *https://&lt;databricks-instance&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobs_create**](DefaultApi.md#jobs_create) | **POST** /2.1/jobs/create | Create a new job
[**jobs_delete**](DefaultApi.md#jobs_delete) | **POST** /2.1/jobs/delete | Delete a job
[**jobs_get**](DefaultApi.md#jobs_get) | **GET** /2.1/jobs/get | Get a single job
[**jobs_list**](DefaultApi.md#jobs_list) | **GET** /2.1/jobs/list | List all jobs
[**jobs_reset**](DefaultApi.md#jobs_reset) | **POST** /2.1/jobs/reset | Overwrites all settings for a job
[**jobs_run_now**](DefaultApi.md#jobs_run_now) | **POST** /2.1/jobs/run-now | Trigger a new job run
[**jobs_runs_cancel**](DefaultApi.md#jobs_runs_cancel) | **POST** /2.1/jobs/runs/cancel | Cancel a job run
[**jobs_runs_cancel_all**](DefaultApi.md#jobs_runs_cancel_all) | **POST** /2.1/jobs/runs/cancel-all | Cancel all runs of a job
[**jobs_runs_delete**](DefaultApi.md#jobs_runs_delete) | **POST** /2.1/jobs/runs/delete | Delete a job run
[**jobs_runs_export**](DefaultApi.md#jobs_runs_export) | **GET** /2.0/jobs/runs/export | Export and retrieve a job run
[**jobs_runs_get**](DefaultApi.md#jobs_runs_get) | **GET** /2.1/jobs/runs/get | Get a single job run
[**jobs_runs_get_output**](DefaultApi.md#jobs_runs_get_output) | **GET** /2.1/jobs/runs/get-output | Get the output for a single run
[**jobs_runs_list**](DefaultApi.md#jobs_runs_list) | **GET** /2.1/jobs/runs/list | List runs for a job
[**jobs_runs_repair**](DefaultApi.md#jobs_runs_repair) | **POST** /2.1/jobs/runs/repair | Repair a job run
[**jobs_runs_submit**](DefaultApi.md#jobs_runs_submit) | **POST** /2.1/jobs/runs/submit | Create and trigger a one-time run
[**jobs_update**](DefaultApi.md#jobs_update) | **POST** /2.1/jobs/update | Partially updates a job


# **jobs_create**
> JobsCreate200Response jobs_create(jobs_create_request)

Create a new job

Create a new job.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    jobs_create_request = databricks_jobs.JobsCreateRequest() # JobsCreateRequest | 

    try:
        # Create a new job
        api_response = api_instance.jobs_create(jobs_create_request)
        print("The response of DefaultApi->jobs_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_create_request** | [**JobsCreateRequest**](JobsCreateRequest.md)|  | 

### Return type

[**JobsCreate200Response**](JobsCreate200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job was created successfully |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_delete**
> object jobs_delete(jobs_delete_request)

Delete a job

Deletes a job.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    jobs_delete_request = databricks_jobs.JobsDeleteRequest() # JobsDeleteRequest | 

    try:
        # Delete a job
        api_response = api_instance.jobs_delete(jobs_delete_request)
        print("The response of DefaultApi->jobs_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_delete_request** | [**JobsDeleteRequest**](JobsDeleteRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job was deleted successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_get**
> JobsGet200Response jobs_get(job_id)

Get a single job

Retrieves the details for a single job.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    job_id = 11223344 # int | The canonical identifier of the job to retrieve information about. This field is required.

    try:
        # Get a single job
        api_response = api_instance.jobs_get(job_id)
        print("The response of DefaultApi->jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| The canonical identifier of the job to retrieve information about. This field is required. | 

### Return type

[**JobsGet200Response**](JobsGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job was retrieved successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_list**
> JobsList200Response jobs_list(limit=limit, offset=offset, name=name, expand_tasks=expand_tasks)

List all jobs

Retrieves a list of jobs.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    limit = 20 # int | The number of jobs to return. This value must be greater than 0 and less or equal to 25. The default value is 20. (optional) (default to 20)
    offset = 0 # int | The offset of the first job to return, relative to the most recently created job. (optional) (default to 0)
    name = 'A%20multitask%20job' # str | A filter on the list based on the exact (case insensitive) job name. (optional)
    expand_tasks = False # bool | Whether to include task and cluster details in the response. (optional) (default to False)

    try:
        # List all jobs
        api_response = api_instance.jobs_list(limit=limit, offset=offset, name=name, expand_tasks=expand_tasks)
        print("The response of DefaultApi->jobs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of jobs to return. This value must be greater than 0 and less or equal to 25. The default value is 20. | [optional] [default to 20]
 **offset** | **int**| The offset of the first job to return, relative to the most recently created job. | [optional] [default to 0]
 **name** | **str**| A filter on the list based on the exact (case insensitive) job name. | [optional] 
 **expand_tasks** | **bool**| Whether to include task and cluster details in the response. | [optional] [default to False]

### Return type

[**JobsList200Response**](JobsList200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs was retrieved successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_reset**
> object jobs_reset(jobs_reset_request)

Overwrites all settings for a job

Overwrites all the settings for a specific job. Use the Update endpoint to update job settings partially.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    jobs_reset_request = databricks_jobs.JobsResetRequest() # JobsResetRequest | 

    try:
        # Overwrites all settings for a job
        api_response = api_instance.jobs_reset(jobs_reset_request)
        print("The response of DefaultApi->jobs_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_reset_request** | [**JobsResetRequest**](JobsResetRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job was overwritten successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_run_now**
> JobsRunNow200Response jobs_run_now(jobs_run_now_request)

Trigger a new job run

Run a job and return the `run_id` of the triggered run.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    jobs_run_now_request = databricks_jobs.JobsRunNowRequest() # JobsRunNowRequest | 

    try:
        # Trigger a new job run
        api_response = api_instance.jobs_run_now(jobs_run_now_request)
        print("The response of DefaultApi->jobs_run_now:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_run_now: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_run_now_request** | [**JobsRunNowRequest**](JobsRunNowRequest.md)|  | 

### Return type

[**JobsRunNow200Response**](JobsRunNow200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run was started successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_runs_cancel**
> object jobs_runs_cancel(jobs_runs_cancel_request)

Cancel a job run

Cancels a job run. The run is canceled asynchronously, so it may still be running when this request completes.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    jobs_runs_cancel_request = databricks_jobs.JobsRunsCancelRequest() # JobsRunsCancelRequest | 

    try:
        # Cancel a job run
        api_response = api_instance.jobs_runs_cancel(jobs_runs_cancel_request)
        print("The response of DefaultApi->jobs_runs_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_runs_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_runs_cancel_request** | [**JobsRunsCancelRequest**](JobsRunsCancelRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run was cancelled successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_runs_cancel_all**
> object jobs_runs_cancel_all(jobs_runs_cancel_all_request)

Cancel all runs of a job

Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new runs from being started.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    jobs_runs_cancel_all_request = databricks_jobs.JobsRunsCancelAllRequest() # JobsRunsCancelAllRequest | 

    try:
        # Cancel all runs of a job
        api_response = api_instance.jobs_runs_cancel_all(jobs_runs_cancel_all_request)
        print("The response of DefaultApi->jobs_runs_cancel_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_runs_cancel_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_runs_cancel_all_request** | [**JobsRunsCancelAllRequest**](JobsRunsCancelAllRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All runs were cancelled successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_runs_delete**
> object jobs_runs_delete(jobs_runs_delete_request)

Delete a job run

Deletes a non-active run. Returns an error if the run is active.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    jobs_runs_delete_request = databricks_jobs.JobsRunsDeleteRequest() # JobsRunsDeleteRequest | 

    try:
        # Delete a job run
        api_response = api_instance.jobs_runs_delete(jobs_runs_delete_request)
        print("The response of DefaultApi->jobs_runs_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_runs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_runs_delete_request** | [**JobsRunsDeleteRequest**](JobsRunsDeleteRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run was deleted successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_runs_export**
> JobsRunsExport200Response jobs_runs_export(run_id, views_to_export=views_to_export)

Export and retrieve a job run

Export and retrieve the job run task.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    run_id = 455644833 # int | The canonical identifier for the run. This field is required.
    views_to_export = databricks_jobs.ViewsToExport() # ViewsToExport | Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE. (optional)

    try:
        # Export and retrieve a job run
        api_response = api_instance.jobs_runs_export(run_id, views_to_export=views_to_export)
        print("The response of DefaultApi->jobs_runs_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_runs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**| The canonical identifier for the run. This field is required. | 
 **views_to_export** | [**ViewsToExport**](.md)| Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE. | [optional] 

### Return type

[**JobsRunsExport200Response**](JobsRunsExport200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run was exported successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_runs_get**
> JobsRunsGet200Response jobs_runs_get(run_id, include_history=include_history)

Get a single job run

Retrieve the metadata of a run.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    run_id = 455644833 # int | The canonical identifier of the run for which to retrieve the metadata. This field is required.
    include_history = true # bool | Whether to include the repair history in the response. (optional)

    try:
        # Get a single job run
        api_response = api_instance.jobs_runs_get(run_id, include_history=include_history)
        print("The response of DefaultApi->jobs_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_runs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**| The canonical identifier of the run for which to retrieve the metadata. This field is required. | 
 **include_history** | **bool**| Whether to include the repair history in the response. | [optional] 

### Return type

[**JobsRunsGet200Response**](JobsRunsGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run was retrieved successfully |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_runs_get_output**
> JobsRunsGetOutput200Response jobs_runs_get_output(run_id)

Get the output for a single run

Retrieve the output and metadata of a single task run. When a notebook task returns a value through the dbutils.notebook.exit() call, you can use this endpoint to retrieve that value. Azure Databricks restricts this API to return the first 5 MB of the output. To return a larger result, you can store job results in a cloud storage service. This endpoint validates that the run_id parameter is valid and returns an HTTP status code 400 if the run_id parameter is invalid. Runs are automatically removed after 60 days. If you to want to reference them beyond 60 days, you must save old run results before they expire. To export using the UI, see Export job run results. To export using the Jobs API, see Runs export.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    run_id = 455644833 # int | The canonical identifier for the run. This field is required.

    try:
        # Get the output for a single run
        api_response = api_instance.jobs_runs_get_output(run_id)
        print("The response of DefaultApi->jobs_runs_get_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_runs_get_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**| The canonical identifier for the run. This field is required. | 

### Return type

[**JobsRunsGetOutput200Response**](JobsRunsGetOutput200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run output was retrieved successfully. |  -  |
**400** | A job run with multiple tasks was provided. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_runs_list**
> JobsRunsList200Response jobs_runs_list(active_only=active_only, completed_only=completed_only, job_id=job_id, offset=offset, limit=limit, run_type=run_type, expand_tasks=expand_tasks, start_time_from=start_time_from, start_time_to=start_time_to)

List runs for a job

List runs in descending order by start time.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    active_only = False # bool | If active_only is `true`, only active runs are included in the results; otherwise, lists both active and completed runs. An active run is a run in the `PENDING`, `RUNNING`, or `TERMINATING`. This field cannot be `true` when completed_only is `true`. (optional) (default to False)
    completed_only = False # bool | If completed_only is `true`, only completed runs are included in the results; otherwise, lists both active and completed runs. This field cannot be `true` when active_only is `true`. (optional) (default to False)
    job_id = 11223344 # int | The job for which to list runs. If omitted, the Jobs service lists runs from all jobs. (optional)
    offset = 0 # int | The offset of the first run to return, relative to the most recent run. (optional) (default to 0)
    limit = 25 # int | The number of runs to return. This value must be greater than 0 and less than 25\\. The default value is 25\\. If a request specifies a limit of 0, the service instead uses the maximum limit. (optional) (default to 25)
    run_type = 'JOB_RUN' # str | The type of runs to return. For a description of run types, see [Run](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsRunsGet). (optional)
    expand_tasks = False # bool | Whether to include task and cluster details in the response. (optional) (default to False)
    start_time_from = 1642521600000 # int | Show runs that started _at or after_ this value. The value must be a UTC timestamp in milliseconds. Can be combined with _start_time_to_ to filter by a time range. (optional)
    start_time_to = 1642608000000 # int | Show runs that started _at or before_ this value. The value must be a UTC timestamp in milliseconds. Can be combined with _start_time_from_ to filter by a time range. (optional)

    try:
        # List runs for a job
        api_response = api_instance.jobs_runs_list(active_only=active_only, completed_only=completed_only, job_id=job_id, offset=offset, limit=limit, run_type=run_type, expand_tasks=expand_tasks, start_time_from=start_time_from, start_time_to=start_time_to)
        print("The response of DefaultApi->jobs_runs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_runs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active_only** | **bool**| If active_only is &#x60;true&#x60;, only active runs are included in the results; otherwise, lists both active and completed runs. An active run is a run in the &#x60;PENDING&#x60;, &#x60;RUNNING&#x60;, or &#x60;TERMINATING&#x60;. This field cannot be &#x60;true&#x60; when completed_only is &#x60;true&#x60;. | [optional] [default to False]
 **completed_only** | **bool**| If completed_only is &#x60;true&#x60;, only completed runs are included in the results; otherwise, lists both active and completed runs. This field cannot be &#x60;true&#x60; when active_only is &#x60;true&#x60;. | [optional] [default to False]
 **job_id** | **int**| The job for which to list runs. If omitted, the Jobs service lists runs from all jobs. | [optional] 
 **offset** | **int**| The offset of the first run to return, relative to the most recent run. | [optional] [default to 0]
 **limit** | **int**| The number of runs to return. This value must be greater than 0 and less than 25\\. The default value is 25\\. If a request specifies a limit of 0, the service instead uses the maximum limit. | [optional] [default to 25]
 **run_type** | **str**| The type of runs to return. For a description of run types, see [Run](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsRunsGet). | [optional] 
 **expand_tasks** | **bool**| Whether to include task and cluster details in the response. | [optional] [default to False]
 **start_time_from** | **int**| Show runs that started _at or after_ this value. The value must be a UTC timestamp in milliseconds. Can be combined with _start_time_to_ to filter by a time range. | [optional] 
 **start_time_to** | **int**| Show runs that started _at or before_ this value. The value must be a UTC timestamp in milliseconds. Can be combined with _start_time_from_ to filter by a time range. | [optional] 

### Return type

[**JobsRunsList200Response**](JobsRunsList200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of runs was retrieved successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_runs_repair**
> JobsRunsRepair200Response jobs_runs_repair(jobs_runs_repair_request)

Repair a job run

Re-run one or more tasks. Tasks are re-run as part of the original job run, use the current job and task settings, and can be viewed in the history for the original job run.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    jobs_runs_repair_request = databricks_jobs.JobsRunsRepairRequest() # JobsRunsRepairRequest | 

    try:
        # Repair a job run
        api_response = api_instance.jobs_runs_repair(jobs_runs_repair_request)
        print("The response of DefaultApi->jobs_runs_repair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_runs_repair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_runs_repair_request** | [**JobsRunsRepairRequest**](JobsRunsRepairRequest.md)|  | 

### Return type

[**JobsRunsRepair200Response**](JobsRunsRepair200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run repair was initiated. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_runs_submit**
> JobsRunsSubmit200Response jobs_runs_submit(jobs_runs_submit_request)

Create and trigger a one-time run

Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job. Use the `jobs/runs/get` API to check the run state after the job is submitted.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    jobs_runs_submit_request = databricks_jobs.JobsRunsSubmitRequest() # JobsRunsSubmitRequest | 

    try:
        # Create and trigger a one-time run
        api_response = api_instance.jobs_runs_submit(jobs_runs_submit_request)
        print("The response of DefaultApi->jobs_runs_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_runs_submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_runs_submit_request** | [**JobsRunsSubmitRequest**](JobsRunsSubmitRequest.md)|  | 

### Return type

[**JobsRunsSubmit200Response**](JobsRunsSubmit200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run was created and started successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_update**
> object jobs_update(jobs_update_request)

Partially updates a job

Add, update, or remove specific settings of an existing job. Use the Reset endpoint to overwrite all job settings.

### Example

* Bearer (api_token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import databricks_jobs
from databricks_jobs.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with databricks_jobs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databricks_jobs.DefaultApi(api_client)
    jobs_update_request = databricks_jobs.JobsUpdateRequest() # JobsUpdateRequest | 

    try:
        # Partially updates a job
        api_response = api_instance.jobs_update(jobs_update_request)
        print("The response of DefaultApi->jobs_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_update_request** | [**JobsUpdateRequest**](JobsUpdateRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job was updated successfully. |  -  |
**400** | The request was malformed. See JSON response for error details. |  -  |
**401** | The request was unauthorized. |  -  |
**500** | The request was not handled correctly due to a server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

