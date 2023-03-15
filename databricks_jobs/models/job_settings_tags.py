from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="JobSettingsTags")


@attr.s(auto_attribs=True)
class JobSettingsTags:
    """A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are
    subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job.

        Example:
            {'cost-center': 'engineering', 'team': 'jobs'}

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_settings_tags = cls()

        job_settings_tags.additional_properties = d
        return job_settings_tags

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
