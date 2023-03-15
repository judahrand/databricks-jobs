from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_branch_source import GitBranchSource
    from ..models.git_commit_source import GitCommitSource
    from ..models.git_snapshot_source import GitSnapshotSource
    from ..models.git_tag_source import GitTagSource
    from ..models.run_submit_task_settings import RunSubmitTaskSettings
    from ..models.webhook_notifications import WebhookNotifications


T = TypeVar("T", bound="RunSubmitSettings")


@attr.s(auto_attribs=True)
class RunSubmitSettings:
    """
    Attributes:
        tasks (Union[Unset, List['RunSubmitTaskSettings']]):  Example: [{'task_key': 'Sessionize', 'description':
            'Extracts session data from events', 'depends_on': [], 'existing_cluster_id': '0923-164208-meows279',
            'spark_jar_task': {'main_class_name': 'com.databricks.Sessionize', 'parameters': ['--data',
            'dbfs:/path/to/data.json']}, 'libraries': [{'jar': 'dbfs:/mnt/databricks/Sessionize.jar'}], 'timeout_seconds':
            86400}, {'task_key': 'Orders_Ingest', 'description': 'Ingests order data', 'depends_on': [],
            'existing_cluster_id': '0923-164208-meows279', 'spark_jar_task': {'main_class_name':
            'com.databricks.OrdersIngest', 'parameters': ['--data', 'dbfs:/path/to/order-data.json']}, 'libraries': [{'jar':
            'dbfs:/mnt/databricks/OrderIngest.jar'}], 'timeout_seconds': 86400}, {'task_key': 'Match', 'description':
            'Matches orders with user sessions', 'depends_on': [{'task_key': 'Orders_Ingest'}, {'task_key': 'Sessionize'}],
            'new_cluster': {'spark_version': '7.3.x-scala2.12', 'node_type_id': 'Standard_D3_v2', 'spark_conf':
            {'spark.speculation': True}, 'azure_attributes': {'availability': 'SPOT_WITH_FALLBACK_AZURE'}, 'autoscale':
            {'min_workers': 2, 'max_workers': 16}}, 'notebook_task': {'notebook_path':
            '/Users/user.name@databricks.com/Match', 'source': 'WORKSPACE', 'base_parameters': {'name': 'John Doe', 'age':
            '35'}}, 'timeout_seconds': 86400}].
        run_name (Union[Unset, str]): An optional name for the run. The default value is `Untitled`. Example: A
            multitask job run.
        webhook_notifications (Union[Unset, WebhookNotifications]):
        git_source (Union['GitBranchSource', 'GitCommitSource', 'GitSnapshotSource', 'GitTagSource', Unset]): This
            functionality is in Public Preview.

            An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.
            Example: {'git_url': 'https://github.com/databricks/databricks-cli', 'git_branch': 'main', 'git_provider':
            'gitHub'}.
        timeout_seconds (Union[Unset, int]): An optional timeout applied to each run of this job. The default behavior
            is to have no timeout. Example: 86400.
        idempotency_token (Union[Unset, str]): An optional token that can be used to guarantee the idempotency of job
            run requests. If a run with the provided token already exists, the request does not create a new run but returns
            the ID of the existing run instead. If a run with the provided token is deleted, an error is returned.

            If you specify the idempotency token, upon failure you can retry until the request succeeds. Databricks
            guarantees that exactly one run is launched with that idempotency token.

            This token must have at most 64 characters.

            For more information, see [How to ensure idempotency for
            jobs](https://docs.microsoft.com/azure/databricks/kb/jobs/jobs-idempotency). Example:
            8f018174-4792-40d5-bcbc-3e6a527352c8.
    """

    tasks: Union[Unset, List["RunSubmitTaskSettings"]] = UNSET
    run_name: Union[Unset, str] = UNSET
    webhook_notifications: Union[Unset, "WebhookNotifications"] = UNSET
    git_source: Union["GitBranchSource", "GitCommitSource", "GitSnapshotSource", "GitTagSource", Unset] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    idempotency_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.git_branch_source import GitBranchSource
        from ..models.git_commit_source import GitCommitSource
        from ..models.git_tag_source import GitTagSource

        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()

                tasks.append(tasks_item)

        run_name = self.run_name
        webhook_notifications: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.webhook_notifications, Unset):
            webhook_notifications = self.webhook_notifications.to_dict()

        git_source: Union[Dict[str, Any], Unset]
        if isinstance(self.git_source, Unset):
            git_source = UNSET

        elif isinstance(self.git_source, GitBranchSource):
            git_source = self.git_source.to_dict()

        elif isinstance(self.git_source, GitTagSource):
            git_source = self.git_source.to_dict()

        elif isinstance(self.git_source, GitCommitSource):
            git_source = self.git_source.to_dict()

        else:
            git_source = self.git_source.to_dict()

        timeout_seconds = self.timeout_seconds
        idempotency_token = self.idempotency_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if run_name is not UNSET:
            field_dict["run_name"] = run_name
        if webhook_notifications is not UNSET:
            field_dict["webhook_notifications"] = webhook_notifications
        if git_source is not UNSET:
            field_dict["git_source"] = git_source
        if timeout_seconds is not UNSET:
            field_dict["timeout_seconds"] = timeout_seconds
        if idempotency_token is not UNSET:
            field_dict["idempotency_token"] = idempotency_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.git_branch_source import GitBranchSource
        from ..models.git_commit_source import GitCommitSource
        from ..models.git_snapshot_source import GitSnapshotSource
        from ..models.git_tag_source import GitTagSource
        from ..models.run_submit_task_settings import RunSubmitTaskSettings
        from ..models.webhook_notifications import WebhookNotifications

        d = src_dict.copy()
        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = RunSubmitTaskSettings.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        run_name = d.pop("run_name", UNSET)

        _webhook_notifications = d.pop("webhook_notifications", UNSET)
        webhook_notifications: Union[Unset, WebhookNotifications]
        if isinstance(_webhook_notifications, Unset):
            webhook_notifications = UNSET
        else:
            webhook_notifications = WebhookNotifications.from_dict(_webhook_notifications)

        def _parse_git_source(
            data: object,
        ) -> Union["GitBranchSource", "GitCommitSource", "GitSnapshotSource", "GitTagSource", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_git_source_type_0 = GitBranchSource.from_dict(data)

                return componentsschemas_git_source_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_git_source_type_1 = GitTagSource.from_dict(data)

                return componentsschemas_git_source_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_git_source_type_2 = GitCommitSource.from_dict(data)

                return componentsschemas_git_source_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_git_source_type_3 = GitSnapshotSource.from_dict(data)

            return componentsschemas_git_source_type_3

        git_source = _parse_git_source(d.pop("git_source", UNSET))

        timeout_seconds = d.pop("timeout_seconds", UNSET)

        idempotency_token = d.pop("idempotency_token", UNSET)

        run_submit_settings = cls(
            tasks=tasks,
            run_name=run_name,
            webhook_notifications=webhook_notifications,
            git_source=git_source,
            timeout_seconds=timeout_seconds,
            idempotency_token=idempotency_token,
        )

        run_submit_settings.additional_properties = d
        return run_submit_settings

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
