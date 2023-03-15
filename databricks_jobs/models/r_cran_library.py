from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RCranLibrary")


@attr.s(auto_attribs=True)
class RCranLibrary:
    """
    Attributes:
        package (str): The name of the CRAN package to install. This field is required. Example: geojson.
        repo (Union[Unset, str]): The repository where the package can be found. If not specified, the default CRAN repo
            is used. Example: https://my-repo.com.
    """

    package: str
    repo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package = self.package
        repo = self.repo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package": package,
            }
        )
        if repo is not UNSET:
            field_dict["repo"] = repo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        package = d.pop("package")

        repo = d.pop("repo", UNSET)

        r_cran_library = cls(
            package=package,
            repo=repo,
        )

        r_cran_library.additional_properties = d
        return r_cran_library

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
