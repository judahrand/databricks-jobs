from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_settings import JobSettings


T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """
    Attributes:
        job_id (Union[Unset, int]): The canonical identifier for this job. Example: 11223344.
        creator_user_name (Union[Unset, str]): The creator user name. This field won’t be included in the response if
            the user has already been deleted. Example: user.name@databricks.com.
        settings (Union[Unset, JobSettings]):
        created_time (Union[Unset, int]): The time at which this job was created in epoch milliseconds (milliseconds
            since 1/1/1970 UTC). Example: 1601370337343.
    """

    job_id: Union[Unset, int] = UNSET
    creator_user_name: Union[Unset, str] = UNSET
    settings: Union[Unset, "JobSettings"] = UNSET
    created_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        creator_user_name = self.creator_user_name
        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        created_time = self.created_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if creator_user_name is not UNSET:
            field_dict["creator_user_name"] = creator_user_name
        if settings is not UNSET:
            field_dict["settings"] = settings
        if created_time is not UNSET:
            field_dict["created_time"] = created_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_settings import JobSettings

        d = src_dict.copy()
        job_id = d.pop("job_id", UNSET)

        creator_user_name = d.pop("creator_user_name", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, JobSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = JobSettings.from_dict(_settings)

        created_time = d.pop("created_time", UNSET)

        job = cls(
            job_id=job_id,
            creator_user_name=creator_user_name,
            settings=settings,
            created_time=created_time,
        )

        job.additional_properties = d
        return job

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
