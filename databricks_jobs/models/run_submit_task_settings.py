from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbt_task import DbtTask
    from ..models.library import Library
    from ..models.new_cluster import NewCluster
    from ..models.notebook_task import NotebookTask
    from ..models.pipeline_task import PipelineTask
    from ..models.python_wheel_task import PythonWheelTask
    from ..models.spark_jar_task import SparkJarTask
    from ..models.spark_python_task import SparkPythonTask
    from ..models.spark_submit_task import SparkSubmitTask
    from ..models.sql_task import SqlTask
    from ..models.task_dependencies_item import TaskDependenciesItem


T = TypeVar("T", bound="RunSubmitTaskSettings")


@attr.s(auto_attribs=True)
class RunSubmitTaskSettings:
    """
    Attributes:
        task_key (str): A unique name for the task. This field is used to refer to this task from other tasks.
            This field is required and must be unique within its parent job.
            On Update or Reset, this field is used to reference the tasks to be updated or reset.
            The maximum length is 100 characters. Example: Task_Key.
        depends_on (Union[Unset, List['TaskDependenciesItem']]): An optional array of objects specifying the dependency
            graph of the task. All tasks specified in this field must complete successfully before executing this task.
            The key is `task_key`, and the value is the name assigned to the dependent task.
            This field is required when a job consists of more than one task. Example: [{'task_key': 'Previous_Task_Key'},
            {'task_key': 'Other_Task_Key'}].
        existing_cluster_id (Union[Unset, str]): If existing_cluster_id, the ID of an existing cluster that is used for
            all runs of this task. When running tasks on an existing cluster, you may need to manually restart the cluster
            if it stops responding. We suggest running jobs on new clusters for greater reliability. Example:
            0923-164208-meows279.
        new_cluster (Union[Unset, NewCluster]):
        notebook_task (Union[Unset, NotebookTask]):
        spark_jar_task (Union[Unset, SparkJarTask]):
        spark_python_task (Union[Unset, SparkPythonTask]):
        spark_submit_task (Union[Unset, SparkSubmitTask]):
        pipeline_task (Union[Unset, PipelineTask]):
        python_wheel_task (Union[Unset, PythonWheelTask]):
        sql_task (Union[Unset, SqlTask]):
        dbt_task (Union[Unset, DbtTask]):
        libraries (Union[Unset, List['Library']]): An optional list of libraries to be installed on the cluster that
            executes the task. The default value is an empty list.
        timeout_seconds (Union[Unset, int]): An optional timeout applied to each run of this job task. The default
            behavior is to have no timeout. Example: 86400.
    """

    task_key: str
    depends_on: Union[Unset, List["TaskDependenciesItem"]] = UNSET
    existing_cluster_id: Union[Unset, str] = UNSET
    new_cluster: Union[Unset, "NewCluster"] = UNSET
    notebook_task: Union[Unset, "NotebookTask"] = UNSET
    spark_jar_task: Union[Unset, "SparkJarTask"] = UNSET
    spark_python_task: Union[Unset, "SparkPythonTask"] = UNSET
    spark_submit_task: Union[Unset, "SparkSubmitTask"] = UNSET
    pipeline_task: Union[Unset, "PipelineTask"] = UNSET
    python_wheel_task: Union[Unset, "PythonWheelTask"] = UNSET
    sql_task: Union[Unset, "SqlTask"] = UNSET
    dbt_task: Union[Unset, "DbtTask"] = UNSET
    libraries: Union[Unset, List["Library"]] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        task_key = self.task_key
        depends_on: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.depends_on, Unset):
            depends_on = []
            for componentsschemas_task_dependencies_item_data in self.depends_on:
                componentsschemas_task_dependencies_item = componentsschemas_task_dependencies_item_data.to_dict()

                depends_on.append(componentsschemas_task_dependencies_item)

        existing_cluster_id = self.existing_cluster_id
        new_cluster: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_cluster, Unset):
            new_cluster = self.new_cluster.to_dict()

        notebook_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notebook_task, Unset):
            notebook_task = self.notebook_task.to_dict()

        spark_jar_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_jar_task, Unset):
            spark_jar_task = self.spark_jar_task.to_dict()

        spark_python_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_python_task, Unset):
            spark_python_task = self.spark_python_task.to_dict()

        spark_submit_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_submit_task, Unset):
            spark_submit_task = self.spark_submit_task.to_dict()

        pipeline_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pipeline_task, Unset):
            pipeline_task = self.pipeline_task.to_dict()

        python_wheel_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.python_wheel_task, Unset):
            python_wheel_task = self.python_wheel_task.to_dict()

        sql_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sql_task, Unset):
            sql_task = self.sql_task.to_dict()

        dbt_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dbt_task, Unset):
            dbt_task = self.dbt_task.to_dict()

        libraries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.libraries, Unset):
            libraries = []
            for libraries_item_data in self.libraries:
                libraries_item = libraries_item_data.to_dict()

                libraries.append(libraries_item)

        timeout_seconds = self.timeout_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_key": task_key,
            }
        )
        if depends_on is not UNSET:
            field_dict["depends_on"] = depends_on
        if existing_cluster_id is not UNSET:
            field_dict["existing_cluster_id"] = existing_cluster_id
        if new_cluster is not UNSET:
            field_dict["new_cluster"] = new_cluster
        if notebook_task is not UNSET:
            field_dict["notebook_task"] = notebook_task
        if spark_jar_task is not UNSET:
            field_dict["spark_jar_task"] = spark_jar_task
        if spark_python_task is not UNSET:
            field_dict["spark_python_task"] = spark_python_task
        if spark_submit_task is not UNSET:
            field_dict["spark_submit_task"] = spark_submit_task
        if pipeline_task is not UNSET:
            field_dict["pipeline_task"] = pipeline_task
        if python_wheel_task is not UNSET:
            field_dict["python_wheel_task"] = python_wheel_task
        if sql_task is not UNSET:
            field_dict["sql_task"] = sql_task
        if dbt_task is not UNSET:
            field_dict["dbt_task"] = dbt_task
        if libraries is not UNSET:
            field_dict["libraries"] = libraries
        if timeout_seconds is not UNSET:
            field_dict["timeout_seconds"] = timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dbt_task import DbtTask
        from ..models.library import Library
        from ..models.new_cluster import NewCluster
        from ..models.notebook_task import NotebookTask
        from ..models.pipeline_task import PipelineTask
        from ..models.python_wheel_task import PythonWheelTask
        from ..models.spark_jar_task import SparkJarTask
        from ..models.spark_python_task import SparkPythonTask
        from ..models.spark_submit_task import SparkSubmitTask
        from ..models.sql_task import SqlTask
        from ..models.task_dependencies_item import TaskDependenciesItem

        d = src_dict.copy()
        task_key = d.pop("task_key")

        depends_on = []
        _depends_on = d.pop("depends_on", UNSET)
        for componentsschemas_task_dependencies_item_data in _depends_on or []:
            componentsschemas_task_dependencies_item = TaskDependenciesItem.from_dict(
                componentsschemas_task_dependencies_item_data
            )

            depends_on.append(componentsschemas_task_dependencies_item)

        existing_cluster_id = d.pop("existing_cluster_id", UNSET)

        _new_cluster = d.pop("new_cluster", UNSET)
        new_cluster: Union[Unset, NewCluster]
        if isinstance(_new_cluster, Unset):
            new_cluster = UNSET
        else:
            new_cluster = NewCluster.from_dict(_new_cluster)

        _notebook_task = d.pop("notebook_task", UNSET)
        notebook_task: Union[Unset, NotebookTask]
        if isinstance(_notebook_task, Unset):
            notebook_task = UNSET
        else:
            notebook_task = NotebookTask.from_dict(_notebook_task)

        _spark_jar_task = d.pop("spark_jar_task", UNSET)
        spark_jar_task: Union[Unset, SparkJarTask]
        if isinstance(_spark_jar_task, Unset):
            spark_jar_task = UNSET
        else:
            spark_jar_task = SparkJarTask.from_dict(_spark_jar_task)

        _spark_python_task = d.pop("spark_python_task", UNSET)
        spark_python_task: Union[Unset, SparkPythonTask]
        if isinstance(_spark_python_task, Unset):
            spark_python_task = UNSET
        else:
            spark_python_task = SparkPythonTask.from_dict(_spark_python_task)

        _spark_submit_task = d.pop("spark_submit_task", UNSET)
        spark_submit_task: Union[Unset, SparkSubmitTask]
        if isinstance(_spark_submit_task, Unset):
            spark_submit_task = UNSET
        else:
            spark_submit_task = SparkSubmitTask.from_dict(_spark_submit_task)

        _pipeline_task = d.pop("pipeline_task", UNSET)
        pipeline_task: Union[Unset, PipelineTask]
        if isinstance(_pipeline_task, Unset):
            pipeline_task = UNSET
        else:
            pipeline_task = PipelineTask.from_dict(_pipeline_task)

        _python_wheel_task = d.pop("python_wheel_task", UNSET)
        python_wheel_task: Union[Unset, PythonWheelTask]
        if isinstance(_python_wheel_task, Unset):
            python_wheel_task = UNSET
        else:
            python_wheel_task = PythonWheelTask.from_dict(_python_wheel_task)

        _sql_task = d.pop("sql_task", UNSET)
        sql_task: Union[Unset, SqlTask]
        if isinstance(_sql_task, Unset):
            sql_task = UNSET
        else:
            sql_task = SqlTask.from_dict(_sql_task)

        _dbt_task = d.pop("dbt_task", UNSET)
        dbt_task: Union[Unset, DbtTask]
        if isinstance(_dbt_task, Unset):
            dbt_task = UNSET
        else:
            dbt_task = DbtTask.from_dict(_dbt_task)

        libraries = []
        _libraries = d.pop("libraries", UNSET)
        for libraries_item_data in _libraries or []:
            libraries_item = Library.from_dict(libraries_item_data)

            libraries.append(libraries_item)

        timeout_seconds = d.pop("timeout_seconds", UNSET)

        run_submit_task_settings = cls(
            task_key=task_key,
            depends_on=depends_on,
            existing_cluster_id=existing_cluster_id,
            new_cluster=new_cluster,
            notebook_task=notebook_task,
            spark_jar_task=spark_jar_task,
            spark_python_task=spark_python_task,
            spark_submit_task=spark_submit_task,
            pipeline_task=pipeline_task,
            python_wheel_task=python_wheel_task,
            sql_task=sql_task,
            dbt_task=dbt_task,
            libraries=libraries,
            timeout_seconds=timeout_seconds,
        )

        run_submit_task_settings.additional_properties = d
        return run_submit_task_settings

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
