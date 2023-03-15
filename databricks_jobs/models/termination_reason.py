from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.termination_code import TerminationCode
from ..models.termination_type import TerminationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameter_pair import ParameterPair


T = TypeVar("T", bound="TerminationReason")


@attr.s(auto_attribs=True)
class TerminationReason:
    """
    Attributes:
        code (Union[Unset, TerminationCode]): * USER_REQUEST: A user terminated the cluster directly. Parameters should
            include a `username` field that indicates the specific user who terminated the cluster.
            * JOB_FINISHED: The cluster was launched by a job, and terminated when the job completed.
            * INACTIVITY: The cluster was terminated since it was idle.
            * CLOUD_PROVIDER_SHUTDOWN: The instance that hosted the Spark driver was terminated by the cloud provider.
            * COMMUNICATION_LOST: Azure Databricks lost connection to services on the driver instance. For example, this can
            happen when problems arise in cloud networking infrastructure, or when the instance itself becomes unhealthy.
            * CLOUD_PROVIDER_LAUNCH_FAILURE: Azure Databricks experienced a cloud provider failure when requesting instances
            to launch clusters.
            * SPARK_STARTUP_FAILURE: The cluster failed to initialize. Possible reasons may include failure to create the
            environment for Spark or issues launching the Spark master and worker processes.
            * INVALID_ARGUMENT: Cannot launch the cluster because the user specified an invalid argument. For example, the
            user might specify an invalid runtime version for the cluster.
            * UNEXPECTED_LAUNCH_FAILURE: While launching this cluster, Databricks failed to complete critical setup steps,
            terminating the cluster.
            * INTERNAL_ERROR: Azure Databricks encountered an unexpected error that forced the running cluster to be
            terminated. Contact Databricks support for additional details.
            * SPARK_ERROR: The Spark driver failed to start. Possible reasons may include incompatible libraries and
            initialization scripts that corrupted the Spark container.
            * METASTORE_COMPONENT_UNHEALTHY: The cluster failed to start because the external metastore could not be
            reached. Refer to [Troubleshooting](https://docs.microsoft.com/azure/databricks/data/metastores/external-hive-
            metastore#troubleshooting).
            * DBFS_COMPONENT_UNHEALTHY: The cluster failed to start because Databricks File System (DBFS) could not be
            reached.
            * AZURE_RESOURCE_PROVIDER_THROTTLING: Azure Databricks reached the Azure Resource Provider request limit.
            Specifically, the API request rate to the specific resource type (compute, network, etc.) can’t exceed the
            limit. Retry might help to resolve the issue. For further information, see
            [https://docs.microsoft.com/azure/virtual-machines/troubleshooting/troubleshooting-throttling-
            errors](https://docs.microsoft.com/azure/virtual-machines/troubleshooting/troubleshooting-throttling-errors).
            * AZURE_RESOURCE_MANAGER_THROTTLING: Azure Databricks reached the Azure Resource Manager request limit which
            prevents the Azure SDK from issuing any read or write request to the Azure Resource Manager. The request limit
            is applied to each subscription every hour. Retry after an hour or changing to a smaller cluster size might help
            to resolve the issue. For further information, see [https://docs.microsoft.com/azure/azure-resource-
            manager/resource-manager-request-limits](https://docs.microsoft.com/azure/azure-resource-manager/resource-
            manager-request-limits).
            * NETWORK_CONFIGURATION_FAILURE: The cluster was terminated due to an error in the network configuration. For
            example, a workspace with VNet injection had incorrect DNS settings that blocked access to worker artifacts.
            * DRIVER_UNREACHABLE: Azure Databricks was not able to access the Spark driver, because it was not reachable.
            * DRIVER_UNRESPONSIVE: Azure Databricks was not able to access the Spark driver, because it was unresponsive.
            * INSTANCE_UNREACHABLE: Azure Databricks was not able to access instances in order to start the cluster. This
            can be a transient networking issue. If the problem persists, this usually indicates a networking environment
            misconfiguration.
            * CONTAINER_LAUNCH_FAILURE: Azure Databricks was unable to launch containers on worker nodes for the cluster.
            Have your admin check your network configuration.
            * INSTANCE_POOL_CLUSTER_FAILURE: Pool backed cluster specific failure. Refer to
            [Pools](https://docs.microsoft.com/azure/databricks/clusters/pools) for details.
            * REQUEST_REJECTED: Azure Databricks cannot handle the request at this moment. Try again later and contact
            Databricks if the problem persists.
            * INIT_SCRIPT_FAILURE: Azure Databricks cannot load and run a cluster-scoped init script on one of the cluster’s
            nodes, or the init script terminates with a non-zero exit code. Refer to [Init script
            logs](https://docs.microsoft.com/azure/databricks/clusters/init-scripts#init-script-log).
            * TRIAL_EXPIRED: The Databricks trial subscription expired.
        type (Union[Unset, TerminationType]): * SUCCESS: Termination succeeded.
            * CLIENT_ERROR: Non-retriable. Client must fix parameters before reattempting the cluster creation.
            * SERVICE_FAULT: Databricks service issue. Client can retry.
            * CLOUD_FAILURECloud provider infrastructure issue. Client can retry after the underlying issue is resolved.
        parameters (Union[Unset, ParameterPair]): An object with additional information about why a cluster was
            terminated. The object keys are one of `TerminationParameter` and the value is the termination information.
    """

    code: Union[Unset, TerminationCode] = UNSET
    type: Union[Unset, TerminationType] = UNSET
    parameters: Union[Unset, "ParameterPair"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if type is not UNSET:
            field_dict["type"] = type
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parameter_pair import ParameterPair

        d = src_dict.copy()
        _code = d.pop("code", UNSET)
        code: Union[Unset, TerminationCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = TerminationCode(_code)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TerminationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TerminationType(_type)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, ParameterPair]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ParameterPair.from_dict(_parameters)

        termination_reason = cls(
            code=code,
            type=type,
            parameters=parameters,
        )

        termination_reason.additional_properties = d
        return termination_reason

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
