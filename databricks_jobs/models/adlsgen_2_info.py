from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Adlsgen2Info")


@attr.s(auto_attribs=True)
class Adlsgen2Info:
    """
    Attributes:
        destination (Union[Unset, str]): abfss destination. Example: `abfss://<container-name>@<storage-account-
            name>.dfs.core.windows.net/<directory-name>`
    """

    destination: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        destination = self.destination

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        destination = d.pop("destination", UNSET)

        adlsgen_2_info = cls(
            destination=destination,
        )

        adlsgen_2_info.additional_properties = d
        return adlsgen_2_info

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
