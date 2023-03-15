from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cluster_cloud_provider_node_status import ClusterCloudProviderNodeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterCloudProviderNodeInfo")


@attr.s(auto_attribs=True)
class ClusterCloudProviderNodeInfo:
    """
    Attributes:
        status (Union[Unset, ClusterCloudProviderNodeStatus]): * NotEnabledOnSubscription: Node type not available for
            subscription.
            * NotAvailableInRegion: Node type not available in region.
        available_core_quota (Union[Unset, int]): Available CPU core quota.
        total_core_quota (Union[Unset, int]): Total CPU core quota.
    """

    status: Union[Unset, ClusterCloudProviderNodeStatus] = UNSET
    available_core_quota: Union[Unset, int] = UNSET
    total_core_quota: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        available_core_quota = self.available_core_quota
        total_core_quota = self.total_core_quota

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if available_core_quota is not UNSET:
            field_dict["available_core_quota"] = available_core_quota
        if total_core_quota is not UNSET:
            field_dict["total_core_quota"] = total_core_quota

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, ClusterCloudProviderNodeStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ClusterCloudProviderNodeStatus(_status)

        available_core_quota = d.pop("available_core_quota", UNSET)

        total_core_quota = d.pop("total_core_quota", UNSET)

        cluster_cloud_provider_node_info = cls(
            status=status,
            available_core_quota=available_core_quota,
            total_core_quota=total_core_quota,
        )

        cluster_cloud_provider_node_info.additional_properties = d
        return cluster_cloud_provider_node_info

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
