from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.view_item import ViewItem


T = TypeVar("T", bound="JobsRunsExportResponse200")


@attr.s(auto_attribs=True)
class JobsRunsExportResponse200:
    """
    Attributes:
        views (Union[Unset, List['ViewItem']]): The exported content in HTML format (one for every view item).
    """

    views: Union[Unset, List["ViewItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        views: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.views, Unset):
            views = []
            for views_item_data in self.views:
                views_item = views_item_data.to_dict()

                views.append(views_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.view_item import ViewItem

        d = src_dict.copy()
        views = []
        _views = d.pop("views", UNSET)
        for views_item_data in _views or []:
            views_item = ViewItem.from_dict(views_item_data)

            views.append(views_item)

        jobs_runs_export_response_200 = cls(
            views=views,
        )

        jobs_runs_export_response_200.additional_properties = d
        return jobs_runs_export_response_200

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
