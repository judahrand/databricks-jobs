from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsRunNowResponse200")


@attr.s(auto_attribs=True)
class JobsRunNowResponse200:
    """
    Attributes:
        run_id (Union[Unset, int]): The globally unique ID of the newly triggered run. Example: 455644833.
        number_in_job (Union[Unset, int]): A unique identifier for this job run. This is set to the same value as
            `run_id`. Example: 455644833.
    """

    run_id: Union[Unset, int] = UNSET
    number_in_job: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_id = self.run_id
        number_in_job = self.number_in_job

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if number_in_job is not UNSET:
            field_dict["number_in_job"] = number_in_job

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        run_id = d.pop("run_id", UNSET)

        number_in_job = d.pop("number_in_job", UNSET)

        jobs_run_now_response_200 = cls(
            run_id=run_id,
            number_in_job=number_in_job,
        )

        jobs_run_now_response_200.additional_properties = d
        return jobs_run_now_response_200

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
