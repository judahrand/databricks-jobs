# ClusterEventType

* `CREATING`: Indicates that the cluster is being created. * `DID_NOT_EXPAND_DISK`: Indicates that a disk is low on space, but adding disks would put it over the max capacity. * `EXPANDED_DISK`: Indicates that a disk was low on space and the disks were expanded. * `FAILED_TO_EXPAND_DISK`: Indicates that a disk was low on space and disk space could not be expanded. * `INIT_SCRIPTS_STARTING`: Indicates that the cluster scoped init script has started. * `INIT_SCRIPTS_FINISHED`: Indicates that the cluster scoped init script has finished. * `STARTING`: Indicates that the cluster is being started. * `RESTARTING`: Indicates that the cluster is being started. * `TERMINATING`: Indicates that the cluster is being terminated. * `EDITED`: Indicates that the cluster has been edited. * `RUNNING`: Indicates the cluster has finished being created. Includes the number of nodes in the cluster and a failure reason if some nodes could not be acquired. * `RESIZING`: Indicates a change in the target size of the cluster (upsize or downsize). * `UPSIZE_COMPLETED`: Indicates that nodes finished being added to the cluster. Includes the number of nodes in the cluster and a failure reason if some nodes could not be acquired. * `NODES_LOST`: Indicates that some nodes were lost from the cluster. * `DRIVER_HEALTHY`: Indicates that the driver is healthy and the cluster is ready for use. * `DRIVER_UNAVAILABLE`: Indicates that the driver is unavailable. * `SPARK_EXCEPTION`: Indicates that a Spark exception was thrown from the driver. * `DRIVER_NOT_RESPONDING`: Indicates that the driver is up but is not responsive, likely due to GC. * `DBFS_DOWN`: Indicates that the driver is up but DBFS is down. * `METASTORE_DOWN`: Indicates that the driver is up but the metastore is down. * `NODE_BLACKLISTED`: Indicates that a node is not allowed by Spark. * `PINNED`: Indicates that the cluster was pinned. * `UNPINNED`: Indicates that the cluster was unpinned.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

