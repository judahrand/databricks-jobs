from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_cloud_provider_node_info import ClusterCloudProviderNodeInfo


T = TypeVar("T", bound="NodeType")


@attr.s(auto_attribs=True)
class NodeType:
    """
    Attributes:
        node_type_id (str): Unique identifier for this node type. This field is required.
        memory_mb (int): Memory (in MB) available for this node type. This field is required.
        description (str): A string description associated with this node type. This field is required.
        instance_type_id (str): An identifier for the type of hardware that this node runs on. This field is required.
        num_cores (Union[Unset, float]): Number of CPU cores available for this node type. This can be fractional if the
            number of cores on a machine instance is not divisible by the number of Spark nodes on that machine. This field
            is required.
        is_deprecated (Union[Unset, bool]): Whether the node type is deprecated. Non-deprecated node types offer greater
            performance.
        node_info (Union[Unset, ClusterCloudProviderNodeInfo]):
    """

    node_type_id: str
    memory_mb: int
    description: str
    instance_type_id: str
    num_cores: Union[Unset, float] = UNSET
    is_deprecated: Union[Unset, bool] = UNSET
    node_info: Union[Unset, "ClusterCloudProviderNodeInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_type_id = self.node_type_id
        memory_mb = self.memory_mb
        description = self.description
        instance_type_id = self.instance_type_id
        num_cores = self.num_cores
        is_deprecated = self.is_deprecated
        node_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.node_info, Unset):
            node_info = self.node_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_type_id": node_type_id,
                "memory_mb": memory_mb,
                "description": description,
                "instance_type_id": instance_type_id,
            }
        )
        if num_cores is not UNSET:
            field_dict["num_cores"] = num_cores
        if is_deprecated is not UNSET:
            field_dict["is_deprecated"] = is_deprecated
        if node_info is not UNSET:
            field_dict["node_info"] = node_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cluster_cloud_provider_node_info import ClusterCloudProviderNodeInfo

        d = src_dict.copy()
        node_type_id = d.pop("node_type_id")

        memory_mb = d.pop("memory_mb")

        description = d.pop("description")

        instance_type_id = d.pop("instance_type_id")

        num_cores = d.pop("num_cores", UNSET)

        is_deprecated = d.pop("is_deprecated", UNSET)

        _node_info = d.pop("node_info", UNSET)
        node_info: Union[Unset, ClusterCloudProviderNodeInfo]
        if isinstance(_node_info, Unset):
            node_info = UNSET
        else:
            node_info = ClusterCloudProviderNodeInfo.from_dict(_node_info)

        node_type = cls(
            node_type_id=node_type_id,
            memory_mb=memory_mb,
            description=description,
            instance_type_id=instance_type_id,
            num_cores=num_cores,
            is_deprecated=is_deprecated,
            node_info=node_info,
        )

        node_type.additional_properties = d
        return node_type

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
