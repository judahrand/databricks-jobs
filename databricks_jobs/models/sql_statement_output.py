from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlStatementOutput")


@attr.s(auto_attribs=True)
class SqlStatementOutput:
    """
    Attributes:
        lookup_key (Union[Unset, str]): A key that can be used to look up query details.
    """

    lookup_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lookup_key = self.lookup_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lookup_key is not UNSET:
            field_dict["lookup_key"] = lookup_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lookup_key = d.pop("lookup_key", UNSET)

        sql_statement_output = cls(
            lookup_key=lookup_key,
        )

        sql_statement_output.additional_properties = d
        return sql_statement_output

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
