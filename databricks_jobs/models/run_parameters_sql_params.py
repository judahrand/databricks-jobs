from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RunParametersSqlParams")


@attr.s(auto_attribs=True)
class RunParametersSqlParams:
    """A map from keys to values for SQL tasks, for example `"sql_params": {"name": "john doe", "age": "35"}`. The SQL
    alert task does not support custom parameters.

        Example:
            {'name': 'john doe', 'age': '35'}

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
        run_parameters_sql_params = cls()

        run_parameters_sql_params.additional_properties = d
        return run_parameters_sql_params

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
