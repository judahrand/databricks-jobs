# LibraryInstallStatus

* `PENDING`: No action has yet been taken to install the library. This state should be very short lived. * `RESOLVING`: Metadata necessary to install the library is being retrieved from the provided repository. For Jar, Egg, and Whl libraries, this step is a no-op. * `INSTALLING`: The library is actively being installed, either by adding resources to Spark or executing system commands inside the Spark nodes. * `INSTALLED`: The library has been successfully instally. * `SKIPPED`: Installation on a Databricks Runtime 7.0 or above cluster was skipped due to Scala version incompatibility. * `FAILED`: Some step in installation failed. More information can be found in the messages field. * `UNINSTALL_ON_RESTART`: The library has been marked for removal. Libraries can be removed only when clusters are restarted, so libraries that enter this state remains until the cluster is restarted.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


