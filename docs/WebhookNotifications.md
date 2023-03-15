# WebhookNotifications


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_start** | [**List[WebhookNotificationsOnStartInner]**](WebhookNotificationsOnStartInner.md) | An optional list of notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the &#x60;on_start&#x60; property. | [optional] 
**on_success** | [**List[WebhookNotificationsOnStartInner]**](WebhookNotificationsOnStartInner.md) | An optional list of notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the &#x60;on_success&#x60; property. | [optional] 
**on_failure** | [**List[WebhookNotificationsOnStartInner]**](WebhookNotificationsOnStartInner.md) | An optional list of notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the &#x60;on_failure&#x60; property. | [optional] 

## Example

```python
from databricks_jobs.models.webhook_notifications import WebhookNotifications

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookNotifications from a JSON string
webhook_notifications_instance = WebhookNotifications.from_json(json)
# print the JSON string representation of the object
print WebhookNotifications.to_json()

# convert the object into a dict
webhook_notifications_dict = webhook_notifications_instance.to_dict()
# create an instance of WebhookNotifications from a dict
webhook_notifications_form_dict = webhook_notifications.from_dict(webhook_notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


