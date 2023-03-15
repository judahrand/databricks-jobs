from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.job_settings_format import JobSettingsFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cron_schedule import CronSchedule
    from ..models.git_branch_source import GitBranchSource
    from ..models.git_commit_source import GitCommitSource
    from ..models.git_snapshot_source import GitSnapshotSource
    from ..models.git_tag_source import GitTagSource
    from ..models.job_cluster import JobCluster
    from ..models.job_email_notifications import JobEmailNotifications
    from ..models.job_settings_tags import JobSettingsTags
    from ..models.job_task_settings import JobTaskSettings
    from ..models.webhook_notifications import WebhookNotifications


T = TypeVar("T", bound="JobSettings")


@attr.s(auto_attribs=True)
class JobSettings:
    """
    Attributes:
        name (Union[Unset, str]): An optional name for the job. Default: 'Untitled'. Example: A multitask job.
        tags (Union[Unset, JobSettingsTags]): A map of tags associated with the job. These are forwarded to the cluster
            as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags
            can be added to the job. Example: {'cost-center': 'engineering', 'team': 'jobs'}.
        tasks (Union[Unset, List['JobTaskSettings']]): A list of task specifications to be executed by this job.
            Example: [{'task_key': 'Sessionize', 'description': 'Extracts session data from events', 'depends_on': [],
            'existing_cluster_id': '0923-164208-meows279', 'spark_jar_task': {'main_class_name':
            'com.databricks.Sessionize', 'parameters': ['--data', 'dbfs:/path/to/data.json']}, 'libraries': [{'jar':
            'dbfs:/mnt/databricks/Sessionize.jar'}], 'timeout_seconds': 86400, 'max_retries': 3,
            'min_retry_interval_millis': 2000, 'retry_on_timeout': False}, {'task_key': 'Orders_Ingest', 'description':
            'Ingests order data', 'depends_on': [], 'job_cluster_key': 'auto_scaling_cluster', 'spark_jar_task':
            {'main_class_name': 'com.databricks.OrdersIngest', 'parameters': ['--data', 'dbfs:/path/to/order-data.json']},
            'libraries': [{'jar': 'dbfs:/mnt/databricks/OrderIngest.jar'}], 'timeout_seconds': 86400, 'max_retries': 3,
            'min_retry_interval_millis': 2000, 'retry_on_timeout': False}, {'task_key': 'Match', 'description': 'Matches
            orders with user sessions', 'depends_on': [{'task_key': 'Orders_Ingest'}, {'task_key': 'Sessionize'}],
            'new_cluster': {'spark_version': '7.3.x-scala2.12', 'node_type_id': 'Standard_D3_v2', 'spark_conf':
            {'spark.speculation': True}, 'azure_attributes': {'availability': 'SPOT_WITH_FALLBACK_AZURE'}, 'autoscale':
            {'min_workers': 2, 'max_workers': 16}}, 'notebook_task': {'notebook_path':
            '/Users/user.name@databricks.com/Match', 'source': 'WORKSPACE', 'base_parameters': {'name': 'John Doe', 'age':
            '35'}}, 'timeout_seconds': 86400, 'max_retries': 3, 'min_retry_interval_millis': 2000, 'retry_on_timeout':
            False}].
        job_clusters (Union[Unset, List['JobCluster']]): A list of job cluster specifications that can be shared and
            reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent
            libraries in task settings. Example: [{'job_cluster_key': 'auto_scaling_cluster', 'new_cluster':
            {'spark_version': '7.3.x-scala2.12', 'node_type_id': 'Standard_D3_v2', 'spark_conf': {'spark.speculation':
            True}, 'azure_attributes': {'availability': 'SPOT_WITH_FALLBACK_AZURE'}, 'autoscale': {'min_workers': 2,
            'max_workers': 16}}}].
        email_notifications (Union[Unset, JobEmailNotifications]):
        webhook_notifications (Union[Unset, WebhookNotifications]):
        timeout_seconds (Union[Unset, int]): An optional timeout applied to each run of this job. The default behavior
            is to have no timeout. Example: 86400.
        schedule (Union[Unset, CronSchedule]):
        max_concurrent_runs (Union[Unset, int]): An optional maximum allowed number of concurrent runs of the job.

            Set this value if you want to be able to execute multiple runs of the same job concurrently. This is useful for
            example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each
            other, or if you want to trigger multiple runs which differ by their input parameters.

            This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent
            active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from then on, new
            runs are skipped unless there are fewer than 3 active runs.

            This value cannot exceed 1000\. Setting this value to 0 causes all new runs to be skipped. The default behavior
            is to allow only 1 concurrent run. Example: 10.
        git_source (Union['GitBranchSource', 'GitCommitSource', 'GitSnapshotSource', 'GitTagSource', Unset]): This
            functionality is in Public Preview.

            An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.
            Example: {'git_url': 'https://github.com/databricks/databricks-cli', 'git_branch': 'main', 'git_provider':
            'gitHub'}.
        format_ (Union[Unset, JobSettingsFormat]): Used to tell what is the format of the job. This field is ignored in
            Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`. Example:
            MULTI_TASK.
    """

    name: Union[Unset, str] = "Untitled"
    tags: Union[Unset, "JobSettingsTags"] = UNSET
    tasks: Union[Unset, List["JobTaskSettings"]] = UNSET
    job_clusters: Union[Unset, List["JobCluster"]] = UNSET
    email_notifications: Union[Unset, "JobEmailNotifications"] = UNSET
    webhook_notifications: Union[Unset, "WebhookNotifications"] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    schedule: Union[Unset, "CronSchedule"] = UNSET
    max_concurrent_runs: Union[Unset, int] = UNSET
    git_source: Union["GitBranchSource", "GitCommitSource", "GitSnapshotSource", "GitTagSource", Unset] = UNSET
    format_: Union[Unset, JobSettingsFormat] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.git_branch_source import GitBranchSource
        from ..models.git_commit_source import GitCommitSource
        from ..models.git_tag_source import GitTagSource

        name = self.name
        tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()

                tasks.append(tasks_item)

        job_clusters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.job_clusters, Unset):
            job_clusters = []
            for job_clusters_item_data in self.job_clusters:
                job_clusters_item = job_clusters_item_data.to_dict()

                job_clusters.append(job_clusters_item)

        email_notifications: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.email_notifications, Unset):
            email_notifications = self.email_notifications.to_dict()

        webhook_notifications: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.webhook_notifications, Unset):
            webhook_notifications = self.webhook_notifications.to_dict()

        timeout_seconds = self.timeout_seconds
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        max_concurrent_runs = self.max_concurrent_runs
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

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if job_clusters is not UNSET:
            field_dict["job_clusters"] = job_clusters
        if email_notifications is not UNSET:
            field_dict["email_notifications"] = email_notifications
        if webhook_notifications is not UNSET:
            field_dict["webhook_notifications"] = webhook_notifications
        if timeout_seconds is not UNSET:
            field_dict["timeout_seconds"] = timeout_seconds
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if max_concurrent_runs is not UNSET:
            field_dict["max_concurrent_runs"] = max_concurrent_runs
        if git_source is not UNSET:
            field_dict["git_source"] = git_source
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cron_schedule import CronSchedule
        from ..models.git_branch_source import GitBranchSource
        from ..models.git_commit_source import GitCommitSource
        from ..models.git_snapshot_source import GitSnapshotSource
        from ..models.git_tag_source import GitTagSource
        from ..models.job_cluster import JobCluster
        from ..models.job_email_notifications import JobEmailNotifications
        from ..models.job_settings_tags import JobSettingsTags
        from ..models.job_task_settings import JobTaskSettings
        from ..models.webhook_notifications import WebhookNotifications

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, JobSettingsTags]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = JobSettingsTags.from_dict(_tags)

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = JobTaskSettings.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        job_clusters = []
        _job_clusters = d.pop("job_clusters", UNSET)
        for job_clusters_item_data in _job_clusters or []:
            job_clusters_item = JobCluster.from_dict(job_clusters_item_data)

            job_clusters.append(job_clusters_item)

        _email_notifications = d.pop("email_notifications", UNSET)
        email_notifications: Union[Unset, JobEmailNotifications]
        if isinstance(_email_notifications, Unset):
            email_notifications = UNSET
        else:
            email_notifications = JobEmailNotifications.from_dict(_email_notifications)

        _webhook_notifications = d.pop("webhook_notifications", UNSET)
        webhook_notifications: Union[Unset, WebhookNotifications]
        if isinstance(_webhook_notifications, Unset):
            webhook_notifications = UNSET
        else:
            webhook_notifications = WebhookNotifications.from_dict(_webhook_notifications)

        timeout_seconds = d.pop("timeout_seconds", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, CronSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = CronSchedule.from_dict(_schedule)

        max_concurrent_runs = d.pop("max_concurrent_runs", UNSET)

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

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, JobSettingsFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = JobSettingsFormat(_format_)

        job_settings = cls(
            name=name,
            tags=tags,
            tasks=tasks,
            job_clusters=job_clusters,
            email_notifications=email_notifications,
            webhook_notifications=webhook_notifications,
            timeout_seconds=timeout_seconds,
            schedule=schedule,
            max_concurrent_runs=max_concurrent_runs,
            git_source=git_source,
            format_=format_,
        )

        job_settings.additional_properties = d
        return job_settings

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
