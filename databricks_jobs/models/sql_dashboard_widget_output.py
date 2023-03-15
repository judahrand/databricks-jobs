from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.sql_dashboard_widget_output_status import SqlDashboardWidgetOutputStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sql_output_error import SqlOutputError


T = TypeVar("T", bound="SqlDashboardWidgetOutput")


@attr.s(auto_attribs=True)
class SqlDashboardWidgetOutput:
    """
    Attributes:
        widget_id (Union[Unset, str]): The canonical identifier of the SQL widget.
        widget_title (Union[Unset, str]): The title of the SQL widget.
        output_link (Union[Unset, str]): The link to find the output results.
        status (Union[Unset, SqlDashboardWidgetOutputStatus]): The execution status of the SQL widget.
        error (Union[Unset, SqlOutputError]):
        start_time (Union[Unset, int]): Time (in epoch milliseconds) when execution of the SQL widget starts.
        end_time (Union[Unset, int]): Time (in epoch milliseconds) when execution of the SQL widget ends.
    """

    widget_id: Union[Unset, str] = UNSET
    widget_title: Union[Unset, str] = UNSET
    output_link: Union[Unset, str] = UNSET
    status: Union[Unset, SqlDashboardWidgetOutputStatus] = UNSET
    error: Union[Unset, "SqlOutputError"] = UNSET
    start_time: Union[Unset, int] = UNSET
    end_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        widget_id = self.widget_id
        widget_title = self.widget_title
        output_link = self.output_link
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        start_time = self.start_time
        end_time = self.end_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if widget_id is not UNSET:
            field_dict["widget_id"] = widget_id
        if widget_title is not UNSET:
            field_dict["widget_title"] = widget_title
        if output_link is not UNSET:
            field_dict["output_link"] = output_link
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sql_output_error import SqlOutputError

        d = src_dict.copy()
        widget_id = d.pop("widget_id", UNSET)

        widget_title = d.pop("widget_title", UNSET)

        output_link = d.pop("output_link", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SqlDashboardWidgetOutputStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SqlDashboardWidgetOutputStatus(_status)

        _error = d.pop("error", UNSET)
        error: Union[Unset, SqlOutputError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = SqlOutputError.from_dict(_error)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        sql_dashboard_widget_output = cls(
            widget_id=widget_id,
            widget_title=widget_title,
            output_link=output_link,
            status=status,
            error=error,
            start_time=start_time,
            end_time=end_time,
        )

        sql_dashboard_widget_output.additional_properties = d
        return sql_dashboard_widget_output

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
