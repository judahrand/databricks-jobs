from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SqlTaskAlert")


@attr.s(auto_attribs=True)
class SqlTaskAlert:
    """
    Attributes:
        alert_id (str): The canonical identifier of the SQL alert.
    """

    alert_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_id = self.alert_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_id": alert_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_id = d.pop("alert_id")

        sql_task_alert = cls(
            alert_id=alert_id,
        )

        sql_task_alert.additional_properties = d
        return sql_task_alert

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
