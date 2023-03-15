from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.notebook_task_source import NotebookTaskSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notebook_task_base_parameters import NotebookTaskBaseParameters


T = TypeVar("T", bound="NotebookTask")


@attr.s(auto_attribs=True)
class NotebookTask:
    """
    Attributes:
        notebook_path (str): The path of the notebook to be run in the Azure Databricks workspace or remote repository.
            For notebooks stored in the Databricks workspace, the path must be absolute and begin with a slash. For
            notebooks stored in a remote repository, the path must be relative. This field is required. Example:
            /Users/user.name@databricks.com/notebook_to_run.
        source (Union[Unset, NotebookTaskSource]): Optional location type of the notebook. When set to `WORKSPACE`, the
            notebook will be retrieved from the local Azure Databricks workspace. When set to `GIT`, the notebook will be
            retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if
            `git_source` is defined and `WORKSPACE` otherwise. Example: WORKSPACE.
        base_parameters (Union[Unset, NotebookTaskBaseParameters]): Base parameters to be used for each run of this job.
            If the run is initiated by a call to [`run-now`](https://docs.microsoft.com/azure/databricks/dev-
            tools/api/latest/jobs#operation/JobsRunNow) with parameters specified, the two parameters maps are merged. If
            the same key is specified in `base_parameters` and in `run-now`, the value from `run-now` is used.

            Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set
            parameters containing information about job runs.

            If the notebook takes a parameter that is not specified in the job’s `base_parameters` or the `run-now` override
            parameters, the default value from the notebook is used.

            Retrieve these parameters in a notebook using
            [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-widgets).
            Example: {'name': 'John Doe', 'age': 35}.
    """

    notebook_path: str
    source: Union[Unset, NotebookTaskSource] = UNSET
    base_parameters: Union[Unset, "NotebookTaskBaseParameters"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notebook_path = self.notebook_path
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        base_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.base_parameters, Unset):
            base_parameters = self.base_parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notebook_path": notebook_path,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source
        if base_parameters is not UNSET:
            field_dict["base_parameters"] = base_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notebook_task_base_parameters import NotebookTaskBaseParameters

        d = src_dict.copy()
        notebook_path = d.pop("notebook_path")

        _source = d.pop("source", UNSET)
        source: Union[Unset, NotebookTaskSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NotebookTaskSource(_source)

        _base_parameters = d.pop("base_parameters", UNSET)
        base_parameters: Union[Unset, NotebookTaskBaseParameters]
        if isinstance(_base_parameters, Unset):
            base_parameters = UNSET
        else:
            base_parameters = NotebookTaskBaseParameters.from_dict(_base_parameters)

        notebook_task = cls(
            notebook_path=notebook_path,
            source=source,
            base_parameters=base_parameters,
        )

        notebook_task.additional_properties = d
        return notebook_task

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
