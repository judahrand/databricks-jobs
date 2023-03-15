from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsRunsRepairResponse200")


@attr.s(auto_attribs=True)
class JobsRunsRepairResponse200:
    """
    Attributes:
        repair_id (Union[Unset, int]): The ID of the repair. Example: 734650698524280.
    """

    repair_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repair_id = self.repair_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repair_id is not UNSET:
            field_dict["repair_id"] = repair_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        repair_id = d.pop("repair_id", UNSET)

        jobs_runs_repair_response_200 = cls(
            repair_id=repair_id,
        )

        jobs_runs_repair_response_200.additional_properties = d
        return jobs_runs_repair_response_200

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
