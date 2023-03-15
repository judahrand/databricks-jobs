from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbfs_storage_info import DbfsStorageInfo


T = TypeVar("T", bound="ClusterLogConf")


@attr.s(auto_attribs=True)
class ClusterLogConf:
    """
    Attributes:
        dbfs (Union[Unset, DbfsStorageInfo]):
    """

    dbfs: Union[Unset, "DbfsStorageInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dbfs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dbfs, Unset):
            dbfs = self.dbfs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dbfs is not UNSET:
            field_dict["dbfs"] = dbfs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dbfs_storage_info import DbfsStorageInfo

        d = src_dict.copy()
        _dbfs = d.pop("dbfs", UNSET)
        dbfs: Union[Unset, DbfsStorageInfo]
        if isinstance(_dbfs, Unset):
            dbfs = UNSET
        else:
            dbfs = DbfsStorageInfo.from_dict(_dbfs)

        cluster_log_conf = cls(
            dbfs=dbfs,
        )

        cluster_log_conf.additional_properties = d
        return cluster_log_conf

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
