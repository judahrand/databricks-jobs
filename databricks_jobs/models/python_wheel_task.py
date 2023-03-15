from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.python_wheel_task_named_parameters import PythonWheelTaskNamedParameters


T = TypeVar("T", bound="PythonWheelTask")


@attr.s(auto_attribs=True)
class PythonWheelTask:
    """
    Attributes:
        package_name (Union[Unset, str]): Name of the package to execute
        entry_point (Union[Unset, str]): Named entry point to use, if it does not exist in the metadata of the package
            it executes the function from the package directly using `$packageName.$entryPoint()`
        parameters (Union[Unset, List[str]]): Command-line parameters passed to Python wheel task. Leave it empty if
            `named_parameters` is not null. Example: ['--name=task', 'one', 'two'].
        named_parameters (Union[Unset, PythonWheelTaskNamedParameters]): Command-line parameters passed to Python wheel
            task in the form of `["--name=task", "--data=dbfs:/path/to/data.json"]`. Leave it empty if `parameters` is not
            null. Example: {'name': 'task', 'data': 'dbfs:/path/to/data.json'}.
    """

    package_name: Union[Unset, str] = UNSET
    entry_point: Union[Unset, str] = UNSET
    parameters: Union[Unset, List[str]] = UNSET
    named_parameters: Union[Unset, "PythonWheelTaskNamedParameters"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_name = self.package_name
        entry_point = self.entry_point
        parameters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters

        named_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.named_parameters, Unset):
            named_parameters = self.named_parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_name is not UNSET:
            field_dict["package_name"] = package_name
        if entry_point is not UNSET:
            field_dict["entry_point"] = entry_point
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if named_parameters is not UNSET:
            field_dict["named_parameters"] = named_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.python_wheel_task_named_parameters import PythonWheelTaskNamedParameters

        d = src_dict.copy()
        package_name = d.pop("package_name", UNSET)

        entry_point = d.pop("entry_point", UNSET)

        parameters = cast(List[str], d.pop("parameters", UNSET))

        _named_parameters = d.pop("named_parameters", UNSET)
        named_parameters: Union[Unset, PythonWheelTaskNamedParameters]
        if isinstance(_named_parameters, Unset):
            named_parameters = UNSET
        else:
            named_parameters = PythonWheelTaskNamedParameters.from_dict(_named_parameters)

        python_wheel_task = cls(
            package_name=package_name,
            entry_point=entry_point,
            parameters=parameters,
            named_parameters=named_parameters,
        )

        python_wheel_task.additional_properties = d
        return python_wheel_task

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