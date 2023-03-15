from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maven_library import MavenLibrary
    from ..models.python_py_pi_library import PythonPyPiLibrary
    from ..models.r_cran_library import RCranLibrary


T = TypeVar("T", bound="Library")


@attr.s(auto_attribs=True)
class Library:
    """
    Attributes:
        jar (Union[Unset, str]): If jar, URI of the JAR to be installed. DBFS and ADLS (`abfss`) URIs are supported. For
            example: `{ "jar": "dbfs:/mnt/databricks/library.jar" }` or `{ "jar": "abfss://my-bucket/library.jar" }`. If
            ADLS is used, make sure the cluster has read access on the library. Example: dbfs:/my-jar.jar.
        egg (Union[Unset, str]): If egg, URI of the egg to be installed. DBFS and ADLS URIs are supported. For example:
            `{ "egg": "dbfs:/my/egg" }` or `{ "egg": "abfss://my-bucket/egg" }`. Example: dbfs:/my/egg.
        whl (Union[Unset, str]): If whl, URI of the wheel or zipped wheels to be installed. DBFS and ADLS URIs are
            supported. For example: `{ "whl": "dbfs:/my/whl" }` or `{ "whl": "abfss://my-bucket/whl" }`. If ADLS is used,
            make sure the cluster has read access on the library. Also the wheel file name needs to use the [correct
            convention](https://www.python.org/dev/peps/pep-0427/#file-format). If zipped wheels are to be installed, the
            file name suffix should be `.wheelhouse.zip`. Example: dbfs:/my/whl.
        pypi (Union[Unset, PythonPyPiLibrary]):
        maven (Union[Unset, MavenLibrary]):
        cran (Union[Unset, RCranLibrary]):
    """

    jar: Union[Unset, str] = UNSET
    egg: Union[Unset, str] = UNSET
    whl: Union[Unset, str] = UNSET
    pypi: Union[Unset, "PythonPyPiLibrary"] = UNSET
    maven: Union[Unset, "MavenLibrary"] = UNSET
    cran: Union[Unset, "RCranLibrary"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jar = self.jar
        egg = self.egg
        whl = self.whl
        pypi: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pypi, Unset):
            pypi = self.pypi.to_dict()

        maven: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.maven, Unset):
            maven = self.maven.to_dict()

        cran: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cran, Unset):
            cran = self.cran.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jar is not UNSET:
            field_dict["jar"] = jar
        if egg is not UNSET:
            field_dict["egg"] = egg
        if whl is not UNSET:
            field_dict["whl"] = whl
        if pypi is not UNSET:
            field_dict["pypi"] = pypi
        if maven is not UNSET:
            field_dict["maven"] = maven
        if cran is not UNSET:
            field_dict["cran"] = cran

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.maven_library import MavenLibrary
        from ..models.python_py_pi_library import PythonPyPiLibrary
        from ..models.r_cran_library import RCranLibrary

        d = src_dict.copy()
        jar = d.pop("jar", UNSET)

        egg = d.pop("egg", UNSET)

        whl = d.pop("whl", UNSET)

        _pypi = d.pop("pypi", UNSET)
        pypi: Union[Unset, PythonPyPiLibrary]
        if isinstance(_pypi, Unset):
            pypi = UNSET
        else:
            pypi = PythonPyPiLibrary.from_dict(_pypi)

        _maven = d.pop("maven", UNSET)
        maven: Union[Unset, MavenLibrary]
        if isinstance(_maven, Unset):
            maven = UNSET
        else:
            maven = MavenLibrary.from_dict(_maven)

        _cran = d.pop("cran", UNSET)
        cran: Union[Unset, RCranLibrary]
        if isinstance(_cran, Unset):
            cran = UNSET
        else:
            cran = RCranLibrary.from_dict(_cran)

        library = cls(
            jar=jar,
            egg=egg,
            whl=whl,
            pypi=pypi,
            maven=maven,
            cran=cran,
        )

        library.additional_properties = d
        return library

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
