from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_scale import AutoScale


T = TypeVar("T", bound="ClusterSize")


@attr.s(auto_attribs=True)
class ClusterSize:
    """
    Attributes:
        num_workers (Union[Unset, int]): If num_workers, number of worker nodes that this cluster must have. A cluster
            has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. When reading the
            properties of a cluster, this field reflects the desired number of workers rather than the actual number of
            workers. For instance, if a cluster is resized from 5 to 10 workers, this field is updated to reflect the target
            size of 10 workers, whereas the workers listed in executors gradually increase from 5 to 10 as the new nodes are
            provisioned.
        autoscale (Union[Unset, AutoScale]):
    """

    num_workers: Union[Unset, int] = UNSET
    autoscale: Union[Unset, "AutoScale"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_workers = self.num_workers
        autoscale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.autoscale, Unset):
            autoscale = self.autoscale.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_workers is not UNSET:
            field_dict["num_workers"] = num_workers
        if autoscale is not UNSET:
            field_dict["autoscale"] = autoscale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.auto_scale import AutoScale

        d = src_dict.copy()
        num_workers = d.pop("num_workers", UNSET)

        _autoscale = d.pop("autoscale", UNSET)
        autoscale: Union[Unset, AutoScale]
        if isinstance(_autoscale, Unset):
            autoscale = UNSET
        else:
            autoscale = AutoScale.from_dict(_autoscale)

        cluster_size = cls(
            num_workers=num_workers,
            autoscale=autoscale,
        )

        cluster_size.additional_properties = d
        return cluster_size

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
