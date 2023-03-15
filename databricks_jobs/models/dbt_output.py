from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbt_output_artifacts_headers import DbtOutputArtifactsHeaders


T = TypeVar("T", bound="DbtOutput")


@attr.s(auto_attribs=True)
class DbtOutput:
    """
    Attributes:
        artifacts_link (Union[Unset, str]): A pre-signed URL to download the (compressed) dbt artifacts. This link is
            valid for a limited time (30 minutes). This information is only available after the run has finished.
        artifacts_headers (Union[Unset, DbtOutputArtifactsHeaders]): An optional map of headers to send when retrieving
            the artifact from the `artifacts_link`.
    """

    artifacts_link: Union[Unset, str] = UNSET
    artifacts_headers: Union[Unset, "DbtOutputArtifactsHeaders"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artifacts_link = self.artifacts_link
        artifacts_headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.artifacts_headers, Unset):
            artifacts_headers = self.artifacts_headers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifacts_link is not UNSET:
            field_dict["artifacts_link"] = artifacts_link
        if artifacts_headers is not UNSET:
            field_dict["artifacts_headers"] = artifacts_headers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dbt_output_artifacts_headers import DbtOutputArtifactsHeaders

        d = src_dict.copy()
        artifacts_link = d.pop("artifacts_link", UNSET)

        _artifacts_headers = d.pop("artifacts_headers", UNSET)
        artifacts_headers: Union[Unset, DbtOutputArtifactsHeaders]
        if isinstance(_artifacts_headers, Unset):
            artifacts_headers = UNSET
        else:
            artifacts_headers = DbtOutputArtifactsHeaders.from_dict(_artifacts_headers)

        dbt_output = cls(
            artifacts_link=artifacts_link,
            artifacts_headers=artifacts_headers,
        )

        dbt_output.additional_properties = d
        return dbt_output

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
