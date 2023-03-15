from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MavenLibrary")


@attr.s(auto_attribs=True)
class MavenLibrary:
    """
    Attributes:
        coordinates (str): Gradle-style Maven coordinates. For example: `org.jsoup:jsoup:1.7.2`. This field is required.
            Example: org.jsoup:jsoup:1.7.2.
        repo (Union[Unset, str]): Maven repo to install the Maven package from. If omitted, both Maven Central
            Repository and Spark Packages are searched. Example: https://my-repo.com.
        exclusions (Union[Unset, List[str]]): List of dependences to exclude. For example: `["slf4j:slf4j", "*:hadoop-
            client"]`.

            Maven dependency exclusions: <https://maven.apache.org/guides/introduction/introduction-to-optional-and-
            excludes-dependencies.html>. Example: ['slf4j:slf4j', '*:hadoop-client'].
    """

    coordinates: str
    repo: Union[Unset, str] = UNSET
    exclusions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        coordinates = self.coordinates
        repo = self.repo
        exclusions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.exclusions, Unset):
            exclusions = self.exclusions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "coordinates": coordinates,
            }
        )
        if repo is not UNSET:
            field_dict["repo"] = repo
        if exclusions is not UNSET:
            field_dict["exclusions"] = exclusions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        coordinates = d.pop("coordinates")

        repo = d.pop("repo", UNSET)

        exclusions = cast(List[str], d.pop("exclusions", UNSET))

        maven_library = cls(
            coordinates=coordinates,
            repo=repo,
            exclusions=exclusions,
        )

        maven_library.additional_properties = d
        return maven_library

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
