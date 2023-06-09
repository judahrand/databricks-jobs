# databricks-jobs
The Jobs API allows you to create, edit, and delete jobs.
You should never hard code secrets or store them in plain text. Use the [Secrets API](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/secrets) to manage secrets in the [Databricks CLI](https://docs.microsoft.com/azure/databricks/dev-tools/cli/index). Use the [Secrets utility](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-secrets) to reference secrets in notebooks and jobs.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonNextgenClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import databricks_jobs
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import databricks_jobs
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
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
    except ApiException as e:
        print("Exception when calling DefaultApi->jobs_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://<databricks-instance>/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**jobs_create**](docs/DefaultApi.md#jobs_create) | **POST** /2.1/jobs/create | Create a new job
*DefaultApi* | [**jobs_delete**](docs/DefaultApi.md#jobs_delete) | **POST** /2.1/jobs/delete | Delete a job
*DefaultApi* | [**jobs_get**](docs/DefaultApi.md#jobs_get) | **GET** /2.1/jobs/get | Get a single job
*DefaultApi* | [**jobs_list**](docs/DefaultApi.md#jobs_list) | **GET** /2.1/jobs/list | List all jobs
*DefaultApi* | [**jobs_reset**](docs/DefaultApi.md#jobs_reset) | **POST** /2.1/jobs/reset | Overwrites all settings for a job
*DefaultApi* | [**jobs_run_now**](docs/DefaultApi.md#jobs_run_now) | **POST** /2.1/jobs/run-now | Trigger a new job run
*DefaultApi* | [**jobs_runs_cancel**](docs/DefaultApi.md#jobs_runs_cancel) | **POST** /2.1/jobs/runs/cancel | Cancel a job run
*DefaultApi* | [**jobs_runs_cancel_all**](docs/DefaultApi.md#jobs_runs_cancel_all) | **POST** /2.1/jobs/runs/cancel-all | Cancel all runs of a job
*DefaultApi* | [**jobs_runs_delete**](docs/DefaultApi.md#jobs_runs_delete) | **POST** /2.1/jobs/runs/delete | Delete a job run
*DefaultApi* | [**jobs_runs_export**](docs/DefaultApi.md#jobs_runs_export) | **GET** /2.0/jobs/runs/export | Export and retrieve a job run
*DefaultApi* | [**jobs_runs_get**](docs/DefaultApi.md#jobs_runs_get) | **GET** /2.1/jobs/runs/get | Get a single job run
*DefaultApi* | [**jobs_runs_get_output**](docs/DefaultApi.md#jobs_runs_get_output) | **GET** /2.1/jobs/runs/get-output | Get the output for a single run
*DefaultApi* | [**jobs_runs_list**](docs/DefaultApi.md#jobs_runs_list) | **GET** /2.1/jobs/runs/list | List runs for a job
*DefaultApi* | [**jobs_runs_repair**](docs/DefaultApi.md#jobs_runs_repair) | **POST** /2.1/jobs/runs/repair | Repair a job run
*DefaultApi* | [**jobs_runs_submit**](docs/DefaultApi.md#jobs_runs_submit) | **POST** /2.1/jobs/runs/submit | Create and trigger a one-time run
*DefaultApi* | [**jobs_update**](docs/DefaultApi.md#jobs_update) | **POST** /2.1/jobs/update | Partially updates a job


## Documentation For Models

 - [AccessControlList](docs/AccessControlList.md)
 - [AccessControlRequest](docs/AccessControlRequest.md)
 - [AccessControlRequestForGroup](docs/AccessControlRequestForGroup.md)
 - [AccessControlRequestForServicePrincipal](docs/AccessControlRequestForServicePrincipal.md)
 - [AccessControlRequestForUser](docs/AccessControlRequestForUser.md)
 - [Adlsgen2Info](docs/Adlsgen2Info.md)
 - [AutoScale](docs/AutoScale.md)
 - [AwsAttributes](docs/AwsAttributes.md)
 - [AzureAttributes](docs/AzureAttributes.md)
 - [CanManage](docs/CanManage.md)
 - [CanManageRun](docs/CanManageRun.md)
 - [CanView](docs/CanView.md)
 - [ClusterAttributes](docs/ClusterAttributes.md)
 - [ClusterCloudProviderNodeInfo](docs/ClusterCloudProviderNodeInfo.md)
 - [ClusterCloudProviderNodeStatus](docs/ClusterCloudProviderNodeStatus.md)
 - [ClusterEvent](docs/ClusterEvent.md)
 - [ClusterEventType](docs/ClusterEventType.md)
 - [ClusterInfo](docs/ClusterInfo.md)
 - [ClusterInstance](docs/ClusterInstance.md)
 - [ClusterLibraryStatuses](docs/ClusterLibraryStatuses.md)
 - [ClusterLogConf](docs/ClusterLogConf.md)
 - [ClusterSize](docs/ClusterSize.md)
 - [ClusterSource](docs/ClusterSource.md)
 - [ClusterSpec](docs/ClusterSpec.md)
 - [ClusterState](docs/ClusterState.md)
 - [CronSchedule](docs/CronSchedule.md)
 - [DbfsStorageInfo](docs/DbfsStorageInfo.md)
 - [DbtOutput](docs/DbtOutput.md)
 - [DbtTask](docs/DbtTask.md)
 - [DockerBasicAuth](docs/DockerBasicAuth.md)
 - [DockerImage](docs/DockerImage.md)
 - [Error](docs/Error.md)
 - [EventDetails](docs/EventDetails.md)
 - [FileStorageInfo](docs/FileStorageInfo.md)
 - [GcpAttributes](docs/GcpAttributes.md)
 - [GitBranchSource](docs/GitBranchSource.md)
 - [GitCommitSource](docs/GitCommitSource.md)
 - [GitProvider](docs/GitProvider.md)
 - [GitSnapshot](docs/GitSnapshot.md)
 - [GitSource](docs/GitSource.md)
 - [GitTagSource](docs/GitTagSource.md)
 - [InitScriptInfo](docs/InitScriptInfo.md)
 - [IsOwner](docs/IsOwner.md)
 - [Job](docs/Job.md)
 - [JobCluster](docs/JobCluster.md)
 - [JobEmailNotifications](docs/JobEmailNotifications.md)
 - [JobSettings](docs/JobSettings.md)
 - [JobTask](docs/JobTask.md)
 - [JobTaskSettings](docs/JobTaskSettings.md)
 - [JobsCreate200Response](docs/JobsCreate200Response.md)
 - [JobsCreateRequest](docs/JobsCreateRequest.md)
 - [JobsDeleteRequest](docs/JobsDeleteRequest.md)
 - [JobsGet200Response](docs/JobsGet200Response.md)
 - [JobsList200Response](docs/JobsList200Response.md)
 - [JobsResetRequest](docs/JobsResetRequest.md)
 - [JobsRunNow200Response](docs/JobsRunNow200Response.md)
 - [JobsRunNowRequest](docs/JobsRunNowRequest.md)
 - [JobsRunsCancelAllRequest](docs/JobsRunsCancelAllRequest.md)
 - [JobsRunsCancelRequest](docs/JobsRunsCancelRequest.md)
 - [JobsRunsDeleteRequest](docs/JobsRunsDeleteRequest.md)
 - [JobsRunsExport200Response](docs/JobsRunsExport200Response.md)
 - [JobsRunsGet200Response](docs/JobsRunsGet200Response.md)
 - [JobsRunsGetOutput200Response](docs/JobsRunsGetOutput200Response.md)
 - [JobsRunsList200Response](docs/JobsRunsList200Response.md)
 - [JobsRunsRepair200Response](docs/JobsRunsRepair200Response.md)
 - [JobsRunsRepairRequest](docs/JobsRunsRepairRequest.md)
 - [JobsRunsSubmit200Response](docs/JobsRunsSubmit200Response.md)
 - [JobsRunsSubmitRequest](docs/JobsRunsSubmitRequest.md)
 - [JobsUpdateRequest](docs/JobsUpdateRequest.md)
 - [Library](docs/Library.md)
 - [LibraryFullStatus](docs/LibraryFullStatus.md)
 - [LibraryInstallStatus](docs/LibraryInstallStatus.md)
 - [ListOrder](docs/ListOrder.md)
 - [LogSyncStatus](docs/LogSyncStatus.md)
 - [MavenLibrary](docs/MavenLibrary.md)
 - [NewCluster](docs/NewCluster.md)
 - [NewTaskCluster](docs/NewTaskCluster.md)
 - [NodeType](docs/NodeType.md)
 - [NotebookOutput](docs/NotebookOutput.md)
 - [NotebookTask](docs/NotebookTask.md)
 - [PermissionLevel](docs/PermissionLevel.md)
 - [PermissionLevelForGroup](docs/PermissionLevelForGroup.md)
 - [PipelineTask](docs/PipelineTask.md)
 - [PoolClusterTerminationCode](docs/PoolClusterTerminationCode.md)
 - [PythonPyPiLibrary](docs/PythonPyPiLibrary.md)
 - [PythonWheelTask](docs/PythonWheelTask.md)
 - [RCranLibrary](docs/RCranLibrary.md)
 - [RepairHistory](docs/RepairHistory.md)
 - [RepairHistoryItem](docs/RepairHistoryItem.md)
 - [RepairRunInput](docs/RepairRunInput.md)
 - [ResizeCause](docs/ResizeCause.md)
 - [Run](docs/Run.md)
 - [RunLifeCycleState](docs/RunLifeCycleState.md)
 - [RunNowInput](docs/RunNowInput.md)
 - [RunParameters](docs/RunParameters.md)
 - [RunParametersPipelineParams](docs/RunParametersPipelineParams.md)
 - [RunResultState](docs/RunResultState.md)
 - [RunState](docs/RunState.md)
 - [RunSubmitSettings](docs/RunSubmitSettings.md)
 - [RunSubmitTaskSettings](docs/RunSubmitTaskSettings.md)
 - [RunTask](docs/RunTask.md)
 - [RunType](docs/RunType.md)
 - [S3StorageInfo](docs/S3StorageInfo.md)
 - [SparkJarTask](docs/SparkJarTask.md)
 - [SparkNode](docs/SparkNode.md)
 - [SparkNodeAwsAttributes](docs/SparkNodeAwsAttributes.md)
 - [SparkPythonTask](docs/SparkPythonTask.md)
 - [SparkSubmitTask](docs/SparkSubmitTask.md)
 - [SparkVersion](docs/SparkVersion.md)
 - [SqlAlertOutput](docs/SqlAlertOutput.md)
 - [SqlDashboardOutput](docs/SqlDashboardOutput.md)
 - [SqlDashboardWidgetOutput](docs/SqlDashboardWidgetOutput.md)
 - [SqlOutput](docs/SqlOutput.md)
 - [SqlOutputError](docs/SqlOutputError.md)
 - [SqlQueryOutput](docs/SqlQueryOutput.md)
 - [SqlStatementOutput](docs/SqlStatementOutput.md)
 - [SqlTask](docs/SqlTask.md)
 - [SqlTaskAlert](docs/SqlTaskAlert.md)
 - [SqlTaskDashboard](docs/SqlTaskDashboard.md)
 - [SqlTaskQuery](docs/SqlTaskQuery.md)
 - [TaskDependenciesInner](docs/TaskDependenciesInner.md)
 - [TaskSparkSubmitTask](docs/TaskSparkSubmitTask.md)
 - [TerminationCode](docs/TerminationCode.md)
 - [TerminationParameter](docs/TerminationParameter.md)
 - [TerminationReason](docs/TerminationReason.md)
 - [TerminationType](docs/TerminationType.md)
 - [TriggerType](docs/TriggerType.md)
 - [ViewItem](docs/ViewItem.md)
 - [ViewType](docs/ViewType.md)
 - [ViewsToExport](docs/ViewsToExport.md)
 - [WebhookNotifications](docs/WebhookNotifications.md)
 - [WebhookNotificationsOnStartInner](docs/WebhookNotificationsOnStartInner.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (api_token)


## Author




