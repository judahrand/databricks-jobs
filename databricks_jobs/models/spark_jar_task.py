from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SparkJarTask")


@attr.s(auto_attribs=True)
class SparkJarTask:
    """
    Attributes:
        main_class_name (Union[Unset, str]): The full name of the class containing the main method to be executed. This
            class must be contained in a JAR provided as a library.

            The code must use `SparkContext.getOrCreate` to obtain a Spark context; otherwise, runs of the job fail.
            Example: com.databricks.ComputeModels.
        parameters (Union[Unset, List[str]]): Parameters passed to the main method.

            Use [Task parameter variables](https://docs.microsoft.com/azure/databricks/jobs#parameter-variables) to set
            parameters containing information about job runs. Example: ['--data', 'dbfs:/path/to/data.json'].
        jar_uri (Union[Unset, str]): Deprecated since 04/2016\. Provide a `jar` through the `libraries` field instead.
            For an example, see [Create](https://docs.microsoft.com/azure/databricks/dev-
            tools/api/latest/jobs#operation/JobsCreate).
    """

    main_class_name: Union[Unset, str] = UNSET
    parameters: Union[Unset, List[str]] = UNSET
    jar_uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        main_class_name = self.main_class_name
        parameters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters

        jar_uri = self.jar_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if main_class_name is not UNSET:
            field_dict["main_class_name"] = main_class_name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if jar_uri is not UNSET:
            field_dict["jar_uri"] = jar_uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        main_class_name = d.pop("main_class_name", UNSET)

        parameters = cast(List[str], d.pop("parameters", UNSET))

        jar_uri = d.pop("jar_uri", UNSET)

        spark_jar_task = cls(
            main_class_name=main_class_name,
            parameters=parameters,
            jar_uri=jar_uri,
        )

        spark_jar_task.additional_properties = d
        return spark_jar_task

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