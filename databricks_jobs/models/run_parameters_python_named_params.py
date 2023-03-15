from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RunParametersPythonNamedParams")


@attr.s(auto_attribs=True)
class RunParametersPythonNamedParams:
    """A map from keys to values for jobs with Python wheel task, for example `"python_named_params": {"name": "task",
    "data": "dbfs:/path/to/data.json"}`.

        Example:
            {'name': 'task', 'data': 'dbfs:/path/to/data.json'}

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
        run_parameters_python_named_params = cls()

        run_parameters_python_named_params.additional_properties = d
        return run_parameters_python_named_params

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
