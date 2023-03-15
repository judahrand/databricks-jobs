from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run import Run


T = TypeVar("T", bound="JobsRunsListResponse200")


@attr.s(auto_attribs=True)
class JobsRunsListResponse200:
    """
    Attributes:
        runs (Union[Unset, List['Run']]): A list of runs, from most recently started to least.
        has_more (Union[Unset, bool]): If true, additional runs matching the provided filter are available for listing.
    """

    runs: Union[Unset, List["Run"]] = UNSET
    has_more: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        runs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.runs, Unset):
            runs = []
            for runs_item_data in self.runs:
                runs_item = runs_item_data.to_dict()

                runs.append(runs_item)

        has_more = self.has_more

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if runs is not UNSET:
            field_dict["runs"] = runs
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.run import Run

        d = src_dict.copy()
        runs = []
        _runs = d.pop("runs", UNSET)
        for runs_item_data in _runs or []:
            runs_item = Run.from_dict(runs_item_data)

            runs.append(runs_item)

        has_more = d.pop("has_more", UNSET)

        jobs_runs_list_response_200 = cls(
            runs=runs,
            has_more=has_more,
        )

        jobs_runs_list_response_200.additional_properties = d
        return jobs_runs_list_response_200

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
