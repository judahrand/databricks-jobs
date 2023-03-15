from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.repair_history_item_type import RepairHistoryItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_state import RunState


T = TypeVar("T", bound="RepairHistoryItem")


@attr.s(auto_attribs=True)
class RepairHistoryItem:
    """
    Attributes:
        type (Union[Unset, RepairHistoryItemType]): The repair history item type. Indicates whether a run is the
            original run or a repair run.
        start_time (Union[Unset, int]): The start time of the (repaired) run. Example: 1625060460483.
        end_time (Union[Unset, int]): The end time of the (repaired) run. Example: 1625060863413.
        state (Union[Unset, RunState]): The result and lifecycle state of the run.
        id (Union[Unset, int]): The ID of the repair. Only returned for the items that represent a repair in
            `repair_history`. Example: 734650698524280.
        task_run_ids (Union[Unset, List[int]]): The run IDs of the task runs that ran as part of this repair history
            item. Example: [1106460542112844, 988297789683452].
    """

    type: Union[Unset, RepairHistoryItemType] = UNSET
    start_time: Union[Unset, int] = UNSET
    end_time: Union[Unset, int] = UNSET
    state: Union[Unset, "RunState"] = UNSET
    id: Union[Unset, int] = UNSET
    task_run_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        start_time = self.start_time
        end_time = self.end_time
        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        id = self.id
        task_run_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.task_run_ids, Unset):
            task_run_ids = self.task_run_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if state is not UNSET:
            field_dict["state"] = state
        if id is not UNSET:
            field_dict["id"] = id
        if task_run_ids is not UNSET:
            field_dict["task_run_ids"] = task_run_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.run_state import RunState

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, RepairHistoryItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = RepairHistoryItemType(_type)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, RunState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RunState.from_dict(_state)

        id = d.pop("id", UNSET)

        task_run_ids = cast(List[int], d.pop("task_run_ids", UNSET))

        repair_history_item = cls(
            type=type,
            start_time=start_time,
            end_time=end_time,
            state=state,
            id=id,
            task_run_ids=task_run_ids,
        )

        repair_history_item.additional_properties = d
        return repair_history_item

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
