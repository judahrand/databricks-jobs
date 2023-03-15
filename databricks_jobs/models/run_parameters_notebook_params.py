from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RunParametersNotebookParams")


@attr.s(auto_attribs=True)
class RunParametersNotebookParams:
    """A map from keys to values for jobs with notebook task, for example `"notebook_params": {"name": "john doe", "age":
    "35"}`. The map is passed to the notebook and is accessible through the
    [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-widgets)
    function.

    If not specified upon `run-now`, the triggered run uses the job’s base parameters.

    notebook_params cannot be specified in conjunction with jar_params.

    Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set
    parameters containing information about job runs.

    The JSON representation of this field (for example `{"notebook_params":{"name":"john doe","age":"35"}}`) cannot
    exceed 10,000 bytes.

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
        run_parameters_notebook_params = cls()

        run_parameters_notebook_params.additional_properties = d
        return run_parameters_notebook_params

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
