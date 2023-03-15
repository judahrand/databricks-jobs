from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RunNowInput")


@attr.s(auto_attribs=True)
class RunNowInput:
    """
    Attributes:
        job_id (Union[Unset, int]): The ID of the job to be executed Example: 11223344.
        idempotency_token (Union[Unset, str]): An optional token to guarantee the idempotency of job run requests. If a
            run with the provided token already exists, the request does not create a new run but returns the ID of the
            existing run instead. If a run with the provided token is deleted, an error is returned.

            If you specify the idempotency token, upon failure you can retry until the request succeeds. Databricks
            guarantees that exactly one run is launched with that idempotency token.

            This token must have at most 64 characters.

            For more information, see [How to ensure idempotency for
            jobs](https://docs.microsoft.com/azure/databricks/kb/jobs/jobs-idempotency). Example:
            8f018174-4792-40d5-bcbc-3e6a527352c8.
    """

    job_id: Union[Unset, int] = UNSET
    idempotency_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        idempotency_token = self.idempotency_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if idempotency_token is not UNSET:
            field_dict["idempotency_token"] = idempotency_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_id = d.pop("job_id", UNSET)

        idempotency_token = d.pop("idempotency_token", UNSET)

        run_now_input = cls(
            job_id=job_id,
            idempotency_token=idempotency_token,
        )

        run_now_input.additional_properties = d
        return run_now_input

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
