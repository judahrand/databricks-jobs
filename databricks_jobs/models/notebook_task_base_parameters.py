from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="NotebookTaskBaseParameters")


@attr.s(auto_attribs=True)
class NotebookTaskBaseParameters:
    """Base parameters to be used for each run of this job. If the run is initiated by a call to [`run-
    now`](https://docs.microsoft.com/azure/databricks/dev-tools/api/latest/jobs#operation/JobsRunNow) with parameters
    specified, the two parameters maps are merged. If the same key is specified in `base_parameters` and in `run-now`,
    the value from `run-now` is used.

    Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set
    parameters containing information about job runs.

    If the notebook takes a parameter that is not specified in the job’s `base_parameters` or the `run-now` override
    parameters, the default value from the notebook is used.

    Retrieve these parameters in a notebook using [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-
    tools/databricks-utils#dbutils-widgets).

        Example:
            {'name': 'John Doe', 'age': 35}

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
        notebook_task_base_parameters = cls()

        notebook_task_base_parameters.additional_properties = d
        return notebook_task_base_parameters

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
