from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PythonWheelTaskNamedParameters")


@attr.s(auto_attribs=True)
class PythonWheelTaskNamedParameters:
    """Command-line parameters passed to Python wheel task in the form of `["--name=task", "--
    data=dbfs:/path/to/data.json"]`. Leave it empty if `parameters` is not null.

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
        python_wheel_task_named_parameters = cls()

        python_wheel_task_named_parameters.additional_properties = d
        return python_wheel_task_named_parameters

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
