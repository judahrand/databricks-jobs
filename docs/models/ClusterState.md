# databricks_jobs.model.cluster_state.ClusterState

* PENDING: Indicates that a cluster is in the process of being created. * RUNNING: Indicates that a cluster has been started and is ready for use. * RESTARTING: Indicates that a cluster is in the process of restarting. * RESIZING: Indicates that a cluster is in the process of adding or removing nodes. * TERMINATING: Indicates that a cluster is in the process of being destroyed. * TERMINATED: Indicates that a cluster has been successfully destroyed. * ERROR: This state is no longer used. It was used to indicate a cluster that failed to be created. `TERMINATING` and `TERMINATED` are used instead. * UNKNOWN: Indicates that a cluster is in an unknown state. A cluster should never be in this state. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | * PENDING: Indicates that a cluster is in the process of being created. * RUNNING: Indicates that a cluster has been started and is ready for use. * RESTARTING: Indicates that a cluster is in the process of restarting. * RESIZING: Indicates that a cluster is in the process of adding or removing nodes. * TERMINATING: Indicates that a cluster is in the process of being destroyed. * TERMINATED: Indicates that a cluster has been successfully destroyed. * ERROR: This state is no longer used. It was used to indicate a cluster that failed to be created. &#x60;TERMINATING&#x60; and &#x60;TERMINATED&#x60; are used instead. * UNKNOWN: Indicates that a cluster is in an unknown state. A cluster should never be in this state.  | must be one of ["PENDING", "RUNNING", "RESTARTING", "RESIZING", "TERMINATING", "TERMINATED", "ERROR", "UNKNOWN", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

