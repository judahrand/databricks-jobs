from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.run_life_cycle_state import RunLifeCycleState
from ..models.run_result_state import RunResultState
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunState")


@attr.s(auto_attribs=True)
class RunState:
    """The result and lifecycle state of the run.

    Attributes:
        life_cycle_state (Union[Unset, RunLifeCycleState]): * `PENDING`: The run has been triggered. If there is not
            already an active run of the same job, the cluster and execution context are being prepared. If there is already
            an active run of the same job, the run immediately transitions into the `SKIPPED` state without preparing any
            resources.
            * `RUNNING`: The task of this run is being executed.
            * `TERMINATING`: The task of this run has completed, and the cluster and execution context are being cleaned up.
            * `TERMINATED`: The task of this run has completed, and the cluster and execution context have been cleaned up.
            This state is terminal.
            * `SKIPPED`: This run was aborted because a previous run of the same job was already active. This state is
            terminal.
            * `INTERNAL_ERROR`: An exceptional state that indicates a failure in the Jobs service, such as network failure
            over a long period. If a run on a new cluster ends in the `INTERNAL_ERROR` state, the Jobs service terminates
            the cluster as soon as possible. This state is terminal.
            * `BLOCKED`: The run is blocked on an upstream dependency.
            * `WAITING_FOR_RETRY`: The run is waiting for a retry.
        result_state (Union[Unset, RunResultState]): * `SUCCESS`: The task completed successfully.
            * `FAILED`: The task completed with an error.
            * `TIMEDOUT`: The run was stopped after reaching the timeout.
            * `CANCELED`: The run was canceled at user request.
        user_cancelled_or_timedout (Union[Unset, bool]): Whether a run was canceled manually by a user or by the
            scheduler because the run timed out.
        state_message (Union[Unset, str]): A descriptive message for the current state. This field is unstructured, and
            its exact format is subject to change.
    """

    life_cycle_state: Union[Unset, RunLifeCycleState] = UNSET
    result_state: Union[Unset, RunResultState] = UNSET
    user_cancelled_or_timedout: Union[Unset, bool] = UNSET
    state_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        life_cycle_state: Union[Unset, str] = UNSET
        if not isinstance(self.life_cycle_state, Unset):
            life_cycle_state = self.life_cycle_state.value

        result_state: Union[Unset, str] = UNSET
        if not isinstance(self.result_state, Unset):
            result_state = self.result_state.value

        user_cancelled_or_timedout = self.user_cancelled_or_timedout
        state_message = self.state_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if life_cycle_state is not UNSET:
            field_dict["life_cycle_state"] = life_cycle_state
        if result_state is not UNSET:
            field_dict["result_state"] = result_state
        if user_cancelled_or_timedout is not UNSET:
            field_dict["user_cancelled_or_timedout"] = user_cancelled_or_timedout
        if state_message is not UNSET:
            field_dict["state_message"] = state_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _life_cycle_state = d.pop("life_cycle_state", UNSET)
        life_cycle_state: Union[Unset, RunLifeCycleState]
        if isinstance(_life_cycle_state, Unset):
            life_cycle_state = UNSET
        else:
            life_cycle_state = RunLifeCycleState(_life_cycle_state)

        _result_state = d.pop("result_state", UNSET)
        result_state: Union[Unset, RunResultState]
        if isinstance(_result_state, Unset):
            result_state = UNSET
        else:
            result_state = RunResultState(_result_state)

        user_cancelled_or_timedout = d.pop("user_cancelled_or_timedout", UNSET)

        state_message = d.pop("state_message", UNSET)

        run_state = cls(
            life_cycle_state=life_cycle_state,
            result_state=result_state,
            user_cancelled_or_timedout=user_cancelled_or_timedout,
            state_message=state_message,
        )

        run_state.additional_properties = d
        return run_state

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
