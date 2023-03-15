from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.git_provider import GitProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitBranchSource")


@attr.s(auto_attribs=True)
class GitBranchSource:
    """This functionality is in Public Preview.

    An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.

        Example:
            {'git_url': 'https://github.com/databricks/databricks-cli', 'git_branch': 'main', 'git_provider': 'gitHub'}

        Attributes:
            git_url (Union[Unset, str]): URL of the repository to be cloned by this job.
                The maximum length is 300 characters. Example: https://github.com/databricks/databricks-cli.
            git_provider (Union[Unset, GitProvider]): Unique identifier of the service used to host the Git repository. The
                value is case insensitive. Example: github.
            git_branch (Union[Unset, str]): Name of the branch to be checked out and used by this job. This field cannot be
                specified in conjunction with git_tag or git_commit.
                The maximum length is 255 characters. Example: main.
    """

    git_url: Union[Unset, str] = UNSET
    git_provider: Union[Unset, GitProvider] = UNSET
    git_branch: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        git_url = self.git_url
        git_provider: Union[Unset, str] = UNSET
        if not isinstance(self.git_provider, Unset):
            git_provider = self.git_provider.value

        git_branch = self.git_branch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if git_url is not UNSET:
            field_dict["git_url"] = git_url
        if git_provider is not UNSET:
            field_dict["git_provider"] = git_provider
        if git_branch is not UNSET:
            field_dict["git_branch"] = git_branch

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

        git_branch = d.pop("git_branch", UNSET)

        git_branch_source = cls(
            git_url=git_url,
            git_provider=git_provider,
            git_branch=git_branch,
        )

        git_branch_source.additional_properties = d
        return git_branch_source

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
