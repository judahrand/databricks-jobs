from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoScale")


@attr.s(auto_attribs=True)
class AutoScale:
    """
    Attributes:
        min_workers (Union[Unset, int]): The minimum number of workers to which the cluster can scale down when
            underutilized. It is also the initial number of workers the cluster has after creation.
        max_workers (Union[Unset, int]): The maximum number of workers to which the cluster can scale up when
            overloaded. max_workers must be strictly greater than min_workers.
    """

    min_workers: Union[Unset, int] = UNSET
    max_workers: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_workers = self.min_workers
        max_workers = self.max_workers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_workers is not UNSET:
            field_dict["min_workers"] = min_workers
        if max_workers is not UNSET:
            field_dict["max_workers"] = max_workers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_workers = d.pop("min_workers", UNSET)

        max_workers = d.pop("max_workers", UNSET)

        auto_scale = cls(
            min_workers=min_workers,
            max_workers=max_workers,
        )

        auto_scale.additional_properties = d
        return auto_scale

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
