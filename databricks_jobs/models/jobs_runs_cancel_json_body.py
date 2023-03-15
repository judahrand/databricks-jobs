from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="JobsRunsCancelJsonBody")


@attr.s(auto_attribs=True)
class JobsRunsCancelJsonBody:
    """
    Attributes:
        run_id (int): This field is required. Example: 455644833.
    """

    run_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_id = self.run_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run_id": run_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        run_id = d.pop("run_id")

        jobs_runs_cancel_json_body = cls(
            run_id=run_id,
        )

        jobs_runs_cancel_json_body.additional_properties = d
        return jobs_runs_cancel_json_body

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
