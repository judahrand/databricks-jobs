# databricks_jobs.model.termination_type.TerminationType

* SUCCESS: Termination succeeded. * CLIENT_ERROR: Non-retriable. Client must fix parameters before reattempting the cluster creation. * SERVICE_FAULT: Databricks service issue. Client can retry. * CLOUD_FAILURECloud provider infrastructure issue. Client can retry after the underlying issue is resolved. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | * SUCCESS: Termination succeeded. * CLIENT_ERROR: Non-retriable. Client must fix parameters before reattempting the cluster creation. * SERVICE_FAULT: Databricks service issue. Client can retry. * CLOUD_FAILURECloud provider infrastructure issue. Client can retry after the underlying issue is resolved.  | must be one of ["SUCCESS", "CLIENT_ERROR", "SERVICE_FAULT", "CLOUD_FAILURE", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

