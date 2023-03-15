from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_settings import JobSettings


T = TypeVar("T", bound="JobsGetResponse200")


@attr.s(auto_attribs=True)
class JobsGetResponse200:
    """
    Attributes:
        job_id (Union[Unset, int]): The canonical identifier for this job. Example: 11223344.
        creator_user_name (Union[Unset, str]): The creator user name. This field won’t be included in the response if
            the user has been deleted. Example: user.name@databricks.com.
        run_as_user_name (Union[Unset, str]): The user name that the job runs as. `run_as_user_name` is based on the
            current job settings, and is set to the creator of the job if job access control is disabled, or the `is_owner`
            permission if job access control is enabled. Example: user.name@databricks.com.
        settings (Union[Unset, JobSettings]):
        created_time (Union[Unset, int]): The time at which this job was created in epoch milliseconds (milliseconds
            since 1/1/1970 UTC). Example: 1601370337343.
    """

    job_id: Union[Unset, int] = UNSET
    creator_user_name: Union[Unset, str] = UNSET
    run_as_user_name: Union[Unset, str] = UNSET
    settings: Union[Unset, "JobSettings"] = UNSET
    created_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        creator_user_name = self.creator_user_name
        run_as_user_name = self.run_as_user_name
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
        if run_as_user_name is not UNSET:
            field_dict["run_as_user_name"] = run_as_user_name
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

        run_as_user_name = d.pop("run_as_user_name", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, JobSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = JobSettings.from_dict(_settings)

        created_time = d.pop("created_time", UNSET)

        jobs_get_response_200 = cls(
            job_id=job_id,
            creator_user_name=creator_user_name,
            run_as_user_name=run_as_user_name,
            settings=settings,
            created_time=created_time,
        )

        jobs_get_response_200.additional_properties = d
        return jobs_get_response_200

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
