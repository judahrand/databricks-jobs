from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_parameters_notebook_params import RunParametersNotebookParams
    from ..models.run_parameters_pipeline_params import RunParametersPipelineParams
    from ..models.run_parameters_python_named_params import RunParametersPythonNamedParams
    from ..models.run_parameters_sql_params import RunParametersSqlParams


T = TypeVar("T", bound="JobsRunsRepairJsonBody")


@attr.s(auto_attribs=True)
class JobsRunsRepairJsonBody:
    """
    Attributes:
        run_id (Union[Unset, int]): The job run ID of the run to repair. The run must not be in progress. Example:
            455644833.
        rerun_tasks (Union[Unset, List[str]]): The task keys of the task runs to repair. Example: ['task0', 'task1'].
        latest_repair_id (Union[Unset, int]): The ID of the latest repair. This parameter is not required when repairing
            a run for the first time, but must be provided on subsequent requests to repair the same run. Example:
            734650698524280.
        rerun_all_failed_tasks (Union[Unset, bool]): If true, repair all failed tasks. Only one of rerun_tasks or
            rerun_all_failed_tasks can be used.
        jar_params (Union[Unset, List[str]]): A list of parameters for jobs with Spark JAR tasks, for example
            `"jar_params": ["john doe", "35"]`. The parameters are used to invoke the main function of the main class
            specified in the Spark JAR task. If not specified upon `run-now`, it defaults to an empty list. jar_params
            cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example
            `{"jar_params":["john doe","35"]}`) cannot exceed 10,000 bytes.

            Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set
            parameters containing information about job runs. Example: ['john', 'doe', '35'].
        notebook_params (Union[Unset, RunParametersNotebookParams]): A map from keys to values for jobs with notebook
            task, for example `"notebook_params": {"name": "john doe", "age": "35"}`. The map is passed to the notebook and
            is accessible through the [dbutils.widgets.get](https://docs.microsoft.com/azure/databricks/dev-
            tools/databricks-utils#dbutils-widgets) function.

            If not specified upon `run-now`, the triggered run uses the job’s base parameters.

            notebook_params cannot be specified in conjunction with jar_params.

            Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set
            parameters containing information about job runs.

            The JSON representation of this field (for example `{"notebook_params":{"name":"john doe","age":"35"}}`) cannot
            exceed 10,000 bytes. Example: {'name': 'john doe', 'age': '35'}.
        python_params (Union[Unset, List[str]]): A list of parameters for jobs with Python tasks, for example
            `"python_params": ["john doe", "35"]`. The parameters are passed to Python file as command-line parameters. If
            specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of
            this field (for example `{"python_params":["john doe","35"]}`) cannot exceed 10,000 bytes.

            Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set
            parameters containing information about job runs.

            Important

            These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an
            error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. Example: ['john doe',
            '35'].
        spark_submit_params (Union[Unset, List[str]]): A list of parameters for jobs with spark submit task, for example
            `"spark_submit_params": ["--class", "org.apache.spark.examples.SparkPi"]`. The parameters are passed to spark-
            submit script as command-line parameters. If specified upon `run-now`, it would overwrite the parameters
            specified in job setting. The JSON representation of this field (for example `{"python_params":["john
            doe","35"]}`) cannot exceed 10,000 bytes.

            Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set
            parameters containing information about job runs.

            Important

            These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an
            error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. Example: ['--class',
            'org.apache.spark.examples.SparkPi'].
        python_named_params (Union[Unset, RunParametersPythonNamedParams]): A map from keys to values for jobs with
            Python wheel task, for example `"python_named_params": {"name": "task", "data": "dbfs:/path/to/data.json"}`.
            Example: {'name': 'task', 'data': 'dbfs:/path/to/data.json'}.
        pipeline_params (Union[Unset, RunParametersPipelineParams]):
        sql_params (Union[Unset, RunParametersSqlParams]): A map from keys to values for SQL tasks, for example
            `"sql_params": {"name": "john doe", "age": "35"}`. The SQL alert task does not support custom parameters.
            Example: {'name': 'john doe', 'age': '35'}.
        dbt_commands (Union[Unset, List[str]]): An array of commands to execute for jobs with the dbt task, for example
            `"dbt_commands": ["dbt deps", "dbt seed", "dbt run"]` Example: ['dbt deps', 'dbt seed', 'dbt run'].
    """

    run_id: Union[Unset, int] = UNSET
    rerun_tasks: Union[Unset, List[str]] = UNSET
    latest_repair_id: Union[Unset, int] = UNSET
    rerun_all_failed_tasks: Union[Unset, bool] = False
    jar_params: Union[Unset, List[str]] = UNSET
    notebook_params: Union[Unset, "RunParametersNotebookParams"] = UNSET
    python_params: Union[Unset, List[str]] = UNSET
    spark_submit_params: Union[Unset, List[str]] = UNSET
    python_named_params: Union[Unset, "RunParametersPythonNamedParams"] = UNSET
    pipeline_params: Union[Unset, "RunParametersPipelineParams"] = UNSET
    sql_params: Union[Unset, "RunParametersSqlParams"] = UNSET
    dbt_commands: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_id = self.run_id
        rerun_tasks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rerun_tasks, Unset):
            rerun_tasks = self.rerun_tasks

        latest_repair_id = self.latest_repair_id
        rerun_all_failed_tasks = self.rerun_all_failed_tasks
        jar_params: Union[Unset, List[str]] = UNSET
        if not isinstance(self.jar_params, Unset):
            jar_params = self.jar_params

        notebook_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notebook_params, Unset):
            notebook_params = self.notebook_params.to_dict()

        python_params: Union[Unset, List[str]] = UNSET
        if not isinstance(self.python_params, Unset):
            python_params = self.python_params

        spark_submit_params: Union[Unset, List[str]] = UNSET
        if not isinstance(self.spark_submit_params, Unset):
            spark_submit_params = self.spark_submit_params

        python_named_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.python_named_params, Unset):
            python_named_params = self.python_named_params.to_dict()

        pipeline_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pipeline_params, Unset):
            pipeline_params = self.pipeline_params.to_dict()

        sql_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sql_params, Unset):
            sql_params = self.sql_params.to_dict()

        dbt_commands: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dbt_commands, Unset):
            dbt_commands = self.dbt_commands

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if rerun_tasks is not UNSET:
            field_dict["rerun_tasks"] = rerun_tasks
        if latest_repair_id is not UNSET:
            field_dict["latest_repair_id"] = latest_repair_id
        if rerun_all_failed_tasks is not UNSET:
            field_dict["rerun_all_failed_tasks"] = rerun_all_failed_tasks
        if jar_params is not UNSET:
            field_dict["jar_params"] = jar_params
        if notebook_params is not UNSET:
            field_dict["notebook_params"] = notebook_params
        if python_params is not UNSET:
            field_dict["python_params"] = python_params
        if spark_submit_params is not UNSET:
            field_dict["spark_submit_params"] = spark_submit_params
        if python_named_params is not UNSET:
            field_dict["python_named_params"] = python_named_params
        if pipeline_params is not UNSET:
            field_dict["pipeline_params"] = pipeline_params
        if sql_params is not UNSET:
            field_dict["sql_params"] = sql_params
        if dbt_commands is not UNSET:
            field_dict["dbt_commands"] = dbt_commands

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.run_parameters_notebook_params import RunParametersNotebookParams
        from ..models.run_parameters_pipeline_params import RunParametersPipelineParams
        from ..models.run_parameters_python_named_params import RunParametersPythonNamedParams
        from ..models.run_parameters_sql_params import RunParametersSqlParams

        d = src_dict.copy()
        run_id = d.pop("run_id", UNSET)

        rerun_tasks = cast(List[str], d.pop("rerun_tasks", UNSET))

        latest_repair_id = d.pop("latest_repair_id", UNSET)

        rerun_all_failed_tasks = d.pop("rerun_all_failed_tasks", UNSET)

        jar_params = cast(List[str], d.pop("jar_params", UNSET))

        _notebook_params = d.pop("notebook_params", UNSET)
        notebook_params: Union[Unset, RunParametersNotebookParams]
        if isinstance(_notebook_params, Unset):
            notebook_params = UNSET
        else:
            notebook_params = RunParametersNotebookParams.from_dict(_notebook_params)

        python_params = cast(List[str], d.pop("python_params", UNSET))

        spark_submit_params = cast(List[str], d.pop("spark_submit_params", UNSET))

        _python_named_params = d.pop("python_named_params", UNSET)
        python_named_params: Union[Unset, RunParametersPythonNamedParams]
        if isinstance(_python_named_params, Unset):
            python_named_params = UNSET
        else:
            python_named_params = RunParametersPythonNamedParams.from_dict(_python_named_params)

        _pipeline_params = d.pop("pipeline_params", UNSET)
        pipeline_params: Union[Unset, RunParametersPipelineParams]
        if isinstance(_pipeline_params, Unset):
            pipeline_params = UNSET
        else:
            pipeline_params = RunParametersPipelineParams.from_dict(_pipeline_params)

        _sql_params = d.pop("sql_params", UNSET)
        sql_params: Union[Unset, RunParametersSqlParams]
        if isinstance(_sql_params, Unset):
            sql_params = UNSET
        else:
            sql_params = RunParametersSqlParams.from_dict(_sql_params)

        dbt_commands = cast(List[str], d.pop("dbt_commands", UNSET))

        jobs_runs_repair_json_body = cls(
            run_id=run_id,
            rerun_tasks=rerun_tasks,
            latest_repair_id=latest_repair_id,
            rerun_all_failed_tasks=rerun_all_failed_tasks,
            jar_params=jar_params,
            notebook_params=notebook_params,
            python_params=python_params,
            spark_submit_params=spark_submit_params,
            python_named_params=python_named_params,
            pipeline_params=pipeline_params,
            sql_params=sql_params,
            dbt_commands=dbt_commands,
        )

        jobs_runs_repair_json_body.additional_properties = d
        return jobs_runs_repair_json_body

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