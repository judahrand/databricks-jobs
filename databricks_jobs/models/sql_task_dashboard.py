from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SqlTaskDashboard")


@attr.s(auto_attribs=True)
class SqlTaskDashboard:
    """
    Attributes:
        dashboard_id (str): The canonical identifier of the SQL dashboard.
    """

    dashboard_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dashboard_id = self.dashboard_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dashboard_id": dashboard_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dashboard_id = d.pop("dashboard_id")

        sql_task_dashboard = cls(
            dashboard_id=dashboard_id,
        )

        sql_task_dashboard.additional_properties = d
        return sql_task_dashboard

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
