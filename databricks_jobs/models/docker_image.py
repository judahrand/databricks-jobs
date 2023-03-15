from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.docker_basic_auth import DockerBasicAuth


T = TypeVar("T", bound="DockerImage")


@attr.s(auto_attribs=True)
class DockerImage:
    """
    Attributes:
        url (Union[Unset, str]): URL for the Docker image.
        basic_auth (Union[Unset, DockerBasicAuth]):
    """

    url: Union[Unset, str] = UNSET
    basic_auth: Union[Unset, "DockerBasicAuth"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        basic_auth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.basic_auth, Unset):
            basic_auth = self.basic_auth.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if basic_auth is not UNSET:
            field_dict["basic_auth"] = basic_auth

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.docker_basic_auth import DockerBasicAuth

        d = src_dict.copy()
        url = d.pop("url", UNSET)

        _basic_auth = d.pop("basic_auth", UNSET)
        basic_auth: Union[Unset, DockerBasicAuth]
        if isinstance(_basic_auth, Unset):
            basic_auth = UNSET
        else:
            basic_auth = DockerBasicAuth.from_dict(_basic_auth)

        docker_image = cls(
            url=url,
            basic_auth=basic_auth,
        )

        docker_image.additional_properties = d
        return docker_image

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
