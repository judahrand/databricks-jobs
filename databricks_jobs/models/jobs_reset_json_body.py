from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_settings import JobSettings


T = TypeVar("T", bound="JobsResetJsonBody")


@attr.s(auto_attribs=True)
class JobsResetJsonBody:
    """
    Attributes:
        job_id (int): The canonical identifier of the job to reset. This field is required. Example: 11223344.
        new_settings (Union[Unset, JobSettings]):
    """

    job_id: int
    new_settings: Union[Unset, "JobSettings"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        new_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_settings, Unset):
            new_settings = self.new_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
            }
        )
        if new_settings is not UNSET:
            field_dict["new_settings"] = new_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_settings import JobSettings

        d = src_dict.copy()
        job_id = d.pop("job_id")

        _new_settings = d.pop("new_settings", UNSET)
        new_settings: Union[Unset, JobSettings]
        if isinstance(_new_settings, Unset):
            new_settings = UNSET
        else:
            new_settings = JobSettings.from_dict(_new_settings)

        jobs_reset_json_body = cls(
            job_id=job_id,
            new_settings=new_settings,
        )

        jobs_reset_json_body.additional_properties = d
        return jobs_reset_json_body

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
