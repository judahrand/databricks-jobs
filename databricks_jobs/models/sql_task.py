from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sql_task_alert import SqlTaskAlert
    from ..models.sql_task_dashboard import SqlTaskDashboard
    from ..models.sql_task_parameters import SqlTaskParameters
    from ..models.sql_task_query import SqlTaskQuery


T = TypeVar("T", bound="SqlTask")


@attr.s(auto_attribs=True)
class SqlTask:
    """
    Attributes:
        warehouse_id (str): The canonical identifier of the SQL warehouse. Only serverless and pro SQL warehouses are
            supported.
        query (Union[Unset, SqlTaskQuery]):
        dashboard (Union[Unset, SqlTaskDashboard]):
        alert (Union[Unset, SqlTaskAlert]):
        parameters (Union[Unset, SqlTaskParameters]): Parameters to be used for each run of this job. The SQL alert task
            does not support custom parameters. Example: {'name': 'John Doe', 'age': 35}.
    """

    warehouse_id: str
    query: Union[Unset, "SqlTaskQuery"] = UNSET
    dashboard: Union[Unset, "SqlTaskDashboard"] = UNSET
    alert: Union[Unset, "SqlTaskAlert"] = UNSET
    parameters: Union[Unset, "SqlTaskParameters"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        warehouse_id = self.warehouse_id
        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        dashboard: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dashboard, Unset):
            dashboard = self.dashboard.to_dict()

        alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouse_id": warehouse_id,
            }
        )
        if query is not UNSET:
            field_dict["query"] = query
        if dashboard is not UNSET:
            field_dict["dashboard"] = dashboard
        if alert is not UNSET:
            field_dict["alert"] = alert
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sql_task_alert import SqlTaskAlert
        from ..models.sql_task_dashboard import SqlTaskDashboard
        from ..models.sql_task_parameters import SqlTaskParameters
        from ..models.sql_task_query import SqlTaskQuery

        d = src_dict.copy()
        warehouse_id = d.pop("warehouse_id")

        _query = d.pop("query", UNSET)
        query: Union[Unset, SqlTaskQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = SqlTaskQuery.from_dict(_query)

        _dashboard = d.pop("dashboard", UNSET)
        dashboard: Union[Unset, SqlTaskDashboard]
        if isinstance(_dashboard, Unset):
            dashboard = UNSET
        else:
            dashboard = SqlTaskDashboard.from_dict(_dashboard)

        _alert = d.pop("alert", UNSET)
        alert: Union[Unset, SqlTaskAlert]
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = SqlTaskAlert.from_dict(_alert)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, SqlTaskParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = SqlTaskParameters.from_dict(_parameters)

        sql_task = cls(
            warehouse_id=warehouse_id,
            query=query,
            dashboard=dashboard,
            alert=alert,
            parameters=parameters,
        )

        sql_task.additional_properties = d
        return sql_task

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
