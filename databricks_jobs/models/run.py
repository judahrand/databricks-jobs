from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.run_type import RunType
from ..models.trigger_type import TriggerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_instance import ClusterInstance
    from ..models.cluster_spec import ClusterSpec
    from ..models.cron_schedule import CronSchedule
    from ..models.git_branch_source import GitBranchSource
    from ..models.git_commit_source import GitCommitSource
    from ..models.git_snapshot_source import GitSnapshotSource
    from ..models.git_tag_source import GitTagSource
    from ..models.job_cluster import JobCluster
    from ..models.run_parameters import RunParameters
    from ..models.run_state import RunState
    from ..models.run_task import RunTask


T = TypeVar("T", bound="Run")


@attr.s(auto_attribs=True)
class Run:
    """
    Attributes:
        job_id (Union[Unset, int]): The canonical identifier of the job that contains this run. Example: 11223344.
        run_id (Union[Unset, int]): The canonical identifier of the run. This ID is unique across all runs of all jobs.
            Example: 455644833.
        number_in_job (Union[Unset, int]): A unique identifier for this job run. This is set to the same value as
            `run_id`. Example: 455644833.
        creator_user_name (Union[Unset, str]): The creator user name. This field won’t be included in the response if
            the user has already been deleted. Example: user.name@databricks.com.
        original_attempt_run_id (Union[Unset, int]): If this run is a retry of a prior run attempt, this field contains
            the run_id of the original attempt; otherwise, it is the same as the run_id. Example: 455644833.
        state (Union[Unset, RunState]): The result and lifecycle state of the run.
        schedule (Union[Unset, CronSchedule]):
        tasks (Union[Unset, List['RunTask']]): The list of tasks performed by the run. Each task has its own `run_id`
            which you can use to call `JobsGetOutput` to retrieve the run resutls. Example: [{'run_id': 2112892, 'task_key':
            'Orders_Ingest', 'description': 'Ingests order data', 'job_cluster_key': 'auto_scaling_cluster',
            'spark_jar_task': {'main_class_name': 'com.databricks.OrdersIngest'}, 'libraries': [{'jar':
            'dbfs:/mnt/databricks/OrderIngest.jar'}], 'state': {'life_cycle_state': 'INTERNAL_ERROR', 'result_state':
            'FAILED', 'state_message': "Library installation failed for library due to user error. Error messages:\n'Manage'
            permissions are required to install libraries on a cluster", 'user_cancelled_or_timedout': False},
            'run_page_url': 'https://my-workspace.cloud.databricks.com/#job/39832/run/20', 'start_time': 1629989929660,
            'setup_duration': 0, 'execution_duration': 0, 'cleanup_duration': 0, 'end_time': 1629989930171,
            'cluster_instance': {'cluster_id': '0923-164208-meows279', 'spark_context_id': '4348585301701786933'},
            'attempt_number': 0}, {'run_id': 2112897, 'task_key': 'Match', 'description': 'Matches orders with user
            sessions', 'depends_on': [{'task_key': 'Orders_Ingest'}, {'task_key': 'Sessionize'}], 'new_cluster':
            {'spark_version': '7.3.x-scala2.12', 'node_type_id': 'Standard_D3_v2', 'spark_conf': {'spark.speculation':
            True}, 'azure_attributes': {'availability': 'SPOT_WITH_FALLBACK_AZURE'}, 'autoscale': {'min_workers': 2,
            'max_workers': 16}}, 'notebook_task': {'notebook_path': '/Users/user.name@databricks.com/Match', 'source':
            'WORKSPACE'}, 'state': {'life_cycle_state': 'SKIPPED', 'state_message': 'An upstream task failed.',
            'user_cancelled_or_timedout': False}, 'run_page_url': 'https://my-
            workspace.cloud.databricks.com/#job/39832/run/21', 'start_time': 0, 'setup_duration': 0, 'execution_duration':
            0, 'cleanup_duration': 0, 'end_time': 1629989930238, 'cluster_instance': {'cluster_id': '0923-164208-meows279'},
            'attempt_number': 0}, {'run_id': 2112902, 'task_key': 'Sessionize', 'description': 'Extracts session data from
            events', 'existing_cluster_id': '0923-164208-meows279', 'spark_jar_task': {'main_class_name':
            'com.databricks.Sessionize'}, 'libraries': [{'jar': 'dbfs:/mnt/databricks/Sessionize.jar'}], 'state':
            {'life_cycle_state': 'INTERNAL_ERROR', 'result_state': 'FAILED', 'state_message': "Library installation failed
            for library due to user error. Error messages:\n'Manage' permissions are required to install libraries on a
            cluster", 'user_cancelled_or_timedout': False}, 'run_page_url': 'https://my-
            workspace.cloud.databricks.com/#job/39832/run/22', 'start_time': 1629989929668, 'setup_duration': 0,
            'execution_duration': 0, 'cleanup_duration': 0, 'end_time': 1629989930144, 'cluster_instance': {'cluster_id':
            '0923-164208-meows279', 'spark_context_id': '4348585301701786933'}, 'attempt_number': 0}].
        job_clusters (Union[Unset, List['JobCluster']]): A list of job cluster specifications that can be shared and
            reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent
            libraries in task settings. Example: [{'job_cluster_key': 'auto_scaling_cluster', 'new_cluster':
            {'spark_version': '7.3.x-scala2.12', 'node_type_id': 'Standard_D3_v2', 'spark_conf': {'spark.speculation':
            True}, 'azure_attributes': {'availability': 'SPOT_WITH_FALLBACK_AZURE'}, 'autoscale': {'min_workers': 2,
            'max_workers': 16}}}].
        cluster_spec (Union[Unset, ClusterSpec]):
        cluster_instance (Union[Unset, ClusterInstance]):
        git_source (Union['GitBranchSource', 'GitCommitSource', 'GitSnapshotSource', 'GitTagSource', Unset]): This
            functionality is in Public Preview.

            An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.
            Example: {'git_url': 'https://github.com/databricks/databricks-cli', 'git_branch': 'main', 'git_provider':
            'gitHub'}.
        overriding_parameters (Union[Unset, RunParameters]):
        start_time (Union[Unset, int]): The time at which this run was started in epoch milliseconds (milliseconds since
            1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled
            to run on a new cluster, this is the time the cluster creation call is issued. Example: 1625060460483.
        setup_duration (Union[Unset, int]): The time in milliseconds it took to set up the cluster. For runs that run on
            new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very
            short. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the
            `cleanup_duration`. The `setup_duration` field is set to 0 for multitask job runs. The total duration of a
            multitask job run is the value of the `run_duration` field.
        execution_duration (Union[Unset, int]): The time in milliseconds it took to execute the commands in the JAR or
            notebook until they  completed, failed, timed out, were cancelled, or encountered an unexpected error. The
            duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the  `cleanup_duration`.
            The `execution_duration` field is set to 0 for multitask job runs. The total  duration of a multitask job run is
            the value of the `run_duration` field.
        cleanup_duration (Union[Unset, int]): The time in milliseconds it took to terminate the cluster and clean up any
            associated artifacts. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and
            the `cleanup_duration`. The `cleanup_duration` field is set to 0 for multitask job runs. The total duration of a
            multitask job run is the value of the `run_duration` field.
        end_time (Union[Unset, int]): The time at which this run ended in epoch milliseconds (milliseconds since
            1/1/1970 UTC). This field is set to 0 if the job is still running. Example: 1625060863413.
        run_duration (Union[Unset, int]): The time in milliseconds it took the job run and all of its repairs to finish.
            This field is only set for multitask job runs and not task runs. The duration of a task run is the sum of the
            `setup_duration`, `execution_duration`, and the `cleanup_duration`. Example: 3879812.
        trigger (Union[Unset, TriggerType]): * `PERIODIC`: Schedules that periodically trigger runs, such as a cron
            scheduler.
            * `ONE_TIME`: One time triggers that fire a single run. This occurs you triggered a single run on demand through
            the UI or the API.
            * `RETRY`: Indicates a run that is triggered as a retry of a previously failed run. This occurs when you request
            to re-run the job in case of failures.
        run_name (Union[Unset, str]): An optional name for the run. The maximum allowed length is 4096 bytes in UTF-8
            encoding. Default: 'Untitled'. Example: A multitask job run.
        run_page_url (Union[Unset, str]): The URL to the detail page of the run. Example: https://my-
            workspace.cloud.databricks.com/#job/11223344/run/123.
        run_type (Union[Unset, RunType]): The type of the run.
            * `JOB_RUN` \- Normal job run. A run created with [Run now](https://docs.microsoft.com/azure/databricks/dev-
            tools/api/latest/jobs#operation/JobsRunNow).
            * `WORKFLOW_RUN` \- Workflow run. A run created with
            [dbutils.notebook.run](https://docs.microsoft.com/azure/databricks/dev-tools/databricks-utils#dbutils-workflow).
            * `SUBMIT_RUN` \- Submit run. A run created with [Run Submit](https://docs.microsoft.com/azure/databricks/dev-
            tools/api/latest/jobs#operation/JobsRunsSubmit). Example: JOB_RUN.
        attempt_number (Union[Unset, int]): The sequence number of this run attempt for a triggered job run. The initial
            attempt of a run has an attempt_number of 0\. If the initial run attempt fails, and the job has a retry policy
            (`max_retries` \> 0), subsequent runs are created with an `original_attempt_run_id` of the original attempt’s ID
            and an incrementing `attempt_number`. Runs are retried only until they succeed, and the maximum `attempt_number`
            is the same as the `max_retries` value for the job.
    """

    job_id: Union[Unset, int] = UNSET
    run_id: Union[Unset, int] = UNSET
    number_in_job: Union[Unset, int] = UNSET
    creator_user_name: Union[Unset, str] = UNSET
    original_attempt_run_id: Union[Unset, int] = UNSET
    state: Union[Unset, "RunState"] = UNSET
    schedule: Union[Unset, "CronSchedule"] = UNSET
    tasks: Union[Unset, List["RunTask"]] = UNSET
    job_clusters: Union[Unset, List["JobCluster"]] = UNSET
    cluster_spec: Union[Unset, "ClusterSpec"] = UNSET
    cluster_instance: Union[Unset, "ClusterInstance"] = UNSET
    git_source: Union["GitBranchSource", "GitCommitSource", "GitSnapshotSource", "GitTagSource", Unset] = UNSET
    overriding_parameters: Union[Unset, "RunParameters"] = UNSET
    start_time: Union[Unset, int] = UNSET
    setup_duration: Union[Unset, int] = UNSET
    execution_duration: Union[Unset, int] = UNSET
    cleanup_duration: Union[Unset, int] = UNSET
    end_time: Union[Unset, int] = UNSET
    run_duration: Union[Unset, int] = UNSET
    trigger: Union[Unset, TriggerType] = UNSET
    run_name: Union[Unset, str] = "Untitled"
    run_page_url: Union[Unset, str] = UNSET
    run_type: Union[Unset, RunType] = UNSET
    attempt_number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.git_branch_source import GitBranchSource
        from ..models.git_commit_source import GitCommitSource
        from ..models.git_tag_source import GitTagSource

        job_id = self.job_id
        run_id = self.run_id
        number_in_job = self.number_in_job
        creator_user_name = self.creator_user_name
        original_attempt_run_id = self.original_attempt_run_id
        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

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

        cluster_spec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_spec, Unset):
            cluster_spec = self.cluster_spec.to_dict()

        cluster_instance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_instance, Unset):
            cluster_instance = self.cluster_instance.to_dict()

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

        overriding_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.overriding_parameters, Unset):
            overriding_parameters = self.overriding_parameters.to_dict()

        start_time = self.start_time
        setup_duration = self.setup_duration
        execution_duration = self.execution_duration
        cleanup_duration = self.cleanup_duration
        end_time = self.end_time
        run_duration = self.run_duration
        trigger: Union[Unset, str] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        run_name = self.run_name
        run_page_url = self.run_page_url
        run_type: Union[Unset, str] = UNSET
        if not isinstance(self.run_type, Unset):
            run_type = self.run_type.value

        attempt_number = self.attempt_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if number_in_job is not UNSET:
            field_dict["number_in_job"] = number_in_job
        if creator_user_name is not UNSET:
            field_dict["creator_user_name"] = creator_user_name
        if original_attempt_run_id is not UNSET:
            field_dict["original_attempt_run_id"] = original_attempt_run_id
        if state is not UNSET:
            field_dict["state"] = state
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if job_clusters is not UNSET:
            field_dict["job_clusters"] = job_clusters
        if cluster_spec is not UNSET:
            field_dict["cluster_spec"] = cluster_spec
        if cluster_instance is not UNSET:
            field_dict["cluster_instance"] = cluster_instance
        if git_source is not UNSET:
            field_dict["git_source"] = git_source
        if overriding_parameters is not UNSET:
            field_dict["overriding_parameters"] = overriding_parameters
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if setup_duration is not UNSET:
            field_dict["setup_duration"] = setup_duration
        if execution_duration is not UNSET:
            field_dict["execution_duration"] = execution_duration
        if cleanup_duration is not UNSET:
            field_dict["cleanup_duration"] = cleanup_duration
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if run_duration is not UNSET:
            field_dict["run_duration"] = run_duration
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if run_name is not UNSET:
            field_dict["run_name"] = run_name
        if run_page_url is not UNSET:
            field_dict["run_page_url"] = run_page_url
        if run_type is not UNSET:
            field_dict["run_type"] = run_type
        if attempt_number is not UNSET:
            field_dict["attempt_number"] = attempt_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cluster_instance import ClusterInstance
        from ..models.cluster_spec import ClusterSpec
        from ..models.cron_schedule import CronSchedule
        from ..models.git_branch_source import GitBranchSource
        from ..models.git_commit_source import GitCommitSource
        from ..models.git_snapshot_source import GitSnapshotSource
        from ..models.git_tag_source import GitTagSource
        from ..models.job_cluster import JobCluster
        from ..models.run_parameters import RunParameters
        from ..models.run_state import RunState
        from ..models.run_task import RunTask

        d = src_dict.copy()
        job_id = d.pop("job_id", UNSET)

        run_id = d.pop("run_id", UNSET)

        number_in_job = d.pop("number_in_job", UNSET)

        creator_user_name = d.pop("creator_user_name", UNSET)

        original_attempt_run_id = d.pop("original_attempt_run_id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, RunState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RunState.from_dict(_state)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, CronSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = CronSchedule.from_dict(_schedule)

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = RunTask.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        job_clusters = []
        _job_clusters = d.pop("job_clusters", UNSET)
        for job_clusters_item_data in _job_clusters or []:
            job_clusters_item = JobCluster.from_dict(job_clusters_item_data)

            job_clusters.append(job_clusters_item)

        _cluster_spec = d.pop("cluster_spec", UNSET)
        cluster_spec: Union[Unset, ClusterSpec]
        if isinstance(_cluster_spec, Unset):
            cluster_spec = UNSET
        else:
            cluster_spec = ClusterSpec.from_dict(_cluster_spec)

        _cluster_instance = d.pop("cluster_instance", UNSET)
        cluster_instance: Union[Unset, ClusterInstance]
        if isinstance(_cluster_instance, Unset):
            cluster_instance = UNSET
        else:
            cluster_instance = ClusterInstance.from_dict(_cluster_instance)

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

        _overriding_parameters = d.pop("overriding_parameters", UNSET)
        overriding_parameters: Union[Unset, RunParameters]
        if isinstance(_overriding_parameters, Unset):
            overriding_parameters = UNSET
        else:
            overriding_parameters = RunParameters.from_dict(_overriding_parameters)

        start_time = d.pop("start_time", UNSET)

        setup_duration = d.pop("setup_duration", UNSET)

        execution_duration = d.pop("execution_duration", UNSET)

        cleanup_duration = d.pop("cleanup_duration", UNSET)

        end_time = d.pop("end_time", UNSET)

        run_duration = d.pop("run_duration", UNSET)

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, TriggerType]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = TriggerType(_trigger)

        run_name = d.pop("run_name", UNSET)

        run_page_url = d.pop("run_page_url", UNSET)

        _run_type = d.pop("run_type", UNSET)
        run_type: Union[Unset, RunType]
        if isinstance(_run_type, Unset):
            run_type = UNSET
        else:
            run_type = RunType(_run_type)

        attempt_number = d.pop("attempt_number", UNSET)

        run = cls(
            job_id=job_id,
            run_id=run_id,
            number_in_job=number_in_job,
            creator_user_name=creator_user_name,
            original_attempt_run_id=original_attempt_run_id,
            state=state,
            schedule=schedule,
            tasks=tasks,
            job_clusters=job_clusters,
            cluster_spec=cluster_spec,
            cluster_instance=cluster_instance,
            git_source=git_source,
            overriding_parameters=overriding_parameters,
            start_time=start_time,
            setup_duration=setup_duration,
            execution_duration=execution_duration,
            cleanup_duration=cleanup_duration,
            end_time=end_time,
            run_duration=run_duration,
            trigger=trigger,
            run_name=run_name,
            run_page_url=run_page_url,
            run_type=run_type,
            attempt_number=attempt_number,
        )

        run.additional_properties = d
        return run

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
