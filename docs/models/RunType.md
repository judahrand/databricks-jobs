# databricks_jobs.model.run_type.RunType

The type of the run. * `JOB_RUN` \\- Normal job run. A run created with [Run now](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsRunNow). * `WORKFLOW_RUN` \\- Workflow run. A run created with [dbutils.notebook.run](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-workflow). * `SUBMIT_RUN` \\- Submit run. A run created with [Run Submit](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsRunsSubmit).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The type of the run. * &#x60;JOB_RUN&#x60; \\- Normal job run. A run created with [Run now](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsRunNow). * &#x60;WORKFLOW_RUN&#x60; \\- Workflow run. A run created with [dbutils.notebook.run](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-workflow). * &#x60;SUBMIT_RUN&#x60; \\- Submit run. A run created with [Run Submit](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsRunsSubmit). | must be one of ["JOB_RUN", "WORKFLOW_RUN", "SUBMIT_RUN", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

