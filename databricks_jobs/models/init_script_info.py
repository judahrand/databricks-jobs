from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adlsgen_2_info import Adlsgen2Info
    from ..models.dbfs_storage_info import DbfsStorageInfo
    from ..models.file_storage_info import FileStorageInfo


T = TypeVar("T", bound="InitScriptInfo")


@attr.s(auto_attribs=True)
class InitScriptInfo:
    """
    Attributes:
        dbfs (Union[Unset, DbfsStorageInfo]):
        file (Union[Unset, FileStorageInfo]):
        abfss (Union[Unset, Adlsgen2Info]):
    """

    dbfs: Union[Unset, "DbfsStorageInfo"] = UNSET
    file: Union[Unset, "FileStorageInfo"] = UNSET
    abfss: Union[Unset, "Adlsgen2Info"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dbfs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dbfs, Unset):
            dbfs = self.dbfs.to_dict()

        file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        abfss: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.abfss, Unset):
            abfss = self.abfss.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dbfs is not UNSET:
            field_dict["dbfs"] = dbfs
        if file is not UNSET:
            field_dict["file"] = file
        if abfss is not UNSET:
            field_dict["abfss"] = abfss

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adlsgen_2_info import Adlsgen2Info
        from ..models.dbfs_storage_info import DbfsStorageInfo
        from ..models.file_storage_info import FileStorageInfo

        d = src_dict.copy()
        _dbfs = d.pop("dbfs", UNSET)
        dbfs: Union[Unset, DbfsStorageInfo]
        if isinstance(_dbfs, Unset):
            dbfs = UNSET
        else:
            dbfs = DbfsStorageInfo.from_dict(_dbfs)

        _file = d.pop("file", UNSET)
        file: Union[Unset, FileStorageInfo]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FileStorageInfo.from_dict(_file)

        _abfss = d.pop("abfss", UNSET)
        abfss: Union[Unset, Adlsgen2Info]
        if isinstance(_abfss, Unset):
            abfss = UNSET
        else:
            abfss = Adlsgen2Info.from_dict(_abfss)

        init_script_info = cls(
            dbfs=dbfs,
            file=file,
            abfss=abfss,
        )

        init_script_info.additional_properties = d
        return init_script_info

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
