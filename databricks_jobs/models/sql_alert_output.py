from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sql_statement_output import SqlStatementOutput


T = TypeVar("T", bound="SqlAlertOutput")


@attr.s(auto_attribs=True)
class SqlAlertOutput:
    """
    Attributes:
        query_text (Union[Unset, str]): The text of the SQL query. Can Run permission of the SQL query associated with
            the SQL alert is required to view this field.
        warehouse_id (Union[Unset, str]): The canonical identifier of the SQL warehouse.
        sql_statements (Union[Unset, SqlStatementOutput]):
        output_link (Union[Unset, str]): The link to find the output results.
    """

    query_text: Union[Unset, str] = UNSET
    warehouse_id: Union[Unset, str] = UNSET
    sql_statements: Union[Unset, "SqlStatementOutput"] = UNSET
    output_link: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_text = self.query_text
        warehouse_id = self.warehouse_id
        sql_statements: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sql_statements, Unset):
            sql_statements = self.sql_statements.to_dict()

        output_link = self.output_link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query_text is not UNSET:
            field_dict["query_text"] = query_text
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id
        if sql_statements is not UNSET:
            field_dict["sql_statements"] = sql_statements
        if output_link is not UNSET:
            field_dict["output_link"] = output_link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sql_statement_output import SqlStatementOutput

        d = src_dict.copy()
        query_text = d.pop("query_text", UNSET)

        warehouse_id = d.pop("warehouse_id", UNSET)

        _sql_statements = d.pop("sql_statements", UNSET)
        sql_statements: Union[Unset, SqlStatementOutput]
        if isinstance(_sql_statements, Unset):
            sql_statements = UNSET
        else:
            sql_statements = SqlStatementOutput.from_dict(_sql_statements)

        output_link = d.pop("output_link", UNSET)

        sql_alert_output = cls(
            query_text=query_text,
            warehouse_id=warehouse_id,
            sql_statements=sql_statements,
            output_link=output_link,
        )

        sql_alert_output.additional_properties = d
        return sql_alert_output

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
