from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library import Library
    from ..models.new_cluster import NewCluster


T = TypeVar("T", bound="ClusterSpec")


@attr.s(auto_attribs=True)
class ClusterSpec:
    """
    Attributes:
        existing_cluster_id (Union[Unset, str]): If existing_cluster_id, the ID of an existing cluster that is used for
            all runs of this job. When running jobs on an existing cluster, you may need to manually restart the cluster if
            it stops responding. We suggest running jobs on new clusters for greater reliability. Example:
            0923-164208-meows279.
        new_cluster (Union[Unset, NewCluster]):
        libraries (Union[Unset, List['Library']]): An optional list of libraries to be installed on the cluster that
            executes the job. The default value is an empty list.
    """

    existing_cluster_id: Union[Unset, str] = UNSET
    new_cluster: Union[Unset, "NewCluster"] = UNSET
    libraries: Union[Unset, List["Library"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        existing_cluster_id = self.existing_cluster_id
        new_cluster: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_cluster, Unset):
            new_cluster = self.new_cluster.to_dict()

        libraries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.libraries, Unset):
            libraries = []
            for libraries_item_data in self.libraries:
                libraries_item = libraries_item_data.to_dict()

                libraries.append(libraries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if existing_cluster_id is not UNSET:
            field_dict["existing_cluster_id"] = existing_cluster_id
        if new_cluster is not UNSET:
            field_dict["new_cluster"] = new_cluster
        if libraries is not UNSET:
            field_dict["libraries"] = libraries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.library import Library
        from ..models.new_cluster import NewCluster

        d = src_dict.copy()
        existing_cluster_id = d.pop("existing_cluster_id", UNSET)

        _new_cluster = d.pop("new_cluster", UNSET)
        new_cluster: Union[Unset, NewCluster]
        if isinstance(_new_cluster, Unset):
            new_cluster = UNSET
        else:
            new_cluster = NewCluster.from_dict(_new_cluster)

        libraries = []
        _libraries = d.pop("libraries", UNSET)
        for libraries_item_data in _libraries or []:
            libraries_item = Library.from_dict(libraries_item_data)

            libraries.append(libraries_item)

        cluster_spec = cls(
            existing_cluster_id=existing_cluster_id,
            new_cluster=new_cluster,
            libraries=libraries,
        )

        cluster_spec.additional_properties = d
        return cluster_spec

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
