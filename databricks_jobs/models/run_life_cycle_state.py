from enum import Enum


class RunLifeCycleState(str, Enum):
    TERMINATED = "TERMINATED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    TERMINATING = "TERMINATING"
    SKIPPED = "SKIPPED"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    BLOCKED = "BLOCKED"
    WAITING_FOR_RETRY = "WAITING_FOR_RETRY"

    def __str__(self) -> str:
        return str(self.value)