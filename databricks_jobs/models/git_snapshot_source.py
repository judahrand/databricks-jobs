from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.git_provider import GitProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitSnapshotSource")


@attr.s(auto_attribs=True)
class GitSnapshotSource:
    """This functionality is in Public Preview.

    An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.

        Example:
            {'git_url': 'https://github.com/databricks/databricks-cli', 'git_snapshot': {'used_commit':
                '4506fdf41e9fa98090570a34df7a5bce163ff15f'}, 'git_provider': 'gitHub'}

        Attributes:
            git_url (Union[Unset, str]): URL of the repository to be cloned by this job.
                The maximum length is 300 characters. Example: https://github.com/databricks/databricks-cli.
            git_provider (Union[Unset, GitProvider]): Unique identifier of the service used to host the Git repository. The
                value is case insensitive. Example: github.
            git_snapshot (Union[Unset, GitSnapshotSource]): This functionality is in Public Preview.

                An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.
                Example: {'git_url': 'https://github.com/databricks/databricks-cli', 'git_snapshot': {'used_commit':
                '4506fdf41e9fa98090570a34df7a5bce163ff15f'}, 'git_provider': 'gitHub'}.
    """

    git_url: Union[Unset, str] = UNSET
    git_provider: Union[Unset, GitProvider] = UNSET
    git_snapshot: Union[Unset, "GitSnapshotSource"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        git_url = self.git_url
        git_provider: Union[Unset, str] = UNSET
        if not isinstance(self.git_provider, Unset):
            git_provider = self.git_provider.value

        git_snapshot: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.git_snapshot, Unset):
            git_snapshot = self.git_snapshot.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if git_url is not UNSET:
            field_dict["git_url"] = git_url
        if git_provider is not UNSET:
            field_dict["git_provider"] = git_provider
        if git_snapshot is not UNSET:
            field_dict["git_snapshot"] = git_snapshot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        git_url = d.pop("git_url", UNSET)

        _git_provider = d.pop("git_provider", UNSET)
        git_provider: Union[Unset, GitProvider]
        if isinstance(_git_provider, Unset):
            git_provider = UNSET
        else:
            git_provider = GitProvider(_git_provider)

        _git_snapshot = d.pop("git_snapshot", UNSET)
        git_snapshot: Union[Unset, GitSnapshotSource]
        if isinstance(_git_snapshot, Unset):
            git_snapshot = UNSET
        else:
            git_snapshot = GitSnapshotSource.from_dict(_git_snapshot)

        git_snapshot_source = cls(
            git_url=git_url,
            git_provider=git_provider,
            git_snapshot=git_snapshot,
        )

        git_snapshot_source.additional_properties = d
        return git_snapshot_source

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
