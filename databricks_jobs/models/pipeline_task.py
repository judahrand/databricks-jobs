from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineTask")


@attr.s(auto_attribs=True)
class PipelineTask:
    """
    Attributes:
        pipeline_id (Union[Unset, str]): The full name of the pipeline task to execute. Example:
            a12cd3e4-0ab1-1abc-1a2b-1a2bcd3e4fg5.
        full_refresh (Union[Unset, bool]): If true, a full refresh will be triggered on the delta live table.
    """

    pipeline_id: Union[Unset, str] = UNSET
    full_refresh: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pipeline_id = self.pipeline_id
        full_refresh = self.full_refresh

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline_id is not UNSET:
            field_dict["pipeline_id"] = pipeline_id
        if full_refresh is not UNSET:
            field_dict["full_refresh"] = full_refresh

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pipeline_id = d.pop("pipeline_id", UNSET)

        full_refresh = d.pop("full_refresh", UNSET)

        pipeline_task = cls(
            pipeline_id=pipeline_id,
            full_refresh=full_refresh,
        )

        pipeline_task.additional_properties = d
        return pipeline_task

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
