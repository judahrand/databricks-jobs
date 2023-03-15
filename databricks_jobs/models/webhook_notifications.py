from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_notifications_on_failure_item import WebhookNotificationsOnFailureItem
    from ..models.webhook_notifications_on_start_item import WebhookNotificationsOnStartItem
    from ..models.webhook_notifications_on_success_item import WebhookNotificationsOnSuccessItem


T = TypeVar("T", bound="WebhookNotifications")


@attr.s(auto_attribs=True)
class WebhookNotifications:
    """
    Attributes:
        on_start (Union[Unset, List['WebhookNotificationsOnStartItem']]): An optional list of notification IDs to call
            when the run starts. A maximum of 3 destinations can be specified for the `on_start` property. Example: [{'id':
            '03dd86e4-57ef-4818-a950-78e41a1d71ab'}, {'id': '0481e838-0a59-4eff-9541-a4ca6f149574'}].
        on_success (Union[Unset, List['WebhookNotificationsOnSuccessItem']]): An optional list of notification IDs to
            call when the run completes successfully. A maximum of 3 destinations can be specified for the `on_success`
            property. Example: [{'id': '03dd86e4-57ef-4818-a950-78e41a1d71ab'}].
        on_failure (Union[Unset, List['WebhookNotificationsOnFailureItem']]): An optional list of notification IDs to
            call when the run fails. A maximum of 3 destinations can be specified for the `on_failure` property. Example:
            [{'id': '0481e838-0a59-4eff-9541-a4ca6f149574'}].
    """

    on_start: Union[Unset, List["WebhookNotificationsOnStartItem"]] = UNSET
    on_success: Union[Unset, List["WebhookNotificationsOnSuccessItem"]] = UNSET
    on_failure: Union[Unset, List["WebhookNotificationsOnFailureItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        on_start: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.on_start, Unset):
            on_start = []
            for on_start_item_data in self.on_start:
                on_start_item = on_start_item_data.to_dict()

                on_start.append(on_start_item)

        on_success: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.on_success, Unset):
            on_success = []
            for on_success_item_data in self.on_success:
                on_success_item = on_success_item_data.to_dict()

                on_success.append(on_success_item)

        on_failure: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.on_failure, Unset):
            on_failure = []
            for on_failure_item_data in self.on_failure:
                on_failure_item = on_failure_item_data.to_dict()

                on_failure.append(on_failure_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if on_start is not UNSET:
            field_dict["on_start"] = on_start
        if on_success is not UNSET:
            field_dict["on_success"] = on_success
        if on_failure is not UNSET:
            field_dict["on_failure"] = on_failure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_notifications_on_failure_item import WebhookNotificationsOnFailureItem
        from ..models.webhook_notifications_on_start_item import WebhookNotificationsOnStartItem
        from ..models.webhook_notifications_on_success_item import WebhookNotificationsOnSuccessItem

        d = src_dict.copy()
        on_start = []
        _on_start = d.pop("on_start", UNSET)
        for on_start_item_data in _on_start or []:
            on_start_item = WebhookNotificationsOnStartItem.from_dict(on_start_item_data)

            on_start.append(on_start_item)

        on_success = []
        _on_success = d.pop("on_success", UNSET)
        for on_success_item_data in _on_success or []:
            on_success_item = WebhookNotificationsOnSuccessItem.from_dict(on_success_item_data)

            on_success.append(on_success_item)

        on_failure = []
        _on_failure = d.pop("on_failure", UNSET)
        for on_failure_item_data in _on_failure or []:
            on_failure_item = WebhookNotificationsOnFailureItem.from_dict(on_failure_item_data)

            on_failure.append(on_failure_item)

        webhook_notifications = cls(
            on_start=on_start,
            on_success=on_success,
            on_failure=on_failure,
        )

        webhook_notifications.additional_properties = d
        return webhook_notifications

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
