from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_settings import JobSettings


T = TypeVar("T", bound="JobsUpdateJsonBody")


@attr.s(auto_attribs=True)
class JobsUpdateJsonBody:
    """
    Attributes:
        job_id (int): The canonical identifier of the job to update. This field is required. Example: 11223344.
        new_settings (Union[Unset, JobSettings]):
        fields_to_remove (Union[Unset, List[str]]): Remove top-level fields in the job settings. Removing nested fields
            is not supported. This field is optional. Example: ['libraries', 'schedule'].
    """

    job_id: int
    new_settings: Union[Unset, "JobSettings"] = UNSET
    fields_to_remove: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        new_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_settings, Unset):
            new_settings = self.new_settings.to_dict()

        fields_to_remove: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fields_to_remove, Unset):
            fields_to_remove = self.fields_to_remove

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
            }
        )
        if new_settings is not UNSET:
            field_dict["new_settings"] = new_settings
        if fields_to_remove is not UNSET:
            field_dict["fields_to_remove"] = fields_to_remove

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

        fields_to_remove = cast(List[str], d.pop("fields_to_remove", UNSET))

        jobs_update_json_body = cls(
            job_id=job_id,
            new_settings=new_settings,
            fields_to_remove=fields_to_remove,
        )

        jobs_update_json_body.additional_properties = d
        return jobs_update_json_body

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
