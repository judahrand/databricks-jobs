from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TerminationParameter")


@attr.s(auto_attribs=True)
class TerminationParameter:
    """
    Attributes:
        username (Union[Unset, str]): The username of the user who terminated the cluster.
        azure_error_code (Union[Unset, str]): The Azure provided error code describing why cluster nodes could not be
            provisioned. For reference, see: [https://docs.microsoft.com/azure/virtual-machines/windows/error-
            messages](https://docs.microsoft.com/azure/virtual-machines/windows/error-messages).
        azure_error_message (Union[Unset, str]): Human-readable context of various failures from Azure. This field is
            unstructured, and its exact format is subject to change.
        databricks_error_message (Union[Unset, str]): Additional context that may explain the reason for cluster
            termination. This field is unstructured, and its exact format is subject to change.
        inactivity_duration_min (Union[Unset, str]): An idle cluster was shut down after being inactive for this
            duration.
        instance_id (Union[Unset, str]): The ID of the instance that was hosting the Spark driver.
        instance_pool_id (Union[Unset, str]): The ID of the instance pool the cluster is using.
        instance_pool_error_code (Union[Unset, str]): The [error code](https://docs.microsoft.com/azure/databricks/dev-
            tools/api/latest/clusters#clusterterminationreasonpoolclusterterminationcode) for cluster failures specific to a
            pool.
    """

    username: Union[Unset, str] = UNSET
    azure_error_code: Union[Unset, str] = UNSET
    azure_error_message: Union[Unset, str] = UNSET
    databricks_error_message: Union[Unset, str] = UNSET
    inactivity_duration_min: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    instance_pool_id: Union[Unset, str] = UNSET
    instance_pool_error_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        azure_error_code = self.azure_error_code
        azure_error_message = self.azure_error_message
        databricks_error_message = self.databricks_error_message
        inactivity_duration_min = self.inactivity_duration_min
        instance_id = self.instance_id
        instance_pool_id = self.instance_pool_id
        instance_pool_error_code = self.instance_pool_error_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if azure_error_code is not UNSET:
            field_dict["azure_error_code"] = azure_error_code
        if azure_error_message is not UNSET:
            field_dict["azure_error_message"] = azure_error_message
        if databricks_error_message is not UNSET:
            field_dict["databricks_error_message"] = databricks_error_message
        if inactivity_duration_min is not UNSET:
            field_dict["inactivity_duration_min"] = inactivity_duration_min
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if instance_pool_id is not UNSET:
            field_dict["instance_pool_id"] = instance_pool_id
        if instance_pool_error_code is not UNSET:
            field_dict["instance_pool_error_code"] = instance_pool_error_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        azure_error_code = d.pop("azure_error_code", UNSET)

        azure_error_message = d.pop("azure_error_message", UNSET)

        databricks_error_message = d.pop("databricks_error_message", UNSET)

        inactivity_duration_min = d.pop("inactivity_duration_min", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        instance_pool_id = d.pop("instance_pool_id", UNSET)

        instance_pool_error_code = d.pop("instance_pool_error_code", UNSET)

        termination_parameter = cls(
            username=username,
            azure_error_code=azure_error_code,
            azure_error_message=azure_error_message,
            databricks_error_message=databricks_error_message,
            inactivity_duration_min=inactivity_duration_min,
            instance_id=instance_id,
            instance_pool_id=instance_pool_id,
            instance_pool_error_code=instance_pool_error_code,
        )

        termination_parameter.additional_properties = d
        return termination_parameter

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
