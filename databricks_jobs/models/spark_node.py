from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SparkNode")


@attr.s(auto_attribs=True)
class SparkNode:
    """
    Attributes:
        private_ip (Union[Unset, str]): Private IP address (typically a 10.x.x.x address) of the Spark node. This is
            different from the private IP address of the host instance.
        public_dns (Union[Unset, str]): Public DNS address of this node. This address can be used to access the Spark
            JDBC server on the driver node.
        node_id (Union[Unset, str]): Globally unique identifier for this node.
        instance_id (Union[Unset, str]): Globally unique identifier for the host instance from the cloud provider.
        start_timestamp (Union[Unset, int]): The timestamp (in millisecond) when the Spark node is launched.
        host_private_ip (Union[Unset, str]): The private IP address of the host instance.
    """

    private_ip: Union[Unset, str] = UNSET
    public_dns: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    start_timestamp: Union[Unset, int] = UNSET
    host_private_ip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        private_ip = self.private_ip
        public_dns = self.public_dns
        node_id = self.node_id
        instance_id = self.instance_id
        start_timestamp = self.start_timestamp
        host_private_ip = self.host_private_ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if private_ip is not UNSET:
            field_dict["private_ip"] = private_ip
        if public_dns is not UNSET:
            field_dict["public_dns"] = public_dns
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if start_timestamp is not UNSET:
            field_dict["start_timestamp"] = start_timestamp
        if host_private_ip is not UNSET:
            field_dict["host_private_ip"] = host_private_ip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        private_ip = d.pop("private_ip", UNSET)

        public_dns = d.pop("public_dns", UNSET)

        node_id = d.pop("node_id", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        start_timestamp = d.pop("start_timestamp", UNSET)

        host_private_ip = d.pop("host_private_ip", UNSET)

        spark_node = cls(
            private_ip=private_ip,
            public_dns=public_dns,
            node_id=node_id,
            instance_id=instance_id,
            start_timestamp=start_timestamp,
            host_private_ip=host_private_ip,
        )

        spark_node.additional_properties = d
        return spark_node

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
