# databricks_jobs.model.webhook_notifications.WebhookNotifications

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[on_start](#on_start)** | list, tuple,  | tuple,  | An optional list of notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the &#x60;on_start&#x60; property. | [optional] 
**[on_success](#on_success)** | list, tuple,  | tuple,  | An optional list of notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the &#x60;on_success&#x60; property. | [optional] 
**[on_failure](#on_failure)** | list, tuple,  | tuple,  | An optional list of notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the &#x60;on_failure&#x60; property. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# on_start

An optional list of notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the `on_start` property.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional list of notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the &#x60;on_start&#x60; property. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WebhookNotificationsOnStartInner**](WebhookNotificationsOnStartInner.md) | [**WebhookNotificationsOnStartInner**](WebhookNotificationsOnStartInner.md) | [**WebhookNotificationsOnStartInner**](WebhookNotificationsOnStartInner.md) |  | 

# on_success

An optional list of notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the `on_success` property.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional list of notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the &#x60;on_success&#x60; property. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WebhookNotificationsOnStartInner**](WebhookNotificationsOnStartInner.md) | [**WebhookNotificationsOnStartInner**](WebhookNotificationsOnStartInner.md) | [**WebhookNotificationsOnStartInner**](WebhookNotificationsOnStartInner.md) |  | 

# on_failure

An optional list of notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the `on_failure` property.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional list of notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the &#x60;on_failure&#x60; property. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WebhookNotificationsOnStartInner**](WebhookNotificationsOnStartInner.md) | [**WebhookNotificationsOnStartInner**](WebhookNotificationsOnStartInner.md) | [**WebhookNotificationsOnStartInner**](WebhookNotificationsOnStartInner.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

